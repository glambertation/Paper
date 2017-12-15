统计部分

1. 业务逻辑里面 logic里面push_event, 有各种类型event_type定义。
2. 服务端发nsq消息，worker对消息进行校验，然后发kafka 最后通过facade平台配置相关任务
    * kafka topic 是：server_stats_log_wenda
    * facade平台配置相关任务，这样把需要统计的数据保存在hive表中
3. 统计数据有两种方式：
    * 一是：去hive上跑sql
    * 二是：用liuji，脚本跑出的数据结果保存在tableau中，检测每天的数据情况
4. 脚本任务配在chronos平台，可以配置跑任务的时间

补充

hive是基于Hadoop的一个数据仓库工具，可以将结构化的数据文件映射为一张数据库表，并提供简单的SQL查询功能，可以将SQL语句转换为MapReduce任务进行运行。其优点是学习成本低，可以通过类SQL语句快速实现简单的MapReduce统计，不必开发专门的MapReduce应用，十分适合数据仓库的统计分析。

Hive是基于Hadoop的一个数据仓库系统，在各大公司都有广泛的应用。美团数据仓库也是基于Hive搭建，每天执行近万次的Hive ETL计算流程，负责每天数百GB的数据存储和分析。Hive的稳定性和性能对我们的数据分析非常关键。

https://tech.meituan.com/hive-sql-to-mapreduce.html

美团 hive sql的编译过程
