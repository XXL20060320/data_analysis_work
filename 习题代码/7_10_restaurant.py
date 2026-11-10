# 练习 1：餐馆
class Restaurant:
    """一次模拟餐馆的简单尝试。"""

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"餐馆名称：{self.restaurant_name}")
        print(f"菜系：{self.cuisine_type}")

    def open_restaurant(self):
        print(f"{self.restaurant_name} 正在营业！")


restaurant = Restaurant('兰州牛肉面', '西北菜')
print(restaurant.restaurant_name)
print(restaurant.cuisine_type)
print()
restaurant.describe_restaurant()
restaurant.open_restaurant()
