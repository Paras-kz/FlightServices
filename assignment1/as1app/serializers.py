from rest_framework import serializers
from .models import Passengers


class PsngrSr(serializers.ModelSerializer):
    class Meta:
        model=Passengers
        fields=['firstname','lastname','travelid']