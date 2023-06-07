from allauth.socialaccount.models import SocialAccount
from allauth.socialaccount.signals import pre_social_login
from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from allauth.account.signals import user_signed_up
from django.dispatch import receiver
from urllib.request import urlopen
from django.core.files import File
from django.utils.crypto import get_random_string


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    phone_number = models.CharField(max_length=20, blank=True, null=True, default="", verbose_name='Телефон')
    phone_number_is_confirmed = models.BooleanField(default=False, verbose_name='Телефон подтверждён')
    address = models.TextField(blank=True, null=True, default="", verbose_name='Адрес')
    image = models.ImageField(upload_to='user_images/', default='user_images/default.jpg', verbose_name='Фото')

    def __str__(self):
        return f'Профиль {self.user}'

    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'


@receiver(user_signed_up)
def handle_user_signed_up(request, user, **kwargs):
    profile = Profile.objects.create(user=user)
    social_account = SocialAccount.objects.filter(user=user).first()
    if social_account:
        profile_image_url = social_account.get_avatar_url()
        if profile_image_url:
            response = urlopen(profile_image_url)
            image_file = File(response)
            profile.image.save(f'{user}_image.jpg', image_file)
    profile.save()
