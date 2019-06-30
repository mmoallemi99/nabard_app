from django import forms

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
        widgets = {
            'app_title': APP_TITLE_WIDGET,
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

