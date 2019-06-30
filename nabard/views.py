from django.shortcuts import render
from django.forms import inlineformset_factory

from django.http.response import HttpResponse

from .models import Team,\
    TeamMember

from .forms import TeamRegistrationForm


def index(request):
    context = {}

    return render(request, 'index.html', context)


def team_register(request):

    MembersFormSet = inlineformset_factory(Team,  TeamMember, fields='__all__', extra=5)

    if request.method == 'POST':
        team_form = TeamRegistrationForm(request.POST, request.FILES)
        members_formset = MembersFormSet(request.POST)

        if members_formset.is_valid() and team_form.is_valid():
            new_team = team_form.save()
            new_members = members_formset.save(commit=False)
            for member in new_members:
                member.team = new_team
                member.save()
            return HttpResponse('good to go')
    else:
        team_form = TeamRegistrationForm()
        members_formset = MembersFormSet()

    context = {
        'members_formset': members_formset,
        'team_form': team_form,

    }

    return render(request, 'team_register.html', context)
