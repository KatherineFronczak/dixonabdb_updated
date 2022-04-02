from django.contrib import admin

# Register your models here.

from .models import Antibody
admin.site.register(Antibody)

from .models import AntibodyArc
admin.site.register(AntibodyArc)

from .models import AntibodyInd
admin.site.register(AntibodyInd)
