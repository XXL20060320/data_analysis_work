# 练习 1：骰子
from random import randint


class Die:
    """一个可以掷的骰子。"""

    def __init__(self, sides=6):
        self.sides = sides

    def roll_die(self):
        """打印 1 到面数之间的随机数。"""
        return randint(1, self.sides)


def roll_many(die, times=10):
    results = [die.roll_die() for _ in range(times)]
    print(f"{die.sides} 面骰子掷 {times} 次：{results}")


roll_many(Die())          # 6 面
roll_many(Die(10))        # 10 面
roll_many(Die(20))        # 20 面
