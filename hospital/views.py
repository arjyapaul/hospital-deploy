from django.shortcuts import render,redirect,reverse
from . import forms,models
from django.db.models import Sum
from django.contrib.auth.models import Group
from django.http import HttpResponseRedirect
from django.core.mail import send_mail
from django.contrib.auth.decorators import login_required,user_passes_test
from datetime import datetime,timedelta,date
from django.conf import settings

# Create your views here.
def home_view(request):
    #if request.user.is_authenticated:
        #return HttpResponseRedirect('afterlogin')
    return render(request,'hospital/index.html')


#for showing signup/login button for admin
def adminclick_view(request):
    #if request.user.is_authenticated:
        #return HttpResponseRedirect('afterlogin')
    return render(request,'hospital/adminclick.html')


#for showing signup/login button for doctor
def doctorclick_view(request):
    #if request.user.is_authenticated:
        #return HttpResponseRedirect('afterlogin')
    return render(request,'hospital/doctorclick.html')

#for showing signup/login button for reception
def receptionclick_view(request):
    #if request.user.is_authenticated:
        #return HttpResponseRedirect('afterlogin')
    return render(request, 'hospital/receptionclick.html')

#for showing signup/login button for patient
def patientclick_view(request):
    #if request.user.is_authenticated:
        #return HttpResponseRedirect('afterlogin')
    return render(request,'hospital/patientclick.html')
def labcustomerclick_view(request):
    return render(request,'hospital/labcustomerclick.html')

def pathologistclick_view(request):
    return render(request,'hospital/pathologistclick.html')




def admin_signup_view(request):
    form=forms.AdminSigupForm()
    if request.method=='POST':
        form=forms.AdminSigupForm(request.POST)
        if form.is_valid():
            user=form.save()
            user.set_password(user.password)
            user.save()
            my_admin_group = Group.objects.get_or_create(name='ADMIN')
            my_admin_group[0].user_set.add(user)
            return HttpResponseRedirect('adminlogin')
    return render(request,'hospital/adminsignup.html',{'form':form})


def doctor_signup_view(request):
    userForm=forms.DoctorUserForm()
    doctorForm=forms.DoctorForm()
    mydict={'userForm':userForm,'doctorForm':doctorForm}
    if request.method=='POST':
        userForm=forms.DoctorUserForm(request.POST)
        doctorForm=forms.DoctorForm(request.POST,request.FILES)
        if userForm.is_valid() and doctorForm.is_valid():
            user=userForm.save()
            user.set_password(user.password)
            user.save()
            doctor=doctorForm.save(commit=False)
            doctor.user=user
            doctor=doctor.save()
            my_doctor_group = Group.objects.get_or_create(name='DOCTOR')
            my_doctor_group[0].user_set.add(user)
        return HttpResponseRedirect('doctorlogin')
    return render(request,'hospital/doctorsignup.html',context=mydict)

def reception_signup_view(request):
    userForm=forms.ReceptionUserForm()
    receptionForm=forms.ReceptionForm()
    mydict={'userForm':userForm,'receptionForm':receptionForm}
    if request.method=='POST':
        userForm=forms.ReceptionUserForm(request.POST)
        receptionForm=forms.ReceptionForm(request.POST,request.FILES)
        if userForm.is_valid() and receptionForm.is_valid():
            user=userForm.save()
            user.set_password(user.password)
            user.save()
            reception=receptionForm.save(commit=False)
            reception.user=user
            reception=reception.save()
            my_reception_group = Group.objects.get_or_create(name='RECEPTION')
            my_reception_group[0].user_set.add(user)
        return HttpResponseRedirect('receptionlogin')
    return render(request,'hospital/receptionsignup.html',context=mydict)

def pathologist_signup_view(request):
    userForm=forms.PathologistUserForm()
    pathologistForm=forms.PathologistForm()
    mydict={'userForm':userForm,'pathologistForm':pathologistForm}
    if request.method=='POST':
        userForm=forms.PathologistUserForm(request.POST)
        pathologistForm=forms.PathologistForm(request.POST,request.FILES)
        if userForm.is_valid() and pathologistForm.is_valid():
            user=userForm.save()
            user.set_password(user.password)
            user.save()
            pathologist=pathologistForm.save(commit=False)
            pathologist.user=user
            pathologist=pathologist.save()
            my_pathologist_group = Group.objects.get_or_create(name='PATHOLOGIST')
            my_pathologist_group[0].user_set.add(user)
        return HttpResponseRedirect('pathologistlogin')
    return render(request,'hospital/pathologistsignup.html',context=mydict)


def patient_signup_view(request):
    userForm=forms.PatientUserForm()
    patientForm=forms.PatientForm()
    mydict={'userForm':userForm,'patientForm':patientForm}
    if request.method=='POST':
        userForm=forms.PatientUserForm(request.POST)
        patientForm=forms.PatientForm(request.POST,request.FILES)
        if userForm.is_valid() and patientForm.is_valid():
            user=userForm.save()
            user.set_password(user.password)
            user.save()
            patient=patientForm.save(commit=False)
            patient.user=user
            patient.assignedDoctorId=request.POST.get('assignedDoctorId')
            patient=patient.save()
            my_patient_group = Group.objects.get_or_create(name='PATIENT')
            my_patient_group[0].user_set.add(user)
        return HttpResponseRedirect('patientlogin')
    return render(request,'hospital/patientsignup.html',context=mydict)

def labcustomer_signup_view(request):
    userForm=forms.LabcustomerUserForm()
    labcustomerForm=forms.LabcustomerForm()
    mydict={'userForm':userForm,'labcustomerForm':labcustomerForm}
    if request.method=='POST':
        userForm=forms.LabcustomerUserForm(request.POST)
        labcustomerForm=forms.LabcustomerForm(request.POST,request.FILES)
        if userForm.is_valid() and labcustomerForm.is_valid():
            user=userForm.save()
            user.set_password(user.password)
            user.save()
            labcustomer=labcustomerForm.save(commit=False)
            labcustomer.user=user
            labcustomer=labcustomer.save()
            my_labcustomer_group = Group.objects.get_or_create(name='LABCUSTOMER')
            my_labcustomer_group[0].user_set.add(user)
        return HttpResponseRedirect('labcustomerlogin')
    return render(request,'hospital/labcustomersignup.html',context=mydict)





