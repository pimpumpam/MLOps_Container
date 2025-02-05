import os
import json
import argparse
import mlflow.artifacts
import pandas as pd

import mlflow

from src.database import connect_to_engine
from src.preparation import split_sliding_window
from utils.utils import load_spec_from_config

# globals
DB_HOST = os.getenv("DB_HOST")
DB_PORT = int(os.getenv("DB_PORT"))
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_NAME = os.getenv("DB_NAME")

mlflow.set_tracking_uri(uri="http://mlflow:8081")
print("🚨🚨🚨🚨🚨🚨")
artifacts_dir = '/app/mlruns' # --> CfgMeta.artifacts_dir
RUN_ID = "f2df83e3022048a6884e237d5d63eee1"
# MODEL_URI = os.path.join(artifacts_dir, RUN_ID, 'artifacts', 'model')
MODEL_URI = f"runs:/{RUN_ID}/model"
MODEL_DIR = mlflow.artifacts.download_artifacts(MODEL_URI)
CODE_DIR = os.path.join(MODEL_DIR, "code")

print(MODEL_DIR)
print(CODE_DIR)

if os.path.exists(CODE_DIR):
    print(f"Append Code Path on System: {CODE_DIR}")
    import sys
    sys.path.append(CODE_DIR)
    from src.models.model import Model
    print(f"Load Model Package")

model = mlflow.pytorch.load_model(MODEL_URI)
print(model)
print("🚨🚨🚨🚨🚨🚨")

import sys
sys.exit()





class Evaluator:
    
    def __init__(self, cfg_meta, cfg_database, cfg_evaluate):
        
        mlflow.set_tracking_uri(uri="http://mlflow:8081")
        
        self.engine = connect_to_engine(
            host=DB_HOST,
            port=DB_PORT,
            user=DB_USER,
            password=DB_PASSWORD,
            database=DB_NAME
        )
        self.conn = self.engine.connect()
        self.cursor = self.engine.raw_connection().cursor()
        
    def run(self):
        with open(os.path.join('/app/static', 'run_ids.json'), 'r') as f:
            RUN_IDs = json.load(f)
        RUN_IDs = RUN_IDs['run_id']
        
        


if __name__ == "__main__":
    
    parser = argparse.ArgumentParser() 
    parser.add_argument('--config', type=str, default='gru', help="Config 파이썬 파일 명. 확장자는 제외.")
    args = parser.parse_args()
    
    # () = load_spec_from_config(args.config)
    
    evaluator = Evaluator()
    evaluator.run()