from django.contrib import admin
from django.urls import path
from hospital import views
from django.views.static import serve
from django.conf.urls import url
from django.contrib.auth.views import LoginView,LogoutView


#-------------FOR ADMIN RELATED URLS
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home_view,name=''),


    path('aboutus', views.aboutus_view),
    path('contactus', views.contactus_view),
    path('centralstore',views.centralstore_view),


    path('adminclick', views.adminclick_view),
    path('doctorclick', views.doctorclick_view),
    path('patientclick', views.patientclick_view),
    path('receptionclick',views.receptionclick_view),
    path('labcustomerclick',views.labcustomerclick_view),
    path('pathologistclick',views.pathologistclick_view),

    path('adminsignup', views.admin_signup_view),
    path('doctorsignup', views.doctor_signup_view,name='doctorsignup'),
    path('patientsignup', views.patient_signup_view),
    path('receptionsignup',views.reception_signup_view,name='receptionsignup'),
    path('labcustomersignup',views.labcustomer_signup_view,name='labcustomersignup'),
    path('pathologistsignup',views.pathologist_signup_view,name='pathologistsignup'),
    
    path('adminlogin', LoginView.as_view(template_name='hospital/adminlogin.html')),
    path('doctorlogin', LoginView.as_view(template_name='hospital/doctorlogin.html')),
    path('patientlogin', LoginView.as_view(template_name='hospital/patientlogin.html')),
    path('receptionlogin',LoginView.as_view(template_name='hospital/receptionlogin.html')),
    path('labcustomerlogin',LoginView.as_view(template_name='hospital/labcustomerlogin.html')),
    path('pathologistlogin',LoginView.as_view(template_name='hospital/pathologistlogin.html')),

    path('afterlogin', views.afterlogin_view,name='afterlogin'),
    path('logout', LogoutView.as_view(template_name='hospital/index.html'),name='logout'),


    path('admin-dashboard', views.admin_dashboard_view,name='admin-dashboard'),

    path('admin-doctor', views.admin_doctor_view,name='admin-doctor'),
    path('admin-view-doctor', views.admin_view_doctor_view,name='admin-view-doctor'),
    path('delete-doctor-from-hospital/<int:pk>', views.delete_doctor_from_hospital_view,name='delete-doctor-from-hospital'),
    path('update-doctor/<int:pk>', views.update_doctor_view,name='update-doctor'),
    path('admin-add-doctor', views.admin_add_doctor_view,name='admin-add-doctor'),
    path('admin-approve-doctor', views.admin_approve_doctor_view,name='admin-approve-doctor'),
    path('approve-doctor/<int:pk>', views.approve_doctor_view,name='approve-doctor'),
    path('reject-doctor/<int:pk>', views.reject_doctor_view,name='reject-doctor'),
    path('admin-view-doctor-specialisation',views.admin_view_doctor_specialisation_view,name='admin-view-doctor-specialisation'),

    path('admin-reception', views.admin_reception_view,name='admin-reception'),
    path('admin-view-reception', views.admin_view_reception_view,name='admin-view-reception'),
    path('delete-reception-from-hospital/<int:pk>', views.delete_reception_from_hospital_view,name='delete-reception-from-hospital'),
    path('update-reception/<int:pk>', views.update_reception_view,name='update-reception'),
    path('admin-add-reception', views.admin_add_reception_view,name='admin-add-reception'),
    path('admin-approve-reception', views.admin_approve_reception_view,name='admin-approve-reception'),
    path('approve-reception/<int:pk>', views.approve_reception_view,name='approve-reception'),
    path('reject-reception/<int:pk>', views.reject_reception_view,name='reject-reception'),
    path('admin-view-reception-specialisation',views.admin_view_reception_specialisation_view,name='admin-view-reception-specialisation'),
    path('admin-pathologist', views.admin_pathologist_view,name='admin-pathologist'),
    path('admin-approve-pathologist', views.admin_approve_pathologist_view,name='admin-approve-pathologist'),
    path('approve-pathologist/<int:pk>', views.approve_pathologist_view,name='approve-pathologist'),
    path('reject-pathologist/<int:pk>', views.reject_pathologist_view,name='reject-pathologist'),


    path('admin-patient', views.admin_patient_view,name='admin-patient'),
    path('admin-view-patient', views.admin_view_patient_view,name='admin-view-patient'),
    path('delete-patient-from-hospital/<int:pk>', views.delete_patient_from_hospital_view,name='delete-patient-from-hospital'),
    path('update-patient/<int:pk>', views.update_patient_view,name='update-patient'),
    path('admin-add-patient', views.admin_add_patient_view,name='admin-add-patient'),
    path('admin-approve-patient', views.admin_approve_patient_view,name='admin-approve-patient'),
    path('approve-patient/<int:pk>', views.approve_patient_view,name='approve-patient'),
    path('reject-patient/<int:pk>', views.reject_patient_view,name='reject-patient'),
    path('reception-approve-labcustomer', views.reception_approve_labcustomer_view,name='reception-approve-labcustomer'),
    path('approve-labcustomer/<int:pk>', views.approve_labcustomer_view,name='approve-labcustomer'),
    path('reject-labcustomer/<int:pk>', views.reject_labcustomer_view,name='reject-labcustomer'),


    path('admin-appointment', views.admin_appointment_view,name='admin-appointment'),
    path('admin-view-appointment', views.admin_view_appointment_view,name='admin-view-appointment'),
]


