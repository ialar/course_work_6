from django import forms
from django.forms import DateTimeInput, CheckboxInput, BooleanField

from main.models import Mailing, Message, Client


class StyleFormMixin(forms.Form):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if isinstance(field, BooleanField):
                field.widget.attrs['class'] = 'form-check-input'
            else:
                field.widget.attrs['class'] = 'form-control'


class MailingForm(StyleFormMixin, forms.ModelForm):

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request')
        user = self.request.user
        super().__init__(*args, **kwargs)
        self.fields['message'].queryset = Message.objects.filter(owner=user)
        self.fields['client'].queryset = Client.objects.filter(owner=user)

    class Meta:
        model = Mailing
        exclude = ('next_date', 'user', 'is_active')
        # fields = '__all__'
        widgets = {'start_date': DateTimeInput(attrs={'placeholder': 'ДД.ММ.ГГГГ ЧЧ:ММ:СС', 'type': 'datetime-local'}),
                   'end_date': DateTimeInput(attrs={'placeholder': 'ДД.ММ.ГГГГ ЧЧ: ММ:СС', 'type': 'datetime-local'}),
                   'is_active': CheckboxInput(attrs={})}


class MailingModerForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Mailing
        fields = ('is_active',)


class MessageForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Message
        exclude = ('user',)


class ClientForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Client
        exclude = ('user',)
