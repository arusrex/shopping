from django.db import models
from utils.model_validators import validate_png
from utils.images import resize_image, resize_image_slide, resize_image_logo

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
    
    # TITLE SITE
    show_title = models.BooleanField(default=True)
    title = models.CharField(max_length=65)

    # DESCRIPTION / SLOGAN
    show_description = models.BooleanField(default=True)
    description = models.CharField(max_length=255, blank=True, null=True)

    # LOGO SITE
    show_logo = models.BooleanField(default=True)
    logo = models.ImageField(upload_to='assets/logo/%Y/%m/%d/', blank=True, null=True, validators=[validate_png])

    # LOGIN / REGISTER
    show_login = models.BooleanField(default=True)

    # BANNER WELCOME
    show_welcome_banner = models.BooleanField(default=True)
    title_welcome_banner = models.CharField(max_length=65, blank=True, null=True)
    welcome_banner = models.TextField(blank=True, null=True)

    # BANNER BESTS
    show_best_banner = models.BooleanField(default=True)
    title_best_banner = models.CharField(max_length=255, blank=True, null=True)
    best_banner = models.TextField(blank=True, null=True)
    link_best_banner = models.CharField(max_length=255, blank=True, null=True)

    # BANNER HISTORY
    show_history_banner = models.BooleanField(default=True)
    title_history_banner = models.CharField(max_length=255, blank=True, null=True)
    history_banner = models.TextField(blank=True, null=True)
    link_history_banner = models.CharField(max_length=255, blank=True, null=True)
    img_history = models.ImageField(upload_to='assets/img_history/%Y/%m/%d', blank=True, null=True, validators=[validate_png])

    # FOOTER OPERATING TIME
    show_operate_shop = models.BooleanField(default=True)
    operate_time_shop = models.TextField(blank=True, null=True)
    show_operate_food = models.BooleanField(default=True)
    operate_time_food = models.TextField(blank=True, null=True)

    # MAPS LOCATION
    show_location = models.BooleanField(default=True)
    endereco = models.CharField(max_length=255, blank=True, null=True)
    numero = models.CharField(max_length=255, blank=True, null=True)
    bairro = models.CharField(max_length=255, blank=True, null=True)
    cidade_estado = models.CharField(max_length=255, blank=True, null=True)
    cep = models.CharField(max_length=255, blank=True, null=True)

    # SOCIAL MEDIAS
    show_social = models.BooleanField(default=True)
    facebook = models.URLField(blank=True, null=True)
    instagram = models.URLField(blank=True, null=True)
    x_twitter = models.URLField(blank=True, null=True)
    youtube = models.URLField(blank=True, null=True)

    # ALL SETUPS
    show_header = models.BooleanField(default=True)
    show_footer = models.BooleanField(default=True)
    show_search = models.BooleanField(default=True)
    show_menu = models.BooleanField(default=True)
    show_pagination = models.BooleanField(default=True)
    show_subscribe = models.BooleanField(default=True)
    show_comments = models.BooleanField(default=True)
    show_news = models.BooleanField(default=True)
    show_events = models.BooleanField(default=True)

    # CAROUSEL SLIDES
    show_carousel = models.BooleanField(default=True)
    slide1 = models.ImageField(upload_to='assets/slides/%Y/%m/%d/', blank=True, default='', validators=[validate_png])
    slide1_title = models.CharField(max_length=65, blank=True, null=True)
    slide1_description = models.CharField(max_length=255, blank=True, null=True)

    slide2 = models.ImageField(upload_to='assets/slides/%Y/%m/%d/', blank=True, default='', validators=[validate_png])
    slide2_title = models.CharField(max_length=65, blank=True, null=True)
    slide2_description = models.CharField(max_length=255, blank=True, null=True)

    slide3 = models.ImageField(upload_to='assets/slides/%Y/%m/%d/', blank=True, default='', validators=[validate_png])
    slide3_title = models.CharField(max_length=65, blank=True, null=True)
    slide3_description = models.CharField(max_length=255, blank=True, null=True)

    favicon = models.ImageField(upload_to='assets/favicon/%Y/%m/%d/', blank=True, default='', validators=[validate_png])

    def save(self, *args, **kwargs):
        current_logo_name =  str(self.logo.name)
        current_img_history_name =  str(self.img_history.name)
        current_favicon_name =  str(self.favicon.name)
        current_slide1_name = str(self.slide1.name)
        current_slide2_name = str(self.slide2.name)
        current_slide3_name = str(self.slide3.name)
        super().save(*args, **kwargs)
        logo_changed = False
        img_history_changed = False
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
        
        if self.logo:
            logo_changed = current_logo_name != self.logo.name

        if self.img_history:
            img_history_changed = current_img_history_name != self.img_history.name

        if logo_changed:
            resize_image_logo(self.logo, 100)

        if favicon_changed:
            resize_image(self.favicon, 32)
        
        if slide1_changed:
            resize_image_slide(self.slide1)

        if slide2_changed:
            resize_image_slide(self.slide2)

        if slide3_changed:
            resize_image_slide(self.slide3)

        if img_history_changed:
            resize_image(self.img_history, 320)

    def __str__(self):
        return self.title

