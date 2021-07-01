import os
import xgboost
import pandas as pd


def download_artifact(s3_path: str, localpath: str):
    """

    :param s3_path:
    :param localpath:
    :return:
    """
    return os.system(command=f"aws s3 cp {s3_path} {localpath}")


def decompress_artifact(localpath: str):
    """

    :param localpath:
    :return:
    """
    return os.system(command=f"tar xvf {localpath}")


def prediction(estimator, filepath: str):
    """

    :param estimator:
    :param filepath:
    :param score:
    :return:
    """
    data = pd.read_csv(filepath, sep=",", header=None)
    data.columns = [f"f{i}" for i in range(0, data.shape[1])]
    data["prediction"] = estimator.predict(xgboost.DMatrix(data=data))
    return data
