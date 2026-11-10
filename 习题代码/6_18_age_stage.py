# 练习 4：人生的不同阶段


def stage_of_life(age):
    if age < 2:
        return "婴儿"
    elif age < 4:
        return "幼儿"
    elif age < 13:
        return "儿童"
    elif age < 18:
        return "少年"
    elif age < 65:
        return "中青年人"
    else:
        return "老年人"


for age in [1, 2, 4, 8, 13, 30, 64, 65, 80]:
    print(f"{age:>3} 岁：这个人是一个{stage_of_life(age)}。")