#-----------for checking user is doctor , patient or admin
def is_admin(user):
    return user.groups.filter(name='ADMIN').exists()
def is_doctor(user):
    return user.groups.filter(name='DOCTOR').exists()
def is_patient(user):
    return user.groups.filter(name='PATIENT').exists()
def is_reception(user):
    return user.groups.filter(name='RECEPTION').exists()
def is_labcustomer(user):
    return user.groups.filter(name='LABCUSTOMER').exists()
def is_pathologist(user):
    return user.groups.filter(name='PATHOLOGIST').exists()


#---------AFTER ENTERING CREDENTIALS WE CHECK WHETHER USERNAME AND PASSWORD IS OF ADMIN,DOCTOR OR PATIENT
def afterlogin_view(request):
    if is_admin(request.user):
        return redirect('admin-dashboard')
    elif is_doctor(request.user):
        accountapproval=models.Doctor.objects.all().filter(user_id=request.user.id,status=True)
        if accountapproval:
            return redirect('doctor-dashboard')
        else:
            return render(request,'hospital/doctor_wait_for_approval.html')
    elif is_patient(request.user):
        accountapproval=models.Patient.objects.all().filter(user_id=request.user.id,status=True)
        if accountapproval:
            return redirect('patient-dashboard')
        else:
            return render(request,'hospital/patient_wait_for_approval.html')
    elif is_reception(request.user):
        accountapproval=models.Reception.objects.all().filter(user_id=request.user.id,status=True)
        if accountapproval:
            return redirect('reception-dashboard')
        else:
            return render(request,'hospital/reception_wait_for_approval.html')
    elif is_labcustomer(request.user):
        accountapproval=models.Labcustomer.objects.all().filter(user_id=request.user.id,status=True)
        if accountapproval:
            return redirect('labcustomer-dashboard')
        else:
            return render(request,'hospital/labcustomer_wait_for_approval.html')
    elif is_pathologist(request.user):
        accountapproval=models.Pathologist.objects.all().filter(user_id=request.user.id,status=True)
        if accountapproval:
            return redirect('pathologist-dashboard')
        else:
            return render(request,'hospital/pathologist_wait_for_approval.html')







#---------------------------------------------------------------------------------
#------------------------ ADMIN RELATED VIEWS START ------------------------------
#---------------------------------------------------------------------------------
@login_required(login_url='adminlogin')
@user_passes_test(is_admin)
def admin_dashboard_view(request):
    #for both table in admin dashboard
    doctors=models.Doctor.objects.all().order_by('-id')
    receptions=models.Reception.objects.all().order_by('-id')
    patients=models.Patient.objects.all().order_by('-id')
    pathologists=models.Pathologist.objects.all().order_by('-id')
    #for three cards
    doctorcount=models.Doctor.objects.all().filter(status=True).count()
    pendingdoctorcount=models.Doctor.objects.all().filter(status=False).count()

    receptioncount=models.Reception.objects.all().filter(status=True).count()
    pendingreceptioncount=models.Reception.objects.all().filter(status=False).count()

    patientcount=models.Patient.objects.all().filter(status=True).count()
    pendingpatientcount=models.Patient.objects.all().filter(status=False).count()

    appointmentcount=models.Appointment.objects.all().filter(status=True).count()
    pendingappointmentcount=models.Appointment.objects.all().filter(status=False).count()

    pathologistcount=models.Pathologist.objects.all().filter(status=True).count()
    pendingpathologistcount=models.Pathologist.objects.all().filter(status=False).count()
    mydict={
    'doctors':doctors,
    'receptions':receptions,
    'patients':patients,
    'pathologists':pathologists,
    'doctorcount':doctorcount,
    'pendingdoctorcount':pendingdoctorcount,
    'receptioncount':receptioncount,
    'pathologistcount':pathologistcount,
    'pendingpathologistcount':pendingpathologistcount,
    'pendingreceptioncount':pendingreceptioncount,
    'patientcount':patientcount,
    'pendingpatientcount':pendingpatientcount,
    'appointmentcount':appointmentcount,
    'pendingappointmentcount':pendingappointmentcount,
    }
    return render(request,'hospital/admin_dashboard.html',context=mydict)


@login_required(login_url='receptionlogin')
@user_passes_test(is_reception)
def reception_dashboard_view(request):
    #for both table in admin dashboard
    patients=models.Patient.objects.all().order_by('-id')
    labcustomers=models.Labcustomer.objects.all().order_by('-id')
    #for two cards

    patientcount=models.Patient.objects.all().filter(status=True).count()
    pendingpatientcount=models.Patient.objects.all().filter(status=False).count()

    appointmentcount=models.Appointment.objects.all().filter(status=True).count()
    pendingappointmentcount=models.Appointment.objects.all().filter(status=False).count()

    labcustomercount=models.Labcustomer.objects.all().filter(status=True).count()
    pendinglabcustomercount=models.Labcustomer.objects.all().filter(status=False).count()
    mydict={
    'patients':patients,
    'labcustomers':labcustomers,
    'patientcount':patientcount,
    'pendingpatientcount':pendingpatientcount,
    'appointmentcount':appointmentcount,
    'pendingappointmentcount':pendingappointmentcount,
    'labcustomercount':labcustomercount,
    'pendinglabcustomercount':pendinglabcustomercount,
    }
    return render(request,'hospital/reception_dashboard.html',context=mydict)

@login_required(login_url='pathologistlogin')
@user_passes_test(is_pathologist)
def pathologist_dashboard_view(request):
    pathologist=models.Pathologist.objects.get(user_id=request.user.id)
    mydict={
    'pathologist':pathologist,
    'role':pathologist.role,
    'address':pathologist.address,
    }
    return render(request,'hospital/pathologist_dashboard.html',context=mydict)


# this view for sidebar click on admin page
@login_required(login_url='adminlogin')
@user_passes_test(is_admin)
def admin_doctor_view(request):
    return render(request,'hospital/admin_doctor.html')



@login_required(login_url='adminlogin')
@user_passes_test(is_admin)
def admin_view_doctor_view(request):
    doctors=models.Doctor.objects.all().filter(status=True)
    return render(request,'hospital/admin_view_doctor.html',{'doctors':doctors})



