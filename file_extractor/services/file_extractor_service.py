from file_extractor.constants import NER_ENTITIES_TAGS
from file_extractor.models import Document, NEREntity, NEREntityTag
from django.core.files.uploadedfile import InMemoryUploadedFile
import fitz
import spacy

import file_extractor.services.aws_service
import file_extractor.services.document_service
import file_extractor.services.ner_entity_service

def parse_file(file: InMemoryUploadedFile):
    text = get_file_text(file)
    file_url  = file_extractor.services.aws_service.upload_file(file)
    entities = extract_entities(text)
    doc = file_extractor.services.document_service.store_document(file_url)
    file_extractor.services.ner_entity_service.store_entities(entities=entities, doc=doc)
    return file_extractor.services.ner_entity_service.get_entities_by_document(document_id=doc.id)

def get_file_text(file: InMemoryUploadedFile):
    doc = None
    text = ''
    try:
        buffer = file.read()
        
        doc = fitz.Document(filename='application/pdf', stream=buffer)
        
        for page in doc:
            text += page.get_text()

    except Exception as err:
        raise err
    finally:
        file.close()
        doc.close()
    return text

def extract_entities(text: str):
    NER = spacy.load('en_core_web_sm')
    ner_text = NER(text)
    return ner_text.ents
