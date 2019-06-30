from django.db import models

from .validators import validate_powerpoint_file,\
    validate_archived_file


class Team(models.Model):
    app_title = models.CharField(max_length=50)
    app_file = models.FileField(upload_to='media/apps/%Y/%m',
                                validators=(validate_archived_file, ))
    powerpoint_file = models.FileField(upload_to='media/powerpoints/%Y/%m',
                                       validators=(validate_powerpoint_file, ))

    @property
    def members(self):
        return TeamMember.objects.filter(team=self)


class TeamMember(models.Model):
    name = models.CharField(max_length=30)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