@login_required(login_url='adminlogin')
@user_passes_test(is_admin)
def delete_doctor_from_hospital_view(request,pk):
    doctor=models.Doctor.objects.get(id=pk)
    user=models.User.objects.get(id=doctor.user_id)
    user.delete()
    doctor.delete()
    return redirect('admin-view-doctor')



@login_required(login_url='adminlogin')
@user_passes_test(is_admin)
def update_doctor_view(request,pk):
    doctor=models.Doctor.objects.get(id=pk)
    user=models.User.objects.get(id=doctor.user_id)

    userForm=forms.DoctorUserForm(instance=user)
    doctorForm=forms.DoctorForm(request.FILES,instance=doctor)
    mydict={'userForm':userForm,'doctorForm':doctorForm}
    if request.method=='POST':
        userForm=forms.DoctorUserForm(request.POST,instance=user)
        doctorForm=forms.DoctorForm(request.POST,request.FILES,instance=doctor)
        if userForm.is_valid() and doctorForm.is_valid():
            user=userForm.save()
            user.set_password(user.password)
            user.save()
            doctor=doctorForm.save(commit=False)
            doctor.status=True
            doctor.save()
            return redirect('admin-view-doctor')
    return render(request,'hospital/admin_update_doctor.html',context=mydict)




@login_required(login_url='adminlogin')
@user_passes_test(is_admin)
def admin_add_doctor_view(request):
    userForm=forms.DoctorUserForm()
    doctorForm=forms.DoctorForm()
    mydict={'userForm':userForm,'doctorForm':doctorForm}
    if request.method=='POST':
        userForm=forms.DoctorUserForm(request.POST)
        doctorForm=forms.DoctorForm(request.POST, request.FILES)
        if userForm.is_valid() and doctorForm.is_valid():
            user=userForm.save()
            user.set_password(user.password)
            user.save()

            doctor=doctorForm.save(commit=False)
            doctor.user=user
            doctor.status=True
            doctor.save()

            my_doctor_group = Group.objects.get_or_create(name='DOCTOR')
            my_doctor_group[0].user_set.add(user)

        return HttpResponseRedirect('admin-view-doctor')
    return render(request,'hospital/admin_add_doctor.html',context=mydict)




@login_required(login_url='adminlogin')
@user_passes_test(is_admin)
def admin_approve_doctor_view(request):
    #those whose approval are needed
    doctors=models.Doctor.objects.all().filter(status=False)
    return render(request,'hospital/admin_approve_doctor.html',{'doctors':doctors})




@login_required(login_url='adminlogin')
@user_passes_test(is_admin)
def approve_doctor_view(request,pk):
    doctor=models.Doctor.objects.get(id=pk)
    doctor.status=True
    doctor.save()
    return redirect(reverse('admin-approve-doctor'))




@login_required(login_url='adminlogin')
@user_passes_test(is_admin)
def reject_doctor_view(request,pk):
    doctor=models.Doctor.objects.get(id=pk)
    user=models.User.objects.get(id=doctor.user_id)
    user.delete()
    doctor.delete()
    return redirect('admin-approve-doctor')





@login_required(login_url='adminlogin')
@user_passes_test(is_admin)
def admin_view_doctor_specialisation_view(request):
    doctors=models.Doctor.objects.all().filter(status=True)
    return render(request,'hospital/admin_view_doctor_specialisation.html',{'doctors':doctors})

@login_required(login_url='adminlogin')
@user_passes_test(is_admin)
def admin_reception_view(request):
    return render(request,'hospital/admin_reception.html')

@login_required(login_url='adminlogin')
@user_passes_test(is_admin)
def admin_pathologist_view(request):
    return render(request,'hospital/admin_pathologist.html')

@login_required(login_url='adminlogin')
@user_passes_test(is_admin)
def admin_view_reception_view(request):
    receptions=models.Reception.objects.all().filter(status=True)
    return render(request,'hospital/admin_view_reception.html',{'receptions':receptions})



@login_required(login_url='adminlogin')
@user_passes_test(is_admin)
def delete_reception_from_hospital_view(request,pk):
    reception=models.Reception.objects.get(id=pk)
    user=models.User.objects.get(id=reception.user_id)
    user.delete()
    reception.delete()
    return redirect('admin-view-reception')



@login_required(login_url='adminlogin')
@user_passes_test(is_admin)
def update_reception_view(request,pk):
    reception=models.Reception.objects.get(id=pk)
    user=models.User.objects.get(id=reception.user_id)

    userForm=forms.ReceptionUserForm(instance=user)
    receptionForm=forms.ReceptionForm(request.FILES,instance=reception)
    mydict={'userForm':userForm,'receptionForm':receptionForm}
    if request.method=='POST':
        userForm=forms.ReceptionUserForm(request.POST,instance=user)
        receptionForm=forms.ReceptionForm(request.POST,request.FILES,instance=reception)
        if userForm.is_valid() and receptionForm.is_valid():
            user=userForm.save()
            user.set_password(user.password)
            user.save()
            reception=receptionForm.save(commit=False)
            reception.status=True
            reception.save()
            return redirect('admin-view-reception')
    return render(request,'hospital/admin_update_reception.html',context=mydict)




@login_required(login_url='adminlogin')
@user_passes_test(is_admin)
def admin_add_reception_view(request):
    userForm=forms.ReceptionUserForm()
    receptionForm=forms.ReceptionForm()
    mydict={'userForm':userForm,'receptionForm':receptionForm}
    if request.method=='POST':
        userForm=forms.ReceptionUserForm(request.POST)
        receptionForm=forms.ReceptionForm(request.POST, request.FILES)
        if userForm.is_valid() and receptionForm.is_valid():
            user=userForm.save()
            user.set_password(user.password)
            user.save()

            reception=receptionForm.save(commit=False)
            reception.user=user
            reception.status=True
            reception.save()

            my_reception_group = Group.objects.get_or_create(name='RECEPTION')
            my_reception_group[0].user_set.add(user)

        return HttpResponseRedirect('admin-view-reception')
    return render(request,'hospital/admin_add_reception.html',context=mydict)




@login_required(login_url='adminlogin')
@user_passes_test(is_admin)
def admin_approve_reception_view(request):
    #those whose approval are needed
    receptions=models.Reception.objects.all().filter(status=False)
    return render(request,'hospital/admin_approve_reception.html',{'receptions':receptions})

