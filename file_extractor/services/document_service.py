from file_extractor.models import Document

def store_document(file_url: str):
    doc = Document(aws_file_link=file_url)
    doc.save()
    return doc
