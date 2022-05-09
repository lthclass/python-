
'''
BD=['a','k','__','m','L']  #___는 빈자리를 의미

r=2 # 빈자리의 번호가 현재 2번 임

print(BD)
while( BD != ['A', 'K', 'M', 'L', '__']):
      
      k=input('a 또는 d를입력:')
      
      if k=='a' and r > 0:
             BD[r],BD[r-1] = BD[r-1],BD[r] #왼쪽으로 서로 값 바꾸기

      elif k=='d' and r < 4:
             BD[r],BD[r+1] = BD[r+1],BD[r] #오른쪽으으로 서로 값 바꾸기
      
      print(BD)
'''


'''*
DB=['A','B','__','C','D']

 

r=2

 

print(DB)

 

while (DB != ['A','B','C','D','__']):

 

    k=input("a 또는 b 입력:")

 

    if k=='a' and r>0:

        DB[r],DB[r-1]=DB[r-1],DB[r]

        r-=1

    elif k=='d' and r<4:

        DB[r],DB[r+1]=DB[r+1],DB[r]

        r+=1

    print(DB)
'''


'''
정답
XXX 서로다른 1~9사이의 숫자 3개

사람1
345 0s 0b 3out

897 0s 3b 0out

798 1s 2b 3out
'''

import random #random 도구상자를 내 코드에 불어오겠다.



aList=[] #비어있는 리스트 만들기

aList.append(random.randint(1,9)) #1~5사이의 임의의 숫자를 a에 추가

while len(aList)<3: #aList안의 요소 갯수가 3개보다 작으면 반복

       r=random.randint(1,9)

      
#만약 r값이 aList에 들어있는 것이 아니라면
       if not(r in aList):
           aList.append(r) # r을 aList에 추가[?,?,
print(aList)

#램덤 모듈을 불러온다

#비어있는 리스트를 만든다.

#1-9사이의 임의의 숫자를 리스트에 넣는다.

#리스트안의 숫자 갯수가 3개보다 작다면 반복한다.

#임의의 숫자 하나를 변수r이 가리키게 한다.

#만약 r이 가리키는 숫자가 리스트안에 없다면

#그 숫자를 추가시킨다.

#숫자 3개를 입력받아 힌트를 출력한다. <== 코드로 작성하기
import random

a=list( range(1,101) ) #1~100사이의 숫자를 리스트로 만들기

a=[1,2,3,4,5,6,7,8,9]

random.shuffle(a) #a리스트 섞기

a=a[0:3] # 인덱스 0,1,2번 만 a리스로 하기

print(a)

n1,n2,n3 = input('숫자 3개 입력(띄어쓰기구분)').split(' ')
n1 = int(n1)
n2 = int(n2)
n3 = int(n3)

print(n1,n2,n3)

if n1 in a:
      if n1==a[0]:
            s+=1
      else
           b+=1

else:
      o+=1
      