@login_required(login_url='adminlogin')
@user_passes_test(is_admin)
def admin_approve_pathologist_view(request):
    #those whose approval are needed
    pathologists=models.Pathologist.objects.all().filter(status=False)
    return render(request,'hospital/admin_approve_pathologist.html',{'pathologists':pathologists})

@login_required(login_url='adminlogin')
@user_passes_test(is_admin)
def approve_reception_view(request,pk):
    reception=models.Reception.objects.get(id=pk)
    reception.status=True
    reception.save()
    return redirect(reverse('admin-approve-reception'))

@login_required(login_url='adminlogin')
@user_passes_test(is_admin)
def approve_pathologist_view(request,pk):
    pathologist=models.Pathologist.objects.get(id=pk)
    pathologist.status=True
    pathologist.save()
    return redirect(reverse('admin-approve-pathologist'))


@login_required(login_url='adminlogin')
@user_passes_test(is_admin)
def reject_reception_view(request,pk):
    reception=models.Reception.objects.get(id=pk)
    user=models.User.objects.get(id=reception.user_id)
    user.delete()
    reception.delete()
    return redirect('admin-approve-reception')

@login_required(login_url='adminlogin')
@user_passes_test(is_admin)
def reject_pathologist_view(request,pk):
    pathologist=models.Pathologist.objects.get(id=pk)
    user=models.User.objects.get(id=pathologist.user_id)
    user.delete()
    pathologist.delete()
    return redirect('admin-approve-pathologist')



@login_required(login_url='adminlogin')
@user_passes_test(is_admin)
def admin_view_reception_specialisation_view(request):
    receptions=models.Reception.objects.all().filter(status=True)
    return render(request,'hospital/admin_view_reception_specialisation.html',{'receptions':receptions})

@login_required(login_url='adminlogin')
@user_passes_test(is_admin)
def admin_patient_view(request):
    return render(request,'hospital/admin_patient.html')

@login_required(login_url='receptionlogin')
@user_passes_test(is_reception)
def reception_patient_view(request):
    return render(request,'hospital/reception_patient.html')

@login_required(login_url='pathologistlogin')
@user_passes_test(is_pathologist)
def pathologist_labcustomer_view(request):
    return render(request,'hospital/pathologist_labcustomer.html')

@login_required(login_url='receptionlogin')
@user_passes_test(is_reception)
def reception_labcustomer_view(request):
    return render(request,'hospital/reception_labcustomer.html')



@login_required(login_url='adminlogin')
@user_passes_test(is_admin)
def admin_view_patient_view(request):
    patients=models.Patient.objects.all().filter(status=True)
    return render(request,'hospital/admin_view_patient.html',{'patients':patients})

@login_required(login_url='receptionlogin')
@user_passes_test(is_reception)
def reception_view_patient_view(request):
    patients=models.Patient.objects.all().filter(status=True)
    return render(request,'hospital/reception_view_patient.html',{'patients':patients})



@login_required(login_url='adminlogin')
@user_passes_test(is_admin)
def delete_patient_from_hospital_view(request,pk):
    patient=models.Patient.objects.get(id=pk)
    user=models.User.objects.get(id=patient.user_id)
    user.delete()
    patient.delete()
    return redirect('admin-view-patient')

@login_required(login_url='receptionlogin')
@user_passes_test(is_reception)
def delete_patient_from_hospital_view(request,pk):
    patient=models.Patient.objects.get(id=pk)
    user=models.User.objects.get(id=patient.user_id)
    user.delete()
    patient.delete()
    return redirect('reception-view-patient')



@login_required(login_url='adminlogin')
@user_passes_test(is_admin)
def update_patient_view(request,pk):
    patient=models.Patient.objects.get(id=pk)
    user=models.User.objects.get(id=patient.user_id)

    userForm=forms.PatientUserForm(instance=user)
    patientForm=forms.PatientForm(request.FILES,instance=patient)
    mydict={'userForm':userForm,'patientForm':patientForm}
    if request.method=='POST':
        userForm=forms.PatientUserForm(request.POST,instance=user)
        patientForm=forms.PatientForm(request.POST,request.FILES,instance=patient)
        if userForm.is_valid() and patientForm.is_valid():
            user=userForm.save()
            user.set_password(user.password)
            user.save()
            patient=patientForm.save(commit=False)
            patient.status=True
            patient.assignedDoctorId=request.POST.get('assignedDoctorId')
            patient.save()
            return redirect('admin-view-patient')
    return render(request,'hospital/admin_update_patient.html',context=mydict)

@login_required(login_url='receptionlogin')
@user_passes_test(is_reception)
def update_patient_view(request,pk):
    patient=models.Patient.objects.get(id=pk)
    user=models.User.objects.get(id=patient.user_id)

    userForm=forms.PatientUserForm(instance=user)
    patientForm=forms.PatientForm(request.FILES,instance=patient)
    mydict={'userForm':userForm,'patientForm':patientForm}
    if request.method=='POST':
        userForm=forms.PatientUserForm(request.POST,instance=user)
        patientForm=forms.PatientForm(request.POST,request.FILES,instance=patient)
        if userForm.is_valid() and patientForm.is_valid():
            user=userForm.save()
            user.set_password(user.password)
            user.save()
            patient=patientForm.save(commit=False)
            patient.status=True
            patient.assignedDoctorId=request.POST.get('assignedDoctorId')
            patient.save()
            return redirect('reception-view-patient')
    return render(request,'hospital/reception_update_patient.html',context=mydict)




@login_required(login_url='adminlogin')
@user_passes_test(is_admin)
def admin_add_patient_view(request):
    userForm=forms.PatientUserForm()
    patientForm=forms.PatientForm()
    mydict={'userForm':userForm,'patientForm':patientForm}
    if request.method=='POST':
        userForm=forms.PatientUserForm(request.POST)
        patientForm=forms.PatientForm(request.POST,request.FILES)
        if userForm.is_valid() and patientForm.is_valid():
            user=userForm.save()
            user.set_password(user.password)
            user.save()

            patient=patientForm.save(commit=False)
            patient.user=user
            patient.status=True
            patient.assignedDoctorId=request.POST.get('assignedDoctorId')
            patient.save()

            my_patient_group = Group.objects.get_or_create(name='PATIENT')
            my_patient_group[0].user_set.add(user)

        return HttpResponseRedirect('admin-view-patient')
    return render(request,'hospital/admin_add_patient.html',context=mydict)



