装饰器模式用于给对象在运行期间动态的增加某个功能。比如，在被装饰者前面或者后面加上自己的行为以达到特定的目的

### 装饰器与代理的区别

装饰器模式，原有的不能满足现有的需求，对原有的进行增强。

代理模式，同一个类而去调用另一个类的方法，不对这个方法进行直接操作。

装饰器模式关注于在一个对象上动态的添加方法，然而代理模式关注于控制对对象的访问。

代理模式是与原对象实现同一个接口，必须要实现原接口和持有真实的对象，才能称之为代理类。代理模式一定是自身持有这个对象，不需要从外部传入。用代理模式，代理类可以对它的客户隐藏一个对象的具体信息。因此，当使用代理模式的时候，我们常常在一个代理类中创建一个对象的实例。

装饰模式的一定是从外部传入，并且可以没有顺序，按照代码的实际需求随意挑换顺序。当我们使用装饰器模式的时候，我们通常的做法是将原始对象作为一个参数传给装饰者的构造器。

```
function People() {

};
People.sayHi = () => {
  console.log('Hi');
}

// 装饰器模式
function Decorator(person){
  this.person = person;
}
Decorator.sayHi = function() {
  console.log('嗨');
  this.person.sayHi();
}

const person = new People();
const decoPerson = new Decorator(person);
decoPerson.sayHi();


// 代理模式
function ProxyPeople() {
  this.person = new People();
}
ProxyPeople.sayHi = function() {
  console.log('嗨');
  this.person.sayHi();
}

const proxyPerson = new ProxyPeople();
proxyPerson.sayHi();

```
### 总结

- 装饰类和被装饰类独立，解耦，把类（函数）的核心职责和装饰功能区分开了。
- 装饰模式是继承的一个替代模式，装饰模式可以动态扩展一个实现类的功能。

### 补充

http://www.cnblogs.com/TomXu/archive/2012/02/24/2353434.html

http://blog.csdn.net/zhang31jian/article/details/50538000
