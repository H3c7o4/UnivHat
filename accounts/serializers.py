from rest_framework import serializers
from accounts.models import CustomUser

class Userserializers(serializers.ModelSerializer):

    class Meta:
        model = CustomUser
        fields = (
            'id',
            'first_name',
            'last_name',
            'email',
            'password',
            'gender',
            'score',
            'field_spec',
            'studying_at',
            'phone_number',
            'profile_pic',
            'is_staff',
        )