#------------------FOR APPROVING PATIENT BY ADMIN----------------------
@login_required(login_url='adminlogin')
@user_passes_test(is_admin)
def admin_approve_patient_view(request):
    #those whose approval are needed
    patients=models.Patient.objects.all().filter(status=False)
    return render(request,'hospital/admin_approve_patient.html',{'patients':patients})

@login_required(login_url='receptionlogin')
@user_passes_test(is_reception)
def reception_approve_labcustomer_view(request):
    #those whose approval are needed
    labcustomers=models.Labcustomer.objects.all().filter(status=False)
    return render(request,'hospital/reception_approve_labcustomer.html',{'labcustomers':labcustomers})



@login_required(login_url='adminlogin')
@user_passes_test(is_admin)
def approve_patient_view(request,pk):
    patient=models.Patient.objects.get(id=pk)
    patient.status=True
    patient.save()
    return redirect(reverse('admin-approve-patient'))

@login_required(login_url='receptionlogin')
@user_passes_test(is_reception)
def approve_labcustomer_view(request,pk):
    labcustomer=models.Labcustomer.objects.get(id=pk)
    labcustomer.status=True
    labcustomer.save()
    return redirect(reverse('reception-approve-labcustomer'))



@login_required(login_url='adminlogin')
@user_passes_test(is_admin)
def reject_patient_view(request,pk):
    patient=models.Patient.objects.get(id=pk)
    user=models.User.objects.get(id=patient.user_id)
    user.delete()
    patient.delete()
    return redirect('admin-approve-patient')

@login_required(login_url='receptionlogin')
@user_passes_test(is_reception)
def reject_labcustomer_view(request,pk):
    labcustomer=models.Labcustomer.objects.get(id=pk)
    user=models.User.objects.get(id=labcustomer.user_id)
    user.delete()
    labcustomer.delete()
    return redirect('reception-approve-labcustomer')



#--------------------- FOR DISCHARGING PATIENT BY ADMIN START-------------------------
@login_required(login_url='pathologistlogin')
@user_passes_test(is_pathologist)
def pathologist_write_labcustomer_view(request):
    labcustomers=models.Labcustomer.objects.all().filter(status=True)
    return render(request,'hospital/pathologist_write_labcustomer.html',{'labcustomers':labcustomers})



@login_required(login_url='receptionlogin')
@user_passes_test(is_reception)
def reception_discharge_patient_view(request):
    patients=models.Patient.objects.all().filter(status=True)
    return render(request,'hospital/reception_discharge_patient.html',{'patients':patients})


@login_required(login_url='receptionlogin')
@user_passes_test(is_reception)
def discharge_patient_view(request,pk):
    patient=models.Patient.objects.get(id=pk)
    days=(date.today()-patient.admitDate) #2 days, 0:00:00
    assignedDoctor=models.User.objects.all().filter(id=patient.assignedDoctorId)
    d=days.days # only how many day that is 2
    patientDict={
        'patientId':pk,
        'name':patient.get_name,
        'mobile':patient.mobile,
        'address':patient.address,
        'symptoms':patient.symptoms,
        'admitDate':patient.admitDate,
        'todayDate':date.today(),
        'day':d,
        'assignedDoctorName':assignedDoctor[0].first_name,
    }
    if request.method == 'POST':
        feeDict ={
            'roomCharge':int(request.POST['roomCharge'])*int(d),
            'doctorFee':request.POST['doctorFee'],
            'medicineCost' : request.POST['medicineCost'],
            'OtherCharge' : request.POST['OtherCharge'],
            'total':(int(request.POST['roomCharge'])*int(d))+int(request.POST['doctorFee'])+int(request.POST['medicineCost'])+int(request.POST['OtherCharge'])
        }
        patientDict.update(feeDict)
        #for updating to database patientDischargeDetails (pDD)
        pDD=models.PatientDischargeDetails()
        pDD.patientId=pk
        pDD.patientName=patient.get_name
        pDD.assignedDoctorName=assignedDoctor[0].first_name
        pDD.address=patient.address
        pDD.mobile=patient.mobile
        pDD.symptoms=patient.symptoms
        pDD.admitDate=patient.admitDate
        pDD.releaseDate=date.today()
        pDD.daySpent=int(d)
        pDD.medicineCost=int(request.POST['medicineCost'])
        pDD.roomCharge=int(request.POST['roomCharge'])*int(d)
        pDD.doctorFee=int(request.POST['doctorFee'])
        pDD.OtherCharge=int(request.POST['OtherCharge'])
        pDD.total=(int(request.POST['roomCharge'])*int(d))+int(request.POST['doctorFee'])+int(request.POST['medicineCost'])+int(request.POST['OtherCharge'])
        pDD.save()
        return render(request,'hospital/patient_final_bill.html',context=patientDict)
    return render(request,'hospital/patient_generate_bill.html',context=patientDict)

@login_required(login_url='pathologistlogin')
@user_passes_test(is_pathologist)
def write_labcustomer_view(request,pk):
    labcustomer=models.Labcustomer.objects.get(id=pk)# only how many day that is 2
    labcustomerDict={
        'labcustomerId':pk,
        'name':labcustomer.get_name,
        'mobile':labcustomer.mobile,
        'address':labcustomer.address,
        'test':labcustomer.test,
        'scheduledate':labcustomer.scheduledate,
    }
    if request.method == 'POST':
        reportDict ={
            'testDetail':request.POST['testDetail'],
            'testResult':request.POST['testResult'],
            'conclusion':request.POST['conclusion'],
            'charge':request.POST['charge']
        }
        labcustomerDict.update(reportDict)
        lP=models.LabcustomerReport()
        lP.labcustomerId=pk
        lP.labcustomerName=labcustomer.get_name
        lP.address=labcustomer.address
        lP.mobile=labcustomer.mobile
        lP.test=labcustomer.test
        lP.scheduledate=labcustomer.scheduledate
        lP.testDetail=request.POST['testDetail']
        lP.testResult=request.POST['testResult']
        lP.conclusion=request.POST['conclusion']
        lP.charge=int(request.POST['charge'])
        lP.save()
        return render(request,'hospital/labcustomer_final_result.html',context=labcustomerDict)
    return render(request,'hospital/labcustomer_generate_result.html',context=labcustomerDict)

