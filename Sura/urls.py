from django.urls import path
from django.urls import path
from .views import HomePageView,ResultViewPage,get_qazo
urlpatterns = [
    path('',HomePageView.as_view(), name='home'),
    path('search/',ResultViewPage.as_view(),name='result'),
    path('qazo',get_qazo,name='qazo'),
]