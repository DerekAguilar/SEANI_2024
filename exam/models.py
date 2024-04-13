from django.db import models
from django.contrib.auth.models import User

from career.models import Career
from library.models import Module, Question

# Create your models here.
class Stage(models.Model):
    stage=models.IntegerField(
        verbose_name='Etapa'
    )
    application_date=models.DateField(
        verbose_name='Fecha de aplicación'
    )

    @property
    def year(self):
        return self.application_date.year
    
    @property
    def month(self):
        months=['enero','febrero','marzo','abril',
                'mayo','junio','julio','agosto',
                'septiembre','octubre','noviembre','diciembre'
                ]
        return months[self.application_date.month -1]

    def __str__(self):
        return f"{self.stage} - {self.month} {self.year}"
    
    class Meta:
        verbose_name='etapa'
        verbose_name_plural='etapas'

class Exam(models.Model):
    user=models.OneToOneField(
        User,on_delete=models.CASCADE,
        verbose_name='Estudiante'
    )
    Career=models.ForeignKey(
        Career,on_delete=models.CASCADE,
        verbose_name='Carrera'
    )
    stage=models.ForeignKey(
        Stage,on_delete=models.CASCADE,
        verbose_name='Etapa'
    )
    modules=models.ManyToManyField(
        Module,
        through='ExamModule'
    )
    questions=models.ManyToManyField(
        Question,
        through='Breakdown'
    )
    score=models.FloatField(
        default=0.0,
        verbose_name='Calificación'
    )
    created=models.DateTimeField(
        auto_now_add=True,
        verbose_name='Fecha de creación'
    )
    updated=models.DateTimeField(
        auto_now=True,
        verbose_name='Fecha de actualización'
    )

    def set_modules(self):
        for module in Module.objects.all():
            self.modules.add(module)

    def set_questions(self):
        for module in self.modules.all():
            for question in module.question_set.all():
                #self.questions.add(question)
                Breakdown.objects.create(
                    exam=self,
                    question=question,
                    correct=question.correct
                )

    def compute_score_by_module(self,m_id):
        score=0.0
        questions=self.breakdown_set.filter(question__module_id=m_id)
        for question in questions:
            if question.correct==question.answer:
                score+=10
        total=score/questions.count()
        module=self.exammodule_set.get(module_id=m_id)
        module.score=total
        module.save()

    def compute_score(self):
        score=0.0
        modules=self.exammodule_set.all()
        for module in modules:
            score+=module.score
        self.score=score/modules.count()
        self.save()

    def __str__(self):
        return f"{self.user.username} - {self.score}"
    
    class Meta:
        verbose_name='examen'
        verbose_name_plural='exámenes'
    
class ExamModule(models.Model):
    exam=models.ForeignKey(
        Exam,
        on_delete=models.CASCADE
    )
    module=models.ForeignKey(
        Module,
        on_delete=models.CASCADE
    )
    active=models.BooleanField(
        default=True
    )
    score=models.FloatField(
        default=0.0
    )

class Breakdown(models.Model):
    exam=models.ForeignKey(
        Exam,
        on_delete=models.CASCADE
    )
    question=models.ForeignKey(
        Question,
        on_delete=models.CASCADE
    )
    answer=models.CharField(
        max_length=5,
        default='-'
    )
    correct=models.CharField(
        max_length=5,
        default='-'
    )