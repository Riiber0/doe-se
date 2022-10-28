from django.db import models
from django.contrib.auth.models import User

class ActivityLog(models.Model):
    type = models.CharField(max_length=64)
    logged_user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    fromuser = models.ForeignKey(User, null=True, blank=True, related_name="activitylogs_withfromuser", on_delete=models.CASCADE)
    jsondata = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField('criado em', auto_now_add=True)

    class Meta:
        ordering = ('-created_at',)

    def __str__(self):
        return '%s / %s / %s' % (
            self.type,
            self.logged_user,
            self.created_at,
        )

class Instituicoes(models.Model):
    nome = models.CharField(max_length=256)
    CNPJ = models.CharField(max_length=32)
    telefone = models.CharField(max_length=32)
    email = models.EmailField(max_length=256)
    endereco = models.CharField(max_length=512)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        db_table = 'Instituicoes'

class User(models.models):
    nome = models.CharField(max_length=25)
    cpf = models.IntegerField()
    UserID = models.IntegerField()
    DataNascimeto = models.DateField()