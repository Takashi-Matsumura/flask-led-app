from flask import Flask, redirect
import requests

app = Flask(__name__)
PICO_IP = "PICO_IP_ADDR"  # Pico W のIPアドレスに適宜変更

@app.route('/')
def index():
    return '''
    <h1>LED Controller</h1>
    <a href="/on"><button>ON</button></a>
    <a href="/off"><button>OFF</button></a>
    '''

@app.route('/on')
def turn_on():
    try:
        requests.get(f"{PICO_IP}/led/on")
    except requests.exceptions.ConnectionError as e:
        print("接続エラー：Pico W に接続できません")
        print(f"詳細: {e}")
    return redirect('/')

@app.route('/off')
def turn_off():
    try:
        requests.get(f"{PICO_IP}/led/off")
    except requests.exceptions.ConnectionError:
        print("接続エラー：Pico W に接続できません")
    return redirect('/')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5002)