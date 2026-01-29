"""
Chatwork 連携 API。

- サンプルコードです。
- 環境変数から API トークンとルーム ID を取得して使用します。

エンドポイント:
  - POST /chatwork/send_message: メッセージ送信
  - POST /chatwork/create_task: タスク作成
  - GET /chatwork/get_rooms: チャットルームのリスト取得

"""

import os
from fastapi import APIRouter, HTTPException
from app.services.chatwork import ChatworkAPI

router = APIRouter(tags=["chatwork"])

# Chatwork APIインスタンスの作成
api_token = os.getenv("API_TOKEN")
if not api_token:
    # APIトークンが設定されていない場合はエラー
    raise ValueError("API_TOKEN is not set in the environment variables")

chatwork_api = ChatworkAPI(api_token=api_token)


def get_room_id():
    """環境変数からルームIDを取得します。"""
    room_id = os.getenv("ROOM_ID")
    if not room_id:
        # ルームIDが設定されていない場合はエラー
        raise HTTPException(
            status_code=500, detail="ROOM_ID is not set in the environment variables"
        )
    return int(room_id)


@router.post("/chatwork/send_message")
def send_message(message: str):
    """チャットルームにメッセージを送信します。"""
    try:
        # ルームID取得
        room_id = get_room_id()
        # メッセージを送信します。
        response = chatwork_api.send_message(room_id, message)
        return {"status": "success", "data": response}
    except Exception as e:
        # 例外をスロー
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/chatwork/create_task")
def create_task(body: str, to_ids: str):
    """チャットルームにタスクを作成します。"""
    try:
        # ルームID取得
        room_id = get_room_id()
        # タスクを作成します。
        response = chatwork_api.create_task(room_id, body, to_ids)
        return {"status": "success", "data": response}
    except Exception as e:
        # 例外をスロー
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/chatwork/get_rooms")
def get_rooms():
    """チャットルームのリストを取得します。"""
    try:
        rooms = chatwork_api.get_rooms()
        return {"rooms": rooms}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
