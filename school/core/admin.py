from django.contrib import admin
from .models import Student

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('student_id', 'first_name', 'last_name', 'date_of_birth',)

    # first_name = models.CharField(max_length=100)
    # last_name = models.CharField(max_length=100)
    # date_of_birth = models.DateField()
    # gender = models.CharField(max_length=10, choices=[('male', 'Male'), ('female', 'Female'), ('other', 'Other')])
    # student_id = models.CharField(max_length=8, unique=True, default=generate_student_id)
    # enrollment_date = models.DateField(auto_now_add=True)
    # photo = models.ImageField(upload_to='student_photos/', blank=True, null=True)

    # # Address fields
    # address_line_1 = models.CharField(max_length=255)
    # address_line_2 = models.CharField(max_length=255, blank=True, null=True)
    # city = models.CharField(max_length=100)
    # state = models.CharField(max_length=100)
    # postal_code = models.CharField(max_length=20)
    # country = models.CharField(max_length=100)

    # # Father's details
    # father_name = models.CharField(max_length=100)
    # father_phone = models.CharField(max_length=15, blank=True, null=True)
    # father_email = models.EmailField(blank=True, null=True)

    # # Mother's details
    # mother_name = models.CharField(max_length=100)
    # mother_phone = models.CharField(max_length=15, blank=True, null=True)
    # mother_email = models.EmailField(blank=True, null=True)

    # # Guardian details (optional if neither parent is available)
    # guardian_name = models.CharField(max_length=100, blank=True, null=True)
    # guardian_phone = models.CharField(max_length=15, blank=True, null=True)
    # guardian_email = models.EmailField(blank=True, null=True)
    # relation_to_guardian = models.CharField(max_length=50, blank=True, null=True, help_text="Relation to the guardian, e.g. Uncle, Aunt")

    # def __str__(self):
    #     return f"{self.first_name} {self.last_name} - {self.student_id}"
