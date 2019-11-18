from django.urls import path
from .views import (IncView, IncDetailView, IncCreateView, IncUpdateView, IncDeleteView, IncLogsView, IncHistoricoView,
                    RDPIView, RDPIDetailView, RDPICreateView, RDPIUpdateView, RDPIDeleteView, RDPILogsView,
                    RDPIHistoricoView)
from . import views

urlpatterns = [
    path('', views.portada, name='portada'),
    path('inicio/', views.inicio, name='inicio'),
    path('instructivos/', views.instructivos, name='instructivos'),
    path('incluido/mostrar/', IncView.as_view(), name='inc_shows'),
    path('incluido_detail/<int:pk>/', IncDetailView.as_view(), name='inc_detail'),
    path('incluido/nuevo/', IncCreateView.as_view(), name='inc_add'),
    path('incluido_edit/<int:pk>/actualizar/', IncUpdateView.as_view(), name='inc_edit'),
    path('incluido_eliminar/<int:pk>/eliminar/', IncDeleteView.as_view(), name='inc_del'),
    path('incluido_historial/<int:pk>/Logs/', IncLogsView.as_view(), name='inc_logs'),
    path('incluido_audit/Auditoria/', IncHistoricoView.as_view(), name='inc_audit'),
    path('rdpi/mostrar/', RDPIView.as_view(), name='rdpi_shows'),
    path('rdpi_detail/<int:pk>/', RDPIDetailView.as_view(), name='rdpi_detail'),
    path('rdpi/nuevo/', RDPICreateView.as_view(), name='rdpi_add'),
    path('rdpi_edit/<int:pk>/actualizar/', RDPIUpdateView.as_view(), name='rdpi_edit'),
    path('rdpi_eliminar/<int:pk>/eliminar/', RDPIDeleteView.as_view(), name='rdpi_del'),
    path('rdpi_historial/<int:pk>/Logs/', RDPILogsView.as_view(), name='rdpi_logs'),
    path('rdpi_audit/Auditoria/', RDPIHistoricoView.as_view(), name='rdpi_audit'),
    path('goodcl/', views.goodcl, name='goodcl'),
    path('aboutus/', views.aboutus, name='aboutus'),
]
