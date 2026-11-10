# restaurant.py：把 Restaurant 类保存在一个模块中
class Restaurant:
    """一次模拟餐馆的简单尝试。"""

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print(f"餐馆名称：{self.restaurant_name}")
        print(f"菜系：{self.cuisine_type}")

    def open_restaurant(self):
        print(f"{self.restaurant_name} 正在营业！")

    def set_number_served(self, number):
        self.number_served = number

    def increment_number_served(self, number):
        self.number_served += number
