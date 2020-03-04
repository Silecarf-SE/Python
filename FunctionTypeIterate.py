print("hello")

print("this is test python repo")

x=1
y=2
print(x+y)

x = 2
y = 2
z = 1.2

print(x + y)
print(x % y)
print(x**y)

a="hello"
b='bye'
print(a+' '+b)
z= """ 안녕하세요 공부중입니다. """
print (z)

print("난 "+str(28)+"살이야") # 캐스팅은 여기도 있다.
x=4
y="4"
print(str(x)+y)
print(x+int(y))
x=True;
y=False;
if not y and y or x:
  print("true")
else :
  print("false")
x=3

if x>5:
  print("x>=3")
elif x==3:
  print("x=3")
else:
  print("x<2")

def chat(name1,name2,point):
  print("%s : this is function test, %s" % (name1, name2))
  print("%s : this is fun. %d/10" % (name2,point))

chat("알렉스","윤하",9)

a=1
b=2
c=a+b

x=1
y=2
z=x+y
def dsum(left,right):
  result = left+right
  return result

d=dsum(9,2)
print(d)

def sayHello(name,age):
  if age<10:
    print("안녕 "+name)
  elif age<=20 and age>10:
    print("안녕하세요 "+name)
  else:
    print("안녕하십니까 "+name+"씨")


sayHello("윤하",8)
sayHello("철수",18)
sayHello("복순",58)
i=0
while i<5:
  print(i)
  i=i+1

for i in range(5):
  print(i)