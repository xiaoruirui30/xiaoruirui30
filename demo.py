a = 10


def fun():
    global a
    a = 30
    print(id(a))
    print(f"这是一个变量：{a}")
    print("这是一个方法")
    return


print(fun())
if __name__ == '__main__':
    print("start")
    fun()

"""
拥有礼物的标识
定义发礼物的方法
定义展示礼物的方法
启动方法

"""

have_gift = False


def send():
    print("发礼物啦")
    global have_gift
    ()
    have_gift = True


def show():
    if have_gift == True:
        print("礼物不错")
    else:
        print("没有礼物")


if __name__ == '__main__':
    send()
    show()
