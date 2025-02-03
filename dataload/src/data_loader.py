import datetime
import requests

def inquire_candle_data(market, tgt_date, unit, time_unit=1, max_per_attmp=180, **kwargs):

    if not isinstance(tgt_date, str):
        tgt_date = datetime.datetime.strftime(tgt_date, "%Y-%m-%dT%H:%M:%S")

    URL = f"https://api.upbit.com/v1/candles/{unit}/{time_unit}"
    PARAMS = {
        "market" : market,
        "to" : tgt_date,
        "count" : max_per_attmp
    }
    
    if 'params' in kwargs:
        for k, v in kwargs['params'].items():
            if v:
                PARAMS[k] = v

    try:
        response = requests.get(URL, params=PARAMS)
        response.raise_for_status()
        
        return response.json()

    except requests.exceptions.RequestException as e:  
        LOGGER.error(f"Error Fetching Data from UpBit : {e}")
        
        return None