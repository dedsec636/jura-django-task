from . import views
from django.urls import path

app_name='app'
urlpatterns=[
    path('<int:pk>/',views.ProdDetailView.as_view(),name='detail'),
    path('',views.Home.as_view(),name='home'),
    path('book/<int:pk>/',views.NewBooking,name='book'),

]