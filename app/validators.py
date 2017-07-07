from PIL import Image
from wtforms.validators import ValidationError

class ImageValidator(object):
    def __init__(self, x=200, y=200, message=None):
        self.x = x
        self.y = y
        if not message:
            message = u'Image must be %ix%i in size' % (x, y)
        self.message = message

    def __call__(self, form, field):
        try:
            img = Image.open(field.data)
        except:
            raise ValidationError(self.message)
        else:
            if img.width > self.x or img.height > self.y:
                raise ValidationError(self.message)
            
            
