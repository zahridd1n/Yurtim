from django.db import models


class SocialMedia(models.Model):
    name = models.CharField(max_length=255)
    icon = models.FileField(upload_to='social_media/')
    link = models.URLField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Social Media'
        verbose_name_plural = 'Social Medias'


class Contact(models.Model):
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    message = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Xabarlar'
        verbose_name_plural = 'Xabarlar'


class ContactOur(models.Model):
    phone = models.CharField(max_length=255)
    email = models.EmailField()
    address_uz = models.TextField()
    address_ru = models.TextField(null=True, blank=True)
    address_en = models.TextField(null=True, blank=True)
    latitude = models.TextField(null=True, blank=True)
    longitude = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.phone
