#Class Example

#Pillars of OPP -- Inheritance, Polymorphism, Encapsulation and Abstraction

class Person:
    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age

    def greeting(self):
        return f'Hi, my name is {self.name} and I am {self.age} yo.\nNice to meet you!'

class Banking_Persons_Account(Person):
    def __init__(self, money) -> None:
        self.__money = money
    
    def taking_money(self, value):
        if value > 0 and value <= self.__money:
            self.__money -= value

    def see_money_account(self):
        return f'Here is your money in banking: {self.__money}'



#objects
person1 = Person("Leandro", 24)
#print(person1.greeting())

leandro = Banking_Persons_Account(2000)
leandro.taking_money(500)
print(leandro.see_money_account())
