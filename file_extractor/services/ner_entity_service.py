from typing import List, Tuple
from spacy.tokens.span import Span
from file_extractor.constants import NER_ENTITIES_TAGS
from file_extractor.models import Document, NEREntity, NEREntityTag

def store_entities(entities: Tuple[Span], doc: Document):
    entitiesList: List[NEREntity] = []
    
    for word in entities:
        entity = NEREntity()
        entity.sentence = word.text
        entity.tag = NEREntityTag(id=NER_ENTITIES_TAGS[word.label_])
        entity.document = doc
        entitiesList.append(entity)

    NEREntity.objects.bulk_create(entitiesList)


def get_entities_by_document(document_id: int):
    return NEREntity.manager.find_by_document_id(document_id=document_id)