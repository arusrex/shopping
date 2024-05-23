from django.core.exceptions import  ValidationError

def validate_png(image):
    print(image.name)
    if not image.name.lower().endswith('.png'):
        raise ValidationError('Apenas imagens ".png" é aceitável')