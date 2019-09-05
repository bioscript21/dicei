from django.contrib import admin
from simple_history.admin import SimpleHistoryAdmin
from .models import Perfil


admin.site.register(Perfil, SimpleHistoryAdmin)