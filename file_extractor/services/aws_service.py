from fileinput import filename
from django.core.files.uploadedfile import InMemoryUploadedFile

def upload_file(file: InMemoryUploadedFile):
    filename = file.name
    
    # upload file to aws and get url
    
    return f'url_{filename}'