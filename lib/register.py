import requests, json
def register(user_id, user_name):
    r = requests.post("http://127.0.0.1/register", json={"user_id":user_id, "user_name":user_name})
    if r != str({"error":"already taken"}):
        print("[{user_name}]さんのユーザーIDは{user_id}です。".format(user_name=user_name, user_id=user_id))
        return user_name
    else:
        print("このユーザー名はすでに使われています。再試行してください。")
        return True