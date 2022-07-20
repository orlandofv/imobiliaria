from django import forms
from .models import Settings
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column, Reset, HTML, Button
from crispy_forms.bootstrap import FieldWithButtons, StrictButton, AccordionGroup, Field
from django.utils.translation import ugettext_lazy as _
from crispy_bootstrap5.bootstrap5 import BS5Accordion

from users.models import User


class SettingsForm(forms.ModelForm):
    name = forms.CharField(label=_('Company Name'))
    address = forms.CharField(label=_('Address'), required=False, max_length=255)
    cell = forms.CharField(label=_('Cell'), required=False, max_length=255)
    cell_2 = forms.CharField(label=_('Cell 2'), required=False, max_length=255)
    telephone = forms.CharField(label=_('Telephone'), required=False, max_length=255)
    fax = forms.CharField(label=_('Fax'), required=False, max_length=255)
    email = forms.EmailField(label=_('Email'), required=True)
    web = forms.CharField(label=_('Web Site'), max_length=255, required=False)
    logo = forms.ImageField(label=_('Logo'), max_length=255, required=False)
    logo_square = forms.ImageField(label=_('Logo Square'), max_length=255, required=False)
    notes = forms.CharField(label=_('Notes'), required=False, widget=forms.Textarea())
   
    def __init__(self, *args, **kwargs):
        super(SettingsForm, self).__init__(*args, **kwargs)

        self.helper = FormHelper()
        self.helper.form_id = "settings-form-id"
        self.helper.form_class = "settings-form-class"
        self.helper.layout = Layout(
        HTML("""
            <p><strong style="font-size: 18px;">{}</strong></p>
            <hr>
        """.format(_('Add/Update Settings'),)),
        BS5Accordion(
        AccordionGroup(_('Settings'),
            'name',
            'address',
            Row(
                Column('cell', css_class='form-group col-md-6 mb-0'),
                Column('cell_2', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'),
            Row(
                Column('telephone', css_class='form-group col-md-6 mb-0'),
                Column('fax', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'),
            Row(
                Column('email', css_class='form-group col-md-6 mb-0'),
                Column('web', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'),
            Row(
                Column('logo', css_class='form-group col-md-6 mb-0'),
                Column('logo_square', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'),
            'notes',
            Submit('save_settings', _('Save & Close'), css_class='btn btn-primary fas fa-save'),
            Submit('save_settings_new', _('Save & Edit'), css_class='btn btn-primary fas fa-save'),
            Reset('reset', 'Clear', css_class='btn btn-danger'),
            flush=True,
            always_open=True
            ),))

    class Meta:
        model = Settings
        exclude = ('date_created', 'date_modified', 'slug', 'created_by', 'modified_by')
