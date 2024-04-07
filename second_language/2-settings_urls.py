from django.contrib import admin
from django.urls import path, include
from django.conf.urls.i18n import i18n_patterns #* (5) : if we need to use more than one language we must add this here

urlpatterns = [
    path("il8n/", include("django.conf.urls.i18n")) #* (4) : if we need to use more than one language we must add this here
] 

urlpatterns += i18n_patterns ( #* (6) : if we need to use more than one language we must add this here
    path('admin/', admin.site.urls),
    path('', include("second_language.urls", namespace="second_language")),
)