from django.urls import path, include



urlpatterns = [
    path('menu-items/', include('menu.urls', namespace='menu')),
]