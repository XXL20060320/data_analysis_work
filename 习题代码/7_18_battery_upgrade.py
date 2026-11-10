# 练习 9：电池升级
class Battery:
    """一次模拟电动汽车电池的简单尝试。"""

    def __init__(self, battery_size=40):
        self.battery_size = battery_size

    def describe_battery(self):
        print(f"这辆汽车有 {self.battery_size} kWh 的电池。")

    def get_range(self):
        """打印电池的续航里程。"""
        if self.battery_size == 40:
            mileage = 150
        elif self.battery_size == 65:
            mileage = 225
        else:
            mileage = int(self.battery_size * 3.4)
        print(f"这辆汽车在满电状态下可行驶约 {mileage} 英里。")

    def upgrade_battery(self):
        """检查电池容量，不是 65 就升级为 65。"""
        if self.battery_size != 65:
            self.battery_size = 65
            print("电池已升级为 65 kWh。")
        else:
            print("电池容量已经是 65 kWh，无需升级。")


class ElectricCar:
    """一次模拟电动汽车的简单尝试。"""

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.battery = Battery()

    def get_descriptive_name(self):
        return f"{self.year} {self.make} {self.model}"

    def get_range(self):
        self.battery.get_range()


car = ElectricCar('BYD', 'Seal', 2024)
print(car.get_descriptive_name())
car.battery.describe_battery()
car.get_range()

print("\n--- 升级电池 ---")
car.battery.upgrade_battery()
car.battery.describe_battery()
car.get_range()

print("\n--- 再次升级（不应重复升级） ---")
car.battery.upgrade_battery()
