from django import forms

from phonenumber_field import widgets

from .models import Team, TeamMember


class TeamRegistrationForm(forms.ModelForm):
    class Meta:
        model = Team
        fields = '__all__'

        APP_TITLE_WIDGET = forms.TextInput(
            attrs={
                'placeholder': 'لطفا عنوان طرح خود را وارد کنید',
                'dir': 'rtl',
            })

        EMAIL_FIELD_WIDGET = forms.EmailInput(
            attrs={
                'placeholder': 'team_email@service.com',
                'dir': 'ltr'
            })

        PHONE_NUMBER_FIELD_WIDGET = widgets.TextInput(
            attrs={
                'placeholder': '0913*******',
                'dir': 'ltr'
            })

        widgets = {
            'app_title': APP_TITLE_WIDGET,
            'email': EMAIL_FIELD_WIDGET,
            'phone_number': PHONE_NUMBER_FIELD_WIDGET,
        }


MEMBER_FIELD_WIDGET = forms.TextInput(
    attrs={
        'placeholder': 'لطفا نام خود را وارد کنید',
        'dir': 'rtl',
    })

MEMBERS_FORMSET = {
    'full_name': MEMBER_FIELD_WIDGET,
}

MembersFormSet = forms.inlineformset_factory(Team, TeamMember, fields=('full_name',),
                                             extra=5, can_delete=False,
                                             widgets=MEMBERS_FORMSET)
