from django.shortcuts import render


from datetime import datetime
import calendar
import time

import requests
import json

import pyrebase

import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

config = {
  "apiKey": "AIzaSyAPkeZMLpbjKhHCBJPYhlapULa95M6xktQ",
  "authDomain": "churn-preddiction-system.firebaseapp.com",
  "projectId": "churn-preddiction-system",
  "databaseURL":"https://churn-preddiction-system-default-rtdb.firebaseio.com/",
  "storageBucket": "churn-preddiction-system.appspot.com",
  "messagingSenderId": "701703854952",
  "appId": "1:701703854952:web:62053c3c2e1ac9ec3c14dd",
 " measurementId": "G-YDYJMJY5HV"
}

firebase = pyrebase.initialize_app(config)
cred = credentials.Certificate("main_app/serviceAccountKey.json")
firebase_admin.initialize_app(cred)
authe = firebase.auth()
  
firestoreDB = firestore.client()

# Create your views here.
def login(request):
    return render(request,'login.html')
def post_login(request):
    request.session['type'] = 'admin'
    username = request.POST.get('username')
    password = request.POST.get('password')
    if username == 'admin' and password == 'admin':
        return render(request,'dashboard.html')
    else:
        return render(request,'login.html',{'validation':'Username or Password is incorrect'})
def logout(request):
    return render(request,'login.html')

def login_user(request):
    return render(request,'login_user.html')

def dashboard(request):
    visuals = firestoreDB.collection(u'visuals')
    services_list = {

    }
    docs = visuals.get()
    for doc in docs:
        services = visuals.document(doc.id).collection(u'services').document(doc.id).get()
        services_list[doc.id] = services.to_dict()
    print(services_list)
    return render(request,'dashboard.html',{'services':services_list})

def customers(request):
    try:
        visuals = firestoreDB.collection(u'visuals').get()
        return render(request,'customers.html',{'visuals':[data.to_dict() for data in visuals]})
    except:
        return render(request,'customers.html')

def manage_users(request):
    try:
        users = firestoreDB.collection(u'users').get()
        return render(request,'manage_users.html',{'users':[data.to_dict() for data in users]})
    except:
        return render(request,'manage_users.html')
def demographics(request):
    return render(request,'demographics.html')

def services(request):
    return render(request,'services.html')

def result(request):
    current_id = request.session['current_id']
    print(current_id)
    visuals = firestoreDB.collection(u'visuals').document(current_id)
    services = visuals.collection(u'services').document(current_id)
    visual_datas = visuals.get()
    service_datas = services.get()
    print(current_id)
    if visual_datas.exists:
        print(service_datas.to_dict())
        pass_data = {
            "visuals_data":[visual_data.to_dict() for visual_data in visual_datas],
            "service_data":[service_data.to_dict() for service_data in service_datas],
            }
        return render(request,'result.html',pass_data)
    return render(request,'result.html')
    
def post_get_demographics(request):
    customer = request.POST.get('customer')
    gender = request.POST.get('gender')
    senior_citizen = request.POST.get('senior_citizen')
    partner = request.POST.get('partner')
    depender= request.POST.get('depender')
    
    date_created = datetime.now()
    user_id =  calendar.timegm(date_created.timetuple())

    data = {
    u'customer': customer,  
    u'gender': gender,
    u'senior_citizen': senior_citizen,
    u'partner': partner,
    u'depender': depender
    }

    firestoreDB.collection(u'visuals').document(str(user_id)).set(data)

    return render(request, 'services.html',{"current_id":str(user_id)})

