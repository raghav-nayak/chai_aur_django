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


# one to many models
class ChaiReview(models.Model):
    chai = models.ForeignKey(
        to=ChaiVariety, on_delete=models.CASCADE, related_name="reviews"
    )
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    rating = models.IntegerField()
    comment = models.TextField()
    date_added = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.user.username} review for {self.chai.name}"


# many to many models
class Store(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    chai_varieties = models.ManyToManyField(to=ChaiVariety, related_name="stores")

    def __str__(self):
        return self.name


# one to one
class ChaiCertificate(models.Model):
    chai = models.OneToOneField(
        ChaiVariety, on_delete=models.CASCADE, related_name="certificate"
    )
    certificate_number = models.CharField(max_length=100)
    issued_date = models.DateTimeField(default=timezone.now)
    valid_till = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"Certificate for {self.chai.name}"
