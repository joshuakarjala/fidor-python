import json

import requests
import fidor_python

GET = 1
POST = 2


def baseRequest(endpoint, method, resource_id=None, meta_filter=None, payload={}, page=1):
    headers = {'Content-Type': 'application/json'}

    url = '{base_url}{endpoint}/{resource_id}/{meta_filter}?access_token={access_token}&page={page}'.format(
        base_url=fidor_python.test_api_url,
        endpoint=endpoint,
        resource_id=resource_id or '',
        meta_filter=meta_filter or '',
        access_token=fidor_python.access_token,
        page=page)

    print url

    if method == GET:
        r = requests.get(url, headers=headers)
    elif method == POST:
        r = requests.post(url, headers=headers, data=json.dumps(payload))

    return r.json()


class Accounts():

    @classmethod
    def all():
        return baseRequest('/accounts', GET)

    @classmethod
    def get(account_id):
        return baseRequest('/accounts', GET, account_id)


class Transactions():

    @classmethod
    def all(for_account=None, transaction_type=None):
        if for_account:
            if transaction_type:
                return baseRequest('/accounts', GET, for_account, transaction_type)
            return baseRequest('/accounts', GET, for_account, 'transactions')

        return baseRequest('/transactions', GET)


    @classmethod
    def get(transaction_id):
        return baseRequest('/transactions', GET, transaction_id)


class SepaDirectDebits():

    @classmethod
    def all(cls, page=1, batch=False):
        if batch:
            return baseRequest('/batch_direct_debits', GET, page=page)
        return baseRequest('/sepa_direct_debits', GET, page=page)

    @classmethod
    def get(cls, transaction_id, batch=False):
        if batch:
            return baseRequest('/batch_direct_debits', GET, transaction_id)
        return baseRequest('/sepa_direct_debits', GET, transaction_id)

    @classmethod
    def create(cls, payload, batch=False):
        if batch:
            return baseRequest('/batch_direct_debits', POST, payload=payload)
        return baseRequest('/sepa_direct_debits', POST, payload=payload)


class SepaCreditTransfers():

    @classmethod
    def all(cls, page=1):
        return baseRequest('/sepa_credit_transfers', GET, page=page)

    @classmethod
    def get(cls, transaction_id):
        return baseRequest('/sepa_credit_transfers', GET, transaction_id)

    @classmethod
    def create(cls, payload):
        return baseRequest('/sepa_credit_transfers', POST, payload=payload)
