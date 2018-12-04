from django.db import models
from django.utils import timezone

class Student(models.Model):
	rollno = models.IntegerField(primary_key=True)
	name = models.CharField(max_length=50)
	def __str__(self):
		return self.name

class Quiz(models.Model):
	name = models.CharField(max_length=20)
	prof = models.CharField(max_length=40)
	classaverage = models.FloatField(null=True, blank=True)
	def __str__(self):
		return self.name

class QuizResult(models.Model):
	quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
	student = models.ForeignKey(Student, on_delete=models.CASCADE)
	marks = models.IntegerField()
	def __str__(self):
		return str(self.quiz.name+'-marks-for-'+self.student.name)
	def save(self, *args, **kwargs):
		avg = 0
		objs = QuizResult.objects.filter(quiz=self.quiz)
		for obj in objs:
			avg = avg + obj.marks
		count = len(objs)
		if self.pk is None:
			count +=1
			avg = avg + self.marks
		avg = avg/(count)
		self.quiz.classaverage = avg
		self.quiz.save()
		super(QuizResult, self).save(*args, **kwargs)

'''from django.db import models

# Create your models here.

class Enrollments(models.Model):
    course_id = models.CharField(max_length=15)
    student_id = models.CharField(max_length=15)
    student_name = models.CharField(max_length=15)
    prof_id = models.CharField(max_length=15)
    status = models.CharField(max_length=15)

class Marks(models.Model):
    student_name = models.CharField(max_length=15)
    student_id = models.CharField(default=0,max_length=15)
    course_id = models.CharField(default=0,max_length=15)
    prof_id = models.CharField(default=0,max_length=15)
    marks = models.FloatField(default=0)
    q_name = models.CharField(max_length=15)

    class Meta:
        unique_together = ('student_id', 'course_id','prof_id','q_name','student_name')'''

"""class Marks(models.Model):
    student_id = models.ForeignKey(Enrollments,on_delete=models.PROTECT)
    course_id = models.ForeignKey(Enrollments, on_delete=models.PROTECT)
    marks = models.FloatField(null=False)
    q_name = models.CharField(max_length=15)"""