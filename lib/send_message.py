import requests, json
def send_message(msg, to, user_id):
    r = requests.post("http://127.0.0.1/send_message", json={"msg":msg, "from":user_id, "to":to})