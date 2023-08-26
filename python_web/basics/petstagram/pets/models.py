from django.db import models


class Pet(models.Model):

    CAT = 'Cat'
    DOG = 'Dog'
    PARROT = 'Parrot'
    DEFAULT = 'Unknown'

    PET_TYPES = [
        (CAT, 'Cat'),
        (DOG, 'Dog'),
        (PARROT, 'Parrot'),
        (DEFAULT, 'Unknown'),

    ]

    type = models.CharField(max_length=8, choices=PET_TYPES, default=PET_TYPES)
    name = models.CharField(max_length=6, blank=False)
    age = models.PositiveIntegerField(blank=False)
    description = models.TextField(blank=False)
    image_url = models.URLField(blank=False)

    def __str__(self):
        return f"{self.id} {self.name} {self.age}"


class Like(models.Model):
    like = models.ForeignKey(Pet, on_delete=models.CASCADE)
    comment = models.CharField(max_length=5)


class Comment(models.Model):
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE)
    text = models.TextField(blank=False)
