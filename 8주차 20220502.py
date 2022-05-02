'''
'''
a = 49
b = 3
c = 0

while a >= b:
      a-=b
      c+=1

print(f'한사람의 몫은 {c} 입니다.')
print(f'남은사과는 {a}입니다.')
'''

#게임

BOARD=[ [1,2,3],
      [4,0,6],
      [7,8,5]]

#화면에 보드 상태 보여주기
print(BOARD[0])
print(BOARD[1])
print(BOARD[2])

r=1
c=1



#만약  key값이  d와 같다면  
#BOARD[2] [2]과 BOARD[2] [1]를 서로 바꾸기


while True:
      key=input('wasd중에 하나입력')
      if key=='d':
            BOARD[r][c],BOARD[r][c+1] =  BOARD[r][c+1],BOARD[c][c]
            r=r
            c=c+1

            
      if key=='a':
            BOARD[r][c],BOARD[r][c-1] =  BOARD[r][c-1],BOARD[r][c] 
            r=1
            c-=1
            
      if key=='w':
            BOARD[r-1][c],BOARD[r][c] =  BOARD[r][c],BOARD[r-1][c] 
            r-=1
            c=1

      if key=='s':
            BOARD[r+1][c],BOARD[r][c] =  BOARD[r][c],BOARD[r+1][c] 
            r+=1
            c=1
      print(BOARD[0])
      print(BOARD[1])
      print(BOARD[2])

