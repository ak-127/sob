from django.contrib import admin
from .models import Attendance

@admin.register(Attendance) 
class AttendanceAdmin(admin.ModelAdmin):
    list_display = ['student', 'date', 'status']
    search_fields = ['student__name']
    list_filter = ['date', 'status']
    date_hierarchy = 'date'
    list_per_page = 10
    list_editable = ['status']
    list_display_links = ['student']
    list_select_related = ['student']
    list_max_show_all = 100
    list_display_links = None
    
