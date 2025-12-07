from django.urls import path
from . import views

app_name = 'learning_logs'

urlpatterns = [
    path('', views.index, name='index'),
    path('topics/', views.topics, name='topics'),
        # Страница с подробной информацией по отдельной теме
    path('topics/<int:topic_id>/', views.topic, name='topic'),
    #страница с возможностью создания новой темы
    path('new_topic/', views.new_topic, name='new_topic'),
    #страница для добавления новой записи в тему
    path('new_entry/<int:topic_id>/', views.new_entry, name='new_entry'),
    #страница для редактирования записей в теме
    path('edit_entry/<int:entry_id>/', views.edit_entry, name='edit_entry'),
    

]
