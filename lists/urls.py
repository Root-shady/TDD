from django.conf.urls import url
from .views import view_list

urlpatterns = [
        url(r'lists/the-only-list-in-the-world/$', view_list, name='view_list'),
        ]