#---------FOR DOCTOR RELATED URLS-------------------------------------
urlpatterns +=[
    path('doctor-dashboard', views.doctor_dashboard_view,name='doctor-dashboard'),

    path('doctor-patient', views.doctor_patient_view,name='doctor-patient'),
    path('doctor-view-patient', views.doctor_view_patient_view,name='doctor-view-patient'),
    path('doctor-view-discharge-patient',views.doctor_view_discharge_patient_view,name='doctor-view-discharge-patient'),

    path('doctor-appointment', views.doctor_appointment_view,name='doctor-appointment'),
    path('doctor-view-appointment', views.doctor_view_appointment_view,name='doctor-view-appointment'),
    path('doctor-delete-appointment',views.doctor_delete_appointment_view,name='doctor-delete-appointment'),
    path('delete-appointment/<int:pk>', views.delete_appointment_view,name='delete-appointment'),
]

#---------FOR RECEPTION RELATED URLS-----------------------------------
urlpatterns+=[
    path('reception-dashboard',views.reception_dashboard_view,name='reception-dashboard'),
    path('reception-patient', views.reception_patient_view,name='reception-patient'),
    path('pathologist-labcustomer', views.pathologist_labcustomer_view,name='pathologist-labcustomer'),
    path('reception-labcustomer',views.reception_labcustomer_view,name='reception-labcustomer'),
    path('reception-view-patient', views.reception_view_patient_view,name='reception-view-patient'),
    path('delete-patient-from-hospital/<int:pk>', views.delete_patient_from_hospital_view,name='delete-patient-from-hospital'),
    path('update-patient/<int:pk>', views.update_patient_view,name='update-patient'),
    path('reception-discharge-patient', views.reception_discharge_patient_view,name='reception-discharge-patient'),
    path('discharge-patient/<int:pk>', views.discharge_patient_view,name='discharge-patient'),
    path('download-pdf/<int:pk>', views.download_pdf_view,name='download-pdf'),
    path('pathologist-write-labcustomer',views.pathologist_write_labcustomer_view,name='pathologist-write-labcustomer'),
    path('write-labcustomer/<int:pk>',views.write_labcustomer_view,name='write-labcustomer'),
    path('download-result/<int:pk>',views.download_result_view,name='download-result'),

    path('reception-appointment', views.reception_appointment_view,name='reception-appointment'),
    path('reception-view-appointment', views.reception_view_appointment_view,name='reception-view-appointment'),
    path('reception-add-appointment', views.reception_add_appointment_view,name='reception-add-appointment'),
    path('reception-approve-appointment', views.reception_approve_appointment_view,name='reception-approve-appointment'),
    path('approve-appointment/<int:pk>', views.r_approve_appointment_view,name='approve-appointment'),
    path('reject-appointment/<int:pk>', views.r_reject_appointment_view,name='reject-appointment'),
]


#---------FOR PATIENT RELATED URLS-------------------------------------
urlpatterns +=[

    path('patient-dashboard', views.patient_dashboard_view,name='patient-dashboard'),
    path('patient-appointment', views.patient_appointment_view,name='patient-appointment'),
    path('patient-book-appointment', views.patient_book_appointment_view,name='patient-book-appointment'),
    path('patient-view-appointment', views.patient_view_appointment_view,name='patient-view-appointment'),
    path('patient-discharge', views.patient_discharge_view,name='patient-discharge'),
    path('labcustomer-write',views.labcustomer_write_view,name='labcustomer-write'),
]

urlpatterns+=[
    path('labcustomer-dashboard',views.labcustomer_dashboard_view,name='labcustomer-dashboard'),
    path('pathologist-dashboard',views.pathologist_dashboard_view,name='pathologist-dashboard'),
]

urlpatterns+=[
    path('whyus',views.whyus_view,name='whyus')
]

urlpatterns+=[
    path('gallery',views.gallery_view,name='gallery'),
    url(r'^media/(?P<path>.*)$', serve,{'document_root':       settings.MEDIA_ROOT}), 
    url(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT})
]

