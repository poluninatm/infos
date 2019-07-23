# -*- coding: utf-8 -*-
import requests
import pprint
import sys

# city_from = input('Введите город отправления: ')
city_from = "Москва"

try:
    req_from = requests.get('http://autocomplete.travelpayouts.com/places2', params={
        'term': city_from,
        'locale': 'ru',
        'types[]': 'city'
    })

    data_from = req_from.json()
    print(data_from[0]['code'])
except Exception:
    print ('Не удалось получить данные для города отправления')
    sys.exit(0)

# city_to = input('Введите город прибытия: ')
city_to = "Тиват"
try:
    req_to = requests.get('http://autocomplete.travelpayouts.com/places2', params={
        'term': city_to,
        'locale': 'ru',
        'types[]': 'city'
    })
    data_to = req_to.json()
    print(data_to[0]['code'])
except Exception:
    print ('Не удалось получить данные для города прибытия')
    sys.exit(0)

flight_params = {
    'origin': data_from[0]['code'],
    'destination': data_to[0]['code'],
    'depart_date': '2019-08-07',
    'one_way': 'true'
}
req = requests.get("http://min-prices.aviasales.ru/calendar_preload", params=flight_params)

data = req.json()
# pprint.pprint(data)
# print(data['best_prices'][0])

need_tickets = []
tickets = data['best_prices']
for ticket in tickets:
    if ticket['depart_date'] > "2019-09-08" and ticket['depart_date'] < "2019-09-15":
        need_tickets.append(ticket)

need_tickets = sorted(need_tickets, key=lambda x: x["value"], reverse=False)
for ticket in need_tickets:
    print(f"{data_from[0]['name']} - {data_to[0]['name']} - {ticket['depart_date']} - {ticket['value']} - {ticket['gate']}")
