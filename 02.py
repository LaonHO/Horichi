print('python 실습입니다')
#=>print " "
name = '장재영 입니다.'
age = input()	
#raw_input() input python 2.7      input=키보드입력
print(name)
print(age)
print(type(age))# age
print(type(name))
#멀티라인
print(""" sakdnasdsdsdlkm
dasdsdasndalksdmlsad
asdassadasdsdsdasdsa""")

aa= len(age)  # len= 문자열의 길이 겁사
print("aa:",aa)
if(int(age)>=100):
	print("age %d 크다.",int(age))
else:
	print("age의 type:",type(age))
	print("제 나이는 %d 이고 %s ." % (int(age),name))

print(age*10)


# %f = 실수
# %d = 정수
# %c = 문자형
# %s = 문자열
# %o = 8진수
# %x = 16진수


B = 13513135.1321531
print('실수 %d' %B)
print('실수 %f' %B)

