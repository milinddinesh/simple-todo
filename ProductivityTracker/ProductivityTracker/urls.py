
from django.contrib import admin
from django.urls import path , include
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = [
    path('admin/', admin.site.urls),
    path ('task/',include('Tasks.urls')),
    path('streak/',include('Streaks.urls')),
    path('api-auth/', include('rest_framework.urls')),
    path('',include('myapp.urls')), 
    path('quote/',include('quotes.urls'))
]
