# ABS
import math


class Unit:
    unit_list = []
    def __init__(self,age:int,name:str):
        Unit.unit_list.append(self)
        self.age : int = age
        self.name : str = name

class BattleUnit(Unit):
    def __init__(self,age:int,name:str,power:int):
        super().__init__(age=age,name=name)
        self.power : int = power

    def hit_unit(self,other:Unit)->str:
        if not isinstance(other,Unit):
            return f"What u even hittin {self.name}? an {type(other)}? uh"
        if not isinstance(other,BattleUnit):
            return f"{self.name} won, as the other unit is incapable of violence and self defence"
        if isinstance(other,BattleUnit): # I am not going to delete object, as we are going to delve into that later xD
            return f"{self.name if self.power>=other.power else other.name} simply destroyed it's oponent..."

    def __abs__(self):
        self.__class__ = AbsoluteUnit
        self.__init__()
        return self

class AbsoluteUnit(BattleUnit):
    absolute_unit = None
    def __init__(self):
        if AbsoluteUnit.absolute_unit:
            raise EOFError('END OF FINANCES FOR AU')
        else:
            AbsoluteUnit.absolute_unit=self
            super().__init__(age=1337,name="Adonis" ,power=math.inf)

    @classmethod
    def goat_finder(cls):
        return cls.absolute_unit

    def hit_unit(self,other:Unit) ->str:
        return f"There can only be one outcome of battle between Absolute Unit and {type(other)}, fool"


m=BattleUnit(1,"marek",15)
d=BattleUnit(2,"darek",13)
print(abs(d).hit_unit(m))

# This is how You can create absolute Unit, rememba, there can only be one.
# btw have You noticed d became the Absolute Unit class?
print(type(d))

# AITER NOW
# ITS ASYNC ITERATOR, BUT WE CAN ALSO MAKE HIM OUR OWN THING

class Thing(BaseException):
    def __init__(self,*args,**kwargs):
        print(f"i dont care about Your {':'.join([*args])} and {kwargs}")
        print( "i can give you async iterator my boi, call aiter on me, i dare you")

    def __aiter__(self):
        return self

    async def __anext__(self):
        raise StopAsyncIteration
a=Thing()
aiter(a)



