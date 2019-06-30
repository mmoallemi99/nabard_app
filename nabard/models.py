from django.db import models

from .validators import validate_powerpoint_file,\
    validate_archived_file


class Team(models.Model):
    app_title = models.CharField(max_length=50)
    app_file = models.FileField(upload_to='apps/%Y/%m',)
                                # validators=(validate_archived_file, ))
    powerpoint_file = models.FileField(upload_to='powerpoints/%Y/%m',)
                                       # validators=(validate_powerpoint_file, ))

    @property
    def members(self):
        return TeamMember.objects.filter(team=self)

    def __str__(self):
        return self.app_title


class TeamMember(models.Model):
    full_name = models.CharField(max_length=30)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)

    def __str__(self):
        return self.full_name
