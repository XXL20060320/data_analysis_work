# 练习 6：冰激凌小店
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


class IceCreamStand(Restaurant):
    """冰激凌小店是一种特殊的餐馆。"""

    def __init__(self, restaurant_name, cuisine_type='冰激凌'):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = ['香草', '巧克力', '草莓', '抹茶', '芒果']

    def show_flavors(self):
        print(f"{self.restaurant_name} 有以下口味：")
        for flavor in self.flavors:
            print(f"  - {flavor}")


stand = IceCreamStand('雪糕小屋')
stand.describe_restaurant()
stand.show_flavors()
stand.open_restaurant()
