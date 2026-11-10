# 练习 2：发送消息
def show_messages(messages):
    for message in messages:
        print(message)


def send_messages(messages, sent_messages):
    """打印每条消息，并将其移入 sent_messages。"""
    while messages:
        message = messages.pop(0)
        print(f"正在发送：{message}")
        sent_messages.append(message)


messages = ['你好！', '今天天气不错。', '晚上一起吃饭吗？']
sent_messages = []

send_messages(messages, sent_messages)

print("\n原列表 messages：", messages)
print("已发送 sent_messages：", sent_messages)