#--------------for discharge patient bill (pdf) download and printing
import io
from xhtml2pdf import pisa
from django.template.loader import get_template
from django.template import Context
from django.http import HttpResponse


def render_to_pdf(template_src, context_dict):
    template = get_template(template_src)
    html  = template.render(context_dict)
    result = io.BytesIO()
    pdf = pisa.pisaDocument(io.BytesIO(html.encode("ISO-8859-1")), result)
    if not pdf.err:
        return HttpResponse(result.getvalue(), content_type='application/pdf')
    return



def download_pdf_view(request,pk):
    dischargeDetails=models.PatientDischargeDetails.objects.all().filter(patientId=pk).order_by('-id')[:1]
    dict={
        'patientName':dischargeDetails[0].patientName,
        'assignedDoctorName':dischargeDetails[0].assignedDoctorName,
        'address':dischargeDetails[0].address,
        'mobile':dischargeDetails[0].mobile,
        'symptoms':dischargeDetails[0].symptoms,
        'admitDate':dischargeDetails[0].admitDate,
        'releaseDate':dischargeDetails[0].releaseDate,
        'daySpent':dischargeDetails[0].daySpent,
        'medicineCost':dischargeDetails[0].medicineCost,
        'roomCharge':dischargeDetails[0].roomCharge,
        'doctorFee':dischargeDetails[0].doctorFee,
        'OtherCharge':dischargeDetails[0].OtherCharge,
        'total':dischargeDetails[0].total,
    }
    return render_to_pdf('hospital/download_bill.html',dict)

def download_result_view(request,pk):
    customerReport=models.LabcustomerReport.objects.all().filter(labcustomerId=pk).order_by('-id')[:1]
    dict={
        'labcustomerName':customerReport[0].labcustomerName,
        'address':customerReport[0].address,
        'mobile':customerReport[0].mobile,
        'test':customerReport[0].test,
        'scheduledate':customerReport[0].scheduledate,
        'testDetail':customerReport[0].testDetail,
        'testResult':customerReport[0].testResult,
        'conclusion':customerReport[0].conclusion,
        'charge':customerReport[0].charge,
    }
    return render_to_pdf('hospital/download_result.html',dict)



#-----------------APPOINTMENT START--------------------------------------------------------------------
@login_required(login_url='adminlogin')
@user_passes_test(is_admin)
def admin_appointment_view(request):
    return render(request,'hospital/admin_appointment.html')

@login_required(login_url='receptionlogin')
@user_passes_test(is_reception)
def reception_appointment_view(request):
    return render(request,'hospital/reception_appointment.html')



@login_required(login_url='adminlogin')
@user_passes_test(is_admin)
def admin_view_appointment_view(request):
    appointments=models.Appointment.objects.all().filter(status=True)
    return render(request,'hospital/admin_view_appointment.html',{'appointments':appointments})

@login_required(login_url='receptionlogin')
@user_passes_test(is_reception)
def reception_view_appointment_view(request):
    appointments=models.Appointment.objects.all().filter(status=True)
    return render(request,'hospital/reception_view_appointment.html',{'appointments':appointments})





@login_required(login_url='receptionlogin')
@user_passes_test(is_reception)
def reception_add_appointment_view(request):
    appointmentForm=forms.AppointmentForm()
    mydict={'appointmentForm':appointmentForm,}
    if request.method=='POST':
        appointmentForm=forms.AppointmentForm(request.POST)
        if appointmentForm.is_valid():
            appointment=appointmentForm.save(commit=False)
            appointment.doctorId=request.POST.get('doctorId')
            appointment.patientId=request.POST.get('patientId')
            appointment.doctorName=models.User.objects.get(id=request.POST.get('doctorId')).first_name
            appointment.patientName=models.User.objects.get(id=request.POST.get('patientId')).first_name
            appointment.status=True
            appointment.save()
        return HttpResponseRedirect('reception-view-appointment')
    return render(request,'hospital/reception_add_appointment.html',context=mydict)

@login_required(login_url='receptionlogin')
@user_passes_test(is_reception)
def reception_approve_appointment_view(request):
    #those whose approval are needed
    appointments=models.Appointment.objects.all().filter(status=False)
    return render(request,'hospital/reception_approve_appointment.html',{'appointments':appointments})

@login_required(login_url='receptionlogin')
@user_passes_test(is_reception)
def r_approve_appointment_view(request,pk):
    appointment=models.Appointment.objects.get(id=pk)
    appointment.status=True
    appointment.save()
    return redirect(reverse('reception-approve-appointment'))

@login_required(login_url='receptionlogin')
@user_passes_test(is_reception)
def r_reject_appointment_view(request,pk):
    appointment=models.Appointment.objects.get(id=pk)
    appointment.delete()
    return redirect('reception-approve-appointment')
#---------------------------------------------------------------------------------
#------------------------ ADMIN RELATED VIEWS END ------------------------------
#---------------------------------------------------------------------------------






#---------------------------------------------------------------------------------
#------------------------ DOCTOR RELATED VIEWS START ------------------------------
#---------------------------------------------------------------------------------
@login_required(login_url='doctorlogin')
@user_passes_test(is_doctor)
def doctor_dashboard_view(request):
    #for three cards
    patientcount=models.Patient.objects.all().filter(status=True,assignedDoctorId=request.user.id).count()
    appointmentcount=models.Appointment.objects.all().filter(status=True,doctorId=request.user.id).count()
    patientdischarged=models.PatientDischargeDetails.objects.all().distinct().filter(assignedDoctorName=request.user.first_name).count()

    #for  table in doctor dashboard
    appointments=models.Appointment.objects.all().filter(status=True,doctorId=request.user.id).order_by('-id')
    patientid=[]
    for a in appointments:
        patientid.append(a.patientId)
    patients=models.Patient.objects.all().filter(status=True,user_id__in=patientid).order_by('-id')
    appointments=zip(appointments,patients)
    mydict={
    'patientcount':patientcount,
    'appointmentcount':appointmentcount,
    'patientdischarged':patientdischarged,
    'appointments':appointments,
    'doctor':models.Doctor.objects.get(user_id=request.user.id), #for profile picture of doctor in sidebar
    }
    return render(request,'hospital/doctor_dashboard.html',context=mydict)



