from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.forms import ValidationError

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = "__all__"
        read_only_fields = ('id','uid')
        email = serializers.EmailField(required=True)
        password = serializers.CharField(min_length=8, required=True)

    # def validate_name(self, value):
    #     if value == "":
    #         raise serializers.ValidationError("Name cannot be empty")
    #     return value
    
    # def validate_description(self, value):
    #     if value == "":
    #         raise serializers.ValidationError("Description cannot be empty")
    #     return value
    