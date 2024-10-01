from django.urls import path
from .views import AttendanceListView, mark_attendance, AttendanceUpdateView

urlpatterns = [
    path('', AttendanceListView.as_view(), name='attendance-list'),
    path('mark/', mark_attendance, name='mark-attendance'),
    path('update/<int:pk>/', AttendanceUpdateView.as_view(), name='attendance-update'),
]