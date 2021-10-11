import requests


url = 'http://localhost:9696/churn'

customer = {
    "contract": "two_year",
    "tenure": 1,
    "monthlycharges": 10
}



response = requests.post(url, json=customer).json()
print(response)

if response['churn'] == True:
    print('sending promo email ')
else:
    print('not sending promo email ')