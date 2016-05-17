from django.conf.urls import url
from .views import view_list, new_list

urlpatterns = [
        url(r'lists/the-only-list-in-the-world/$', view_list, name='view_list'),
        url(r'lists/new$', new_list, name='new_list'),
        ]

