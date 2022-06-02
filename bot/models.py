from django.db import models

from core.models import User


class TgUser(models.Model):
    chat_id = models.PositiveBigIntegerField(unique=True)
    username = models.CharField(max_length=255, null=True, blank=True, default=None)
    user = models.ForeignKey(User, on_delete=models.PROTECT, null=True, blank=True, default=None)
    verification_code = models.CharField(max_length=50, blank=True, null=True, default=None)

    def __str__(self):
        if self.username:
            return self.username
        elif self.user and self.user.username:
            return self.user.username
        else:
            return super().__str__()

    class Meta:
        verbose_name = 'TG User'
        verbose_name_plural = 'TG User'

