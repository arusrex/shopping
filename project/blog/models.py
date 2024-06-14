from django.db import models
from django.contrib.auth.models import User
from utils.rands import slug_rand
from utils.images import resize_image, resize_image_slide
from django_summernote.models import AbstractAttachment
from django.urls import reverse
from django.template.defaultfilters import slugify

class Profile(models.Model):
    user = models.OneToOneField(User, related_name='profile_image', on_delete=models.CASCADE)
    profile_image = models.ImageField(upload_to='profile_images/', blank=True, null=True)

    def save(self, *args, **kwargs):
        current_profile_image_name = str(self.profile_image.name)
        super_save = super().save(*args, **kwargs)
        profile_image_changed = False

        if self.profile_image:
            profile_image_changed = current_profile_image_name != self.profile_image.name
        
        if profile_image_changed:
            resize_image(self.profile_image, 100, True, 70)
        
        return super_save

    def __str__(self):
        return f'{self.user.username} Profile'

# MODEL ATTACHMENTS SUMMERNOTE

class PostAttachment(AbstractAttachment):
    def save(self, *args, **kwargs):
        if not self.name:
            self.name = self.file.name
            
        current_file_name = str(self.file.name)
        super_save = super().save(*args, **kwargs)
        file_changed = False

        if self.file:
            file_changed = current_file_name != self.file.name
        
        if file_changed:
            resize_image(self.file, 939, True, 70)
        
        return super_save
    

# MODELS TAGS

class Tag(models.Model):
    class Meta:
        verbose_name = 'Tag'
        verbose_name_plural = 'Tags'

    name = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(unique=True, default=None, blank=True, null=True, max_length=255)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slug_rand(self.name)
        return super(Tag, self).save(*args, **kwargs)
    
    def __str__(self):
        return self.name
    

# MODELS CATEGORY

class Category(models.Model):
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(unique=True, default=None, blank=True, null=True, max_length=255)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slug_rand(self.name)
        return super(Category, self).save(*args, **kwargs)
    
    def __str__(self):
        return self.name


# MODELS PAGE

class Page(models.Model):
    class Meta:
        verbose_name = 'Page'
        verbose_name_plural = 'Pages'

    is_published = models.BooleanField(default=False, help_text='Esta opção é necessária para publicar a página')
    title = models.CharField(max_length=255,)
    slug = models.SlugField(unique=True, default='', null=False, blank=True, max_length=255)
    content = models.TextField()

    def get_absolute_url(self):
        if not self.is_published:
            return reverse('blog:index')

        return reverse("blog:page", args=(self.slug,))

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slug_rand(self.title)
        return super(Page, self).save(*args, **kwargs)
    
    def __str__(self):
        return self.title
    

# MODELS POST
    
class PostManager(models.Manager):
    def get_published(self):
        return self.filter(is_published=True)
    
class Post(models.Model):
    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'

    objects = PostManager()

    title = models.CharField(max_length=255)
    short_description = models.CharField(max_length=255)
    description = models.TextField()
    number = models.IntegerField()
    fone = models.CharField(max_length=20, blank=True, null=True, default='N/D')
    whatsapp = models.BigIntegerField(blank=True, null=True)
    email = models.EmailField(max_length=255, blank=True, null=True)
    site = models.URLField(blank=True, null=True)
    facebook = models.URLField(blank=True, null=True)
    instagram = models.URLField(blank=True, null=True)
    x_twitter = models.URLField(blank=True, null=True)
    youtube = models.URLField(blank=True, null=True)
    cover = models.ImageField(upload_to="posts/%Y/%m/%d", blank=True, default='', help_text='Imagem para exibição no início',)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True, related_name='post_created_by')
    updated_at = models.DateTimeField(auto_now=True)
    updated_by = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True, related_name='post_updated_by')

    slug = models.SlugField(unique=True, default='', null=False, blank=True, max_length=255)
    is_published = models.BooleanField(default=False, help_text='Esta opção é necessária para publicar a loja',)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, blank=True, null=True, default=None)
    tags = models.ManyToManyField(Tag, blank=True)

    def get_absolute_url(self):
        if not self.is_published:
            return reverse('blog:index')

        return reverse("blog:post", args=(self.slug,))
    

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slug_rand(self.title)

        current_cover_name = str(self.cover.name)
        super_save = super().save(*args, **kwargs)
        cover_changed = False

        if self.cover:
            cover_changed = current_cover_name != self.cover.name
        
        if cover_changed:
            resize_image(self.cover, 939, True, 70)
        
        return super_save

    def __str__(self):
        return self.title
    
