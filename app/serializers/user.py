from re import I
from rest_framework import serializers
from app.models.user import User


class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','name','email', 'password','employee_number','is_admin']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance
