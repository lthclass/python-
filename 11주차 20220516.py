'''
import random

# 정답이 되는 네 자리수 선택
while True:
    number = str(random.randint(1000, 9999))
    if len(list(set(number))) == 4: # 중복된 자릿수가 없는 경우 숫자 선택
        break

# 게임 진행
attempt = 0
while True:
    # 예외 처리
    try:
        ans = int(input('네자리 숫자를 입력해 주세요 : '))
        ans = str(ans)
        if len(ans) != 4:
            print('네자리 숫자가 아닙니다.')
            continue
    except:
        print('올바른 형태를 입력해주세요.')
        continue
    
    # 스트라이크, 볼 판정
    attempt += 1
    strike = 0
    ball = 0
    for i in range(4):
        if ans[i] == number[i]:
            strike += 1
        if ans[i] == number[(i + 1) % 4] or ans[i] == number[(i + 2) % 4] or ans[i] == number[(i + 3) % 4]:
            ball += 1
    if strike == 0 and ball == 0: print('아웃입니다!')
    elif strike == 4:
        print('정답입니다! 총 시도 횟수는 %d회 입니다'%attempt)
        break
    else:
        print('%d스트라이크 %d볼 입니다.'%(strike, ball))

'''
'''
import random #램덤 추가
st=0          #스트라이크 카운트
c=0           #시도횟수 카운트
a=[]        
while len(a)<3 : #a의 갯구가 3미만일동안
      r=str(random.randint(0,9)) #srt=문자열, r안에 0~9까지 수자입력
      if not(r in a) :  #a안에 r이 없을때
            a.append(r) #a에 r추가
            
while st<3 : #스트라이크가 3미만일때
      st=0   #스트라이크 초기화
      ba=0   #볼 초기화
      o=0    #아웃 초기화
      r=str(input("세개의 숫자를 입력하시오(ex:123) :"))
      for i in range(0,3) :
            for x in range(0,3) :
                #리스트 r의 i
                if r[i]==a[x] and i==x :
                     st+=1
                elif r[i]==a[x] and i!=x :
                      ba+=1
      o=3-(ba+st)
      print(f"스트라이크{st}, 볼:{ba}, 아웃{o}")
      c+=1
print("정답입니다 시도횟수:",c)
'''



import random #램덤 함수를 추가시킨다.
st=0  #스트라이크 변수 지정
c=0   #시도횟수 카운트
a=[]  
while len(a)<3: # len은 리스트 숫자를 센다 3미만
      r=str(random.randint(0,9)) #무작위로 0.9까지 숫자착출 (str은 문자열로 변환)
      if not (r in a): # a의 안에 r이 없을떄 
            a.append(r) #a안에 r을 포함시키는거

while st<3: # 스트라이크 3미만
      st=0  # 스트라이크 초기화
      ba=0  # 볼 초기화
      o=0   # 아웃 초기화
      r=str(input("세개의 숫자를 입렵하세요:")) #세개의 숫자를 입력받음
      for i in range (0,3): # i 0에서2까지 반복
            for x in range (0,3): # x 0에서2까지 반복
                  if r[i]==a[x] and i==x: #만약 r에 i번째랑 a의 x번째가 같고 i랑 x같을때
                        st+=1     #스트라이크 1씩증가
                  elif r[i]==a[x] and i!=x:#만약 r에 i번째랑 a의 x번째가 같고 i랑 x 다를때
                        ba+=1     #볼 1씩증가
      o=3-(st+ba) #아웃은 3에서 스트라이크랑 볼 더한값 빼기
      print(f"스트라이크{st}, 볼{ba}, 아웃{o}")
      c+=1 #시도횟수 1중가
print("정답입니다 시도횟수:",c) #c도 출력


