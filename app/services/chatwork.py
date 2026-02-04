# ChatworkAPIクラス
# Chatwork APIを利用して、チャットルームの操作やメッセージ送信、タスク作成を行うためのクラスです。
# APIトークンを使用して認証を行い、各種操作を実行します。
# 各APIメソッドでは、response.raise_for_status() を使用してエラーをスローし、
# レスポンスをJSON形式で返します。
import requests


class ChatworkAPI:
    def __init__(self, api_token: str):
        """
        Chatwork API のクライアント初期化

        Args:
            api_token (str): Chatwork の API トークン
        """
        # APIトークンをインスタンス変数に保存
        self.api_token = api_token
        # Chatwork API のベースURL
        self.base_url = "https://api.chatwork.com/v2"

    def _headers(self):
        """
        APIリクエスト用の HTTP ヘッダーを作成

        Returns:
            dict: X-ChatWorkToken を含むヘッダー
        """
        return {"X-ChatWorkToken": self.api_token}

    def get_rooms(self):
        """
        ユーザーが参加しているチャットルームの一覧を取得

        Returns:
            list: ルーム情報のリスト（JSON形式）

        Raises:
            requests.exceptions.HTTPError: リクエストが失敗した場合
        """
        url = f"{self.base_url}/rooms"
        # GETリクエストを送信（headers に API トークンを含める）
        response = requests.get(url, headers=self._headers())
        # ステータスコードが 400 以上なら例外を投げる
        response.raise_for_status()
        return response.json()

    def send_message(self, room_id: int, message: str):
        """
        指定したチャットルームにメッセージを送信

        Args:
            room_id (int): 送信先のチャットルームID
            message (str): 送信するメッセージ本文

        Returns:
            dict: メッセージ送信結果のJSON

        Raises:
            requests.exceptions.HTTPError: リクエストが失敗した場合
        """
        url = f"{self.base_url}/rooms/{room_id}/messages"
        data = {"body": message}
        response = requests.post(url, headers=self._headers(), data=data)
        response.raise_for_status()
        return response.json()

    def create_task(self, room_id: int, body: str, to_ids: str):
        """
        指定したチャットルームにタスクを作成

        Args:
            room_id (int): タスク作成先のチャットルームID
            body (str): タスクの内容
            to_ids (str): 担当者のアカウントIDをカンマ区切りで指定

        Returns:
            dict: タスク作成結果のJSON

        Raises:
            requests.exceptions.HTTPError: リクエストが失敗した場合
        """
        url = f"{self.base_url}/rooms/{room_id}/tasks"
        data = {"body": body, "to_ids": to_ids}
        response = requests.post(url, headers=self._headers(), data=data)
        response.raise_for_status()
        return response.json()
