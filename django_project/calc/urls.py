from django.urls import path
from .views import HomePageView, CalcPageView
from calc import views

urlpatterns = [
    path("calc/", CalcPageView.as_view(), name="calc"),
    path("calc/answer/", views.answer, name="answer"),
    path("calc/extra/", views.extra, name="extra"),
    path("", HomePageView.as_view(), name="home"),
]

