enlightenment 启蒙

Explicit 明确的

Explicit is better than implicit.

awareness 意识

karma 因果 因缘

flat 平坦

nested 内嵌

Flat is better than nested.

mangled 损坏

convention 约定

* 补充阅读 ：
    * map/reduce
    * https://static.googleusercontent.com/media/research.google.com/zh-CN//archive/mapreduce-osdi04.pdf

* assert
    * assertTrue(True, "some message")
    * assertEqual(expect, actually), 如果用assertTrue(expect == actually), equal更好一点
    * assert 抛出异常

* string
    * '', "", """string""", '''string''', r'string', 
    * "包含'", '包含"', "\'", '\"' \转义 
    * \n 长度为1
    * """ """下 换行长度为1
    * """ """下 "string\" == \"string\"

* None
    * 啥是object

* list
    * [], list()
    * list[1:]  从第二个元素开始截取列表
    * list.insert(位置，value)
    * list.append(), list.pop(位置)
    * deque.leftpop()
    * list[:]全部元素  list[:2]前两个元素
* 命名
    * a, b = b, a
* dict
    * dict(), {},
    * 无序
    * xx.keys(); xx.values(); a in xx.keys()
    * card = {}.formkeys(('key1','key2','key3'),value)
* string 操作
    * sss = " i like {0} and {1} ".format('pink', 2) 
    * string = "The square root of 5 is {0:.{1}f}".format(math.sqrt(5), \
                decimal_places)
    * 97 == ord('a')
    * string.split() 按空格分开字符串成list
    * pattern = re.compile(',|;') pattern.split(string) 按， ； 把string分开成list 
    * r'\n' == '\\n'
    * ' '.join(somelist) 把list按照空格间隔join成字符串
    * string.capitalize()首字母大写 upper 全部大写 lower全部小写 title单词首字母大写 swapcase大小写交换

* tuple
    * (a,); tuple(['a', 'bbb']), tuple('bbb')= ('b','b','b')
    
* exception
    * TypeError
    *
* class
    * 没有return的方法 返回是None
    * *args是tuple
    * def xx(self, a, b) 调用的时候 self.xx(a, b)
    * 内嵌的函数，不用self.xx调用，
    * pass 啥也没做
    * __doc__ 打印函数里面的字符串"" """ """
    * 下划线
        * 需要注意的是，在Python中，变量名类似__xxx__的，也就是以双下划线开头，并且以双下划线结尾的，是特殊变量，特殊变量是可以直接访问的，不是private变量，所以，不能用__name__、__score__这样的变量名。

        * 有些时候，你会看到以一个下划线开头的实例变量名，比如_name，这样的实例变量外部是可以访问的，但是，按照约定俗成的规定，当你看到这样的变量时，意思就是，“虽然我可以被访问，但是，请把我视为私有变量，不要随意访问”。

        * 双下划线开头的实例变量是不是一定不能从外部访问呢？其实也不是。不能直接访问__name是因为Python解释器对外把__name变量改成了_Student__name，所以，仍然可以通过_Student__name来访问__name变量：
     * __name__ : cover the class into a string value


* set
    * set('12345') = set([1,2,3,4,5])
    * set() 或者 {'a', 'b', 'c'}  或者 内嵌一个list  set(['ops']) != {'o','p','s'}
    * sort()后又变成list
    * - 删掉共同原色 | 取所有元素 & 取共同元素 ^ 取不同元素
     
* exception
    * http://www.runoob.com/python/python-exceptions.html
    * StandardError 所有的内建标准异常的基类
        * 子类
            * RuntimeError

* iterator
    * range(1, 6) = [1,2,3,4,5] 是个list
    * iter(range(1,6)) 变成迭代器
    * list string dict 本身可以for循环迭代，但不是迭代器，不能next(list)，需要iter(list)
    * map函数 map(fucn, list) list每个元素都执行一遍func
    * filter函数 
        * 和map()类似，filter()也接收一个函数和一个序列。和map()不同的是，filter()把传入的函数依次作用于每个元素，然后根据返回值是True还是False决定保留还是丢弃该元素。
    * reduce
        * 再看reduce的用法。reduce把一个函数作用在一个序列[x1, x2, x3, ...]上，这个函数必须接收两个参数，reduce把结果继续和序列的下一个元素做累积计算，其效果就是：
        * reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4)
        * reduce()还可以接收第3个可选参数，作为计算的初始值
    * line.strip() 分割成list
    
* comprehension
    * 两个for 是排列组合 

