from django import forms
from portfolio.models import Project

class portfolio_records_form(forms.Modelform):
    class Meta():
        model = Project
        fields = '__all__'
