from django.contrib.auth.models import AbstractUser

from django.db import models


# Create your models here.
import user.models


class Profile(AbstractUser):
    # برای استففاده از یوزر خود جنگو
    # user = models.OneToOneField(User, on_delete=models.CASCADE)
    REQUIRED_FIELDS = []
    USERNAME_FIELD = 'username'
    GENDER_CHOICES = [('M', 'Male'), ('F', 'Female')]

    first_name = models.CharField('first name', max_length=100, null=True)
    last_name = models.CharField('last name', max_length=100, null=True, blank=True)
    username = models.CharField('username', max_length=50, unique=True)
    # profile = models.TextField('description', max_length=150)
    gender = models.CharField('gender', choices=GENDER_CHOICES, max_length=1, default='F')
    phone_number = models.CharField('phone number', max_length=11, blank=True)
    biography = models.CharField('biography', max_length=50, null=True)
    country = models.CharField('country', max_length=20, null=True)
    website = models.URLField('website')
    email = models.EmailField('email')
    register_date = models.DateTimeField('register date', auto_now_add=True)
    updated = models.DateTimeField('update date', auto_now=True)
    credit = models.IntegerField('credit', default=20)
    friends = models.ManyToManyField("Profile", blank=True, related_name='my_friend')

    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'

    def __str__(self):
        return f'{self.username} registered at {self.register_date}'

    def delete(self):
        message = f'{self.fullname} deleted!'
        self.delete()
        return message

    def update_credit(self, amount):
        self.credit += amount
        self.save()

    def get_friend(self):
        return self.friends.all()

    def get_friend_no(self):
        return self.friends.count()

    def get_book(self):
        return self.user.all()

    def get_book_no(self):
        return self.user.count()


class Relationship(models.Model):
    STATUS_CHOICES = [('A', 'accepted'), ('R', 'requested'), ('N', 'none')]
    sender = models.ForeignKey(Profile, max_length=20, on_delete=models.CASCADE, related_name='sender')
    receiver = models.ForeignKey(Profile, max_length=50, on_delete=models.CASCADE, related_name='receiver')
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default='N')
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.sender}, {self.receiver}, {self.status}"