* generate
    * (xx for xx in list)
    * generate对象只能被迭代一次 比如 list(generate) = [2,4,6,8], 第二次就是[]
    * 函数是顺序执行，遇到return语句或者最后一行函数语句就返回。而变成generator的函数，在每次调用next()的时候执行，遇到yield语句返回，再次执行时从上次返回的yield语句处继续执行。
    * http://www.python.org/dev/peps/pep-0342/
    * 提出了一种新的生成迭代器的方法，称为send（）。它只需要一个参数，这是应该发送到生成器的值。调用send（None）与调用generator的next（）方法完全相同。除了由生成器的当前yield表达式产生的值不同之外，用任何其他值调用send（）都是一样的。
    * 由于生成器迭代器在生成器的函数体的顶部开始执行，因此在刚刚创建生成器时没有yield表达式来接收值。因此，当生成器迭代器刚刚启动时，禁止使用非无参数调用send（），如果发生此类错误（可能是由于某种逻辑错误），则会引发TypeError。因此，在你可以和协程通信之前，你必须先调用next（）或者发送（None）来将其执行提前到第一个yield表达式。
    * 与next（）方法一样，send（）方法返回由generator-iterator生成的下一个值，或者如果生成器正常退出或已经退出，则引发StopIteration。如果生成器引发一个未捕获的异常，它会传播给send（）的调用者。 
    * 第一次send（None）或者next（generate），第二次开始才可以send（valuea）

* lambda
    * 关键字lambda表示匿名函数，冒号前面的x表示函数参数
    * 匿名函数有个限制，就是只能有一个表达式，不用写return，返回值就是该表达式的结果。

* class
    * __init__ 是构造器
    * _name 私有变量 可以被访问
    * getattr 获取属性 getattr('实例'，'变量')
    * setattr(obj, 'y', 19) # 设置一个属性'y'
    * hasattr(obj, 'x') # 有属性'x'吗？
    * __dict__ 可能打不全 用上面的好一点
    * property
        * 还记得装饰器（decorator）可以给函数动态加上功能吗？对于类的方法，装饰器一样起作用。Python内置的@property装饰器就是负责把一个方法变成属性调用的：
        * 把一个getter方法变成属性，只需要加上@property就可以了，此时，@property本身又创建了另一个装饰器@score.setter，负责把一个setter方法变成属性赋值，于是，我们就拥有一个可控的属性操作：
        * 还可以定义只读属性，只定义getter方法，不定义setter方法就是一个只读属性：
    * 类要实例化 a = std("sss"),然后可以调用方法 a.func()
    * __str__()方法，返回一个好看的字符串就可以了
    * __repr__
        * __repr__()，两者的区别是__str__()返回用户看到的字符串，而__repr__()返回程序开发者看到的字符串，也就是说，__repr__()是为调试服务的。
        * 不用print，打印出来的实例还是不好看, 再定义一个__repr__
    * str 提供string版对象 str(Fido) Fido是狗狗的实例
        * a = [1,2,3] str(a) = '[1,2,3]' 

* newstyleclass
    * https://www.python.org/download/releases/2.2.3/descrintro/
    * type() = xx.__class__

* file
    * with xx as f:
        * 自开自闭

* openclass
    * 给已有类增加方法
    * 不能给内建类增加方法 "can't set attributes of built-in/extension type 'int'"

