from django.db import models
from django.contrib.auth.models import User
from utils.rands import slug_rand
from django.core.validators import MinLengthValidator

class Tag(models.Model):
    class Meta:
        verbose_name = 'Tag'
        verbose_name_plural = 'Tags'

    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, default=None, blank=True, null=True, max_length=255)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slug_rand(self.name)
        return super(Tag, self).save(*args, **kwargs)
    
    def __str__(self):
        return self.name

class Catergory(models.Model):
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, default=None, blank=True, null=True, max_length=255)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slug_rand(self.name)
        return super(Catergory, self).save(*args, **kwargs)
    
    def __str__(self):
        return self.name


class Page(models.Model):
    class Meta:
        verbose_name = 'Page'
        verbose_name_plural = 'Pages'

    title = models.CharField(max_length=255,)
    slug = models.SlugField(unique=True, default='', null=False, blank=True, max_length=255)
    is_published = models.BooleanField(default=False, help_text='Esta opção é necessária para publicar a página')
    content = models.TextField()

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slug_rand(self.title)
        return super(Page, self).save(*args, **kwargs)
    
    def __str__(self):
        return self.title
    
class Post(models.Model):
    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'

    title = models.CharField(max_length=255)
    short_description = models.CharField(max_length=255)
    description = models.TextField()
    number = models.IntegerField()
    fone = models.CharField(max_length=20, blank=True, null=True, default='N/D')
    whatsapp = models.BigIntegerField(max_length=11, blank=True, null=True)
    email = models.EmailField(max_length=255, blank=True, null=True)
    site = models.URLField(blank=True, null=True)
    facebook = models.URLField(blank=True, null=True)
    instagram = models.URLField(blank=True, null=True)
    x_twitter = models.URLField(blank=True, null=True)
    youtube = models.URLField(blank=True, null=True)
    cover = models.ImageField(upload_to="posts/%Y/%m/%d", blank=True, default='', help_text='Imagem para exibição no início',)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    slug = models.SlugField(unique=True, default='', null=False, blank=True, max_length=255)
    is_published = models.BooleanField(default=False, help_text='Esta opção é necessária para publicar a loja',)
    category = models.ForeignKey(Catergory, on_delete=models.SET_NULL, blank=True, null=True, default=None)
    tags = models.ManyToManyField(Tag, blank=True, default='')

    def __str__(self):
        return self.title
    
class ImagesPost(models.Model):
    class Meta:
        verbose_name = 'Imagem do Post'
        verbose_name_plural = 'Imagens do Post'
    
    post = models.ForeignKey(Post, related_name='images', on_delete=models.CASCADE, blank=True, null=True,)
    image = models.ImageField(upload_to='posts/%Y/%m/%d')
    caption = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f"Imagem de {self.post}"