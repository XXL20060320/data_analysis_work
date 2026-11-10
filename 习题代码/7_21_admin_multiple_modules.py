# 练习 3：多个模块
from admin_privileges import Admin

admin = Admin('Ming', 'Li')
admin.describe_user()
admin.greet_user()
print("权限列表：")
admin.privileges.show_privileges()
