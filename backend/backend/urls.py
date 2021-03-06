from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('movies/',include('movies.urls')),
    path('users/',include('user.urls')),
    path('watchlists/',include('watchlists.urls'))
]
handler500 = 'rest_framework.exceptions.server_error'
handler400 = 'rest_framework.exceptions.bad_request'
