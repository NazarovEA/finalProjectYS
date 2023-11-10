import requests
import configuration
import data

# Создаем заказ с запросом из data
def post_zakaz():
    return requests.post (configuration.URL_SERVICE + configuration.POST_CREATE_ORDER, json = data.body)



# Получить заявку по номеру заказа

def get_zakaz (numbers):
    return requests.get (configuration.URL_SERVICE + configuration.GET_ORDER_NUMBER, params = {"t": numbers} )
