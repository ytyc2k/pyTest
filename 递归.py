'''
阶乘递归
5*4*3*2*1=120
'''
def factorial(n):
    if n < 0:
        raise ValueError("n must be a non-negative integer")
    if n<2:
        return 1
    return n * factorial(n - 1)

# 示例
number = 5
print(f"{number}! = {factorial(number)}")
