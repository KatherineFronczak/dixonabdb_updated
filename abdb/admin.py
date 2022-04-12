#built in django admin page with models registered
from django.contrib import admin

from .models import Antibody
admin.site.register(Antibody)

from .models import AntibodyArc
admin.site.register(AntibodyArc)

from .models import AntibodyInd
admin.site.register(AntibodyInd)
