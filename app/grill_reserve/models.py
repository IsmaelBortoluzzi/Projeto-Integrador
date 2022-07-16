from django.db import models

from client.models import Client


class GrillReserve(models.Model):
    start_hour = models.DateTimeField(db_column='start_hour')
    finish_hour = models.DateTimeField(db_column='finish_hour')
    observation = models.CharField(max_length=512, db_column='observation', null=True, default='')
    client_id = models.ForeignKey(Client, db_column='client_id', on_delete=models.DO_NOTHING)