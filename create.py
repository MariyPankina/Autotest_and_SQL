# Мария Панкина, 9-я когорта — Финальный проект. Инженер по тестированию плюс
import sender_stand_request
import data


def test_create_and_get_order():
    create_resp = sender_stand_request.create_order(data.TEST_ORDER_DATA)
    # Проверяем http статус создания заказа
    assert create_resp.status_code == 201
    # Сохраняем трек заказа
    track = create_resp.json()["track"]
    # Отправляем запрос на получение заказа
    get_resp = sender_stand_request.get_order(track)
    # Проверяем ttp татус получения заказа
    assert get_resp.status_code == 200
