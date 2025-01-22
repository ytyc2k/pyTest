'''
阶乘递归
5*4*3*2*1=120
'''
def factorial(n):
    if n < 0:
        raise ValueError("n must be a non-negative integer")
    if n < 2:
        return 1
    return n * factorial(n - 1)

# 示例
number = 5
print(f"{number}! = {factorial(number)}")

def fs(n):
    global s
    if n < 0:
        raise ValueError("n must be a non-negative integer")
    if n < 2:
        s+='1'
        return 1
    s+=f'{n}*'
    return n*fs(n-1)
s=''
rs=fs(5)
print(f'{s}={rs}')