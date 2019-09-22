from django.contrib import admin
from django.urls import path
from parse_edges import views as pe_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('parse_ctrl/', pe_views.parse_ctrl, name='parse_ctrl_pg'),
    path('parse_left/<int:img_index>/', pe_views.trim_left, name='parse_left_pg'),
    path('parse_right/<int:img_index>/', pe_views.trim_right, name='parse_right_pg'),
    path('parse_top/<int:img_index>/', pe_views.trim_top, name='parse_top_pg'),
    path('parse_bottom/<int:img_index>/', pe_views.trim_bottom, name='parse_bottom_pg'),
    path('parse_header/<int:img_index>/', pe_views.trim_header, name='parse_header_pg'),
    path('parse_footer/<int:img_index>/', pe_views.trim_footer, name='parse_footer_pg'),
]