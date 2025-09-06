from rest_framework.exceptions import ValidationError


class LinkValidator:
    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        if not('youtube.com' in value['link']):
            raise ValidationError('Invalid link')