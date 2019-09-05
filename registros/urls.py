from django.urls import path
from .views import IncView, IncDetailView, IncCreateView, IncUpdateView, IncDeleteView, IncLogsView
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
    path('goodcl/', views.goodcl, name='goodcl'),
    path('aboutus/', views.aboutus, name='aboutus'),
]
