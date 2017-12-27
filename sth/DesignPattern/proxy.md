概念

- 意图：为其他对象提供一种代理以控制对这个对象的访问。
- 何时使用：想在访问一个对象时做一些控制。
- 如何解决：增加中间层。
- 应用实例：
    - Windows 里面的快捷方式
    - 买火车票不一定在火车站买，也可以去代售点。

传统语言实现

# 接口

```

class GiveGift(object):
    def breakfast(self):
        raise NotImplementedError()


# 男孩
class Boy(GiveGift):
    def __init__(self, girl):
        self.girl = girl

    def breakfast(self):
        print '送爱心早餐给' + self.girl


# 非代理模式
shuaixian = Boy('民族大学妹子')
shuaixian.breakfast()


# 代理模式
class Proxy(GiveGift):
    def __init__(self, girl):
        self.shuaixian = Boy(girl)

    def breakfast(self):
        print '此早餐是使用代理模式送出:'
        self.shuaixian.breakfast()

proxy = Proxy('民族大学妹子')
proxy.breakfast()

```

### 补充：

https://segmentfault.com/a/1190000004298707
