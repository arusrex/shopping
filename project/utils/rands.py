import string
from random import SystemRandom
from django.utils.text import slugify

def random_algs(k=5):
    return ''.join(SystemRandom().choices(
        string.ascii_lowercase + string.digits,
        k=k
    ))

def slug_rand(text):
    return slugify(text + '-' + random_algs(5))