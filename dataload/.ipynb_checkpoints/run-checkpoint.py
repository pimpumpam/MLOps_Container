import sys
import time
import sqlite3
import pandas as pd
from datetime import datetime, timedelta

from src.data_loader import inquire_candle_data
from src.table_manager import fetch_one
from src.query_manager import is_exists, get_recent_timestamp, dataframe_to_tale

from config import CfgSqlite, CfgLoader

class Loader:
    
    def __init__(self, cfg_sqlite, cfg_loader):
        
        self.cfg_sqlite = cfg_sqlite
        self.cfg_loader = cfg_loader
        
        self.conn = sqlite3.connect(cfg_sqlite.db_path)
        self.cursor = self.conn.cursor()
        
        
    def run(self):
        
        if bool(
            fetch_one(cursor=self.cursor, query=is_exists(self.cfg_sqlite.brz_table))
        ):
            latest_time = fetch_one(
                cursor=self.cursor,
                query=get_recent_timestamp(self.cfg_sqlite.brz_table)
            )[0]
            
            tic = datetime.strptime(latest_time, "%Y-%m-%dT%H:%M:%S") + timedelta(minutes=1)
#             toc = datetime.now()
            toc = tic + timedelta(days=1)
            
        else:
            tic = datetime.strptime(self.cfg_loader.tic, "%Y-%m-%dT%H:%M:%S")
#             toc = datetime.now()
            toc = datetime.strptime(self.cfg_loader.toc, "%Y-%m-%dT%H:%M:%S")
            
        
        data = []
        while True:
             
            if tic > toc:
                break
                
            datum = inquire_candle_data(
                market=self.cfg_loader.market,
                tgt_date=toc,
                unit=self.cfg_loader.unit,
                time_unit=self.cfg_loader.time_unit,
                max_per_attmp=self.cfg_loader.max_per_attmp
            )
                
            data.extend(datum)
            
            toc = datetime.strptime(
                datum[-1]['candle_date_time_utc'],
                "%Y-%m-%dT%H:%M:%S"
            )
            toc -= timedelta(seconds=1)

            time.sleep(0.1)
                
        
        data = pd.DataFrame(data)
        data.drop_duplicates(inplace=True)
        
        dataframe_to_tale(
            table_name=self.cfg_sqlite.brz_table,
            data=data,
            conn=self.conn
        )
        
        
if __name__ == "__main__":
        
    loader = Loader(CfgSqlite, CfgLoader)
    loader.run()