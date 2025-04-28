# expenses/filters.py
import django_filters
from .models import Expense

class ExpenseFilter(django_filters.FilterSet):
    year = django_filters.NumberFilter(field_name='date', lookup_expr='year')
    month = django_filters.NumberFilter(field_name='date', lookup_expr='month')
    category = django_filters.CharFilter(field_name='category', lookup_expr='iexact')
    class Meta:
        model = Expense
        fields = ['category', 'year', 'month']