##    반에서 랜덤하게 발표순서 정하기   ##
## 무작위로 선정하여 반별 파일로 생성하기 ##
## 매번 파일 생성 
## 대건고 정보교사 권순찬 

import random
import os.path

ban = input("1학년 몇반? : ")
# 파일 처리부분 ####
if os.path.isfile("1학년 "+ ban + "반 발표순서.txt"): # 반 파일이 있으면 추가, 없으면 생성
    print("파일이 이미 생성되어 있습니다. 확인해주세요")
else:
    f = open("1학년 "+ ban + "반 발표순서.txt", "w", encoding="utf8")
######
end = int(input("가장 끝 번호는 몇번 ? : "))
num = int(input("몇명을 뽑을까? : ")) 
sunseo = random.sample(range(1,end+1),num) # 1부터 end까지의 범위중에 num개를 중복없이 뽑겠다.
print(sunseo)
result = "1학년"+ ban + "반 : " + str(sunseo)
f.write(result)
f.write("\n")
f.close()