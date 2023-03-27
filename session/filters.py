import django_filters
from session.models import Session
from django.contrib.auth.models import User
class SessionFilter(django_filters.FilterSet):
    
    campo_de_filtro = django_filters.CharFilter(field_name='fk_mestre', lookup_expr='icontains')
    class Meta:
        model = Session
        fields = ["fk_mestre"]

class UserFilter(django_filters.FilterSet):
    username = django_filters.CharFilter(field_name='username', lookup_expr='icontains')
    
    class Meta:
        model = User
        fields = ['username']
