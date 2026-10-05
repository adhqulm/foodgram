"""Models for the users app."""

from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    """Custom user model."""

    email = models.EmailField(
        'Email address',
        max_length=254,
        unique=True
    )
    first_name = models.CharField(
        'First name',
        max_length=150
    )
    last_name = models.CharField(
        'Last name',
        max_length=150
    )
    avatar = models.ImageField(
        'Avatar',
        upload_to='avatars/',
        null=True,
        blank=True
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']

    class Meta:
        """User model metadata."""

        ordering = ['id']
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    def __str__(self):
        """Return the string representation of the user."""
        return self.username


class Subscription(models.Model):
    """Model for subscriptions to authors."""

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='follower',
        verbose_name='Subscriber'
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='following',
        verbose_name='Author'
    )

    class Meta:
        """Subscription model metadata."""

        ordering = ['-id']
        verbose_name = 'Subscription'
        verbose_name_plural = 'Subscriptions'
        constraints = [
            models.UniqueConstraint(
                fields=['user', 'author'],
                name='unique_subscription'
            ),
            models.CheckConstraint(
                check=~models.Q(user=models.F('author')),
                name='no_self_subscription'
            )
        ]

    def __str__(self):
        """Return the string representation of the subscription."""
        return f'{self.user} is subscribed to {self.author}'
