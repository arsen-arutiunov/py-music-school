from django.db import models


class Musician(models.Model):
    first_name = models.CharField(max_length=63)
    last_name = models.CharField(max_length=63)
    instrument = models.CharField(max_length=63)
    age = models.IntegerField()
    date_of_applying = models.DateField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if self.age < 14:
            raise ValueError("Age must be 14 or older.")
        super().save(*args, **kwargs)

    @property
    def is_adult(self):
        return self.age >= 21

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        verbose_name = "musician"
        verbose_name_plural = "musicians"
