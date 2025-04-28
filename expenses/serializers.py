# expenses/serializers.py
from rest_framework import serializers
from .models import Expense
from datetime import date 

class ExpenseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Expense
        fields = [
            'id',
            'title',
            'amount',
            'date',
            'category',
            'notes',
            'created_at',
            'updated_at'
        ]
        read_only_fields = ['created_at', 'updated_at']

    def validate_amount(self, value):    
        if value <= 0:
            raise serializers.ValidationError("Amount must be a positive number.")
        return value

    def validate_title(self, value):      
        if not value:
            raise serializers.ValidationError("Title cannot be empty.")
        return value
  
    def validate_date(self, value):       
        if value.year < 2000 or value.year > 2100:
            raise serializers.ValidationError("Date must be between the year 2000 and 2100.")
        return value
