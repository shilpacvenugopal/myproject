from django.urls import path
from .views import Table2Api,ObtainAuthToken

urlpatterns = [
    path('dashboard/', Table2Api.as_view(), name='table2_api'),
    path('dashboard/<uuid:id>/', Table2Api.as_view(), name='table2_detail'),
    path('api/token-auth/', ObtainAuthToken.as_view(), name='token_auth'),

]
