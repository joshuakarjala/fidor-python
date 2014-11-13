__version__ = '0.0.1'
Version = __version__  # for backware compatibility

import json
import requests

GET = 1
POST = 2


class FidorClient:

    def __init__(self, access_token, api_url='http://aps.test.fidor.de'):
        self.access_token = access_token
        self.api_url = api_url

        self.accounts = self.Accounts(self)
        self.transactions = self.Transactions(self)
        self.internal_transfers = self.InternalTransfers(self)
        self.sepa_credit_transfers = self.SepaCreditTransfers(self)
        self.sepa_mandates = self.SepaMandates(self)
        self.sepa_direct_debits = self.SepaDirectDebits(self)

    def baseRequest(self, endpoint, method, resource_id=None, meta_filter=None, payload={}, params={'page': 1}):
        headers = {'Content-Type': 'application/json'}
        params.update({'access_token': self.access_token})

        url = '{base_url}{endpoint}{resource_id}/{meta_filter}'.format(
            base_url=self.api_url,
            endpoint=endpoint,
            resource_id="/{resource_id}".format(resource_id=resource_id) if resource_id else '',
            meta_filter="/{meta_filter}".format(meta_filter=meta_filter) if meta_filter else '')

        if method == GET:
            r = requests.get(url, params=params, headers=headers)
        elif method == POST:
            r = requests.post(url, params=params, headers=headers, data=json.dumps(payload))

        return r.json()

    class Accounts():
        def __init__(self, base):
            self.base = base

        def all(self, params={'page': 1}):
            return self.base.baseRequest('/accounts', GET, params=params)

        def get(self, account_id):
            return self.base.baseRequest('/accounts', GET, account_id)

    class Transactions():
        def __init__(self, base):
            self.base = base

        def all(self, for_account=None, params={'page': 1}, transaction_type=None):
            if for_account:
                if transaction_type:
                    return self.base.baseRequest('/accounts', GET, for_account, transaction_type, params=params)
                return self.base.baseRequest('/accounts', GET, for_account, 'transactions', params=params)

            return self.base.baseRequest('/transactions', GET, params=params)

        def get(self, transaction_id):
            return self.base.baseRequest('/transactions', GET, transaction_id)

    class InternalTransfers():
        def __init__(self, base):
            self.base = base

        def all(self, params={'page': 1}, batch=False):
            if batch:
                return self.base.baseRequest('/batch_transfers', GET, params=params)
            return self.base.baseRequest('/internal_transfers', GET, params=params)

        def get(self, transaction_id, batch=False):
            if batch:
                return self.base.baseRequest('/batch_transfers', GET, transaction_id)
            return self.base.baseRequest('/internal_transfers', GET, transaction_id)

        def create(self, payload, batch=False):
            if batch:
                return self.base.baseRequest('/batch_transfers', POST, payload=payload)
            return self.base.baseRequest('/internal_transfers', POST, payload=payload)

    class SepaCreditTransfers():
        def __init__(self, base):
            self.base = base

        def all(self, params={'page': 1}, batch=False):
            if batch:
                return self.base.baseRequest('/batch_transfers', GET, params=params)
            return self.base.baseRequest('/sepa_credit_transfers', GET, params=params)

        def get(self, transaction_id, batch=False):
            if batch:
                return self.base.baseRequest('/batch_transfers', GET, transaction_id)
            return self.base.baseRequest('/sepa_credit_transfers', GET, transaction_id)

        def create(self, payload, batch=False):
            if batch:
                return self.base.baseRequest('/batch_transfers', POST, payload=payload)
            return self.base.baseRequest('/sepa_credit_transfers', POST, payload=payload)

    class SepaMandates():
        def __init__(self, base):
            self.base = base

        def all(self, params={'page': 1}):
            return self.base.baseRequest('/sepa_mandates', GET, params=params)

        def get(self, mandate_id):
            return self.base.baseRequest('/sepa_mandates', GET, mandate_id)

        def create(self, payload):
            return self.base.baseRequest('/sepa_mandates', POST, payload=payload)

    class SepaDirectDebits():
        def __init__(self, base):
            self.base = base

        def all(self, params={'page': 1}, batch=False):
            if batch:
                return self.base.baseRequest('/batch_direct_debits', GET, params=params)
            return self.base.baseRequest('/sepa_direct_debits', GET, params=params)

        def get(self, transaction_id, batch=False):
            if batch:
                return self.base.baseRequest('/batch_direct_debits', GET, transaction_id)
            return self.base.baseRequest('/sepa_direct_debits', GET, transaction_id)

        def create(self, payload, batch=False):
            if batch:
                return self.base.baseRequest('/batch_direct_debits', POST, payload=payload)
            return self.base.baseRequest('/sepa_direct_debits', POST, payload=payload)
