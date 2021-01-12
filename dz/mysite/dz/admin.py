from django.contrib import admin

from .models import Student, Group, Discipline, Schedule

admin.site.register(Student)
admin.site.register(Group)
admin.site.register(Schedule)
admin.site.register(Discipline)
