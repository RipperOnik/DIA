from django.db import models


class Student(models.Model):
    full_name_text = models.CharField(max_length=20)
    birth_date = models.DateTimeField()

    def __str__(self):
        return self.full_name_text


class Discipline(models.Model):
    discipline_name_text = models.CharField(max_length=20)

    def __str__(self):
        return self.discipline_name_text

    def __repr__(self):
        return self.discipline_name_text


class Group(models.Model):
    group_name_text = models.CharField(max_length=20)
    students = models.ManyToManyField(Student)
    discipline = models.ForeignKey(Discipline, on_delete=models.CASCADE)

    def __str__(self):
        return self.group_name_text


class Schedule(models.Model):
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    date_time = models.DateTimeField()
