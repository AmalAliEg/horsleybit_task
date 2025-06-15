from django.db import models

# Create your models here.


#class for the courses 
class Course(models.Model):
    name= models.CharField(max_length=30)
    code=models.CharField(max_length=10, unique=True)
    credit_hours = models.PositiveSmallIntegerField()
    
    #string representation 
    def __str__(self):
        return (f"ID is {self.id} Course name is {self.name}, the course code is {self.code} the credit hour is ${self.credit_hours}")



class Student(models.Model):
    #username, password , email
    username=models.CharField(max_length=20)
    password=models.IntegerField()
    email=models.CharField(max_length=30)
    courses_no=models.IntegerField()
    courses_name=models.ManyToManyField(Course,related_name='students')

    #string representation 
    def __str__(self):
        return (f"ID is {self.id}, student name is {self.username} the email addess is {self.email}, number of courses taken is {self.courses_no}")
    


class Grade(models.Model):
    student= models.ForeignKey(Student, on_delete=models.CASCADE)
    course=models.ForeignKey(Course,on_delete=models.CASCADE)
    score=models.FloatField()
    #creat the coorospond char
    charCro=models.CharField(max_length=2)

    #string representation
    def __str__(self):
        return (f"ID is {self.id} the numerical grade is ${self.score} the corospond grade is {self.charCro}")

class Teacher(models.Model):
    username= models.CharField(max_length=20)
    password=models.IntegerField()
    email=models.CharField(max_length=30)
    courses_no=models.IntegerField()
    courses_name=models.ForeignKey(Course,related_name='teachers',on_delete=models.CASCADE)
    
    #string representation
    def __str__(self):

        return (f"ID is {self.id} teacher name is {self.username} the email addess is {self.email}, the number of the courses is {self.courses_no}, the courses' name is {self.courses_name}")
