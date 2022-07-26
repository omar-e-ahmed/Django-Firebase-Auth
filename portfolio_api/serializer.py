from rest_framework import serializers
from portfolio_api.models import Portfolio
from django.forms import ValidationError

class PortfolioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Portfolio
        fields = "__all__"
        read_only_fields = ('id',)

    # def validate_name(self, value):
    #     if value == "":
    #         raise serializers.ValidationError("Name cannot be empty")
    #     return value
    
    # def validate_description(self, value):
    #     if value == "":
    #         raise serializers.ValidationError("Description cannot be empty")
    #     return value
    