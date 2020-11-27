import money
import sendmoney


def select_money():
    if sendmoney.send is True:
        print(f"工资余额为：{money.saved_money + 1000} ")
    else:
        print(f"工资余额为：{money.saved_money} ")
