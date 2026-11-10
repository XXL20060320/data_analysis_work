# 练习 3：添加嘉宾
guests = ['苏轼', '爱因斯坦', '阿兰·图灵']

print("我找到了一张更大的餐桌，可以邀请更多客人了！")

guests.insert(0, '老子')                      # 添加到名单开头
guests.insert(len(guests) // 2, '居里夫人')   # 添加到名单中间
guests.append('白居易')                       # 添加到名单末尾

for guest in guests:
    print(f"{guest}，诚挚邀请您与我共进晚餐。")
