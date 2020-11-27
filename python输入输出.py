# name ="zhangrui"
# print(f"my name is {name.upper()}")

# print(f'result is {(lambda x:x+1)(10)}')


# x=10
# print(f"result is {x**2}")

# f=open('123.txt')
# print(f.readable())
# # print(f.readlines())
# print(f.readline())
# print(f.readline())
# print(f.readline())
# f.close()

with open('123.txt') as f:
    while True:
        line = f.readline()
        if line:
            print(line)
        else:
            break
    # print(f.readline())
