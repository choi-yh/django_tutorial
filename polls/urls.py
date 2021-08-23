from django.urls import path

from . import views

# Django 프로젝트 내에 앱이 여러 개 있을 때, Django가 각 앱들의 url을 구분하기 위해 namespace 지정
app_name = "polls"
urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("<int:pk>/", views.DetailView.as_view(), name="detail"),
    path("<int:pk>/results/", views.ResultsView.as_view(), name="results"),
    path("<int:question_id>/vote/", views.vote, name="vote"),
]
