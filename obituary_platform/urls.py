from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

urlpatterns = [
    path('', RedirectView.as_view(url='/obituaries/view/', permanent=True)),  # Changed 'views' to 'view'
    path('admin/', admin.site.urls),
    path('obituaries/', include('obituaries.urls')),
]