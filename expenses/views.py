from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from .filters import ExpenseFilter
from .models import Expense
from .serializers import ExpenseSerializer
from django.db.models import Sum
from rest_framework.decorators import api_view
from rest_framework.response import Response
from decimal import Decimal # Import Decimal for handling potential None aggregate



class ExpenseViewSet(viewsets.ModelViewSet):
    queryset = Expense.objects.all().order_by('-date', '-created_at')
    serializer_class = ExpenseSerializer

class ExpenseViewSet(viewsets.ModelViewSet):
    
    queryset = Expense.objects.all().order_by('-date', '-created_at')
    serializer_class = ExpenseSerializer

  
    filter_backends = [DjangoFilterBackend] 
    filterset_class = ExpenseFilter     

@api_view(['GET']) 
def expense_summary(request):
    total_spent_result = Expense.objects.aggregate(total=Sum('amount'))
    total_spent = total_spent_result['total'] if total_spent_result['total'] is not None else Decimal('0.00')
    category_summary_query = Expense.objects.values('category').annotate(total=Sum('amount')).order_by('category')
    category_summary = {
        item['category']: item['total'] for item in category_summary_query
    }
    summary_data = {
        'total_spent': total_spent,
        'category_summary': category_summary
    }
    return Response(summary_data)
   

    

   