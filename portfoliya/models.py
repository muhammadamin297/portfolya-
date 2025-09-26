from django.db import models

class AboutMe(models.Model):
    title = models.CharField(max_length=100)
    def __str__(self):
        return self.title



class Skills(models.Model):
    title = models.CharField(max_length=100)
    def __str__(self):
        return self.title


class Experiences(models.Model):
    title = models.CharField(max_length=100)
    def __str__(self):
        return self.title


class Portfolio(models.Model):
    title = models.CharField(max_length=100)
    github_link = models.URLField(max_length=200, blank=True, null=True)
    def __str__(self):
        return self.title

import random
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from .utils import send_verification_code

class Student(models.Model):
    email = models.EmailField(unique=True)
    code = models.CharField(max_length=6, blank=True, null=True, editable=False)  # 🔒 admin ko‘rmasin
    is_verified = models.BooleanField(default=False, editable=False)  # 🔒 admin qo‘lda o‘zgartirmasin
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email


@receiver(post_save, sender=Student)
def send_code_on_create(sender, instance, created, **kwargs):
    if created:
        code = str(random.randint(100000, 999999))  # 6 xonali kod
        instance.code = code
        instance.save()
        send_verification_code(instance.email, code)
