import sys
import time
from sqlalchemy import create_engine


def connect_to_engine(host, port, user, password, database):

    # sleep for initialize DB
    time.sleep(3)
    
    try:
        connection = f"mysql+pymysql://{user}:{password}@{host}:{port}/{database}"
        engine = create_engine(connection, echo=False)
        print("⚙️ MySQL 엔진 생성 성공")
        
        return engine
    
    except:
        print("🚨 MySQL 엔진 생성 실패")
        sys.exit()