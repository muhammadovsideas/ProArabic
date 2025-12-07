from django.db import models
from django.conf import settings
from users.models import User
from django_ckeditor_5.fields import CKEditor5Field


class Lesson(models.Model):
    title = models.CharField(max_length=255)
    description = CKEditor5Field('description',null=True,blank=True)
    video = models.FileField(upload_to="lessons/videos/", blank=True, null=True)
    image = models.ImageField(upload_to="lessons/images/", blank=True, null=True)
    file = models.FileField(upload_to="lessons/files/", blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class LessonImage(models.Model):
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, related_name="images")
    image = models.ImageField("Image", upload_to='lessons/files/', blank=True, null=True)

    def __str__(self):
        return str(self.image)


class Book(models.Model):
    title = models.CharField(max_length=255)
    description = CKEditor5Field('description', null=True,blank=True)
    author = models.CharField(max_length=255, blank=True)
    pdf = models.FileField(upload_to="books/pdf/")
    image = models.ImageField(upload_to="books/images/", blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class BookImage(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name="images")
    image = models.ImageField("Image", upload_to='books/files/', blank=True, null=True)

    def __str__(self):
        return str(self.image)

class SocialLinks(models.Model):
    telegram_channel = models.URLField(max_length=500, blank=True, null=True)
    telegram_bot = models.URLField(max_length=500, blank=True, null=True)
    instagram = models.URLField(max_length=500, blank=True, null=True)
    youtube = models.URLField(max_length=500, blank=True, null=True)
    facebook = models.URLField(max_length=500, blank=True, null=True)

    def __str__(self):
        return self.telegram_channel

class Announcement(models.Model):
    title = models.CharField(max_length=255)                # e'lon sarlavhasi
    description = CKEditor5Field('description',null=True,blank=True)                         # matn (uzun)
    image = models.ImageField(upload_to="announcements/images/",blank=True, null=True)        # ixtiyoriy rasm
    created_at = models.DateTimeField(auto_now_add=True)     # avtomatik vaqt
    updated_at = models.DateTimeField(auto_now=True)         # o'zgartirilgan sana
    is_active = models.BooleanField(default=True)            # ko‘rsatish/ko‘rsatmaslik

    def __str__(self):
        return self.title

class AnnouncementImage(models.Model):
    announcement = models.ForeignKey(Announcement, on_delete=models.CASCADE, related_name="images")
    image = models.ImageField("Image", upload_to='announcements/files/', blank=True, null=True)

    def __str__(self):
        return str(self.image)


class About(models.Model):
    title = models.CharField("About title", max_length=255)
    description = CKEditor5Field('description',null=True,blank=True)
    image = models.ImageField("About images", upload_to='about/images/', blank=True, null=True)
    
    def __str__(self):
        return self.title


class AboutImage(models.Model):
    about = models.ForeignKey(About, on_delete=models.CASCADE, related_name="images")
    image = models.ImageField("Image", upload_to='about/images', blank=True, null=True)

    def __str__(self):
        return str(self.image)

class Certificate(models.Model):
    name = models.CharField(max_length=255)
    description = CKEditor5Field('description',null=True,blank=True)
    image = models.ImageField("Certificate images", upload_to='certificates/images/', blank=True, null=True)

class SertificateImage(models.Model):
    sertificate = models.ForeignKey(Certificate, on_delete=models.CASCADE, related_name="images")
    image = models.ImageField("Image", upload_to='certificates/images/', blank=True, null=True)

    def __str__(self):
        return str(self.image)

class Results(models.Model):
    name = models.CharField(max_length=255,null=True,blank=True)
    description = CKEditor5Field('description',null=True,blank=True)
    image = models.ImageField("Image", upload_to='results/images/', blank=True, null=True)

class ResultsImage(models.Model):
    results = models.ForeignKey(Results, on_delete=models.CASCADE, related_name="images")
    image = models.ImageField("Image", upload_to='results/images/', blank=True, null=True)

    def __str__(self):
        return str(self.image)