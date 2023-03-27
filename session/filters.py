import django_filters
from session.models import Session

class SessionFilter(django_filters.FilterSet):
    
    campo_de_filtro = django_filters.CharFilter(field_name='fk_mestre', lookup_expr='icontains')
    class Meta:
        model = Session
        fields = ["fk_mestre"]