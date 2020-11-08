from core.views import ans_add_view
from django.urls import path
from .import views

urlpatterns = [
    path('', views.main_view, name='main_view'),
    path('question/add/', views.qn_add_view, name='qn_add_view'),
    path('answer/add/<int:qn_id>', views.ans_add_view, name='ans_add_view'),
    path('answer/vote/<int:ans_id>', views.ans_vote_view, name='ans_vote_view')
]