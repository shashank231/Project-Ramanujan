from django.db import models
from django.contrib.auth.models import User   # Profile me use kia hai
from django_mysql.models import ListCharField

class Display(models.Model):
    qnum = models.CharField(max_length=15, null=True)
    qnam = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.qnum

class Question(models.Model):
    ques = models.ForeignKey(Display, null=True, blank=True, on_delete=models.CASCADE)
    que = models.TextField(max_length=500, null=True)
    ans = models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.ques.qnam


class Profile(models.Model):
    anna = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, null=True)
    phone = models.CharField(max_length=12, null=True)
    note = models.CharField(max_length=100, null=True)
    pic = models.ImageField(default="default.png", null=True, blank=True)
    score = models.IntegerField(null=True, blank=True, default=0)
    qdone = ListCharField(
        base_field=models.CharField(max_length=16, null=True, blank=True),
        size=6,
        max_length=(6 * 17),
        default=[0],
    )

    def __str__(self):
        return self.anna.username




