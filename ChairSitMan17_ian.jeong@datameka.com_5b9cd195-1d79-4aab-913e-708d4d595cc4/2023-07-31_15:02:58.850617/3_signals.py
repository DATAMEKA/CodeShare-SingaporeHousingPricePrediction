from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import CompetitionCodeShareModel
from pathlib import PurePath
import os


@receiver(post_save, sender=CompetitionCodeShareModel)
def convert_ipynb_to_html(sender, instance, created, **kwargs):
    code_file = PurePath('/var/www/datameka_django/datameka/', *[dir for dir in instance.code_file.url.split('/')[3:]])
    os.system(f'jupyter nbconvert --to html {code_file}')
