from django.urls import path
from . import views


urlpatterns = [
    path("", views.home, name='home'),
    path("home", views.home, name='home'),
    path("chart", views.chart, name='chart'),
    path("category-book", views.avg_book, name='category-chart'),
    path("custom-data-generation", views.custom_data_generation, name='custom-data-generation'),
    path("history_data/<str:pk>/", views.history_data, name='history-data'),
    path("sign-up", views.sign_up, name='sign-up'),
]
