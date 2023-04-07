from django.db import models

#By default django creates id column for each model
#And when we do not give any primary key to 1st table and in
#other table we make a forein key then, the 2nd table will take 
#the id column of 1st table as pk.

# Create your models here.
class Author(models.Model):
    
    # field_name = models.Field(primary_key = True) it is created by default
    firstname=models.CharField(max_length=20)
    lasttname=models.CharField(max_length=20)

    def __str__(self) -> str:
        return self.firstname+"_"+self.lasttname

class Book(models.Model):
    title=models.CharField(max_length=20)
    ratings=models.CharField(max_length=20)
    author=models.ForeignKey(Author,related_name='books', on_delete=models.CASCADE)
#with this a author_id colum will be created which will relate to author id against each book