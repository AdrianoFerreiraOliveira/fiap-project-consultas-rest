from rest_framework import serializers
from RestConsulta.models import Medico, Paciente
from RestConsulta.validators import *

class MedicoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medico
        fields= '__all__'
        
    def validate(self,data):
        if not rg_medico_valido(data['rg']):
            raise serializers.ValidationError({'rg':"O RG Deve ter 9 digitos"})
        return data               
    

class PacienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Paciente
        fields= '__all__'
    def validate(self,data):
        if not rg_paciente_valido(data['rg']):
            raise serializers.ValidationError({'rg':"O RG Deve ter 9 digitos"})
        return data    
    