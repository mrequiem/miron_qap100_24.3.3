import requests
import json

baseurl = 'https://petstore.swagger.io/v2'

headers = {'Accept': 'application/json',
           'Content-Type': 'application/json',
           'Host': 'petstore.swagger.io',
           'Content-Length': '236',
           'Cache-Control': 'no-cache'}

data={
  'id': 0,
  'category': {'id': 0,'name': 'string'},
  'name': 'Lucifer',
  'photoUrls': ['string'],
  'tags': [{'id': 0,'name': 'string'}],
  'status': 'available'
}

print('Выполнение запроса GET:')

res1 = requests.get(f'{baseurl}/pet/findByStatus', headers = headers, params = {'status': 'sold'})
print('Код ответа: ', res1.status_code)
print(res1.json())

print('\nВыполнение запроса POST:')

res2 = requests.post(f'{baseurl}/pet', headers = headers, data = json.dumps(data))

print('Код ответа: ', res2.status_code)
print(res2.json())
pet_id = dict(res2.json())['id']


print('\nВыполнение запроса PUT с изменением имени питомца:')

data["id"] = pet_id
data["name"] = 'Baltasar'

res3 = requests.put(f'{baseurl}/pet', headers = headers, data = json.dumps(data))

print('Код ответа: ', res3.status_code)
print(res3.json())

print('\nВыполнение запроса DELETE:')

res4 = requests.delete(f'{baseurl}/pet/{pet_id}')
print('Код ответа: ', res4.status_code)
print(res4.json())