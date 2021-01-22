from countries.models import Countries
from rest_framework import viewsets
from countries.api.searializers import CountriesSerializer

# ViewSets define the view behavior.
class CountriesViewSet(viewsets.ModelViewSet):
    queryset = Countries.objects.all()
    serializer_class = CountriesSerializer