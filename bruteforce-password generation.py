import itertools

numlist = '0123456789'

'''
#for문을 활용한 3자리 패스워드 출력 0부터 999까지 
for i in numlist:
    for j in numlist:
        for k in numlist:
            print(i,j,k)
'''

aa=''
for password in itertools.product(numlist, repeat=1):
    aa += ''.join(password)+','
    
#print(aa[:-1],end="")

file = open('passwordlist.txt','w')
file.write(aa[:-1])
file.close()
