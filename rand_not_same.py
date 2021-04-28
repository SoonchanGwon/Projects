## 반에서 랜덤하게 발표순서 정하기
## 무작위로 선정하여 한 파일로 생성하기 
## 누적하여 추가 됨 
## 대건고 정보교사 권순찬 

import random
import os.path

ban = input("1학년 몇반? : ")
# 파일 처리부분 
if os.path.isfile("balpyo.txt"): # 발표 파일이 있으면 추가, 없으면 생성
    f = open("balpyo.txt", "a", encoding="utf8")
else:
    f = open("balpyo.txt", "w", encoding="utf8")
######
end = int(input("가장 끝 번호는 몇번 ? : "))
num = int(input("몇명을 뽑을까? : ")) 
result = random.sample(range(1,end+1),num) # 1부터 end까지의 범위중에 num개를 중복없이 뽑겠다.
print(result)
f.write("1학년 "+ ban + "반 : " + str(result))
f.write("\n")
f.close()