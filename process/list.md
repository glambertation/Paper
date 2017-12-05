* fuc
    * 建立一个fuc 启动进程
    * 建立一个class 启动进程

* process
    * start 
        * 自动调用run
    * join
        * 阻塞当前进程
    * daemon
        * 子进程设置了daemon属性，主进程结束
        * 什么是主进程？main？multiprocessing？对！main！
* 组件
    * lock
        * acquire
        * release
    * queue
        * put
        * get
    * pipe
        * send
        * recv
    * pool
        * 进程池 
        * Pool(processes=4) 维持执行的进程总数为processes，当一个进程执行完毕后会添加新的进程进去
        * apply_async 非阻塞
        * apply 阻塞
        * imap_unordered 无序
    * 线程池


