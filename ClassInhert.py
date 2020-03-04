class Person:
  def __init__(self,name,age):
    self.name = name
    self.age = age
  def sayHello(self, to_name):
    print("hello!"+to_name+" I'm "+self.name)
  def introduce(self):
    print("내 이름은 "+ self.name +"그리고 나는 "+str(self.age)+"살이야")

p = Person("p",16)
steve = Person("steve",20)
p.sayHello("wonho")
steve.sayHello("p")
steve.introduce()

#inherit 상속
class Police(Person):
  def arrest(self,to_arrest):
    print("넌 체포됐다! "+ to_arrest)

class Programmer(Person):
  def program(self,to_program):
    print("다음엔 뭘 만들까?, "+to_program)

rachel = Programmer("Rachel",38)
rachel.introduce()
rachel.program("이메일 클라이언트?")

kim = Police("kim",29)
kim.introduce()
kim.arrest("park")