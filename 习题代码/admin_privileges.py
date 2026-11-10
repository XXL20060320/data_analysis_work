# admin_privileges.py：保存 Privileges 和 Admin 类
from user import User


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
