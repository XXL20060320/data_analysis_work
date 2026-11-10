# 练习 1：放眼世界
places = ['冰岛', '京都', '撒哈拉沙漠', '挪威峡湾', '大理']

print("原始顺序：", places)

print("\n--- sorted()：按字母顺序，临时排序 ---")
print(sorted(places))
print("核实原列表未变：", places)

print("\n--- sorted(reverse=True)：按相反顺序，临时排序 ---")
print(sorted(places, reverse=True))
print("核实原列表未变：", places)

print("\n--- reverse()：永久反转 ---")
places.reverse()
print(places)
places.reverse()
print("再反转一次，已恢复原顺序：", places)

print("\n--- sort()：永久排序 ---")
places.sort()
print(places)
places.sort(reverse=True)
print(places)
