# 创建Thread实例，传给他一个可调用的类实例

import threading
from time import ctime, sleep

loops = [4, 2]

class ThreadFunc(object):
    def __init__(self, func, args, name=""):
        self.name = name
        self.func = func
        self.args = args

    def __call__(self, *args, **kwargs):
        self.func(*self.args)


def loop(nloop, nsec):
    print("start loop", nloop, "at: ", ctime())
    sleep(nsec)
    print("loop", nloop, "done at: ", ctime())


def main():
    print("starting at: ", ctime())
    threads = []
    nloops = range(len(loops))

    for i in nloops:
        t = threading.Thread(
            target=ThreadFunc(loop, (i, loops[i]), loop.__name__)
        )
        threads.append(t)

    for t in threads:
        t.start()

    for t in threads:
        t.join()

    print("all DONE at ", ctime())


if __name__ == '__main__':
    main()