from django.urls import path, include
from . import views

urlpatterns = [
        path('', views.main, name = 'main'),
        path('commission_form/', views.form, name = 'form'),
        path('about_me/', views.about, name = 'about'),
        path('dungeon_box/', views.dungeonbox, name = 'dungeonbox'),
        path('faq/', views.faq, name = 'faq'),
        path('crystal_jewlery/', views.crystals, name = 'crystals'),
        path('minis/', views.minis, name = 'minis'),
]