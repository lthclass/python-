'''
2022_03_14
2주차 수업
'''
'''

print('hello') ;
print("hello") ;

print( "He's name is 태현")
print( 'He said "I am Ok!" ')

print( "He said \ " I am OK!\" ")
'''
'''
print("a" * 10)

print("=" * 25)
print( 'He said "python is Easy" ')
print("34256곱하기 2365 는", 34256*2365, "입니다")
print("=" * 25)

print("A")
print("B")
'''
'''
#\n은 new line을 의미
print("A\nBC\nDEF") 
'''
#=====문자열 슬라이싱(slice)=====
#print("Hello"[0])
#print("Hello"[1])
print("Hello"[-1]) #뒤에서 첫글자
print("Hello"[0:3]) #0<=범위 <3 까지 출력

'''
a=input(_) #a는 입력된 숫자를 가리킴
print(a) #a가 가리키는 것을 출력
'''
'''
b="2022년 3월 14일"
print(b)
'''
'''
b=input("오늘날짜입력:");

# 01234 567 8910 
# 2035년01월31일

print(b[0:4])
print(b[5:7])
print(b[8:10])
'''
'''
b=input("태어난연도입력:");
#b가 문자열인지 숫자 인지 알아보기
print ( type(b) )

#나이 출력하기
#문자를 숫자로 바꿔줍니다.
print('당신의나이는',2022-int(b), '입니다')
'''
'''
b=input("태어난연도입력:");
print('당신의 한국나이는',2022-int(b)+1,'살 입니다')
print('만으로는',2022-int(b),'살 입니다')
'''
'''
a= 1333; #a가 133을 가리킴
a= 123;  #a가 123을 가리킴

#a가 가리키는 것에 100을 더한 값을 a가 가리킴
a= a+100
print(a) #현재 a는 223을 가리킴, 그 값을 출력

a-=3; #a가 가리키는 값에서 3을 뺌, 그리고 그값 가리킴
a+=3; #a가 가리키는 값에 3을 더함, 그리고 그값 가리킴

b=100 
#a가 가리키는 값을 4배 함, 그리고 그 값 가리키기
b*=4;
'''
'''
a=100;
b=2;
c=2;

print(a+b*c) # 예상되는 결과값 : 104

print( (a+b)*c) # 예상되는 결과값 : 204
'''
a= int( input("첫번쨰 숫자 입력:") )
b= int( input("두번쨰 숫자 입력:") )
      

print(a+b)
print(a*b)
print(a-b) 

