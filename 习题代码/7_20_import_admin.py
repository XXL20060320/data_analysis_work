# 练习 2：导入 Admin 类
from admin import Admin

admin = Admin('Ming', 'Li')
admin.describe_user()
print("权限列表：")
admin.privileges.show_privileges()
