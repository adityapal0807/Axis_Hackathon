from django import forms
from django.forms import formset_factory
from django.forms import ClearableFileInput
from .models import *
from django.core.validators import FileExtensionValidator

class jd_submission_form(forms.Form):
    dropdown_field = forms.ModelChoiceField(
        queryset=Job_Description.objects.all().order_by('-created_at'),
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    # File upload field to upload up to 10 PDF files
    pdf_files = forms.FileField(
        widget=forms.ClearableFileInput(attrs={'multiple': True, 'class': 'form-control'}),
        validators=[FileExtensionValidator(allowed_extensions=['pdf', 'docx'])]

    )
