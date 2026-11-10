# 练习 2：修改嘉宾名单
guests = ['苏轼', '达·芬奇', '阿兰·图灵']

absent = '达·芬奇'
print(f"很遗憾，{absent} 临时有事，无法赴约。")

# 按姓名找到位置后替换，名单长度不变
guests[guests.index(absent)] = '爱因斯坦'

print("\n新的邀请名单如下：")
for guest in guests:
    print(f"{guest}，诚挚邀请您与我共进晚餐。")
