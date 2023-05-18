from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.index),
    path('add_emp', views.add_emp),
    path('all_emp', views.all_emp),
    path('filter_emp', views.filter_emp),
    path('rem_emp', views.rem_emp),
    path('rem_emp/<int:emp_id>', views.rem_emp)
]
