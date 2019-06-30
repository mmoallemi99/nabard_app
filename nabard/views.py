from django.shortcuts import render
from django.forms import inlineformset_factory

from django.http.response import HttpResponse

from .models import Team,\
    TeamMember

from .forms import TeamRegistrationForm


def team_register(request):

    MembersFormSet = inlineformset_factory(Team,  TeamMember, fields='__all__', extra=5)

    if request.method == 'POST':
        team_form = TeamRegistrationForm(request.POST, request.FILES)
        members_formset = MembersFormSet(request.POST)

        if members_formset.is_valid():

            return HttpResponse('good to go')
    else:
        team_form = TeamRegistrationForm()
        members_formset = MembersFormSet()

    context = {
        'members_formset': members_formset,
        'team_form': team_form,

    }

    return render(request, 'team_register.html', context)
