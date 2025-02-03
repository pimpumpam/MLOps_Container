class CfgMeta:
    name = 'DOCKER_TEST'
    

class CfgSqlite:
    db_path = '/data1/MLOps/AirFlow/MLOps_Container/crypto.db'
    brz_table = 'dw_brz_crypto_transc_candle_upbit_minutes'
    slv_table = 'dw_slv_crypto_transc_candle_upbit_minutes'

    
class CfgLoader:
    platform = 'upbit'
    market = 'KRW-BTC'
    unit = 'minutes'
    time_unit = 1
    tic = '2024-11-01T00:00:00'
    toc = '2024-11-10T23:59:00'
    max_per_attmp = 180 # 한번에 가져 올 데이터 개수 (최대 200)
    
    
class CfgPreprocessor:
    platform = 'upbit'
    market = 'KRW-BTC'
    unit = 'minutes'
    seq_len = 120
    pred_len = 60
    split_ratio = 0.7
    split_point = '2024-12-31T23:59:59'