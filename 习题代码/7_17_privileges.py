# 练习 8：权限
class Privileges:
    """存储并显示管理员权限。"""

    def __init__(self, privileges=None):
        self.privileges = privileges or [
            'can add post', 'can delete post', 'can ban user'
        ]

    def show_privileges(self):
        for privilege in self.privileges:
            print(f"  - {privilege}")


class User:
    """模拟一个用户。"""

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def describe_user(self):
        print(f"用户：{self.first_name} {self.last_name}")


class Admin(User):
    """管理员是一种特殊的用户。"""

    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)
        self.privileges = Privileges()     # 用一个实例作属性


admin = Admin('Ming', 'Li')
admin.describe_user()
print("权限列表：")
admin.privileges.show_privileges()
