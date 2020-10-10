from django.urls import path

from tasks.views import TaskListView, TaskDetailView, TaskCreateView

urlpatterns = [
    path('', TaskListView.as_view()),
    path('create', TaskCreateView.as_view()),
    path('<int:task_id>/delete', TaskDetailView.as_view()),
    path('<int:task_id>/update', TaskDetailView.as_view()),
]