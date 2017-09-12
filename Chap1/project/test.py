
def test(a,b,c):
    #print(a)
    d = a+b+c
    print(d,'d')
    return d

def test1(d,b):
    c = d + b
    print(c,'c')
    return c

dragon = test(1,2,3)
easy = test1(dragon,5)

# 类似实例的感觉，怎么用就怎么写
# 如果需要在别的函数引用他的返回值，那就需要用 return 接收它

# ---

# 梳理逻辑、切片
# 明确输入、输出
# 明确各片段输入、输出如何衔接
