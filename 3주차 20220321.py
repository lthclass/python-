'''
2022_03_21
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
a = float(input("키(cm);"))
b = float(input("몸무게(kg);"))


a = float(a/100)
print( b/ (a*a))


'''



a=float(input("키(cm);"))
b=float(input("몸무게(kg);"))

a = float( a/100)
print(b /(a*a))

