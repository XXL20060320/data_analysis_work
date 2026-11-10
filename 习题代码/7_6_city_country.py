# 练习 1：城市名
def city_country(city, country):
    """返回“城市, 国家”格式的字符串。"""
    return f"{city.title()}, {country.title()}"


print(city_country('santiago', 'chile'))
print(city_country('beijing', 'china'))
print(city_country('reykjavik', 'iceland'))
