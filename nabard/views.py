from django.shortcuts import render
from django.http.response import HttpResponse

from django import forms

from .forms import TeamRegistrationForm, MembersFormSet


def index(request):
    context = {}

    return render(request, 'index.html', context)


def team_register(request):

    if request.method == 'POST':
        team_form = TeamRegistrationForm(request.POST, request.FILES)
        members_formset = MembersFormSet(request.POST)

        if members_formset.is_valid() and team_form.is_valid():
            new_team = team_form.save()
            new_members = members_formset.save(commit=False)
            if not new_members:
                raise forms.ValidationError("باید حداقل نام یک عضو را وارد کنید")
            for member in new_members:
                member.team = new_team
                member.save()
            return HttpResponse('good to go')
    else:
        team_form = TeamRegistrationForm()
        members_formset = MembersFormSet()

    members_formset[0].use_required_attribute = True

    context = {
        'members_formset': members_formset,
        'team_form': team_form,

    }

    return render(request, 'team_register.html', context)
