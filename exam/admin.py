from django.contrib import admin

from .models import Stage,Exam,ExamModule

# Register your models here.
@admin.register(Stage)
class StageAdmin(admin.ModelAdmin):
    list_display=['stage','month','year']

class ExamModuleInline(admin.TabularInline):
    model=ExamModule
    extra=1

@admin.register(Exam)
class ExamAdmin(admin.ModelAdmin):
    list_display=['user','score','Career']
    inlines=[ExamModuleInline]