def post_get_services(request):
    tenure = request.POST.get('tenure')
    phone_service = request.POST.get('phone_service')
    multiple_lines = request.POST.get('multiple_lines')
    internet_service = request.POST.get('internet_service')
    online_security = request.POST.get('online_security')

    online_backup = request.POST.get('online_backup')
    device_protection = request.POST.get('device_protection')
    tech_support = request.POST.get('tech_support')
    streaming_tv = request.POST.get('streaming_tv')
    streaming_movie = request.POST.get('streaming_movie')

    contract = request.POST.get('contract')
    paperless_billing = request.POST.get('paperless_billing')
    payment_method = request.POST.get('payment_method')
    monthly_charges = request.POST.get('monthly_charges')
    total_charges = request.POST.get('total_charges')

    current_id = request.POST.get('current_id')
    request.session['current_id'] = current_id  
    data = {
    u'tenure': tenure,  
    u'phone_service': phone_service,
    u'multiple_lines': multiple_lines,
    u'internet_service': internet_service,
    u'online_security': online_security,
    u'online_backup': online_backup,  
    u'device_protection': device_protection,
    u'tech_support': tech_support,
    u'streaming_tv': streaming_tv,
    u'streaming_movie': streaming_movie,
    u'contract': contract,  
    u'paperless_billing': paperless_billing,
    u'payment_method': payment_method,
    u'monthly_charges': monthly_charges,
    u'total_charges': total_charges,
    }

    
    visuals = firestoreDB.collection(u'visuals').document(current_id)
    visuals.collection(u'services').document(current_id).set(data)

    current_id = request.session['current_id']
    print(current_id)
    visuals = firestoreDB.collection(u'visuals').document(current_id)
    services = visuals.collection(u'services').document(current_id)
    visual_datas = visuals.get()
    service_datas = services.get()
    customer = u'{}'.format(visual_datas.to_dict()['customer'])


    if visual_datas.exists:
        print(service_datas.to_dict())
        pass_data = {
            "customer":u'{}'.format(visual_datas.to_dict()['customer']),
            "gender":u'{}'.format(visual_datas.to_dict()['gender']),
            "senior_citizen":u'{}'.format(visual_datas.to_dict()['senior_citizen']),
            "partner":u'{}'.format(visual_datas.to_dict()['partner']),
            "depender":u'{}'.format(visual_datas.to_dict()['depender']),
            "tenure":u'{}'.format( service_datas.to_dict()['tenure']),
            "phone_service":u'{}'.format( service_datas.to_dict()['phone_service']),
            "multiple_lines":u'{}'.format( service_datas.to_dict()['multiple_lines']),
            "internet_service":u'{}'.format( service_datas.to_dict()['internet_service']),
            "online_security":u'{}'.format( service_datas.to_dict()['online_security']),
            "online_backup":u'{}'.format( service_datas.to_dict()['online_backup']),
            "device_protection":u'{}'.format( service_datas.to_dict()['device_protection']),
            "tech_support":u'{}'.format( service_datas.to_dict()['tech_support']),
            "streaming_tv":u'{}'.format( service_datas.to_dict()['streaming_tv']),
            "streaming_movie":u'{}'.format( service_datas.to_dict()['streaming_movie']),
            "contract":u'{}'.format( service_datas.to_dict()['contract']),
            "paperless_billingr":u'{}'.format( service_datas.to_dict()['paperless_billing']),
            "payment_method":u'{}'.format( service_datas.to_dict()['payment_method']),
            "monthly_charges":u'{}'.format( service_datas.to_dict()['monthly_charges']),
            "total_charges":u'{}'.format( service_datas.to_dict()['total_charges']),
            }
        return render(request,'result.html',pass_data)
    return render(request, 'result.html')

def post_add_user(request):
    first_name = request.POST.get('last_name')
    last_name = request.POST.get('last_name')
    password = str(first_name) + "_" + str(last_name)
    email = request.POST.get('email')
    create = request.POST.get('create')
    cancel = request.POST.get('cancel')
    date_created = datetime.now()
    user_id =  calendar.timegm(date_created.timetuple())
    if 'create' in request.POST:
        try:
            user = authe.create_user_with_email_and_password(email,password)
            data = {
                u'first_name': first_name,
                u'last_name': last_name,
                u'email': email,
                u'status': 'active',
                u'uid':str(user['idToken'])
            }
            firestoreDB.collection(u'users').document(str(user_id)).set(data)
            users = firestoreDB.collection(u'users').get()
            return render(request,'manage_users.html',{'users':[data.to_dict() for data in users],"validation_success":"Successfully Add "+first_name + " " + last_name +" as User."})
        except Exception as e:
           return render(request,'manage_users.html',{'validation':"Email not found"})
    try:
        users = firestoreDB.collection(u'users').get()
        return render(request,'manage_users.html',{'users':[data.to_dict() for data in users]})
    except:
        return render(request,'manage_users.html')

def post_login_user(request):
    request.session['type'] = 'user'
    email=request.POST.get('email')
    pasw=request.POST.get('password')

    try:
        # if there is no error then signin the user with given email and password
        user=authe.sign_in_with_email_and_password(email,pasw)
    except:
        message="Invalid Credentials !! Please ChecK your Data"
        return render(request,"login_user.html",{"validation":message})
    session_id=user['idToken']
    request.session['uid']=str(session_id)
    return render(request,"dashboard.html")
    