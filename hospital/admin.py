from django.contrib import admin
from .models import Doctor,Reception,Patient,Appointment,PatientDischargeDetails,Labcustomer,Pathologist,LabcustomerReport
# Register your models here.
class DoctorAdmin(admin.ModelAdmin):
    pass
admin.site.register(Doctor, DoctorAdmin)

class ReceptionAdmin(admin.ModelAdmin):
    pass
admin.site.register(Reception, ReceptionAdmin)

class PathologistAdmin(admin.ModelAdmin):
    pass
admin.site.register(Pathologist,PathologistAdmin)

class PatientAdmin(admin.ModelAdmin):
    pass
admin.site.register(Patient, PatientAdmin)

class LabcustomerAdmin(admin.ModelAdmin):
    pass
admin.site.register(Labcustomer,LabcustomerAdmin)


class AppointmentAdmin(admin.ModelAdmin):
    pass
admin.site.register(Appointment, AppointmentAdmin)

class PatientDischargeDetailsAdmin(admin.ModelAdmin):
    pass
admin.site.register(PatientDischargeDetails, PatientDischargeDetailsAdmin)

class LabcustomerReportAdmin(admin.ModelAdmin):
    pass
admin.site.register(LabcustomerReport,LabcustomerReportAdmin)