# 练习 1：T 恤
def make_shirt(size, text):
    """简要说明 T 恤的尺码和字样。"""
    print(f"这件 T 恤是 {size} 码，印着“{text}”。")


make_shirt('L', 'Hello Python')             # 位置实参
make_shirt(text='Hello Python', size='L')   # 关键字实参
