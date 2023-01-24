import requests

response = requests.post('http://127.0.0.1:8000/api-token-auth/', data={'username':
                                                                        'dev', 'password': 'GBHrVL44'})

# {'token': '2efa08beed5727856319740df3747df4e0a3655e'}
print(response.status_code)
print(response.json())  # {'token': '2efa08beed5727856319740df3747df4e0a3655e'}
