# 练习 2：餐馆订位
count = int(input("请问有多少人用餐？"))

if count > 8:
    print(f"抱歉，{count} 位的话目前没有空桌，需要稍等一会儿。")
else:
    print(f"有空桌，{count} 位请跟我来。")
