import spacy

from file_extractor.constants import NER_MODEL_NAME

class NERModel(object):
    _instance = None
    model = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(NERModel, cls).__new__(cls)
            cls._instance.__load_model()

        return cls._instance

    def __load_model(self):
        print(f'====> Loading NER model {NER_MODEL_NAME}')
        self.model = spacy.load(NER_MODEL_NAME)
        print(f'====> Model {NER_MODEL_NAME} loaded successfully')