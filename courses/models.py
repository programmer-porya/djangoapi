from django.db import models

class Course(models.Model):
 	name = models.CharField('Course name',max_length=50)
 	language = models.CharField('Course language',max_length=50)
 	price = models.CharField('Course price',max_length=10)


 	def __str__(self):
 		return self.name