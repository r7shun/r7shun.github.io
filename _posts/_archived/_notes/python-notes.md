---
tags: python
---

### @staticmethod in Python

- Python @staticmethod decorator is used to label a class method as a static method, which means that it can be called without >  instantiating the class first. It simply defines a normal function that is logically contained in the class for readability purposes. Here, we do not need to pass the class instance as the first argument via self, unlike other class functions.

    ~~~python
    class Student():
        def __init__(self, mark):
            self.mark = mark
        @staticmethod
        def find_min(mark):
            return min(mark, 100)
    print(Student.find_min(20))
    # output
    # 20
    ~~~


- Static methods can also be accessed via class instances or objects. For example :
    
    ~~~python
    class Bank():
        def __init__(self, balance):
            self.balance = balance
    
        @staticmethod
        def find_interest(loan_money, interest_rate):
            return loan_money * (1 + interest_rate)
    
    bank = Bank(1000)
    print(bank.find_interest(bank.balance, 0.3))
    ~~~

- Comparison between @staticmethod, @classmethod, instance method
  ![compatison](../assets/img/staticmethods.png)


### Abstract Method & Class in Python

#### Abstract Method
- An Abstract method is a method which is declared but does not have implementation such type of methods are called as abstract methods. In Python, we can declare an abstract method by using @abstractmethod decorator.

- This abstract method is present in the abc module in python, and hence, while declaring the abstract method, we have to import the abc module compulsory.

- Here the Child class is responsible for providing an implementation for the parent class abstract method.

#### Abstract Class
##### `class abc.ABC`
- The partially implemented classes are called an abstract class; every abstract class in python should be a child of ABC class, which is present in the abc module.
- The following example demonstrates the creation of parent abstract class defining an abstract method, which is partially implemented, creating child classes that are responsible for providing implementation to parent abstract class. These classes are called **concrete classes**. We cannot create an object to the abstract class, but we can create an object to the child's class.

    ~~~python
    from abc import ABC, abstractmethod
    class Vehicle(ABC):
        @abstractmethod
        def getNoOfWheels(Self):
            pass

    class Bus(Vehicle):   ##implementing parent abstract class by using child class
        def getNoOfWheels(self):
            return 6

    class Auto(Vehicle):   ##implementing parent abstract class by using child class
        def getNoOfWheels(self):
            return 3

    b=Bus()
    print(b.getNoOfWheels())


    a=Auto()
    print(a.getNoOfWheels())
    ~~~

##### `class abc.ABCMeta`
- Metaclass for defining Abstract Base Classes (ABCs).




### @property
  - 我们可以使用@property装饰器来创建只读属性，@property装饰器会将方法转换为相同名称的只读属性,可以与所定义的属性配合使用，这样可以防止属性被修改。
    ```python
    class DataSet(object):
    @property
    def method_with_property(self): ##含有@property
        return 15
    def method_without_property(self): ##不含@property
        return 15

    l = DataSet()
    print(l.method_with_property) # 加了@property后，可以用调用属性的形式来调用方法,后面不需要加（）。
    print(l.method_without_property())  #没有加@property , 必须使用正常的调用方法的形式，即在后面加()

    class DataSet(object):
    def __init__(self):
        self._images = 1
        self._labels = 2 #定义属性的名称
    @property
    def images(self): #方法加入@property后，这个方法相当于一个属性，这个属性可以让用户进行使用，而且用户有没办法随意修改。
        return self._images 
    @property
    def labels(self):
        return self._labels
    l = DataSet()
    #用户进行属性调用的时候，直接调用images即可，而不用知道属性名_images，因此用户无法更改属性，从而保护了类的属性。
    print(l.images) # 加了@property后，可以用调用属性的形式来调用方法,后面不需要加（）。
    ```

    - 还可以定义`@property_names.setter`和`@property_names.delter`