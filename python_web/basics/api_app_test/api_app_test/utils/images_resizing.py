import sys
from PIL import Image
import io
from django.core.files.uploadedfile import InMemoryUploadedFile


def resize_image(img):
    image = Image.open(img)
    image = image.convert('RGB')
    image = image.resize((400, 400), Image.LANCZOS)
    output = io.BytesIO()
    image.save(output, format='JPEG', quality=85)
    output.seek(0)
    return InMemoryUploadedFile(output, 'ImageField',
                                img.name,
                                'image/jpeg',
                                sys.getsizeof(output), None)
