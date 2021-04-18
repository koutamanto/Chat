from flask.helpers import make_response
import requests, json, sqlite3, uuid
from flask import Flask, render_template, request, jsonify
from datetime import datetime
app = Flask(__name__)

db_name = "main.db"
conn = sqlite3.connect(db_name, check_same_thread=False)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/send_message", methods=["POST"])
def send_message():
    if request.method == "GET":
        return render_template("send_message/invalid_method.html")
    elif request.method == "POST":
        raw = request.get_data()
        datas = json.loads(raw)
        msg = datas["msg"]
        sender = datas["from"]
        to = datas["to"]
        cur = conn.cursor()
        cur.execute("SELECT * FROM ACCOUNT WHERE UserID = '{0}'".format(sender))
        conn.commit()
        user_data = cur.fetchall()
        print(user_data)
        cur.execute("SELECT * FROM {0}".format(to))
        conn.commit()
        cur.execute("INSERT INTO {0}(Text, sended_date, sender_id, sender_name) values ('{1}', '{2}', '{3}', '{4}')".format(to, msg, datetime.now().strftime('%Y/%m/%d %H:%M:%S'), sender, user_data[0][1]))
        conn.commit()

@app.route("/get_messages", methods=["POST"])
def get_messages():
    if request.method == "GET":
        return render_template("send_message/invalid_method.html")
    elif request.method == "POST":          
        raw = request.get_data()
        datas = json.loads(raw)
        user_id = datas["user_id"]
        cur = conn.cursor()
        response_messages = []
        for messages in cur.execute("SELECT * FROM {0}".format(user_id)):            
            messages_datas = {}
            messages_datas["text"] = messages[0]
            messages_datas["date"] = messages[1]
            messages_datas["sender_id"] = messages[2]
            messages_datas["sender_name"] = messages[3]
            response_messages.append(messages_datas)
        return json.dumps({"messages":response_messages})

@app.route("/register", methods=["POST"])
def register():
    if request.method == "GET":
        return render_template("send_message/invalid_method.html")
    elif request.method == "POST":
        raw = request.get_data()
        datas = json.loads(raw)
        user_id = datas["user_id"]
        user_name = datas["user_name"]
        cur = conn.cursor()
        #cur.execute("CREATE TABLE ACCOUNT(UserID text, UserName text)")
        cur.execute("SELECT * FROM ACCOUNT")
        conn.commit()
        user_datas = []
        for user_data in cur.execute("SELECT * FROM ACCOUNT"):
            user_datas.append(user_data)
        if (user_id, user_name) not in user_datas:
            cur.execute("INSERT INTO ACCOUNT(UserID, UserName) values ('{0}','{1}')".format(user_id, user_name))
        else:
            return json.dumps({"error":"already taken"})
        conn.commit()
        cur.execute("CREATE TABLE {0}(Text text, sended_date text, sender_id text, sender_name text)".format(user_id))
        cur.close()
if __name__ == "__main__":
    app.debug = True
    app.run(host="0.0.0.0", port=80)