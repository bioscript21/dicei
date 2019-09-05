from django.contrib import admin
from simple_history.admin import SimpleHistoryAdmin
from registros.models import *

admin.site.register(Incluido, SimpleHistoryAdmin)
