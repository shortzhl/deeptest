class Fib(object):
    def __init__(self):
        self.a = 0  # 初始化两个计数器a，b
        self.b = 1
    def __iter__(self):
        return self #实例本身就是迭代对象，故返回自己
    def __next__(self):
        self.a,self.b=self.b,self.a+self.b
        if self.a>10000: # 退出循环的条件
            raise StopAsyncIteration()
        return self.a

for n in Fib():
    print(n)


