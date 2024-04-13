from django.db import models
from cloudinary.models import CloudinaryField

# Create your models here.
class Module(models.Model):
    name=models.CharField(
        max_length=100,
        verbose_name="Nombre"
    )
    description=models.CharField(
        max_length=200,
        verbose_name="Descripción"
    )
    def num_questions(self):
        return self.question_set.count()
    
    num_questions.short_description="Número de Preguntas"

    def __str__(self):
        return self.name
    class Meta:
        verbose_name="módulo"
        verbose_name_plural="módulos"

class Question(models.Model):
    module=models.ForeignKey(
        Module,
        on_delete=models.CASCADE,
        verbose_name="Módulo"
    )
    question_text=models.TextField(
        verbose_name="Texto de Pregunta",
        null=True,
        blank=True
    )
#    question_image=models.ImageField(
#    question_image=models.ImageField(
#        verbose_name="Imagen de Pregunta",
#        upload_to="questions",
#       null=True,
#        blank=True,
#    )
    question_image=CloudinaryField(
        verbose_name='Imagen de Pregunta',
        null=True, blank=True,
        resource_type='image',
        folder='questions',
    )
    answer1=models.CharField(
        max_length=200,
        verbose_name="Respuesta A",
    )
    answer2=models.CharField(
        max_length=200,
        verbose_name="Respuesta B"
    )
    answer3=models.CharField(
        max_length=200,
        verbose_name="Respuesta C",
        null=True,
        blank=True
    )
    answer4=models.CharField(
        max_length=200,
        verbose_name="Respuesta D",
        null=True,
        blank=True
    )
    correct=models.CharField(
        max_length=5,
        verbose_name="Respuesta Correcta"
    )
    def __str__(self):
        return f"{ self.module } - { self.id }"
    class Meta:
        verbose_name="pregunta"
        verbose_name_plural="preguntas"