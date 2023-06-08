# (콘솔로부터) 입력을 받아서 입력값을 변수에 저장
## input 함수 사용하기
# input() # in - put.
# a = input() # input -> (실행창을 통해) 입력을 받으면 -> a라고 하는 변수에 저장
# print(a) # a를 출력.
# input의 결과를 변수에 할당
# 가이드 메시지를 입력
# x = input("오늘은 무엇을 드셨습니까?: ")
# print(x)
# 입력은 input, 출력은 print. (표준입출력)
# input("...여기안에 문자열...") <- 프롬프트(prompt)
# -> 사용자에게 입력받는 값의 용도를 알려줄 때 사용

# 입력 값을 변수 두 개에 저장하기
'''
* input 한 번에 값을 여러 개 입력 받으려면,
  input에 split을 사용하여 변수 여러 개에 저장.
  (각 변수는 콤마로 구분)
* 변수1, 변수2 = input().split()
* 변수1, 변수2 = input().split('기준문자열')
* 변수1, 변수2 = input('문자열').split()
* 변수1, 변수2 = input('문자열').split('기준문자열')
'''

# a, b = input('문자열 두 개를 입력하세요: ').split()
# split() -> 입력받은 값(input)을 공백(스페이스) 기준으로 분리
# print(a, b)

# 두 숫자를 한번에 입력 받아서 합 구하기
''' 
a,b = input("숫자 두 개를 입력하세요 (스페이스로구분): ").split()
print(a+b)

a = int(a)
b = int(b)

print(a+b)
'''

# map을 사용하여 정수로 변환
# map -> 지도. / 사상. -> 2개 이상 쌍을 짝짓는다
'''
map에 int와 input().split()을 넣으면 split의 결과를 모두 int로 변환(실수로 변환할 때는 int 대신 float를 넣음)
변수1, 변수2 = map(int, input().split()) # space -> 공백으로 구분되어 있다면 각각 쪼개주는 역할
변수1, 변수2 = map(int, input().split('기준문자열'))
변수1, 변수2 = map(int, input('문자열').split())
변수1, 변수2 = map(int, input('문자열').split('기준문자열'))
'''
# map(짝지을 함수이름, 대상이 되는 여러 값들)
a, b = map(int, input("숫자 두 개를 입력하세요 (스페이스로 구분): ").split())
print(a + b)  # 37, 29 -> 66
a, b = map(int, input("숫자 두 개를 입력하세요 (콤마(,) 구분): ").split(','))
print(a + b)  # 37, 29 -> 66