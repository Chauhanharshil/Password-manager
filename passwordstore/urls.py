from django.urls import path
from . import views
urlpatterns = [
    path('', views.home,name='index'),
    path('ajax_newcreate/',views.ajax_newcreate,name='ajax_newcreate'),
    path('ajax_delete_newcustomer/',views.ajax_delete_newcustomer,name='ajax_delete_newcustomer'),
    path('ajax_edit_customer',views.ajax_edit_customer,name='ajax_edit_customer'),
    path('editpassword/<int:pk>',views.editpassword,name='editpassword'),
    path('add_pass/',views.add_pass,name='add_pass')
]