from django.contrib import admin
from django.urls import path,include

admin.site.site_header = "Hair Salon  Admin"
admin.site.site_title = "Hair Salon Admin Portal"
admin.site.index_title = "Welcome to Hair Salon Portal"



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls'))
]