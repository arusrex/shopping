from django.db import models
from utils.model_validators import validate_png
from utils.images import resize_image, resize_image_slide

class MenuLink(models.Model):
    class Meta:
        verbose_name = 'Menu Link'
        verbose_name_plural = 'Menu Links'

    text = models.CharField(max_length=50)
    url_or_path = models.CharField(max_length=2048)
    new_tab = models.BooleanField(default=False)

    site_setup = models.ForeignKey('SiteSetup', on_delete=models.CASCADE, blank=True, null=True, default=None)

    def __str__(self):
        return self.text
    
class SiteSetup(models.Model):
    class Meta:
        verbose_name = 'Setup'
        verbose_name_plural = 'Setup'
    
    title = models.CharField(max_length=65)
    description = models.CharField(max_length=255, blank=True, null=True)
    title_welcome_banner = models.CharField(max_length=65, blank=True, null=True)
    welcome_banner = models.TextField(blank=True, null=True)
    title_best_banner = models.CharField(max_length=255, blank=True, null=True)
    best_banner = models.TextField(blank=True, null=True)
    link_best_banner = models.CharField(max_length=255, blank=True, null=True)
    operate_time_shop = models.TextField(blank=True, null=True)
    operate_time_food = models.TextField(blank=True, null=True)

    endereco = models.CharField(max_length=255, blank=True, null=True)
    numero = models.CharField(max_length=255, blank=True, null=True)
    bairro = models.CharField(max_length=255, blank=True, null=True)
    cidade_estado = models.CharField(max_length=255, blank=True, null=True)
    cep = models.CharField(max_length=255, blank=True, null=True)



    show_header = models.BooleanField(default=True)
    show_search = models.BooleanField(default=True)
    show_welcome_banner = models.BooleanField(default=True)
    show_best_banner = models.BooleanField(default=True)
    show_menu = models.BooleanField(default=True)
    show_description = models.BooleanField(default=True)
    show_pagination = models.BooleanField(default=True)
    show_footer = models.BooleanField(default=True)
    show_carousel = models.BooleanField(default=True)
    show_location = models.BooleanField(default=True)
    show_operate_shop = models.BooleanField(default=True)
    show_operate_food = models.BooleanField(default=True)



    slide1 = models.ImageField(upload_to='assets/slides/%Y/%m/%d/', blank=True, default='', validators=[validate_png])
    slide2 = models.ImageField(upload_to='assets/slides/%Y/%m/%d/', blank=True, default='', validators=[validate_png])
    slide3 = models.ImageField(upload_to='assets/slides/%Y/%m/%d/', blank=True, default='', validators=[validate_png])

    favicon = models.ImageField(upload_to='assets/favicon/%Y/%m/%d/', blank=True, default='', validators=[validate_png])

    def save(self, *args, **kwargs):
        current_favicon_name =  str(self.favicon.name)
        current_slide1_name = str(self.slide1.name)
        current_slide2_name = str(self.slide2.name)
        current_slide3_name = str(self.slide3.name)
        super().save(*args, **kwargs)
        favicon_changed = False
        slide1_changed = False
        slide2_changed = False
        slide3_changed = False

        if self.slide1:
            slide1_changed = current_slide1_name != self.slide1.name

        if self.slide2:
            slide2_changed = current_slide2_name != self.slide2.name

        if self.slide3:
            slide3_changed = current_slide3_name != self.slide3.name

        if self.favicon:
            favicon_changed = current_favicon_name != self.favicon.name

        if favicon_changed:
            resize_image(self.favicon, 32)
        
        if slide1_changed:
            resize_image_slide(self.slide1)

        if slide2_changed:
            resize_image_slide(self.slide2)

        if slide3_changed:
            resize_image_slide(self.slide3)

    def __str__(self):
        return self.title

