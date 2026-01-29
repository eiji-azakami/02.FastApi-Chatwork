# ChatworkAPIクラス
# Chatwork APIを利用して、チャットルームの操作やメッセージ送信、タスク作成を行うためのクラスです。
# APIトークンを使用して認証を行い、各種操作を実行します。
# 各APIメソッドでは、response.raise_for_status() を使用してエラーをスローし、
# レスポンスをJSON形式で返します。
import requests


class ChatworkAPI:
    def __init__(self, api_token: str):
        # Chatwork APIの初期化
        # APIトークンとベースURLを設定します。
        self.api_token = api_token
        self.base_url = "https://api.chatwork.com/v2"

    def _headers(self):
        # APIリクエストに必要なヘッダーを作成します。
        return {"X-ChatWorkToken": self.api_token}

    def get_rooms(self):
        """チャットルームのリストを取得します。"""
        url = f"{self.base_url}/rooms"
        response = requests.get(url, headers=self._headers())
        response.raise_for_status()
        return response.json()

    def send_message(self, room_id: int, message: str):
        """特定のチャットルームにメッセージを送信します。"""
        url = f"{self.base_url}/rooms/{room_id}/messages"
        data = {"body": message}
        response = requests.post(url, headers=self._headers(), data=data)
        response.raise_for_status()
        return response.json()

    def create_task(self, room_id: int, body: str, to_ids: str):
        """特定のチャットルームにタスクを作成します。"""
        url = f"{self.base_url}/rooms/{room_id}/tasks"
        data = {"body": body, "to_ids": to_ids}
        response = requests.post(url, headers=self._headers(), data=data)
        response.raise_for_status()
        return response.json()
