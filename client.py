from lib.get_messages import get_messages
from lib.send_message import send_message
import json
with open("user_data.json", "r") as f:
    user_datas = json.load(f)
user_id = user_datas["user_id"]
user_name = user_datas["user_name"]

while True:
    get_messages(user_id)
    to = input("送信先のユーザーIDを入力してください:")
    msg = input("送信したいメッセージを入力してください:")
    send_message(msg, to, user_id)