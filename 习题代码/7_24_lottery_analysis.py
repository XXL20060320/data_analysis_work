# 练习 3：彩票分析
from random import choice

pool = list(range(10)) + ['a', 'b', 'c', 'd', 'e']
my_ticket = ['3', 'b', '7', 'e']        # 自选的 4 个字符

plays = 0
while True:
    plays += 1
    draw = [str(choice(pool)) for _ in range(4)]
    if draw == my_ticket:               # 顺序也完全一致才算中奖
        break

print(f"我的彩票：{my_ticket}")
print(f"循环了 {plays} 次才中大奖！")
