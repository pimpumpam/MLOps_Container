class CfgMeta:
    static_dir = '/app/static'
    artifacts_dir = '/app/mlruns'
    experiment_name = 'CryptoForecast'


class CfgDatabase:
    layer = {
        'gold': {
            'scheme': 'dw_gld',
            'table': 'crypto_transc_candle_upbit_minutes_test'
        }
    }
    
    
class CfgEvaluate:
    time_field = 'candle_date_time_kst'
    feature_field = [
        'opening_price', 'trade_price', 'low_price', 'high_price',
        'candle_acc_trade_price', 'candle_acc_trade_volume',
        'diff_opening_price', 'diff_trade_price', 'diff_low_price', 'diff_high_price',
        'diff_candle_acc_trade_price', 'diff_candle_acc_trade_volume',
        'ratio_opening_price', 'ratio_trade_price', 'ratio_low_price', 'ratio_high_price',
        'ratio_candle_acc_trade_price', 'ratio_candle_acc_trade_volume'
    ]
    label_field = ['opening_price', 'trade_price', 'low_price', 'high_price']