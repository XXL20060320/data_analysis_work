# 练习 3：100 万求和
import time

numbers = list(range(1, 1_000_001))

print(f"列表长度：{len(numbers)}")
print(f"最小值 min()：{min(numbers)}")
print(f"最大值 max()：{max(numbers)}")

start = time.perf_counter()
total = sum(numbers)
elapsed = time.perf_counter() - start

print(f"总和 sum()：{total}")
print(f"sum() 耗时：{elapsed:.6f} 秒")
print(f"等差数列公式核对：{1_000_000 * 1_000_001 // 2}")
