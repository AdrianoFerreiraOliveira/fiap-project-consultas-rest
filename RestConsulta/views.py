from rest_framework import viewsets, filters, status
from RestConsulta.models import Medico, Paciente
from RestConsulta.serializer import MedicoSerializer, PacienteSerializer
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page


class MedicosViewSet(viewsets.ModelViewSet):
    """Exibindo a lista de médicos"""

    queryset = Medico.objects.all()
    serializer_class = MedicoSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    filter_backends = [
        DjangoFilterBackend,
        filters.OrderingFilter,
        filters.SearchFilter,
    ]
    ordering_fileds = ["nome"]
    search_fields = ["nome", "crm_medico"]
    filterset_fields = ["especialidade"]

    @method_decorator(cache_page(10))
    def dispatch(self, *args, **kwargs):
        return super(MedicosViewSet, self).dispatch(*args, **kwargs)


class PacientesViewSet(viewsets.ModelViewSet):
    """Exibindo a lista de pacientes"""

    queryset = Paciente.objects.all()
    serializer_class = PacienteSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    ordering_fileds = ["nome"]

    def create(self, request):
        serializer = self.get_serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            response = Response(serializer.data, status=status.HTTP_201_CREATED)
            id = str(serializer.data["id"])
            response["Location"] = request.build_absolute_uri() + id
            return response
