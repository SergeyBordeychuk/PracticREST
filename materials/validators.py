from rest_framework.exceptions import ValidationError
from urllib.parse import urlparse


class LinkValidator:
    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        netloc = urlparse(value['link']).netloc
        if not(netloc in {'youtube.com','www.youtube.com','youtu.be'}):
            raise ValidationError('Invalid link')