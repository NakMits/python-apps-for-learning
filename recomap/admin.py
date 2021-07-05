from django.contrib import admin

# Register your models here.
from recomap.models import MarkerModel
from recomap.api.models import Snippet

admin.site.register(MarkerModel)
admin.site.register(Snippet)

