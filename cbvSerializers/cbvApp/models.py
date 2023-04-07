from django.db import models

# Create your models here.
class Student(models.Model):
    id=models.IntegerField(primary_key=True)
    name=models.CharField(max_length=25)
    score=models.DecimalField(max_digits=12,decimal_places=2)

    def __str__(self) -> str:
        return self.id + self.name + self.score
