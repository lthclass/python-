
'''
2022_03_28
4주차 수업
'''

'''
# b 가 비어있는 상자 (list)를 가리킴

b=[]

b.append(10) # .d은 "~의", append()는 "추가동작"를 의미
print(b)

#b리스트의 마지막에 20 추가하기
b.append(20)
print(b)

b.append(30)
b.append(40)

#b의 각 요소 출력하기
print(b[0], b[1], b[2], b[3])
'''
'''
c=[10,20,30,40]
print(c)

#자료의 종류에 상관없이 담을 수 있다.
d=[10, 3.14, "hello"]

#d요소의 갯수 알아보기
#len()는 길이를 알아내는 동작을 의미
print( len(d) ) #length(길이)의 첫3글자

myroom=["스탠드","책상",405,"책"]

a= [10, 20, 30]
a[0] = 1000; #a[0]의 요소값을 바꾸기

print(a)

del a[0]; #a[0]요소의 값 지우기
print(a)

a.append(44)
print(a)

b=[0,1,2,3,4,5,6]

b[0:3]=[] # 0<= 범위 < 3의 요소 지우기
print(b)

b[0:2]=[100,200] #0<= 범위 <2 요소값 바꾸기
print(b)
'''
'''
c=[1,2,3]
d=[4,5,6] #c리스트와 d리스트 합치기
e= c+d

print(e)

k=[1,2,3]*4 #요소 1,2,3을 4번 반복한 리스트 만들기
print(k)
'''
'''
a=[1,2,3]


a리스트의 마지막 요소를 꺼내어,
b가 가리키도록 함

b= a.pop()
print(a) #a는 리스트를 가리키고
print(b) #b는 3이라는 값을 가리킴


c=[10,11,12,13]
c.pop(2)#c의 2번요소를 꺼내라.
print(c)
'''

'''
d=['a','b','c','d']
#a리스트에서 값 'c'를 찾아 그 인덱스 번호를 출력
print(d.index('c'))

# 인덱스 2번에 정수 30 끼어넣기
d.insert(2,30)
print(d)
'''
'''
a= [3,5,1,2,6]
#a의 요소 정렬하기
a.sort()
print(a)

b=[3,5,1,2,6]
#b요소의 순서 뒤집기
b.reverse()
print(b)

'''
'''
a= [1,2,3]
b=a;

print(a)
print(b)
'''

'''
#c가 가리키는 리스트를 복사하여 d가 가리키킴
c=['a','b','c']
d=c[:]

print(c)
print(d)

c[0]='hello'

print(c)
print(d)
'''

'''
#슬라이스
#문자열 슬라이스
a="Hello"
b=a[0:4] #0<= 범위 < 4
print(b)

#리스트 슬라이스
a=['mon','tue','wed','thu','fri','sat']
b=a[:] #a리스트 전부
c=a[0:3] #0<=범위 <3
print(c)
c=a[0:] #0번부터 끝까지
c=a[:5] #처음부터 5번 인덱스 까지
c=a[::2] #2칸씩 띄엄띄엄
c=a[5:1:-1] #5번 인덱스에서 2번까지 거꾸로 1칸씩
print(c)
'''

'''
#문제

a=[ [1,2,3], ['a','b',11], 'python', 38.5]

#a리스트에서 py를 출력하도록 해봅시다.

c=a [2][0:2]
print(c)
'''

'''
 만약에 비오면 , 우산 챙겨라
 그렇지 않으면 , 양산 챙겨라
'''

'''
#짝수 홀수 구분 프로그램
n = int( input('숫자입력:'))
if n%2==0:
    print('짝수(even)')
else:
    print('홀수(odd)')
'''

'''
n = int(input('점수입력:'))

if n>=90:
      print('A')

if n>80:
      print('B')

if n>=70:
      print('c')
'''
'''
#그리고(뭉), 또는(ㅐㄱ)

if(12343 % 6==0 and 342%2==0):

    print('ok')
    

if(12343 % 6==0 or 342%2==0):
    print('okkkkk')
'''
#문제
'''
자연수를 하나를 입력받아
2의 배수인지, 3의 배수인지,
6의 배수인지, 판단해주는 프러그램을
작성해 봅시다.
ex)
입력:12
출력:6의 배수 입니다.
'''
'''
a = int(input('자연수입력:'))

if a%2==0:
      print('2의배수')
if a%3==0:
      print('3의배수')
if a%6==0:
      print('6의배수')
print("입니다")
'''
'''
n = int(input('자연수 입력:'))

if n%6==0:
      print('6의배수')
elif n%3==0:
      print('3의배수')
elif n%2==0:
      print('2의배수')
print("입니다")

'''
'''
n= int(input('자연수입력:'))

if n%6==0:
      print('6의배수')

elif n%3==0:
      print('3의배수')

elif n%2==0:
      print('2의배수')

'''

'''
n=int(input('자연수입력:'))

if n%6==0:
      print('6의배수')
elif n%3==0:
      print('3의배수')
elif n%2==0:
      print('2의배수')

'''
'''
n=int(input('자연수입력:'))

if n%6==0:
  print('6의배수')

elif n%3==0:
  print('3의배수')
  
elif n%2==0:
  print('2의배수')
'''

'''
n= int(input('자연수입력'))

if n%6==0:
      print('6의배수')
      

elif n%3==0:
      print('3의배수')
      

elif n%2==0:
      print('2의배수')
      
'''
