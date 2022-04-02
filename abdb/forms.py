from django.forms import ModelForm
from django import forms

from .models import Antibody, AntibodyArc, AntibodyInd

class AntibodyForm(ModelForm):
    class Meta:
        model = Antibody
        fields = '__all__'
class AntibodyIndForm(ModelForm):
    class Meta:
        model = AntibodyInd
        fields = '__all__'
        exclude = ('cat_num',)
class AntibodyArcForm(ModelForm):
    class Meta:
        model = AntibodyArc
        fields = '__all__'
