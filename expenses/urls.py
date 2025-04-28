
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ExpenseViewSet,expense_summary


router = DefaultRouter()
router.register(r'expenses', ExpenseViewSet, basename='expense')
urlpatterns = [
    path('', include(router.urls)),
    path('summary/', expense_summary, name='expense-summary'),
]
