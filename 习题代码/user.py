# user.py：只保存 User 类
class User:
    """模拟一个用户。"""

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def describe_user(self):
        print(f"用户：{self.first_name} {self.last_name}")

    def greet_user(self):
        print(f"你好，{self.first_name}！")
