from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


# Create your models here.
class ChaiVariety(models.Model):
    CHAI_TYPES = [
        ("ML", "MASALA"),
        ("GR", "GINGER"),
        ("PL", "PLAIN"),
        ("EL", "ELAICHI"),
    ]

    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to="chais/")
    date_added = models.DateTimeField(default=timezone.now)
    type = models.CharField(max_length=2, choices=CHAI_TYPES)
    description = models.TextField(default="")

    def __str__(self):
        return self.name


# one to many model
class ChaiReview(models.Model):
    chai = models.ForeignKey(
        to=ChaiVariety, one_delete=models.CASCADE, related_name="reviews"
    )
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    rating = models.IntegerField()
    comment = models.TextField()
    date_added = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.user.username} review for {self.chai.name}"
