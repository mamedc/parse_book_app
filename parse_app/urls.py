from django.contrib import admin
from django.urls import path
from parse_edges import views as pe_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('parse_left/<int:img_index>/', pe_views.trim_left, name='parse_left_pg'),
    path('parse_right/<int:img_index>/', pe_views.trim_right, name='parse_right_pg'),
]