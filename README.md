# FastAPI Chatwork Cooperation Sample

## 概要
FastAPI Chatwork連携 サンプル

- メッセージの送信
- タスクの作成
- ログ出力は左記を利用 [01.FastApi-Logging](https://github.com/eiji-azakami/01.FastApi-Logging)
- テスト付き（pytest）

## 設定
.env.example に従って、.env を作成してください。

## 起動方法

pythonコマンドは環境によって「python3」だったり、「python」、「py」だったりするようです。<br>
お使いの環境に合わせてコマンドを変更してください。

```bash
python3 -m venv venv
# Windows (PowerShell)
venv\Scripts\Activate.ps1
# Windows (cmd.exe)
venv\Scripts\activate.bat
pip install -r requirements.txt
uvicorn app.main:app --reload --no-access-log
```

## 起動後
- Swagger UI: http://127.0.0.1:8000/docs
- Redoc:        http://127.0.0.1:8000/redoc

## テスト

```bash
# 環境変数を設定してからテストを実行
$env:API_TOKEN="test_api_token"
$env:ROOM_ID="12345"
python -m pytest
```

# Note
 
業務システムなどから、メッセージを通知したり、<br>
タスクを作ったりすることができるようになります。<br>

他社チャットツールでもAPIを公開していますので、<br>
公開しているAPI次第で様々な事が可能になります。<br>
・Microsoft Teams<br>
・Google Chat<br>
・Line<br>
<br>
活用方法<br>
・通知<br>
・タスク作成<br>
・チャットボット<br>
・予約等の受付<br>
　　などなど

# Author
 
* 作成者 阿座上 英治
* 所属 　株式会社Ｌ．Ｓ．Ｅ
 
## 📝 License

MIT License  
Copyright (c) 2026 L.S.E Eiji.Azakami

This project is licensed under the MIT License.  
See the [LICENSE](https://en.wikipedia.org/wiki/MIT_License) file for details.
