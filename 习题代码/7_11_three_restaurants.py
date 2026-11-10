# 练习 2：三家餐馆
class Restaurant:
    """一次模拟餐馆的简单尝试。"""

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"餐馆名称：{self.restaurant_name}")
        print(f"菜系：{self.cuisine_type}")


restaurants = [
    Restaurant('兰州牛肉面', '西北菜'),
    Restaurant('鼎泰丰', '江浙菜'),
    Restaurant('Pizza Hut', '意式快餐'),
]

for restaurant in restaurants:
    restaurant.describe_restaurant()
    print()
