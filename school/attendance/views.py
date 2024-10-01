from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, CreateView, UpdateView
from .models import Attendance
from .forms import AttendanceForm
from core.models import Student

class AttendanceListView(ListView):
    model = Attendance
    template_name = 'attendance/attendance_list.html'
    context_object_name = 'attendances'

    # def get_queryset(self):
    #     date = self.request.GET.get('date')
    #     if date:
    #         return Attendance.objects.filter(date=date)
    #     return Attendance.objects.none()

def mark_attendance(request):
    students = Student.objects.all()
    if request.method == 'POST':
        for student in students:
            status = request.POST.get(f'status_{student.id}')
            date = request.POST.get('date')
            if status and date:
                Attendance.objects.create(
                    student=student,
                    date=date,
                    status=status
                )
        return redirect('attendance-list')
    return render(request, 'attendance/mark_attendance.html', {'students': students})

class AttendanceUpdateView(UpdateView):
    model = Attendance
    form_class = AttendanceForm
    template_name = 'attendance/attendance_form.html'
    success_url = '/attendance/'