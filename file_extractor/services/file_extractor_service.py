from django.core.files.uploadedfile import InMemoryUploadedFile
import fitz

def get_file_text(file: InMemoryUploadedFile):
    doc = None
    text = ''
    try:
        buffer = file.read()
        
        doc = fitz.Document(filename="application/pdf", stream=buffer)
        
        for page in doc:
            text += page.get_text()

    except Exception as err:
        raise err
    finally:
        file.close()
        doc.close()
    return text