@login_required(login_url='doctorlogin')
@user_passes_test(is_doctor)
def doctor_patient_view(request):
    mydict={
    'doctor':models.Doctor.objects.get(user_id=request.user.id), #for profile picture of doctor in sidebar
    }
    return render(request,'hospital/doctor_patient.html',context=mydict)



@login_required(login_url='doctorlogin')
@user_passes_test(is_doctor)
def doctor_view_patient_view(request):
    patients=models.Patient.objects.all().filter(status=True,assignedDoctorId=request.user.id)
    doctor=models.Doctor.objects.get(user_id=request.user.id) #for profile picture of doctor in sidebar
    return render(request,'hospital/doctor_view_patient.html',{'patients':patients,'doctor':doctor})



@login_required(login_url='doctorlogin')
@user_passes_test(is_doctor)
def doctor_view_discharge_patient_view(request):
    dischargedpatients=models.PatientDischargeDetails.objects.all().distinct().filter(assignedDoctorName=request.user.first_name)
    doctor=models.Doctor.objects.get(user_id=request.user.id) #for profile picture of doctor in sidebar
    return render(request,'hospital/doctor_view_discharge_patient.html',{'dischargedpatients':dischargedpatients,'doctor':doctor})



@login_required(login_url='doctorlogin')
@user_passes_test(is_doctor)
def doctor_appointment_view(request):
    doctor=models.Doctor.objects.get(user_id=request.user.id) #for profile picture of doctor in sidebar
    return render(request,'hospital/doctor_appointment.html',{'doctor':doctor})



@login_required(login_url='doctorlogin')
@user_passes_test(is_doctor)
def doctor_view_appointment_view(request):
    doctor=models.Doctor.objects.get(user_id=request.user.id) #for profile picture of doctor in sidebar
    appointments=models.Appointment.objects.all().filter(status=True,doctorId=request.user.id)
    patientid=[]
    for a in appointments:
        patientid.append(a.patientId)
    patients=models.Patient.objects.all().filter(status=True,user_id__in=patientid)
    appointments=zip(appointments,patients)
    return render(request,'hospital/doctor_view_appointment.html',{'appointments':appointments,'doctor':doctor})



@login_required(login_url='doctorlogin')
@user_passes_test(is_doctor)
def doctor_delete_appointment_view(request):
    doctor=models.Doctor.objects.get(user_id=request.user.id) #for profile picture of doctor in sidebar
    appointments=models.Appointment.objects.all().filter(status=True,doctorId=request.user.id)
    patientid=[]
    for a in appointments:
        patientid.append(a.patientId)
    patients=models.Patient.objects.all().filter(status=True,user_id__in=patientid)
    appointments=zip(appointments,patients)
    return render(request,'hospital/doctor_delete_appointment.html',{'appointments':appointments,'doctor':doctor})



@login_required(login_url='doctorlogin')
@user_passes_test(is_doctor)
def delete_appointment_view(request,pk):
    appointment=models.Appointment.objects.get(id=pk)
    appointment.delete()
    doctor=models.Doctor.objects.get(user_id=request.user.id) #for profile picture of doctor in sidebar
    appointments=models.Appointment.objects.all().filter(status=True,doctorId=request.user.id)
    patientid=[]
    for a in appointments:
        patientid.append(a.patientId)
    patients=models.Patient.objects.all().filter(status=True,user_id__in=patientid)
    appointments=zip(appointments,patients)
    return render(request,'hospital/doctor_delete_appointment.html',{'appointments':appointments,'doctor':doctor})



#---------------------------------------------------------------------------------
#------------------------ DOCTOR RELATED VIEWS END ------------------------------
#---------------------------------------------------------------------------------






#---------------------------------------------------------------------------------
#------------------------ PATIENT RELATED VIEWS START ------------------------------
#---------------------------------------------------------------------------------
@login_required(login_url='patientlogin')
@user_passes_test(is_patient)
def patient_dashboard_view(request):
    patient=models.Patient.objects.get(user_id=request.user.id)
    doctor=models.Doctor.objects.get(user_id=patient.assignedDoctorId)
    mydict={
    'patient':patient,
    'doctorName':doctor.get_name,
    'doctorMobile':doctor.mobile,
    'doctorAddress':doctor.address,
    'symptoms':patient.symptoms,
    'doctorDepartment':doctor.department,
    'admitDate':patient.admitDate,
    'patienttype':patient.patienttype,
    }
    return render(request,'hospital/patient_dashboard.html',context=mydict)

@login_required(login_url='labcustomerlogin')
@user_passes_test(is_labcustomer)
def labcustomer_dashboard_view(request):
    labcustomer=models.Labcustomer.objects.get(user_id=request.user.id)
    mydict={
    'labcustomer':labcustomer,
    'test':labcustomer.test,
    'scheduledate':labcustomer.scheduledate,
    }
    return render(request,'hospital/labcustomer_dashboard.html',context=mydict)



@login_required(login_url='patientlogin')
@user_passes_test(is_patient)
def patient_appointment_view(request):
    patient=models.Patient.objects.get(user_id=request.user.id) #for profile picture of patient in sidebar
    return render(request,'hospital/patient_appointment.html',{'patient':patient})



