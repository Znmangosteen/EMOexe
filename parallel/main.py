import multiprocessing as mp
import threading

from parallel.data_distributor import DataDistributor
from parallel.data_reader import DataReader
from parallel.ga_example import GA
from parallel.pop_pool import PopPool


def run(dataset, pipe):
    ga = GA(dataset)

    #init part
    ga.init_run()
    pipe.send(ga.pop)
    pipe.recv() # wait for a signal. TODO: need auth?

    # main part
    while True:
        terminate_flag = ga.run()
        if terminate_flag:
            break
        # update pop
        pipe.send(ga.pop)
        new_pop = pipe.recv()
        ga.pop = new_pop
    pipe.send("END_FALG")


def lisen(pipe):
    global popPool
    global listen_lock
    while True:
        info = pipe.recv()
        if info == "END_FALG":
            break
        pop = info
        with listen_lock:
            new_pop = popPool.update_pool(pop)
        pipe.send(new_pop)


if __name__ == '__main__':
    CPU_NUM = mp.cpu_count()
    reader = DataReader()
    distributor = DataDistributor(CPU_NUM)
    popPool = PopPool()
    listen_lock = threading.RLock()

    distributor.set_dataset(reader.getTrainingData())
    datasets = distributor.partition()

    init_worker = []
    pipe_conns = []
    lisen_threads = []
    for i in range(CPU_NUM):
        parent_conn, child_conn = mp.Pipe()
        worker = mp.Process(target=run, args=(datasets[i], child_conn))
        lisener = threading.Thread(target=lisen, args=(parent_conn,))
        init_worker.append(worker)
        lisen_threads.append(lisener)
        pipe_conns.append(parent_conn)

    for worker in init_worker:
        worker.start()

    pops = []
    for conn in pipe_conns:
        pop = conn.recv()
        pops.append(pop)

    popPool.init_pool(pops)



    #run main part
    for lisen_thread in lisen_threads:
        lisen_thread.start()

    # send run main signal
    for conn in pipe_conns:
        conn.send('Run Main')

    for lisen_thread in lisen_threads:
        lisen_thread.join()
