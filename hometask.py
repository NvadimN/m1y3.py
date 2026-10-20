from flask import Flask
import random
app = Flask(__name__)

@app.route("/")
def hello_world():
    facts = ["Этот пост посвящённый программированию на Python.<br> Здесь вы вспомните и выучите осовные необходимые команды. Поймете принцип работы программ.<br> Да и в целом лучше начнёте писать код и создавать проэкты."]
    return random.choice(facts)

app.run(debug=True)  
