# 练习 5：尝试登录次数
class User:
    """模拟一个用户。"""

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.login_attempts = 0

    def describe_user(self):
        print(f"用户：{self.first_name} {self.last_name}")

    def greet_user(self):
        print(f"你好，{self.first_name}！")

    def increment_login_attempts(self):
        """登录次数加 1。"""
        self.login_attempts += 1

    def reset_login_attempts(self):
        """将登录次数重置为 0。"""
        self.login_attempts = 0


user = User('Ming', 'Li')

for _ in range(4):
    user.increment_login_attempts()

print(f"尝试登录次数：{user.login_attempts}")

user.reset_login_attempts()
print(f"重置后登录次数：{user.login_attempts}")
