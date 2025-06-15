from django.db import models

# Create your models here.
#create the column headings for the database 


class Users_db(models.Model):
    username= models.CharField(max_length=20)
    Phone_num=models.IntegerField()
    email=models.CharField(max_length=30)
    Gender=models.CharField(max_length=6)
    birthday=models.DateField()
    
    #string representation
    '''
    def __str__(self):

        return (f"ID is {self.id}   user name is {self.username}\nthe Phone no. is {self.Phone_num}\nThe email addess is {self.email}\nthe gender is {self.Gender}\nThe birthday is {self.birthday}") 

'''
