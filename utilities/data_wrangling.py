import pandas as pd
import config.config as cfg
from sklearn.model_selection import train_test_split

logger = cfg.logger


def load_data(filepath: str, type_file: str = "csv", **kwargs):
    """

    :param filepath:
    :param type_file:
    :param kwargs:
    :return:
    """
    if type_file not in ["csv", "xlsx"]:
        raise ValueError("Error: solo se admiten archivos csv o xlsx.")
    if type_file == "csv":
        dataframe = pd.read_csv(filepath, **kwargs)
    else:
        dataframe = pd.read_excel(filepath, **kwargs)
    return dataframe


def split_dataframe(dataframe: pd.DataFrame, label: str):
    """

    :param dataframe:
    :param label:
    :return:
    """
    target = dataframe.pop(label)
    train_data, test_data, train_label, test_label = train_test_split(dataframe, target, test_size=0.3, random_state=42)
    test_data, validation_data, test_label, validation_label = train_test_split(test_data, test_label,
                                                                                train_size=0.4, random_state=42)
    logger.info('Se ha partido el conjunto de datos en conjuntos de entrenamiento, validación y prueba.')
    return train_data, validation_data, test_data, train_label, validation_label, test_label


def concatenate_data(first_df: pd.DataFrame, second_df: pd.DataFrame, **kwargs):
    """

    :param first_df:
    :param second_df:
    :return:
    """
    dataframe = pd.concat(objs=[first_df, second_df], axis=1, **kwargs).reset_index(drop=True)
    logger.info("Se han unido los DataFrames correctamente.")
    return dataframe


