# serializers.py
'''from rest_framework import serializers
from .models import WorkingDays


class WorkingDaysSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkingDays
        fields = ['id', 'technician', 'customer', 'service',
                  'date_start', 'date_finish', 'status']
'''

# serializers.py
from rest_framework import serializers
from .models import WorkingDays


class WorkingDaysSerializer(serializers.ModelSerializer):
    technician_name = serializers.CharField(
        source='technician.name', read_only=True)  # Obtem o nome do técnico
    customer_corporate_reason = serializers.CharField(
        source='customer.corporate_reason', read_only=True)  # Obtem o nome do cliente
    service_service = serializers.CharField(
        source='service.service', read_only=True)  # Obtem o nome do serviço

    class Meta:
        model = WorkingDays
        fields = [
            'id',
            'technician_name',
            'customer_corporate_reason',
            'service_service',
            'date_start',
            'date_finish',
            'status'
        ]
