# 练习 2：大号 T 恤
def make_shirt(size='L', text='I love Python'):
    """默认制作印有 I love Python 的大号 T 恤。"""
    print(f"这件 T 恤是 {size} 码，印着“{text}”。")


make_shirt()                            # 默认：大号 + 默认字样
make_shirt(size='M')                    # 中号 + 默认字样
make_shirt(size='S', text='代码改变世界')  # 其他字样
