import pytest
from fastapi.testclient import TestClient
from unittest.mock import patch
from app.main import app

client = TestClient(app)


# 環境変数をモックする
@pytest.fixture(autouse=True)
def mock_env_vars(monkeypatch):
    monkeypatch.setenv("API_TOKEN", "test_api_token")
    monkeypatch.setenv("ROOM_ID", "12345")


# ChatworkAPIのモック
@pytest.fixture
def mock_chatwork_api():
    with (
        patch("app.services.chatwork.ChatworkAPI.send_message") as mock_send_message,
        patch("app.services.chatwork.ChatworkAPI.create_task") as mock_create_task,
    ):
        mock_send_message.return_value = {"message_id": "123"}
        mock_create_task.return_value = {"task_id": "456"}
        yield mock_send_message, mock_create_task


# メッセージ送信のテスト
def test_send_message(mock_chatwork_api):
    mock_send_message, _ = mock_chatwork_api
    response = client.post("/chatwork/send_message", json={"message": "Hello, Chatwork!"})
    assert response.status_code == 200
    assert response.json() == {"status": "success", "data": {"message_id": "123"}}
    mock_send_message.assert_called_once_with(12345, "Hello, Chatwork!")


# タスク作成のテスト
def test_create_task(mock_chatwork_api):
    _, mock_create_task = mock_chatwork_api
    response = client.post(
        "/chatwork/create_task", json={"body": "Complete this task", "to_ids": "1,2,3"}
    )
    assert response.status_code == 200
    assert response.json() == {"status": "success", "data": {"task_id": "456"}}
    mock_create_task.assert_called_once_with(12345, "Complete this task", "1,2,3")


# 環境変数が設定されていない場合のテスト
def test_missing_env_vars(monkeypatch):
    monkeypatch.delenv("ROOM_ID", raising=False)
    response = client.post("/chatwork/send_message", json={"message": "Hello, Chatwork!"})
    assert response.status_code == 500
    assert "ROOM_ID is not set in the environment variables" in response.json()["detail"]
