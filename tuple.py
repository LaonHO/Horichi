# tuple은 단일개체일떄 t={1,}/t = 1,2,3,4/

#인덱싱 
t1 = (1,2,'a','b')
t1[0] => 1
t1[3] =>'b'

#슬라이싱
t1 = (1,2,'a','b')
t1[1:] => (2,'a','b')

#tuple 더하기
t2 = {3,4)
t1 + t2 => (1,2,'a','b',3,4)

#tuple 곱하기 
t2*3 => (3,4,3,4,3,4)



#딕셔너리  기본 dic = {'name':'pey', 'phone':'0119993323', 'birth': '1118'}

a = {1: 'hi'} ===>Key로 정수값 1, Value로 'hi'라는 문자열
a = { 'a': [1,2,3]}====>Value에 리스트

#딕셔너리 쌍 추가 
a = {1:'a'}
a[2] = 'b' ==> {2:'b',1:'a'}
a['name'] = 'pey'
==> {'name':'pey',2:'b',1:'a'}
a[3] = [1,2,3]
==>{'name': 'pey', 3: [1, 2, 3], 2: 'b', 1: 'a'}

질문필요