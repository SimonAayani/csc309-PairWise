from os import environ
from django import setup

environ.setdefault("DJANGO_SETTINGS_MODULE", "PairWise_Server.settings")
setup()

from PairWise_Server.models import *
