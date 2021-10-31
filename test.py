import requests

Base = 'http://127.0.0.1:5000/'


data = [
        [
                {'description': 'A Fruit called Apple', 'name': 'Apple', 'price': '15'},
                {'description': 'A Fruit called Mango', 'name': 'Mango', 'price': '17'},
                {'description': 'A Fruit called Orange', 'name': 'Orange', 'price': '21'}
        ],
        [
                {"name": "Apple", "price": "150"},
                {"name": "Mango", "price": "170"},
                {"name": "Apple, Mango", "price": "32"}
        ]
]

# 1 Test for Product Model
print('For Product')
# put
print('PUT')
response = requests.put(Base + 'product/3', {'description': 'A Fruit called Tomato', 'name': 'Tomato', 'price': '12'})
print(response)
print(response.json())

input()

# patch
print('PATCH')
response = requests.patch(Base + 'product/3', {'description': 'A Vegetable called Tomato'})
print(response)
print(response.json())

input()

# get
print('GET')
response = requests.get(Base + 'product/3')
print(response)
print(response.json())

input()

# delete
print('DELETE')
response = requests.delete(Base + 'product/3')
print(response)
# print(response.json())

'''
'''
input()

# 2 Test for Order Model
print('For Order')
# put
print('PUT')
response = requests.put(Base + 'order/3', {'name': 'Tomato', 'price': '12'})
print(response)
print(response.json())

input()

# patch
print('PATCH')
response = requests.patch(Base + 'order/3', {'price': '0'})
print(response)
print(response.json())

input()

# get
print('GET')
response = requests.get(Base + 'order/3')
print(response)
print(response.json())

input()

# delete
print('DELETE')
response = requests.delete(Base + 'product/3')
print(response)