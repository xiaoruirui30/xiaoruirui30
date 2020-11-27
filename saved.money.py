# 存款变量

# 定义发工资变量
def send_money(saved_money=1000):
    send_money = 3000
    saved_money = saved_money + send_money
    print(f"发工资了，发放数目为{saved_money}")


# 定义工资展示
def select_money():
    if saved_money > 1000:
        select_money = saved_money
        print(f"发工资了，工资余额为{select_money}")
    else:
        print(f"没有发工资，工资余额为{select_money}")


if __name__ == '__main__':
    send_money()
    select_money()
