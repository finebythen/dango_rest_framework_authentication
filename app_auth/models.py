from django.conf import settings
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.validators import MinValueValidator, MaxValueValidator
from rest_framework.authtoken.models import Token


USER = settings.AUTH_USER_MODEL


class Author(models.Model):
    first_name = models.CharField(max_length=50, null=False, blank=False)
    last_name = models.CharField(max_length=50, null=False, blank=False)
    born = models.IntegerField(default=1900, validators=[MinValueValidator(1700), MaxValueValidator(2022)])
    died = models.IntegerField(null=True, blank=True)
    age = models.IntegerField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['last_name', 'first_name']
        constraints = [
            models.UniqueConstraint(fields=['last_name', 'first_name'], name='unique author')            
        ]
        verbose_name = "Author"
        verbose_name_plural = "Authors"

    def save(self, *args, **kwargs):
        if self.died is None:
            self.age = None
        elif self.died is not None and self.died < self.born:
            self.age = None
        else:
            self.age = self.died - self.born
        super(Author, self).save(*args, **kwargs)

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"


class Book(models.Model):
    title = models.CharField(max_length=50, null=False, blank=False)
    author = models.ForeignKey(Author, null=False, blank=False, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['title', 'author']
        constraints = [
            models.UniqueConstraint(fields=['title', 'author'], name='unique book author')
        ]
        verbose_name = 'Book'
        verbose_name_plural = 'Books'

    def __str__(self) -> str:
        return self.title


@receiver(post_save, sender=USER)
def create_auth_token(sender, instance, created, *args, **kwargs):
    if created:
        Token.objects.create(user=instance)
