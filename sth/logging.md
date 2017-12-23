## python 日志模块

### 1. import logging

### 2. 设置格式

``` format = '%(asctime)s, %(levelname)s %(message)s' ```
```
 %(levelname)s: 打印日志级别名称
 %(asctime)s: 打印日志的时间
 %(message)s: 打印日志信息
```

### 3. 输出到文件
```
from logging.handlers import TimedRotatingFileHandler
定义一个TimedRotatingFileHandler，将INFO级别或更高的日志信息打印到标准错误，并将其添加到当前的日志处理对象

handler =MultiProcessRotatingFileHandler()
handler.setFormatter(format)
access = logging.getLogger()
access.setLevel(logging.WARNING)
access.addHandler(handler)

```

### 4. 打在屏幕上

```
StreamHandler
setFormatter 设置格式
setLevel 设置日志级别
addHandler
```

### 5. 补充

https://www.cnblogs.com/dkblog/archive/2011/08/26/2155018.html
