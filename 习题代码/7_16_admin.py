# 练习 7：管理员
class User:
    """模拟一个用户。"""

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def describe_user(self):
        print(f"用户：{self.first_name} {self.last_name}")

    def greet_user(self):
        print(f"你好，{self.first_name}！")


class Admin(User):
    """管理员是一种特殊的用户。"""

    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)
        self.privileges = ['can add post', 'can delete post', 'can ban user']

    def show_privileges(self):
        print(f"{self.first_name} 的权限：")
        for privilege in self.privileges:
            print(f"  - {privilege}")


admin = Admin('Ming', 'Li')
admin.describe_user()
admin.show_privileges()
