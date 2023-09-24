# Владимир Зеленов, 8-я когорта — Финальный проект. Инженер по тестированию плюс
import zaprosi

# Позитивная проверка
def positive_assert():
    response = zaprosi.get_order_by_track()
    assert response.status_code == 200

#Тест
def test_create_order_get_success_response():
    positive_assert()
