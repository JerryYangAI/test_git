#斐波那契数列的函数
def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b
#打印前10个斐波那契数
for num in fibonacci(10):
    print(num)
#输出结果:

a+b=c
