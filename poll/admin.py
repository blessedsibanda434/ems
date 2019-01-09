from django.contrib import admin

from poll.models import *

admin.site.register(Question)
admin.site.register(Choice)
