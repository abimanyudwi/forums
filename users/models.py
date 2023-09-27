from django.db import models
from django.contrib.auth.models import AbstractUser
from django.shortcuts import reverse
import main.models

# Create your models here.


class User(AbstractUser):
    class Role(models.TextChoices):
        ADMIN = "ADMIN", "Admin"
        USER = "USER", "User"
        VERIFIKATOR = "VERIFIKATOR", "Verifikator"

    base_role = Role.ADMIN
    is_verified = models.BooleanField(default=True)
    role = models.CharField(max_length=50, choices=Role.choices)
    is_candidate = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        if not self.pk:
            self.role = self.base_role
        return super().save(*args, **kwargs)

    def get_url(self):
        user = User.objects.exclude(role="VERIFIKATOR").get(email=self.email)

        slug = main.models.Author.objects.get(user=user)
        return reverse("lihat-profil-user", kwargs={"slug": slug.slug})

    def requester(self):
        user = User.objects.exclude(role="VERIFIKATOR").get(email=self.email)
        #
        slug = main.models.Author.objects.get(user=user)
        requester = slug
        return requester


class Translator(User):
    base_role = User.Role.USER

    class Meta:
        proxy = True


class Verifikator(User):
    base_role = User.Role.VERIFIKATOR

    class Meta:
        proxy = True
