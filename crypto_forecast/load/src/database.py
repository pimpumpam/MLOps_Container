import sys
import time
import mysql.connector
from sqlalchemy import create_engine


def connect_to_database(host, port, user, password, database):
    
    # sleep for initialize DB
    time.sleep(3)
    
    try:
        conn = mysql.connector.connect(
            host = host,
            port=port,
            user=user,
            password=password,
            database=database
        )
        print("✅ MySQL 커넥션 성공")
        return conn
        
    except mysql.connector.Error as e:
        print(f"🚨 MySQL 커넥션 실패 | 에러: {e}")
        sys.exit()
            
            
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
        
        
def fetch_one(cursor, query):
    
    cursor.execute(query)
    
    return cursor.fetchone()