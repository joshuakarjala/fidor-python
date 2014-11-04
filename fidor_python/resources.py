import requests
import fidor_python

GET = 1
POST = 2


def baseRequest(endpoint, method, resource_id=None):
    headers = {'Content-Type': 'application/json'}

    url = '{base_url}{endpoint}/{resource_id}?access_token={access_token}'.format(
        base_url=fidor_python.test_api_url,
        endpoint=endpoint,
        resource_id=resource_id or '',
        access_token=fidor_python.access_token)

    if method == GET:
        r = requests.get(url, headers=headers)

    return r.json()


def getAccounts():
    return baseRequest('/accounts', GET)


def getAccount(account_id):
    return baseRequest('/accounts', GET, account_id)


def getTransactions():
    return baseRequest('/transactions', GET)


def getTransaction(transaction_id):
    return baseRequest('/transactions', GET, transaction_id)
