# 练习 3：消息归档
def send_messages(messages, sent_messages):
    while messages:
        message = messages.pop(0)
        print(f"正在发送：{message}")
        sent_messages.append(message)


messages = ['你好！', '今天天气不错。', '晚上一起吃饭吗？']
sent_messages = []

send_messages(messages[:], sent_messages)   # 传入副本，保护原列表

print("\n原列表 messages（消息仍在）：", messages)
print("已发送 sent_messages：", sent_messages)
