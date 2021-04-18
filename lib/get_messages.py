import requests, json

def get_messages(user_id):
    r = requests.post("http://127.0.0.1/get_messages", json={"user_id":user_id})
#    print(r, r.text)
    messages = json.loads(r.text)["messages"]
    for message in messages:
        print("[{date}] [{sender_name}({sender_id}):] {text}".format(text=message["text"], date=message["date"], sender_name=message["sender_name"], sender_id=message["sender_id"]))