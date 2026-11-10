# 练习 3：城市
def describe_city(city, country='China'):
    """打印“城市位于国家”的句子。"""
    print(f"{city} is in {country}.")


describe_city('Reykjavik', 'Iceland')   # 不属于默认国家
describe_city('Beijing')
describe_city('Lanzhou')
