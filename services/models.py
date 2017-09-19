from django.conf import settings
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)


class Keg(models.Model):
    name = models.CharField(max_length=100, blank=False, default='Keg1')
    created = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey('auth.User', related_name='kegs')

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('created',)


class Recipe(models.Model):
    name = models.CharField(max_length=100, default='Recipe1')
    srm = models.FloatField()
    ibus = models.FloatField()
    created = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey('auth.User', related_name='recipes')

    class Meta:
        ordering = ('created',)


class KegRecipe(models.Model):
    keg_id = models.ManyToManyField(Keg)
    recipe_id = models.ManyToManyField(Recipe)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('created',)
