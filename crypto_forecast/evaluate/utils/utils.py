from typing import Sequence, cast


def load_spec_from_config(cfg_name):
    
    meta_spec = __import__(
        f"configs.{cfg_name}", fromlist=cast(Sequence[str], [None])
    ).CfgMeta
    
    database_spec = __import__(
        f"configs.{cfg_name}", fromlist=cast(Sequence[str], [None])
    ).CfgDatabase
    
    transform_spec = __import__(
        f"configs.{cfg_name}", fromlist=cast(Sequence[str], [None])
    ).CfgTransform
    
    model_spec = __import__(
        f"configs.{cfg_name}", fromlist=cast(Sequence[str], [None])
    ).CfgModel
    
    evaluate_spec = __import__(
        f"configs.{cfg_name}", fromlist=cast(Sequence[str], [None])
    ).CfgEvaluate
    
    return meta_spec, database_spec, transform_spec, model_spec, evaluate_spec