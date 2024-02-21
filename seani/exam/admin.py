from django.contrib import admin

from .models import Stage

# Register your models here.
@admin.register(Stage)
class StageAdmin(admin.ModelAdmin):
    list_display=['stage','month','year']
