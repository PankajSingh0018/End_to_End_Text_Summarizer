from TextSummarizer.config.configuration import ConfigurationManager
from TextSummarizer.components.data_transformation import DataTransformation
from TextSummarizer import logger 

class DataTransformationTrainingPipeline:
    def __init__(self) -> None:
        pass
    
    def main(self):
        config = ConfigurationManager()
        data_transformation_config = config.get_data_transformation_config()
        data_transformation = DataTransformation(config=data_transformation_config)
        data_transformation.convert()