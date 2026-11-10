# 练习 4：就餐人数
class Restaurant:
    """一次模拟餐馆的简单尝试。"""

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0            # 默认值

    def describe_restaurant(self):
        print(f"餐馆名称：{self.restaurant_name}")
        print(f"菜系：{self.cuisine_type}")

    def open_restaurant(self):
        print(f"{self.restaurant_name} 正在营业！")

    def set_number_served(self, number):
        """设置就餐人数。"""
        self.number_served = number

    def increment_number_served(self, number):
        """让就餐人数递增。"""
        self.number_served += number


restaurant = Restaurant('兰州牛肉面', '西北菜')
print(f"初始就餐人数：{restaurant.number_served}")

restaurant.number_served = 12
print(f"直接修改属性后：{restaurant.number_served}")

restaurant.set_number_served(35)
print(f"set_number_served(35) 之后：{restaurant.number_served}")

restaurant.increment_number_served(200)
print(f"increment_number_served(200) 之后：{restaurant.number_served}")
