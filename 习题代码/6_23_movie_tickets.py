# 练习 1：电影票
while True:
    age = input("请输入观众年龄（输入 quit 退出）：")
    if age == 'quit':
        break

    age = int(age)
    if age < 3:
        print("  票价：免费。")
    elif age <= 12:
        print("  票价：10 美元。")
    else:
        print("  票价：15 美元。")
