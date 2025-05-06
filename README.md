# Flask LED Controller for Raspberry Pi Pico W

Web ブラウザから Raspberry Pi Pico W の LED を ON/OFF 制御する IoT アプリケーションです。 Python + Flask を使用し、Pico W とは HTTP で通信を行います。

## 使用技術

- Python 3.11+
- Flask / requests ライブラリ
- Raspberry Pi Pico W（MicroPython）
- VSCode（+ MicroPico 拡張）
- venv（仮想環境管理）

## セットアップ手順

### 1. リポジトリをクローン

```bash
git clone https://github.com/Takashi-Matsumura/flask-led-app.git
cd flask-led-app
```

### 2. 仮想環境の作成と有効化

```bash
python3 -m venv venv
source venv/bin/activate  # bash/zsh の場合
```

### 3. 必要なライブラリのインストール

```bash
pip install flask requests
```

## アプリケーションの起動

### 1. Pico W の IP アドレスを `flask_webapp.py` 内で設定

```python
PICO_IP = "http://192.168.x.x"  # あなたのPico WのIPに置き換え
```

### 2. Flask アプリを実行

```bash
python flask_webapp.py
```

ブラウザで [http://localhost:5002](http://localhost:5002) を開きます。  
ON / OFF ボタンで Pico W の LED が切り替わります。

## Pico W 側の準備

1. `main.py` を VSCode の MicroPico 拡張で Pico W に転送
2. Wi-Fi の SSID / パスワード を書き換えて保存
3. 実行後、シリアルモニタで IP アドレスを確認

## 補足情報

- `.venv` フォルダは `.gitignore` に追加し、Git 管理対象にしないでください。
- Docker 環境でも構築可能ですが、macOS の場合ネットワーク制限により Pico W に接続できないことがあります。そのため本プロジェクトでは `venv` を推奨します。

## ライセンス

MIT License
