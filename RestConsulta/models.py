from django.db import models
from datetime import datetime

class Medico(models.Model):
    data_cadastro = models.DateField(default=datetime.now)
    nome = models.CharField(max_length=50,  null=False, blank=False)
    rg = models.CharField(max_length=9,  null=False, blank=False, unique=True)
    especialidade = models.CharField(max_length=30, null=False, blank=False)
    data_nascimento = models.DateField( null=False, blank=False)
    SEXO =(
        ('M', 'Masculino'),
        ('F', 'Feminino')
    )
    sexo = models.CharField(max_length=1,choices=SEXO, blank=False, null=False, default='M')
    experiencia = models.CharField(max_length=30,  null=False, blank=False)
    crm_medico = models.CharField(max_length=10, blank=False, null=False)
    foto = models.ImageField(blank=True)

    def __str__(self): 
        return self.nome

class Paciente(models.Model):
    data_consulta = models.DateField(default=datetime.now)
    nome = models.CharField(max_length=50,  null=False, blank=False)
    rg = models.CharField(max_length=9,  null=False, blank=False, unique=True)
    sintomas = models.CharField(max_length=30,  null=False, blank=False)
    doenca_historico_familiar = models.CharField(max_length=30,  null=False, blank=False)
    medicacoes_em_uso = models.CharField(max_length=30, null=False, blank=False)
    alergias = models.CharField(max_length=30,  null=False, blank=False)
    exames_recentes = models.CharField(max_length=20,  null=False, blank=False)
    pressao = models.CharField(max_length=10,  null=False, blank=False)
    temperatura = models.CharField(max_length=10,  null=False, blank=False)
    frequencia_cardiaca = models.CharField(max_length=10,  null=False, blank=False)
    saturacao = models.CharField(max_length=10,  null=False, blank=False)
    frequencia_respiratoria = models.CharField(max_length=10,  null=False, blank=False)

    def __str__(self): 
        return self.sintomas
     