class ImagesPost(models.Model):
    class Meta:
        verbose_name = 'Imagem do Post'
        verbose_name_plural = 'Imagens do Post'
    
    post = models.ForeignKey(Post, related_name='images', on_delete=models.CASCADE, blank=True, null=True,)
    image = models.ImageField(upload_to='posts/%Y/%m/%d', blank=True, null=True)
    caption = models.CharField(max_length=255, blank=True, null=True)

    def save(self, *args, **kwargs):
        current_image_name = str(self.image.name)
        super_save = super().save(*args, **kwargs)
        image_changed = False

        if self.image:
            image_changed = current_image_name != self.image.name
        
        if image_changed:
            resize_image_slide(self.image, 939, 537, True, 70)
        
        return super_save

    def __str__(self):
        return f"Imagem de {self.post}"


# MODELS NEWS

class NewsManager(models.Manager):
    def get_published(self):
        return self.filter(is_published=True)

class News(models.Model):
    class Meta:
        verbose_name = 'New'
        verbose_name_plural = "News"

    objects = NewsManager()

    is_published = models.BooleanField(default=True)
    title = models.CharField(max_length=255)
    short_description = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    cover = models.ImageField(upload_to='news/%Y/%m/%d')
    cover_caption = models.CharField(max_length=255, blank=True, null=True)
    slug = models.SlugField(unique=True, default='', null=False, blank=True, max_length=255)

    def get_absolute_url(self):
        if not self.is_published:
            return reverse('blog:index')

        return reverse("blog:new", args=(self.slug,))

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slug_rand(self.title)

        current_cover_name = str(self.cover.name)
        super_save = super().save(*args, **kwargs)
        cover_changed = False

        if self.cover:
            cover_changed = current_cover_name != self.cover.name
        
        if cover_changed:
            resize_image(self.cover, 939, True, 70)
        
        return super_save

    def __str__(self):
        return self.title
    
class ImageNew(models.Model):
    class Meta:
        verbose_name = 'Imagem da New'
        verbose_name_plural = 'Imagens da New'

    new = models.ForeignKey(News, related_name='images', on_delete=models.CASCADE, blank=True, null=True)
    image = models.ImageField(upload_to='news/%Y/%m/%d')

    def save(self, *args, **kwargs):
        current_image_name = str(self.image.name)
        super_save = super().save(*args, **kwargs)
        image_changed = False

        if self.image:
            image_changed = current_image_name != self.image.name
        
        if image_changed:
            resize_image_slide(self.image, 939, 537, True, 70)
        
        return super_save

    def __str__(self):
        return f'Imagens da New {self.new}'

class CommentsNews(models.Model):
    is_published = models.BooleanField(default=True)
    new = models.ForeignKey(News, related_name='comments', on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Comment by {self.author} on {self.new}'



# MODELS EVENTS

class EventsManager(models.Manager):
    def get_published(self):
        return self.filter(is_published=True)

class Events(models.Model):
    class Meta:
        verbose_name = 'Event'
        verbose_name_plural = "Events"

    objects = EventsManager()

    is_published = models.BooleanField(default=True)
    title = models.CharField(max_length=255)
    short_description = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    cover = models.ImageField(upload_to='events/%Y/%m/%d')
    cover_caption = models.CharField(max_length=255, blank=True, null=True)
    slug = models.SlugField(unique=True, default='', null=False, blank=True, max_length=255)

    def get_absolute_url(self):
        if not self.is_published:
            return reverse('blog:index')

        return reverse("blog:event", args=(self.slug,))

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slug_rand(self.title)
            
        current_cover_name = str(self.cover.name)
        super_save = super().save(*args, **kwargs)
        cover_changed = False

        if self.cover:
            cover_changed = current_cover_name != self.cover.name
        
        if cover_changed:
            resize_image(self.cover, 939, True, 70)
        
        return super_save

    def __str__(self):
        return self.title
    
class ImageEvent(models.Model):
    class Meta:
        verbose_name = 'Imagem do Event'
        verbose_name_plural = 'Imagens do Event'

    event = models.ForeignKey(Events, related_name='images', on_delete=models.CASCADE, blank=True, null=True)
    image = models.ImageField(upload_to='events/%Y/%m/%d')

    def save(self, *args, **kwargs):
        current_image_name = str(self.image.name)
        super_save = super().save(*args, **kwargs)
        image_changed = False

        if self.image:
            image_changed = current_image_name != self.image.name
        
        if image_changed:
            resize_image_slide(self.image, 939, 537, True, 70)
        
        return super_save

    def __str__(self):
        return f'Imagens do Event {self.event}'

class CommentsEvents(models.Model):
    is_published = models.BooleanField(default=True)
    event = models.ForeignKey(Events, related_name='comments', on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Comment by {self.author} on {self.event}'

