import config.config as cfg
from aws.aws_helper import AwsHelper
from utilities.data_wrangling import load_data, split_dataframe, concatenate_data

aws = AwsHelper()
logger = cfg.logger


def main():
    logger.info("El proceso ha comenzado ...")
    aws.download_from_s3(bucket=cfg.BUCKET, key=f"{cfg.KEY}/Boston.csv", local_path="data/Boston.csv")
    data = load_data(filepath="data/Boston.csv")
    train_data, validation_data, test_data, train_label, validation_label, test_label = split_dataframe(dataframe=data,
                                                                                                        label=cfg.LABEL)
    train = concatenate_data(first_df=train_label, second_df=train_data)
    train.to_csv("data/train.csv", index=False, header=False)
    logger.info("Se ha exportado el archivo de entrenamiento correctamente.")
    validation = concatenate_data(first_df=validation_label, second_df=validation_data)
    validation.to_csv("data/validation.csv", index=False, header=False)
    logger.info("Se ha exportado el archivo de validacion correctamente.")
    test_data.to_csv("data/new_housing.csv", index=False, header=False)
    aws.upload_to_s3(local_path="data/train.csv", bucket=cfg.BUCKET, key=f"{cfg.KEY}/train/train.csv")
    aws.upload_to_s3(local_path="data/validation.csv", bucket=cfg.BUCKET, key=f"{cfg.KEY}/validation/validation.csv")
    aws.upload_to_s3(local_path="data/new_housing.csv", bucket=cfg.BUCKET, key=f"{cfg.KEY}/new_data/new_housing.csv")
    logger.info("El proceso ha finalizado correctamente")
    return True


if __name__ == '__main__':
    main()
