from django.db import models


class Base(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField


    class Meta:
        verbose_name = "Base"
        verbose_name_plural = "Base"

class BotKeys(models.Model):
    token = models.CharField(max_length=255)
    chat_id = models.CharField(max_length=255)

    class Meta:
        verbose_name = "Bot Keys"
        verbose_name_plural = "Bot Keys"

    def __str__(self):
        return self.token