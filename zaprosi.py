import configuration
import requests
import data


# Создание нового заказа
def post_new_order(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER,
                         json=body)

# Сохранение номера трека заказа
def save_order_track():
    order_body = data.order_body
    response_order = post_new_order(order_body)
    return response_order.json()["track"]

# Получение заказа по треку
def get_order_by_track():
    return requests.get(configuration.URL_SERVICE + configuration.FIND_ORDER + str(save_order_track()))
