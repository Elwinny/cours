from django.db import models
import locale
from django.utils.text import slugify
from ckeditor.fields import RichTextField
from django.contrib.auth.models import AbstractUser
from core.utils.slug_title import generate_slug
from django.utils.translation import gettext_lazy as _


# Create your models here.






# BaseModel

class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True




# Category

class Category(BaseModel):
    title = models.CharField(max_length=255)
    icon_class = models.CharField(max_length=255)
    
    class Meta:
        verbose_name = _("Category")
        verbose_name_plural = _("Categories")

    def __str__(self):
        return self.title



# Setting

class Setting(BaseModel):
    phone = models.CharField(max_length=255)
    header_title = models.CharField(max_length=255)
    email = models.EmailField()
    logo = models.CharField(max_length=255)
    facebook = models.URLField()
    twitter = models.URLField()
    instagram = models.URLField()
    bgimg = models.ImageField(upload_to="bgimg")
    title = models.CharField(max_length=255)
    description = models.TextField()
    location = models.CharField(max_length=255)
    advertising_product_title = models.CharField(max_length=255)
    advertising_product_content = models.CharField(max_length=255)
    footer_title = models.CharField(max_length=255)
    footer_content = models.CharField(max_length=255)
    footer_copyright = models.CharField(max_length=255)
    social_advertising_title = models.CharField(max_length=255)
    social_advertising_content = models.CharField(max_length=255)

    

    class Meta:
        verbose_name = _("Setting")
        verbose_name_plural = _("Settings")

    
    def __str__(self):
        return  self.title







# Product

class Product(BaseModel):
    title = models.CharField(max_length=255)
    content = RichTextField()
    image = models.ImageField(upload_to="product", null=True, blank=True)
    price = models.IntegerField(default=0)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    slug = models.SlugField(null=True, blank=True)
    is_activate = models.BooleanField(default=True)


    def __str__(self):
        return self.title
    

    class Meta:
        verbose_name = _("Product")
        verbose_name_plural = _("Products")
        
    def save(self, *args, **kwargs):
        self.slug = slugify(f"{self.title}")
        super().save(*args, **kwargs)




# News

class News (BaseModel):
    title = models.CharField(max_length=255)
    content = models.TextField(help_text="Aqlina Geleni Yazma")
    image = models.ImageField(upload_to="news", null=True, blank=True)
    creat_at = models.DateTimeField(auto_now_add=True)
    like = models.IntegerField(default=0)
    dislike = models.IntegerField(default=0)
    views = models.IntegerField(default=0)
    category = models.ForeignKey('Category', on_delete=models.CASCADE ,  null=True, blank=True)



    def __str__(self):
        return  self.title




# Testimonial

class Testimonial(BaseModel):
    content = models.TextField()
    title = models.CharField(max_length=255)
    job = models.CharField(max_length=255)
    image = models.ImageField(upload_to="testimonial", null=True , blank=True)

    class Meta:
        verbose_name = _("Testimonial")
        verbose_name_plural = _("Testimonials")

    def __str__(self):
        return self.title




# Contact

class Contact(BaseModel):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=100)
    message = models.TextField()



# Advertising


class Advertising(BaseModel):
    title = models.CharField(max_length=255)
    content = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    image = models.ImageField(upload_to="advertising", null=True, blank=True)




    class Meta:
        verbose_name = _("Advertising")
        verbose_name_plural = _("Advertisings")
    
    def __str__(self):
        return self.title


