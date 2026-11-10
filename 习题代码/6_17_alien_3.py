# 练习 3：外星人颜色 3：三个版本


def play(alien_color):
    """根据外星人颜色给出得分。"""
    if alien_color == 'green':
        print("绿色外星人：获得 5 分！")
    elif alien_color == 'yellow':
        print("黄色外星人：获得 10 分！")
    else:
        print("红色外星人：获得 15 分！")


play('green')     # 版本 1
play('yellow')    # 版本 2
play('red')       # 版本 3
