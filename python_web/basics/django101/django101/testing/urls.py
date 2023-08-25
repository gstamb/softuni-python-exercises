from django.urls import path

from django101.testing.views.index import index
from django101.testing.views.query_params import query_params_view

urlpatterns = (
    path('', index, name='profiles'),
    path('query_params/', query_params_view, name='query params'),
)