* method binding
    * im_func: 使用这个属性可以拿到方法里实际的函数对象的引用。另外如果是2.6以上的版本，还可以使用属性名__func__。
    * im_self: 如果是绑定的(bound)，则指向调用该方法的类（如果是类方法）或实例（如果是实例方法），否则为None。如果是2.6以上的版本，还可以使用属性名__self__。
    * im_class: 实际调用该方法的类，或实际调用该方法的实例的类。注意不是方法的定义所在的类，如果有继承关系的话。
    * dir(fucn)
        * ['__call__', '__class__', '__closure__', '__code__', '__defaults__', '__delattr__', '__dict__', '__doc__', '__format__', '__get__', '__getattribute__', '__globals__', '__hash__', '__init__', '__module__', '__name__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'func_closure', 'func_code', 'func_defaults', 'func_dict', 'func_doc', 'func_globals', 'func_name']
    * 实例化后 属性会少
    * def __set__ 可以改变

* 装饰器
* 偏函数
    * Python的functools模块提供了很多有用的功能，其中一个就是偏函数（Partial function）
    * 简单总结functools.partial的作用就是，把一个函数的某些参数给固定住（也就是设置默认值），返回一个新的函数，调用这个新函数会更简单。
    * 参数加在左边

* 继承
* 多重继承
    * mro = type(xx).__mro__ Method Resulution Order 可以看继承顺序

* scope
    * 全局变量 写在最外面的
    * PI = 3.14 python常量是可以改了，请自觉不要改
    * 引用函数外定义变量 global a

* module
    * import xxx
    * from ss import xxx
    * import xxx, sss
    * class _SecretSquirrel(object): 这种被module hide了，import后没法调用
    * duck._sss() 这种可以调用 module里面的hide不影响调用 除非class是hide情况
    * __all__ = ( 'Goat', '_Velociraptor') 这样可以访问_velociraptor这个类


* package
    * __init__
    * __module__
        * 看函数是从哪个模块导入进来的 有时有重名的
    * __class__:
        * 获得已知对象的类 ： 对象.__class__
        * type 是个什么类啊
    * @classmethod
        * 普通的类方法foo()需要通过self参数隐式的传递当前类对象的实例。 @classmethod修饰的方法class_foo()需要通过cls参数传递当前类对象。@staticmethod修饰的方法定义与普通函数是一样的。
        * self和cls的区别不是强制的，只是PEP8中一种编程风格，slef通常用作实例方法的第一参数，cls通常用作类方法的第一参数。即通常用self来传递当前类对象的实例，cls传递当前类对象。
        * 我们要写一个只在类中运行而不在实例中运行的方法. 如果我们想让方法不在实例中运行
        * https://www.zhihu.com/question/20021164
        * 这样的好处是: 不管这个方式是从实例调用还是从类调用，它都用第一个参数把类传递过来.
        * 显式调用
            * fido.__class__.a_class_method()
        * 隐式调用
            * fido.a_class_method()
    * @staticmethod
        * 经常有一些跟类有关系的功能但在运行时又不需要实例和类参与的情况下需要用到静态方法. 比如更改环境变量或者修改其他类的属性等能用到静态方法
    * 实例和类不共享实例参数， 实例和类共享类参数

* attribute
    * __getattribute__
        * 找不到会抛出异常 AttributeError xxx dont have attribute sss
        * 可以重定义__getattribute__
        * callable (Called when the instance is ''called'' as a function)
            * an instance of a class with a __call__ method or
            * is of a type that has a non null tp_call (c struct) member which indicates callability otherwise (such as in functions, methods etc.)
        * 改动__getattribute__会改变getattr(对象,'attr')的调用结果
        * self.xxxx 也会调用__getattribute__
    * getattr
        * only catch unkown attribute
    * __setattr__
        * 可以设定属性, 没有__init__那种

    * __get__,__getattr__和__getattribute都是访问属性的方法，但不太相同。
        * object.__getattr__(self, name) 
            * 当一般位置找不到attribute的时候，会调用getattr，返回一个值或AttributeError异常。
        * object.__getattribute__(self, name) 
            * 无条件被调用，通过实例访问属性。如果class中定义了__getattr__()，则__getattr__()不会被调用（除非显示调用或引发AttributeError异常） 
        * object.__get__(self, instance, owner) 
            * 如果class定义了它，则这个class就可以称为descriptor。owner是所有者的类，instance是访问descriptor的实例，如果不是通过实例访问，而是通过类访问的话，instance则为None。（descriptor的实例自己访问自己是不会触发__get__，而会触发__call__，只有descriptor作为其它类的属性才有意义。）
        * 可以看出，每次通过实例访问属性，都会经过__getattribute__函数。而当属性不存在时，仍然需要访问__getattribute__，不过接着要访问__getattr__。这就好像是一个异常处理函数。 
        * 每次访问descriptor（即实现了__get__的类），都会先经过__get__函数。
        * http://luozhaoyu.iteye.com/blog/1506426
        * https://docs.python.org/release/2.5.2/ref/attribute-access.html
            * __getattr__ 当调用不属于实例或者类的属性时调用
                * Called when an attribute lookup has not found the attribute in the usual places (i.e. it is not an instance attribute nor is it found in the class tree for self). name is the attribute name. This method should return the (computed) attribute value or raise an AttributeError exception.
            * __setattr__ class
                * Called when an attribute assignment is attempted. This is called instead of the normal mechanism (i.e. store the value in the instance dictionary). name is the attribute name, value is the value to be assigned to it.
                * If __setattr__() wants to assign to an instance attribute, it should not simply execute "self.name = value" -- this would cause a recursive call to itself. Instead, it should insert the value in the dictionary of instance attributes, e.g., "self.__dict__[name] = value". For new-style classes, rather than accessing the instance dictionary, it should call the base class method with the same name, for example, "object.__setattr__(self, name, value)".
                * 设置实例属性时 "self.__dict__[name] = value".
                * 设置类属性 "self.name = value"
            * __getattribute__( self, name)
                * Called unconditionally to implement attribute accesses for instances of the class. If the class also defines __getattr__(), the latter will not be called unless __getattribute__() either calls it explicitly or raises an AttributeError. This method should return the (computed) attribute value or raise an AttributeError exception. In order to avoid infinite recursion in this method, its implementation should always call the base class method with the same name to access any attributes it needs, for example, "object.__getattribute__(self, name)".

        * 其他
            * __getattr__
                * 属性没有找到时 被调用 
                * 通过self.attr访问属性 会造成无限递归错误
            * __getattribute__
                * 随时被调用
                * self.attr访问 递归错误
                * Attribute错误时调用__getattr__
            * __setattr__
                * 对实例属性赋值
            * https://www.cnblogs.com/elie/p/6685429.html
            * https://www.cnblogs.com/wwxbi/p/7751778.html

         
* del
    * 可以删数组元素 可以删整个数组
    * 可以删class下面的方法
        * "'ClosingSale' object has no attribute 'toilet_brushes'"
    * 可以删对象的方法
        * "'ClosingSale' object has no attribute 'hamsters'"

* property
    * property()函数中的三个函数分别对应的是获取属性的方法、设置属性的方法以及删除属性的方法，这样一来，外部的对象就可以通过访问x的方式，来达到获取、设置或删除属性的目的。
    * https://www.cnblogs.com/paomaliuju/p/5122761.html

* proxy class
    *      


