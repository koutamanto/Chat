from lib.register import register
import json
while True:
    user_id = input("ユーザーIDを入力してください(英数字):")
    user_name = input("ユーザー名を入力してください:")
    if register(user_id, user_name) == True:
        continue
    else:
        with open("user_data.json", "r") as f:
            user_data = json.load(f)
        user_data["user_id"] = user_id
        user_data["user_name"] = user_name
        with open("user_data.json", "w") as f:
            user_data = json.dump(user_data, f)
        break