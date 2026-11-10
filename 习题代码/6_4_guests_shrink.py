# 练习 4：缩短名单
guests = ['老子', '苏轼', '居里夫人', '爱因斯坦', '阿兰·图灵', '白居易']

print("很抱歉，新餐桌无法及时送达，只能邀请两位嘉宾。")

guests.remove('爱因斯坦')   # remove()：按值（姓名）删除
del guests[1]               # del：按位置删除，删掉“苏轼”

while len(guests) > 2:      # pop()：删除末尾元素并取出
    guest = guests.pop()
    print(f"抱歉，{guest}，这次无法邀请您共进晚餐了。")

print("\n仍被邀请的嘉宾：")
for guest in guests:
    print(f"{guest}，您仍在邀请名单上。")

del guests[:]               # del 也可以用来清空整个列表
print(f"\n名单已清空：{guests}")
