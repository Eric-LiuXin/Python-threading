# 创建Thread实例，传给他一个参数

import threading
from time import ctime, sleep

loops = [4, 2]

def loop(nloop, nsec):
    print("start loop", nloop, "at: ", ctime())
    sleep(nsec)
    print("loop", nloop, "done at: ", ctime())


def main():
    print("starting at: ", ctime())
    threads = []
    nloops = range(len(loops))

    for i in nloops:
        t = threading.Thread(target=loop, args=(i, loops[i]))
        threads.append(t)

    for t in threads:
        t.start()

    for t in threads:
        t.join()

    print("all DONE at ", ctime())


if __name__ == '__main__':
    main()