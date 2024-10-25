from django.db import models

# Create your models here.

class Students(models.Model):
    name = models.CharField(max_length=20)
    roll = models.IntegerField(primary_key= True)
    address = models.TextField()
    father_name = models.TextField(default="Rahim")
    # father_name = models.TextField(null= True)
    # father_name = models.TextField(blank= True)

    def __str__(self):
        return f"Roll : {self.roll} {self.name}"