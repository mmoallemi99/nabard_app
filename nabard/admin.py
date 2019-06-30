from django.contrib import admin

from .models import Team, TeamMember


class MemberInline(admin.TabularInline):
    model = TeamMember


@admin.decorators.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ('app_title', )
    inlines = [
        MemberInline
    ]


@admin.decorators.register(TeamMember)
class TeamMemberAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'team', )
    list_filter = ('full_name', 'team', )


