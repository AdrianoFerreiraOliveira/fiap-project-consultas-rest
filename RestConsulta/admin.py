from django.contrib import admin
from RestConsulta.models import Medico, Paciente

class Medicos(admin.ModelAdmin):
    list_display=('id','nome','rg','especialidade','data_nascimento','sexo','experiencia','crm_medico')
    list_display_links =('nome',)
    search_fields =('nome','especialidade')
    list_filter= ('especialidade','experiencia',)
    list_per_page =20
    ordering=('nome',)
   

admin.site.register(Medico, Medicos)

class Pacientes(admin.ModelAdmin):
    list_display=('id','nome','sintomas','rg','doenca_historico_familiar','medicacoes_em_uso','alergias','exames_recentes','pressao','temperatura','frequencia_cardiaca','saturacao','frequencia_respiratoria')
    list_display_links =('nome',)
    search_fields =('nome',)
    list_per_page =20
    ordering=('nome',)

admin.site.register(Paciente, Pacientes)
