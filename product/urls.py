from django.urls import path
from . import views

urlpatterns = {
    path('index/', views.index_view, name='index'),
    path('cont/', views.cont_view, name='cont'),
    path('input/', views.input_view, name='input'),
    path('output/', views.output_view, name='output'),
}
