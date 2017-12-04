# -*- coding:utf-8 -*-
# 因子进程设置了daemon属性，主进程结束，它们就随着结束了。
# 所以使用多进程的常规方法是，先依次调用start启动进程，再依次调用join要求主进程等待子进程的结束。
# p1.start()
# p2.start()
# p1.join()

# 如果p1.start() p1.join() p2.start()
# join是用来阻塞当前线程的，p1.start()之后，p1就提示主线程，需要等待p1结束才向下执行

import multiprocessing
import time

def worker(interval):
    print("work{} start:{}".format(interval, time.ctime()));
    time.sleep(interval)
    print("work{0} end:{1}".format(interval, time.ctime()));

if __name__ == "__main__":
    p = multiprocessing.Process(target = worker, args = (3,))
    p1 = multiprocessing.Process(target = worker, args = (1,))
    p.daemon = True
    p.daemon = True
    p.start()
    p1.start()
    p.join()
    p1.join()
    print "end!"
