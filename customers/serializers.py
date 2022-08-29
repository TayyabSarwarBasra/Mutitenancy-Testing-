from rest_framework import serializers

from customers.models import Client, Domain


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ('id', 'name', 'paid_until', 'on_trial')

class DomainSerializer(serializers.ModelSerializer):
    class Meta:
        model = Domain
        fields = ('id', 'domain', 'is_primary', 'tenant')

