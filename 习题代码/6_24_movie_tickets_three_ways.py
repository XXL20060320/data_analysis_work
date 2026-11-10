# 练习 2：三种出路


def ticket_message(age):
    if age < 3:
        return "免费"
    elif age <= 12:
        return "10 美元"
    else:
        return "15 美元"


print("=== 方式一：用条件测试结束循环 ===")
age = input("请输入观众年龄（输入 quit 退出）：")
while age != 'quit':
    print(f"  票价：{ticket_message(int(age))}")
    age = input("请输入观众年龄（输入 quit 退出）：")

print("\n=== 方式二：用变量 active 控制 ===")
active = True
while active:
    age = input("请输入观众年龄（输入 quit 退出）：")
    if age == 'quit':
        active = False
    else:
        print(f"  票价：{ticket_message(int(age))}")

print("\n=== 方式三：用 break 退出 ===")
while True:
    age = input("请输入观众年龄（输入 quit 退出）：")
    if age == 'quit':
        break
    print(f"  票价：{ticket_message(int(age))}")
