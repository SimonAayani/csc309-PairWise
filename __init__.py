from os import environ
from django import setup

environ.setdefault("DJANGO_SETTINGS_MODULE", "PairWise.PairWise.settings")
setup()

from PairWise.models import *
