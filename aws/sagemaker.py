from sagemaker.estimator import Estimator
from sagemaker.amazon.amazon_estimator import image_uris


def create_model(image: str, version: str, role: str, instance_type: str,
                 region_name: str = "us-east-1", params: dict = None, **kwargs):
    """

    :param image:
    :param version:
    :param role:
    :param instance_type:
    :param region_name:
    :param params:
    :return:
    """
    ecr_container = image_uris.retrieve(framework=image, region=region_name, version=version)
    model = Estimator(image_uri=ecr_container,
                      role=role,
                      instance_count=1,
                      instance_type=instance_type,
                      use_spot_instances=True,
                      max_run=300,
                      max_wait=600,
                      **kwargs)
    model.set_hyperparameters(**params)
    return model
