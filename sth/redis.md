## Redis

和普通的Key-Value结构不同，Redis的Key支持灵活的数据结构，除了strings，还有hashes、lists、 sets 和sorted sets等结构。正是这些灵活的数据结构，丰富了Redis的应用场景，能满足更多业务上的灵活存储需求。

Redis的数据都保存在内存中，而且底层实现上是自己写了epoll event loop部分，而没有采用开源的libevent等通用框架，所以读写效率很高。为了实现数据的持久化，Redis支持定期刷新(可通过配置实现)或写日志的方式来保存数据到磁盘。

### 1. 数据类型
    
作为Key-value型数据库，Redis也提供了键(Key)和键值(Value)的映射关系。但是，除了常规的数值或字符串，Redis的键值(value)还可以是以下形式之一：

    * Lists (列表)

　　* Sets (集合)

　　* Sorted sets (有序集合)

　　* Hashes (哈希表)

键值的数据类型决定了该键值支持的操作。Redis支持诸如列表、集合或有序集合的交集、并集、查集等高级原子操作;同时，如果键值的类型是普通数字，Redis则提供自增等原子操作。

### 2. 持久化

通常，Redis将数据存储于内存中，或被配置为使用虚拟内存。通过两种方式可以实现数据持久化：使用截图的方式，将内存中的数据不断写入磁盘;或使用类似MySQL的日志方式，记录每次更新的日志。前者性能较高，但是可能会引起一定程度的数据丢失;后者相反。


### 3. 补充原文

http://langgufu.iteye.com/blog/1434408

https://www.2cto.com/database/201501/372410.html

### 4. 各类型及基本操作

1. strings类型及操作

    * string是最简单的类型，你可以理解成与Memcached是一模一样的类型，一个key对应一个value，其上支持的操作与Memcached的操作类似。但它的功能更丰富。

    * msetnx key2 HongWan2_new key3 HongWan3

2. hash

    * Redis hash是一个string类型的field和value的映射表.它的添加、删除操作都是O(1)(平均)。hash特别适合用于存储对象。相较于将对象的每个字段存成单个string类型。将一个对象存储在hash类型中会占用更少的内存，并且可以更方便的存取整个对象。省内存的原因是新建一个hash对象时开始是用zipmap(又称为small hash)来存储的。这个zipmap其实并不是hash table，但是zipmap相比正常的hash实现可以节省不少hash本身需要的一些元数据存储开销。尽管zipmap的添加，删除，查找都是O(n)，但是由于一般对象的field数量都不太多。所以使用zipmap也是很快的,也就是说添加删除平均还是O(1)。如果field或者value的大小超出一定限制后，Redis会在内部自动将zipmap替换成正常的hash实现.
    * hmset myhash field1 Hello field2 World

3. list

    * Redis的list类型其实就是一个每个子元素都是string类型的双向链表。链表的最大长度是(2的32次方)。我们可以通过push,pop操作从链表的头部或者尾部添加删除元素。这使得list既可以用作栈，也可以用作队列。

    * lpush
        * 在key对应list的头部添加字符串元素：
        * lpush mylist "world"

    * rpush
        * 在key对应list的尾部添加字符串元素：
        * rpush mylist2 "hello"

4. sets

    * Redis的set是string类型的无序集合。set元素最大可以包含(2的32次方)个元素。
    * set的是通过hash table实现的，所以添加、删除和查找的复杂度都是O(1)。hash table会随着添加或者删除自动的调整大小。需要注意的是调整hash table大小时候需要同步(获取写锁)会阻塞其他读写操作，可能不久后就会改用跳表(skip list)来实现，跳表已经在sorted set中使用了。关于set集合类型除了基本的添加删除操作，其他有用的操作还包含集合的取并集(union)，交集(intersection)，差集(difference)。通过这些操作可以很容易的实现sns中的好友推荐和blog的tag功能。下面详细介绍set相关命令：
    * sadd myset "hello"

5. sorted sets

    * 和set一样sorted set也是string类型元素的集合，不同的是每个元素都会关联一个double类型的score。sorted set的实现是skip list和hash table的混合体。
    * 当元素被添加到集合中时，一个元素到score的映射被添加到hash table中，所以给定一个元素获取score的开销是O(1),另一个score到元素的映射被添加到skip list，并按照score排序，所以就可以有序的获取集合中的元素。添加，删除操作开销都是O(log(N))和skip list的开销一致,redis的skip list实现用的是双向链表,这样就可以逆序从尾部取元素。sorted set最经常的使用方式应该是作为索引来使用.我们可以把要排序的字段作为score存储，对象的id当元素存储。下面是sorted set相关命令
    * zadd
        * 向名称为key的zset中添加元素member，score用于排序。如果该元素已经存在，则根据score更新该元素的顺序
        * zadd myzset 1 "one"
