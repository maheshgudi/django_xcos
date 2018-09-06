import os
import csv
from django.http import HttpResponse, JsonResponse
from django.contrib.auth import login, logout, authenticate
from django.shortcuts import render, get_object_or_404, redirect
from django.template import Context, Template
from django.http import Http404
from django.db.models import Max, Q, F
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from django.forms.models import inlineformset_factory
from django.utils import timezone
from django.core.exceptions import (
    MultipleObjectsReturned, ObjectDoesNotExist
)
import json
from textwrap import dedent
import zipfile
try:
    from StringIO import StringIO as string_io
except ImportError:
    from io import BytesIO as string_io
import re


def index(request, next_url=None):
    """The start page.
    """
    return render(request, "index.html")

