from rest_framework import serializers
from user_profile.models.partner import Partner


class PartnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Partner
        fields = '__all__'