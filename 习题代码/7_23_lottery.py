# 练习 2：彩票
from random import choice

pool = list(range(10)) + ['a', 'b', 'c', 'd', 'e']   # 10 个数字 + 5 个字母

winning_ticket = []
while len(winning_ticket) < 4:
    picked = choice(pool)
    if picked not in winning_ticket:                 # 不重复抽取
        winning_ticket.append(picked)

print(f"本期中奖号码是：{winning_ticket}")
print("只要彩票上是这 4 个数字或字母，就中大奖了！")
