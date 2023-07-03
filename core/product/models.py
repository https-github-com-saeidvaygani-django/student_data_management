from django.db import models

class HighSchoolMajor(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name

class Course(models.Model):
    name = models.CharField(max_length=100)
    high_school_major = models.ForeignKey(HighSchoolMajor, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name

class Student(models.Model):
    name = models.CharField(max_length=100)
    family_name = models.CharField(max_length=100)
    national_id = models.CharField(max_length=100)
    high_school_major = models.ForeignKey(HighSchoolMajor, on_delete=models.CASCADE)
    courses = models.ManyToManyField(Course)
    
    def __str__(self):
        return self.name
