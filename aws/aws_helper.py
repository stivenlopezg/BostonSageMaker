import boto3
import config.config as cfg
from botocore.exceptions import ClientError

logger = cfg.logger


class AwsHelper:
    """

    """

    def __init__(self):
        self.s3_client = boto3.client("s3", region_name=cfg.AWS_REGION)

    def download_from_s3(self, bucket: str, key: str, local_path: str):
        """
        Download from S3 a file in specific bucket to a specific local path
        :param bucket: s3 bucket name
        :param key: filename (subfolder/filename)
        :param local_path: local path
        :return: None
        """
        logger.info('Se ha empezado a descargar el archivo ...')
        try:
            self.s3_client.download_file(bucket, key, local_path)
            logger.info('Se ha descargado el artefacto correctamente.')
        except (Exception, ClientError) as e:
            logger.error(f'Error descargando desde S3, {e}')
            if e.response['Error']['Code'] == '404':
                logger.info('El objeto no existe')
        return True

    def upload_to_s3(self, local_path: str, bucket: str, key: str):
        """
        Load a file from a specific route to an S3 bucket
        :param local_path: file
        :param bucket: s3 bucket name
        :param key: (subfolder/filename)
        :return: None
        """
        logger.info('Se ha empezado a cargar el archivo a S3 ...')
        try:
            self.s3_client.upload_file(local_path, bucket, key)
            logger.info('Se ha cargado el archivo en S3 correctamente.')
        except (Exception, ClientError) as e:
            logger.error(f'Error cargando a S3, {e}')
        return True
