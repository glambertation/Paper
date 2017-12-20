Metrics 目前是的统计收集系统。会收集来自开发者的数据上报，作为打点统计或者报警的数据源。

前有两个平台可以看到 metrics 统计数据的可视化展示，通常采用的是 grafana，这里可以很直观的看到数据的图表，作为 dashboard 使用。同时可以基于自定义的策略添加报警。

另外一个平台是metrics， 这个可视化功能比较弱，但是可以支持比较复杂一些的查询，也支持 json 数据展示。

metrics是基于opentsdb开发而成，

首先，metrics分成以下几个方法：

1.  EmitCounter                 常用于累加计数
2.  EmitTimer                     常用于记录一个函数耗时长度
3.  EmitStore                      常用于直接保存数据，该数据不用于进一步统计分析

### counter
1. emitcounter 先计数

2. 查询：query sum +rate

    rate的意思是求每秒机器提交的counter的结果，可以当做qps看待。代表每个时刻点上，一共出现的xx点数，是线上所有机器相加的结果。

3. 查询query avg + rate
    
    代表的是线上每台机器平均出现xx的次数

    每台机器的qps

4. query count + rate
    
    统计的是线上有多少机器 对xx结果加和

    统计的是线上机器数

5. query p99 + rate
    
    把每台机器xx的时间，从小到大排序，选取前50%，前90%，前99%的数据结果点，也就是50%，90%，99%的数据结果点，表示99%的结果都小于这个数。

    用于监控函数延迟。

    max，min是在这些结果中返回最大最小值。

### timer
1. emittimer计数

2. query avg + store
   
    字段latency.avg

    字段的avg是这个时刻点这台机器上平均执行这个操作记录的延迟。

    query的avg是所有线上机器的字段平均后再平均，那么现在得到的也就是所有请求的平均耗时了。

3. query avg + store ，字段.pct99

    pct99计算出每台机器上99%的请求耗时，然后再求平均值。

    能反馈出实际最长的请求延时。
