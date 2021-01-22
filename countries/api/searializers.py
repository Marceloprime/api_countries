from rest_framework import serializers
from countries.models import Countries

# Serializers define the API representation.
class CountriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Countries
        fields = ['id', 'name', 'capital'] 