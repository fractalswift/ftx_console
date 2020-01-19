import api_keys

import time
from typing import Optional, Dict, Any, List

from requests import Request, Session, Response
import hmac


class FtxClient:
    _ENDPOINT = 'https://ftx.com/api/'

    def __init__(self) -> None:
        self._session = Session()
        self._api_key =  "no key"  # ADD YOUR OWN API KEY HERE
        self._api_secret = "no secret" # ADD YOUR OWN API SECRET HERE
        self._subaccount_name = 'Battle Royale'  # TODO: If using a subaccount, put its name here as a string

    def _get(self, path: str, params: Optional[Dict[str, Any]] = None) -> Any:
        return self._request('GET', path, params=params)

    def _post(self, path: str, params: Optional[Dict[str, Any]] = None) -> Any:
        return self._request('POST', path, json=params)

    def _delete(self, path: str) -> Any:
        return self._request('DELETE', path)

    def _request(self, method: str, path: str, **kwargs) -> Any:
        request = Request(method, self._ENDPOINT + path, **kwargs)
        self._sign_request(request)
        response = self._session.send(request.prepare())
        return self._process_response(response)

    def _sign_request(self, request: Request) -> None:
        ts = int(time.time() * 1000)
        prepared = request.prepare()
        signature_payload = f'{ts}{prepared.method}{prepared.path_url}'.encode()
        if prepared.body:
            signature_payload += prepared.body
        signature = hmac.new(self._api_secret.encode(), signature_payload, 'sha256').hexdigest()
        request.headers['FTX-KEY'] = self._api_key
        request.headers['FTX-SIGN'] = signature
        request.headers['FTX-TS'] = str(ts)
        if self._subaccount_name:
            request.headers['FTX-SUBACCOUNT'] = self._subaccount_name

    def _process_response(self, response: Response) -> Any:
        try:
            data = response.json()
        except ValueError:
            response.raise_for_status()
            raise
        else:
            if not data['success']:
                raise Exception(data['error'])
            return data['result']

    def list_futures(self) -> List[dict]:
        return self._get('futures')

    def list_markets(self) -> List[dict]:
        return self._get('markets')

    def get_orderbook(self, market: str) -> dict:
        return self._get(f'markets/{market}/orderbook', {'depth': 100})

    def get_trades(self, market: str) -> dict:
        return self._get(f'markets/{market}/trades')

    def get_account_info(self) -> dict:
        return self._get(f'account')

    def get_open_orders(self) -> List[dict]:
        return self._get(f'orders')

    def place_order(self, market: str, side: str, price: float, size: float,
                    ioc: bool = False, post_only: bool = False) -> dict:
        return self._post('orders', {'market': market,
                                     'side': side,
                                     'price': price,
                                     'size': size,
                                     'ioc': ioc,
                                     'postOnly': post_only})

    def cancel_order(self, order_id: str) -> dict:
        return self._delete(f'orders/{order_id}')

    def get_fills(self) -> List[dict]:
        return self._get(f'fills')

    def get_balances(self) -> List[dict]:
        return self._get('wallet/balances')

    def get_deposit_address(self, ticker: str) -> dict:
        return self._get(f'wallet/deposit_address/{ticker}')
    
    def get_hist_futures(self, future_name: str, resolution: str) -> dict:
        return self._get(f'futures/{future_name}/mark_candles?resolution={resolution}')
    
    def get_positions(self) -> dict:
        return self._get(f'positions')
    
    def get_hist_markets(self, market_name: str, resolution: str) -> dict:
        return [market_name, self._get(f'markets/{market_name}/candles?resolution={resolution}')]
    
    
    
    