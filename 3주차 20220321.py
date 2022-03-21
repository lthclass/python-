
'''
2022_03_14
3주차 수업
'''

a = "200"

#a가 가리키는 자료의 종류를 출력
print (type(a))

'''
#a가 가리키는 자료를 정수로 변환후
#a가 그 값을 가리킴
a = int(a)


#문자열 "3.14"를 실수숫자로 바꾼 후
# b가 가리키도록 하는 코드 작성
b= float("3.14");
print( type(b))


#정수 3을 시수로 바꾸면 어떻게 될 까요?
c = float(3)
print(c) #정수 3은 실수 3.0으로 바뀝니다.
'''

'''
BMI (body measure index) /체질량 지수
bmi는 몸무게(kg)를 키(미터)의 제곱값으로 나눈 숫자

'''
#문제
'''
키와 몸무게를 입력으로 받아,
bmi값을 출력해주는 프로그램을 작성해 봅시다.
'''
'''
cm = float(input("키를 입력하시오(cm): "))    
kg = float(input("몸무게를 입력하시오(kg): "))    

cm = float(cm /100)
print(kg / (cm * cm))
'''
'''
a = float(input("키를 입력하세요(cm);"))
b = float(input("몸무게를 입력하세요(kg);"))

a = float( a / 100)
print( b / (a*a))

'''




'''
a = float(input("키(cm);"))
b = float(input("몸무게(kg);"))

a= float( a /100)
print(b / (a*a))
'''
'''
#print는 기본적으로 줄바꿈을 실행함
print("Hello") 
print("python")

#줄바꿈 하지 않을 경우 end를 활용합니다.
print("Hello", end="");
print("python");


#ead 를 이용하여 끝에 문자 추가 가능
print("Hello", end=":");
print("python");

#콤마는 스페이스 키로 구분되어 출력 됩니다.
print("a","b","c")


#sep는 구분 기호를 바굴 수 있습니다.
print("010", "1111", "1234", sep="-")
'''
'''
#문자열 format 지정하기
#format의 의미는 형식 (구조, 틀)

print(f'ㅑ am {27}years old')
              # 공간 10간 확보하기
print(f'ㅑ am {27:10}years old')

#가운데 정렬하여 출력하기
print(f'ㅑ am {27:^10}years old')

#자리 확보할 때 빈 공간을 특정 문자로 채우기
print(f'ㅑ am {27:=^10}years old')

#소수점 길이 지정하기(마지막 f는float을 의미)
print(f'PI is {3.141592:=^10.2f}')

#변수값을 형식에 맞춰 출력하기
weight=65
height=177.5

     #마지막에 \를 이용하면 다음줄에 이어서 코드 작성이 가능합니다.
print(f"몸무게는 {weight:^10}kg, \
키는 {height:^10.2f}cm 입니다")
'''
'''
a = 10
b = 20
print (a,b)

c, d = 30 , 40

print(c)
print(d)
'''
#가리키는 대상을 찾아 들어가보면 아무것도 없음
e=None;

a=100;
b=200;
print(a,b)


'''
변수 e를 이용하여 a와 b가 가리키는 값을
서로 바꾸는 코트를 작성해 봅시다.
'''
#두 변수의 값을 서로 바꾸는 코
a, b= b, a;

print(a,b)


