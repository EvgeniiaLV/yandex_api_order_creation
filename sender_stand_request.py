import configuration
import requests

def post_new_order(order_body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER_PATH, #подставляем полный URL
                        json=order_body) #передаем тело заказа

def get_order_by_track(track_number):
    return requests.get(configuration.URL_SERVICE + configuration.GET_ORDER_BY_TRACK, #подставляем полный URL
                        params={'t':track_number}) #передаем номер заказа