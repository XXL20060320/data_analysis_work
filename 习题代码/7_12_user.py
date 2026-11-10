# 练习 3：用户
class User:
    """模拟一个用户。"""

    def __init__(self, first_name, last_name, age, city, email):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.city = city
        self.email = email

    def describe_user(self):
        print(f"姓名：{self.first_name} {self.last_name}")
        print(f"年龄：{self.age}　城市：{self.city}　邮箱：{self.email}")

    def greet_user(self):
        print(f"你好，{self.first_name} {self.last_name}，欢迎回来！")


users = [
    User('Ming', 'Li', 23, 'Lanzhou', 'ming.li@example.com'),
    User('Xiaohong', 'Wang', 31, 'Shanghai', 'xiaohong.wang@example.com'),
    User('Alice', 'Smith', 26, 'New York', 'alice@example.com'),
]

for user in users:
    user.describe_user()
    user.greet_user()
    print()