@login_required(login_url='patientlogin')
@user_passes_test(is_patient)
def patient_book_appointment_view(request):
    appointmentForm=forms.PatientAppointmentForm()
    patient=models.Patient.objects.get(user_id=request.user.id) #for profile picture of patient in sidebar
    message=None
    mydict={'appointmentForm':appointmentForm,'patient':patient,'message':message}
    if request.method=='POST':
        appointmentForm=forms.PatientAppointmentForm(request.POST)
        if appointmentForm.is_valid():
            print(request.POST.get('doctorId'))
            desc=request.POST.get('description')

            doctor=models.Doctor.objects.get(user_id=request.POST.get('doctorId'))
            
            if doctor.department == 'Cardiologist':
                if 'heart' in desc:
                    pass
                else:
                    print('else')
                    message="Please Choose Doctor According To Disease"
                    return render(request,'hospital/patient_book_appointment.html',{'appointmentForm':appointmentForm,'patient':patient,'message':message})


            if doctor.department == 'Dermatologists':
                if 'skin' in desc:
                    pass
                else:
                    print('else')
                    message="Please Choose Doctor According To Disease"
                    return render(request,'hospital/patient_book_appointment.html',{'appointmentForm':appointmentForm,'patient':patient,'message':message})

            if doctor.department == 'Emergency Medicine Specialists':
                if 'fever' in desc:
                    pass
                else:
                    print('else')
                    message="Please Choose Doctor According To Disease"
                    return render(request,'hospital/patient_book_appointment.html',{'appointmentForm':appointmentForm,'patient':patient,'message':message})

            if doctor.department == 'Allergists/Immunologists':
                if 'allergy' in desc:
                    pass
                else:
                    print('else')
                    message="Please Choose Doctor According To Disease"
                    return render(request,'hospital/patient_book_appointment.html',{'appointmentForm':appointmentForm,'patient':patient,'message':message})

            if doctor.department == 'Anesthesiologists':
                if 'surgery' in desc:
                    pass
                else:
                    print('else')
                    message="Please Choose Doctor According To Disease"
                    return render(request,'hospital/patient_book_appointment.html',{'appointmentForm':appointmentForm,'patient':patient,'message':message})

            if doctor.department == 'Colon and Rectal Surgeons':
                if 'cancer' in desc:
                    pass
                else:
                    print('else')
                    message="Please Choose Doctor According To Disease"
                    return render(request,'hospital/patient_book_appointment.html',{'appointmentForm':appointmentForm,'patient':patient,'message':message})





            appointment=appointmentForm.save(commit=False)
            appointment.doctorId=request.POST.get('doctorId')
            appointment.patientId=request.user.id #----user can choose any patient but only their info will be stored
            appointment.doctorName=models.User.objects.get(id=request.POST.get('doctorId')).first_name
            appointment.patientName=request.user.first_name #----user can choose any patient but only their info will be stored
            appointment.status=False
            appointment.save()
        return HttpResponseRedirect('patient-view-appointment')
    return render(request,'hospital/patient_book_appointment.html',context=mydict)





@login_required(login_url='patientlogin')
@user_passes_test(is_patient)
def patient_view_appointment_view(request):
    patient=models.Patient.objects.get(user_id=request.user.id) #for profile picture of patient in sidebar
    appointments=models.Appointment.objects.all().filter(patientId=request.user.id)
    return render(request,'hospital/patient_view_appointment.html',{'appointments':appointments,'patient':patient})



@login_required(login_url='patientlogin')
@user_passes_test(is_patient)
def patient_discharge_view(request):
    patient=models.Patient.objects.get(user_id=request.user.id) #for profile picture of patient in sidebar
    dischargeDetails=models.PatientDischargeDetails.objects.all().filter(patientId=patient.id).order_by('-id')[:1]
    patientDict=None
    if dischargeDetails:
        patientDict ={
        'is_discharged':True,
        'patient':patient,
        'patientId':patient.id,
        'patientName':patient.get_name,
        'assignedDoctorName':dischargeDetails[0].assignedDoctorName,
        'address':patient.address,
        'mobile':patient.mobile,
        'symptoms':patient.symptoms,
        'admitDate':patient.admitDate,
        'releaseDate':dischargeDetails[0].releaseDate,
        'daySpent':dischargeDetails[0].daySpent,
        'medicineCost':dischargeDetails[0].medicineCost,
        'roomCharge':dischargeDetails[0].roomCharge,
        'doctorFee':dischargeDetails[0].doctorFee,
        'OtherCharge':dischargeDetails[0].OtherCharge,
        'total':dischargeDetails[0].total,
        }
        print(patientDict)
    else:
        patientDict={
            'is_discharged':False,
            'patient':patient,
            'patientId':request.user.id,
        }
    return render(request,'hospital/patient_discharge.html',context=patientDict)


@login_required(login_url='labcustomerlogin')
@user_passes_test(is_labcustomer)
def labcustomer_write_view(request):
    labcustomer=models.Labcustomer.objects.get(user_id=request.user.id) #for profile picture of patient in sidebar
    customerReport=models.LabcustomerReport.objects.all().filter(labcustomerId=labcustomer.id).order_by('-id')[:1]
    labcustomerDict=None
    if customerReport:
        labcustomerDict ={
        'is_resulted':True,
        'labcustomer':labcustomer,
        'labcustomerId':labcustomer.id,
        'labcustomerName':labcustomer.get_name,
        'address':labcustomer.address,
        'mobile':labcustomer.mobile,
        'test':labcustomer.test,
        'scheduledate':labcustomer.scheduledate,
        'testDetail':customerReport[0].testDetail,
        'testResult':customerReport[0].testResult,
        'conclusion':customerReport[0].conclusion,
        'charge':customerReport[0].charge,
        }
        print(labcustomerDict)
    else:
        labcustomerDict={
            'is_resulted':False,
            'labcustomer':labcustomer,
            'labcustomerId':request.user.id,
        }
    return render(request,'hospital/labcustomer_write.html',context=labcustomerDict)


#------------------------ PATIENT RELATED VIEWS END ------------------------------
#---------------------------------------------------------------------------------








#---------------------------------------------------------------------------------
#------------------------ ABOUT US AND CONTACT US VIEWS START ------------------------------
#---------------------------------------------------------------------------------
def aboutus_view(request):
    return render(request,'hospital/aboutus.html')

def contactus_view(request):
    sub = forms.ContactusForm()
    if request.method == 'POST':
        sub = forms.ContactusForm(request.POST)
        if sub.is_valid():
            email = sub.cleaned_data['Email']
            name=sub.cleaned_data['Name']
            message = sub.cleaned_data['Message']
            send_mail(str(name)+' || '+str(email),message,settings.EMAIL_HOST_USER, settings.EMAIL_RECEIVING_USER, fail_silently = True)
            return render(request, 'hospital/contactussuccess.html')
    return render(request, 'hospital/contactus.html', {'form':sub})

def centralstore_view(request):
    return render(request,'hospital/centralstore.html')
def whyus_view(request):
    return render(request,'hospital/whyus.html')

def gallery_view(request):
    return render(request,'hospital/gallery.html')

