
print("튜플")
x= ('a','b','c')
y = (1,3,4,5)
z = (1,"hello","there")

print(x+y)
print(y)
print(z)
print(z.index("hello"))

#튜플과 리스트의 차이. assignment가 안됨

#x[1]=3 튜플은 불변이다. 처음 선언해서 변할 수 없다.
#리스트는 가변이다.

print("딕셔너리")
x = {
  "name":"Jeongwoo",
  "age":20
}
y = {
  0 :"Jeongwoo",
  1 :20
}
print(x)
print(x["name"])
print(x["age"])
print(y)
print(y[0])
print(y[1])
print("age"in x)
print("Jeongwoo" in x ) # 키 값만 검사할 수 있다.
print(x.keys())

for key in x:
  print(key+":" + str(x[key]))

y[0]="Wonhee" # 딕셔너리는 가변이다.
print(y)
x["school"] = "inha" # 새로운 키와 값 추가
print(x)