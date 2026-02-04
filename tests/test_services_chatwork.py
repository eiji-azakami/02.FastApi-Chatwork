# テスト対象のクラスをインポート
# 本物の Chatwork API を呼ぶクラスだが、
# テストでは「呼ばない」ようにする
from app.services.chatwork import ChatworkAPI


# requests.Response の代わりになる「偽物のレスポンス」
class FakeResponse:
    def __init__(self, status_code, json_data):
        # HTTPステータスコード（200, 400など）
        self.status_code = status_code
        # response.json() で返したいデータ
        self._json = json_data

    # ChatworkAPI 内で呼ばれる raise_for_status() を再現
    def raise_for_status(self):
        # ステータスコードが 400以上ならエラーにする
        if self.status_code >= 400:
            raise Exception("HTTP Error")

    # ChatworkAPI 内で呼ばれる json() を再現
    def json(self):
        return self._json


def test_get_rooms(monkeypatch):
    """
    ChatworkAPI.get_rooms() のテスト
    - 正しい URL でリクエストを投げているか
    - headers に正しい API トークンがセットされているか
    - 返り値が期待通りの JSON か
    """

    # Chatwork API が成功したときの「偽レスポンス」を作る
    fake = FakeResponse(200, [{"room_id": 1}])

    # requests.get の代わりになる関数
    def fake_get(url, headers):
        assert url == "https://api.chatwork.com/v2/rooms"
        assert headers["X-ChatWorkToken"] == "dummy-token"
        return fake

    # requests.get を fake_get に差し替え
    monkeypatch.setattr(
        "app.services.chatwork.requests.get",
        fake_get
    )

    # ダミーのトークンで ChatworkAPI を作成
    api = ChatworkAPI("dummy-token")

    # get_rooms() を呼ぶと fake.json() が返るはず
    assert api.get_rooms() == [{"room_id": 1}]


def test_send_message(monkeypatch):
    """
    ChatworkAPI.send_message() のテスト
    - 正しい URL でリクエストを投げているか
    - headers に正しい API トークンがセットされているか
    - body が正しいか
    - 返り値が期待通りの JSON か
    """

    fake = FakeResponse(200, {"message_id": 123})

    def fake_post(url, headers, data):
        assert url == "https://api.chatwork.com/v2/rooms/42/messages"
        assert headers["X-ChatWorkToken"] == "dummy-token"
        assert data["body"] == "hello"
        return fake

    monkeypatch.setattr(
        "app.services.chatwork.requests.post",
        fake_post
    )

    api = ChatworkAPI("dummy-token")
    resp = api.send_message(42, "hello")
    assert resp == {"message_id": 123}


def test_create_task(monkeypatch):
    """
    ChatworkAPI.create_task() のテスト
    - 正しい URL でリクエストを投げているか
    - headers に正しい API トークンがセットされているか
    - body と to_ids が正しいか
    - 返り値が期待通りの JSON か
    """

    fake = FakeResponse(200, {"task_id": 321})

    def fake_post(url, headers, data):
        assert url == "https://api.chatwork.com/v2/rooms/42/tasks"
        assert headers["X-ChatWorkToken"] == "dummy-token"
        assert data["body"] == "do this"
        assert data["to_ids"] == "1,2"
        return fake

    monkeypatch.setattr(
        "app.services.chatwork.requests.post",
        fake_post
    )

    api = ChatworkAPI("dummy-token")
    resp = api.create_task(42, "do this", "1,2")
    assert resp == {"task_id": 321}