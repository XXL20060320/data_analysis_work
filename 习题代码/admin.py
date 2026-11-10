# admin.py：把 User、Privileges 和 Admin 保存在同一个模块中
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
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0


class Privileges:
    """存储并显示管理员权限。"""

    def __init__(self):
        self.privileges = [
            'can add post', 'can delete post', 'can ban user'
        ]

    def show_privileges(self):
        for privilege in self.privileges:
            print(f"  - {privilege}")


class Admin(User):
    """管理员是一种特殊的用户。"""

    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)
        self.privileges = Privileges()
