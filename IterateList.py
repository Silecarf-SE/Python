
i=0
while True:
  print(i)
  i=i+1
  if i>2:
    break

for i in range(100):
  print(i)
  if i==2:
    break

for i in range(6):
  if i==2 or i==5:
    continue
  print(i)

print("list")
x = list()
x = [1,2,3,[4,5,6,7,8]]
y = ["hah","aj","you"]
z = ["hello",1,2,3]
print(x[3][2])
print(x[-1][0])
print(x)
print(y)
print(z)

num_elements=len(x[-1])
print(num_elements)
y=sorted(y)
print(y)

for n in x:
  if isinstance(n, list):
    for m in n:
      print("in list"+str(m))
  else:
    print("not in list"+str(n))

x=[4,2,3,1]

print(y.index("aj"))
if "hello"in y:
  print("hello 있어")
else:
  print("hello 없어")
if "hah"in y:
  print("hah 있어")

