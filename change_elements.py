'''
hello
'''
ls=[1,2,3,4,6,10,12,13,15,16,30]
dic={3:'3',5:'5'}
def ch(n):
    if n%3==0:
        return f'{dic[3]}*{str(n//3)}'
    elif n%5==0:
        return f'{dic[5]}*{str(n//3)}'
    else:
        return n
lst=[ch(i) for i in ls]
print(lst)