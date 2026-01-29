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

```bash
python -m venv venv
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
python -m pytest
```

# Note
 
業務システムなどから、メッセージを通知したり、
タスクを作ったりすることができるようになります。

他社チャットツールでもAPIを公開していますので、
公開しているAPI次第で様々な事が可能になります。
・Microsoft Teams
・Google Chat
・Line

活用方法
・通知
・タスク作成
・チャットボット
・予約等の受付
　　などなど

# Author
 
* 作成者 阿座上 英治
* 所属 　株式会社Ｌ．Ｓ．Ｅ
 
## 📝 License

MIT License  
Copyright (c) 2026 L.S.E Eiji.Azakami

This project is licensed under the MIT License.  
See the [LICENSE](https://en.wikipedia.org/wiki/MIT_License) file for details.
