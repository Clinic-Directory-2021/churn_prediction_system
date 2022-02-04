from csv import excel
from django.shortcuts import redirect, render


from datetime import datetime
import calendar
import time

import requests
import json

import pyrebase
from main_app import rule_sets as rs

import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

# from django.shortcuts import render_to_response
from django.http import HttpResponse, HttpResponseBadRequest, JsonResponse
from django import forms
from django.template import RequestContext
import django_excel as excel
import pandas as pd
from firebase_admin import auth

import os
from django.conf import settings
from django.template.loader import get_template
from xhtml2pdf import pisa
from django.contrib.staticfiles import finders

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
    try:
        visuals = firestoreDB.collection(u'visuals')
        visual_docs = visuals.get()
        return render(request,'dashboard.html',{'visuals':[doc.to_dict() for doc in visual_docs]})
    except:
        visuals = firestoreDB.collection(u'visuals')
        visual_docs = visuals.get()
        return render(request,'dashboard.html',{'visuals':[doc.to_dict() for doc in visual_docs]})

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

# def result(request):
#     current_id = request.session['current_id']
#     print(current_id)
#     visuals = firestoreDB.collection(u'visuals').document(current_id)
#     services = visuals.collection(u'services').document(current_id)
#     visual_datas = visuals.get()
#     service_datas = services.get()
#     print(current_id)
#     if visual_datas.exists:
#         print(service_datas.to_dict())
#         pass_data = {
#             "visuals_data":[visual_data.to_dict() for visual_data in visual_datas],
#             "service_data":[service_data.to_dict() for service_data in service_datas],
#             }
#         return render(request,'result.html',pass_data)
#     return render(request,'result.html')
    
# def post_get_demographics(request):
#     customer = request.POST.get('customer')
#     gender = request.POST.get('gender')
#     senior_citizen = request.POST.get('senior_citizen')
#     partner = request.POST.get('partner')
#     depender= request.POST.get('depender')
    
#     date_created = datetime.now()
#     user_id =  calendar.timegm(date_created.timetuple())

#     data = {
#     u'customer': customer,  
#     u'gender': gender,
#     u'senior_citizen': senior_citizen,
#     u'partner': partner,
#     u'depender': depender
#     }

#     firestoreDB.collection(u'visuals').document(str(user_id)).set(data)

#     return render(request, 'services.html',{"current_id":str(user_id)})

# def post_get_services(request):
#     tenure = request.POST.get('tenure')
#     phone_service = request.POST.get('phone_service')
#     multiple_lines = request.POST.get('multiple_lines')
#     internet_service = request.POST.get('internet_service')
#     online_security = request.POST.get('online_security')

#     online_backup = request.POST.get('online_backup')
#     device_protection = request.POST.get('device_protection')
#     tech_support = request.POST.get('tech_support')
#     streaming_tv = request.POST.get('streaming_tv')
#     streaming_movie = request.POST.get('streaming_movie')

#     contract = request.POST.get('contract')
#     paperless_billing = request.POST.get('paperless_billing')
#     payment_method = request.POST.get('payment_method')
#     monthly_charges = request.POST.get('monthly_charges')
#     total_charges = request.POST.get('total_charges')

#     current_id = request.POST.get('current_id')
#     request.session['current_id'] = current_id  
#     data = {
#     u'tenure': tenure,  
#     u'phone_service': phone_service,
#     u'multiple_lines': multiple_lines,
#     u'internet_service': internet_service,
#     u'online_security': online_security,
#     u'online_backup': online_backup,  
#     u'device_protection': device_protection,
#     u'tech_support': tech_support,
#     u'streaming_tv': streaming_tv,
#     u'streaming_movie': streaming_movie,
#     u'contract': contract,  
#     u'paperless_billing': paperless_billing,
#     u'payment_method': payment_method,
#     u'monthly_charges': monthly_charges,
#     u'total_charges': total_charges,
#     }

    
#     visuals = firestoreDB.collection(u'visuals').document(current_id)
#     visuals.collection(u'services').document(current_id).set(data)

#     current_id = request.session['current_id']
#     print(current_id)
#     visuals = firestoreDB.collection(u'visuals').document(current_id)
#     services = visuals.collection(u'services').document(current_id)
#     visual_datas = visuals.get()
#     service_datas = services.get()
#     customer = u'{}'.format(visual_datas.to_dict()['customer'])


#     if visual_datas.exists:
#         print(service_datas.to_dict())
#         pass_data = {
#             "customer":u'{}'.format(visual_datas.to_dict()['customer']),
#             "gender":u'{}'.format(visual_datas.to_dict()['gender']),
#             "senior_citizen":u'{}'.format(visual_datas.to_dict()['senior_citizen']),
#             "partner":u'{}'.format(visual_datas.to_dict()['partner']),
#             "depender":u'{}'.format(visual_datas.to_dict()['depender']),
#             "tenure":u'{}'.format( service_datas.to_dict()['tenure']),
#             "phone_service":u'{}'.format( service_datas.to_dict()['phone_service']),
#             "multiple_lines":u'{}'.format( service_datas.to_dict()['multiple_lines']),
#             "internet_service":u'{}'.format( service_datas.to_dict()['internet_service']),
#             "online_security":u'{}'.format( service_datas.to_dict()['online_security']),
#             "online_backup":u'{}'.format( service_datas.to_dict()['online_backup']),
#             "device_protection":u'{}'.format( service_datas.to_dict()['device_protection']),
#             "tech_support":u'{}'.format( service_datas.to_dict()['tech_support']),
#             "streaming_tv":u'{}'.format( service_datas.to_dict()['streaming_tv']),
#             "streaming_movie":u'{}'.format( service_datas.to_dict()['streaming_movie']),
#             "contract":u'{}'.format( service_datas.to_dict()['contract']),
#             "paperless_billingr":u'{}'.format( service_datas.to_dict()['paperless_billing']),
#             "payment_method":u'{}'.format( service_datas.to_dict()['payment_method']),
#             "monthly_charges":u'{}'.format( service_datas.to_dict()['monthly_charges']),
#             "total_charges":u'{}'.format( service_datas.to_dict()['total_charges']),
#             }
#         return render(request,'result.html',pass_data)
#     return render(request, 'result.html')

def post_add_user(request):
    first_name = request.POST.get('first_name')
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
                u'uid':str(user['localId']),
                u'user_id':str(user_id)
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

def post_edit_user(request):
    first_name = request.POST.get('first_name')
    last_name = request.POST.get('last_name')
    email = request.POST.get('email')
    status = request.POST.get('status')
    uid = request.POST.get('uid')
    user_id = request.POST.get('selected_id')
    create = request.POST.get('save')

    user_document = firestoreDB.collection(u'users').document(u'user_id')
    data = {
        u"first_name":first_name,
        u"last_name":last_name,
        u"email":email,
        u'status': status,
        u"uid":uid,
        u"user_id":user_id
    }

def post_login_user(request):
    request.session['type'] = 'user'
    email=request.POST.get('email')
    pasw=request.POST.get('password')

    try:
        # if there is no error then signin the user with given email and password
        user=authe.sign_in_with_email_and_password(email,pasw)
        uid = user['localId']
        docs = firestoreDB.collection(u'users').where(u'uid', u'==', str(uid)).get()
        for doc in docs:
            status = u'{}'.format(doc.to_dict()['status'])
            if status == "inactive":
                return render(request,"login_user.html",{{"validation_inactive":"Your account is inactive. Please contact the administrator."}})    
    except:
        message="Invalid Credentials !! Please ChecK your Data"
        return render(request,"login_user.html",{"validation":message})
    session_id=user['idToken']
    request.session['uid']=str(session_id)
    return render(request,"dashboard.html")

class UploadFileForm(forms.Form):
    file = forms.FileField()

def import_customers(request):
        date_created = datetime.now()
        visual_id =  calendar.timegm(date_created.timetuple())
    # try:
        if request.method == "POST":
                file = request.FILES['excel']
                csv = pd.read_csv(file)
                csv_size = 0
                arr = csv
                for index, row in csv.iterrows():
                    csv_size += 1
                visual = firestoreDB.collection(u'visuals').document(str(visual_id))
                visual_info = {
                        "batch_size":str(csv_size),
                        "visual_id":str(visual_id),
                        "date_created":str(date_created),
                    }
                visual.set(visual_info)
                customer = visual.collection(u"customer")
                for index, row in csv.iterrows():
                    
                    rs.rule_set(row["CustomerID"],row["Tenure"],row["MonthlyCharges"],row["TotalCharges"],row["Senior_Citizen"],
                    row["Partner"],row["Dependents"],row["Multiple_Lines"],row["Internet_Service"],row["Online_Security"],
                    row["Online_Backup"],row["Device_Protection"],row["Tech_Support"],row["Streaming_TV"],row["Streaming_Movies"],
                    row["Contract"],row["Paperless_Billing"],row["Payment_Method"])
                    
                    customer_data = {
                        "ID":str(index),
                        "customerID":str(row["CustomerID"]),
                        "Tenure":str(row["Tenure"]),
                        "MonthlyCharges":str(row["MonthlyCharges"]),
                        "TotalCharges":str(row["TotalCharges"]),
                        "Senior_Citizen":str(row["Senior_Citizen"]),
                        "Partner":str(row["Partner"]),
                        "Dependents":str(row["Dependents"]),
                        "Multiple_Lines":str(row["Multiple_Lines"]),
                        "Internet_Service":str(row["Internet_Service"]),
                        "Online_Security":str(row["Online_Security"]),
                        "Online_Backup":str(row["Online_Backup"]),
                        "Device_Protection":str(row["Device_Protection"]),
                        "Tech_Support":str(row["Tech_Support"]),
                        "Streaming_TV":str(row["Streaming_TV"]),
                        "Streaming_Movies":str(row["Streaming_Movies"]),
                        "Contract":str(row["Contract"]),
                        "Paperless_Billing":str(row["Paperless_Billing"]),
                        "Payment_Method":str(row["Payment_Method"]),
                        "Churn_Label": rs.get_churn(),
                    }
                    customer_document = customer.document(str(index))
                    customer_document.set(customer_data)

                visuals = firestoreDB.collection(u'visuals').get()
                return render(request,'customers.html',{'visuals':[data.to_dict() for data in visuals]})
    # except Exception as e:
    #     print(str(e))
    #     visuals = firestoreDB.collection(u'visuals').get()
    #     return render(request,'customers.html',{'visuals':[data.to_dict() for data in visuals]})
        else:
            form = UploadFileForm()
        return render(
                request,
                'result.html')
        # context_instance=RequestContext(request)

def batch_list(request):
    current_id = request.GET.get('current_id')
    customer = firestoreDB.collection(u'visuals').document(current_id).collection(u'customer').get()
    return render(request,'batch_list.html',{'customer':[data.to_dict() for data in customer],"current_id":current_id})

def add_customer(request):
    current_id = request.GET.get('current_id')
    customerID = request.POST.get('customerID')
    Tenure = request.POST.get('Tenure')
    MonthlyCharges = request.POST.get('MonthlyCharges')
    TotalCharges = request.POST.get('TotalCharges')
    Senior_Citizen = request.POST.get('Senior_Citizen')
    Partner = request.POST.get('Partner')
    Dependents = request.POST.get('Dependents')
    Phone_Service = request.POST.get('Phone_Service')
    Multiple_Lines = request.POST.get('Multiple_Lines')
    Internet_Service = request.POST.get('Internet_Service')
    Online_Security = request.POST.get('Online_Security')
    Online_Backup = request.POST.get('Online_Backup')
    Device_Protection = request.POST.get('Device_Protection')
    Tech_Support = request.POST.get('Tech_Support')
    Streaming_TV = request.POST.get('Streaming_TV')
    Streaming_Movies = request.POST.get('Streaming_Movies')
    Contract = request.POST.get('Contract')
    Paperless_Billing = request.POST.get('Paperless_Billing')
    Payment_Method = request.POST.get('Payment_Method')

    rs.rule_set(customerID,int(Tenure),int(MonthlyCharges),int(TotalCharges),Senior_Citizen,
                    Partner,Dependents,Multiple_Lines,Internet_Service,Online_Security,
                    Online_Backup,Device_Protection,Tech_Support,Streaming_TV,Streaming_Movies,
                    Contract,Paperless_Billing,Payment_Method)
    print(current_id)
    visuals = firestoreDB.collection(u'visuals')
    get_visual = visuals.get()
    batch_size = 0
    for doc in get_visual:
        if(doc.id == current_id):
            batch_size = int(doc.to_dict()['batch_size'])
    # visuals.document(current_id).update({"batch_size":str(batch_size + 1)})
    
    data = {
        "ID":str(batch_size),
        "customerID":customerID,
        "Tenure":Tenure,
        "MonthlyCharges":MonthlyCharges,
        "TotalCharges":TotalCharges,
        "Senior_Citizen":Senior_Citizen,
        "Partner":Partner,
        "Dependents":Dependents,
        "Multiple_Lines":Multiple_Lines,
        "Internet_Service":Internet_Service,
        "Online_Security":Online_Security,
        "Online_Backup":Online_Backup,
        "Device_Protection":Device_Protection,
        "Tech_Support":Tech_Support,
        "Streaming_TV":Streaming_TV,
        "Streaming_Movies":Streaming_Movies,
        "Contract":Contract,
        "Paperless_Billing":Paperless_Billing,
        "Payment_Method":Payment_Method,
        "Churn_Label": rs.get_churn(),
    }

    
    visuals.document(current_id).collection('customer').document(str(batch_size)).set(data)

    return redirect('/batch_list/?current_id='+current_id)
def delete_user(request):
    uid = request.GET.get('uid')
    user_id = request.GET.get('user_id')
    auth.delete_user(uid)
    firestoreDB.collection(u'users').document(user_id).delete()
    try:
        users = firestoreDB.collection(u'users').get()
        return render(request,'manage_users.html',{'users':[data.to_dict() for data in users]})
    except:
        return render(request,'manage_users.html')

def edit_user(request):
    user_id = request.POST.get('selected_id')
    first_name = request.POST.get('first_name')
    last_name = request.POST.get('last_name')
    status = request.POST.get('status')
    updated_data = {
        "first_name": first_name,
        "last_name":last_name,
        'status':status
    }
    users = firestoreDB.collection(u'users').document(user_id)
    users.update(updated_data)
    try:
        users = firestoreDB.collection(u'users').get()
        return render(request,'manage_users.html',{'users':[data.to_dict() for data in users],"validation_success":"Successfully Edit User " + first_name + " " + last_name})
    except:
        return render(request,'manage_users.html')

def delete_batch(request):
    visual_id = request.GET.get('visual_id')
    visuals = firestoreDB.collection(u'visuals').get()
    for doc1 in visuals:
        customer = firestoreDB.collection(u'visuals').document(visual_id).collection('customer').get()
        for doc2 in customer:
            firestoreDB.collection(u'visuals').document(visual_id).collection('customer').document(doc2.id).delete()
        firestoreDB.collection(u'visuals').document(visual_id).delete()
    visuals = firestoreDB.collection(u'visuals').get()
    return render(request,'customers.html',{'visuals':[data.to_dict() for data in visuals]})

def delete_customer(request):
    current_id = request.GET.get('current_id')
    ID = request.GET.get('ID')
    firestoreDB.collection(u'visuals').document(current_id).collection('customer').document(ID).delete()
    return redirect('/batch_list/?current_id='+current_id)

def link_callback(uri, rel):
            """
            Convert HTML URIs to absolute system paths so xhtml2pdf can access those
            resources
            """
            result = finders.find(uri)
            if result:
                    if not isinstance(result, (list, tuple)):
                            result = [result]
                    result = list(os.path.realpath(path) for path in result)
                    path=result[0]
            else:
                    sUrl = settings.STATIC_URL        # Typically /static/
                    sRoot = settings.STATIC_ROOT      # Typically /home/userX/project_static/
                    mUrl = settings.MEDIA_URL         # Typically /media/
                    mRoot = settings.MEDIA_ROOT       # Typically /home/userX/project_static/media/

                    if uri.startswith(mUrl):
                            path = os.path.join(mRoot, uri.replace(mUrl, ""))
                    elif uri.startswith(sUrl):
                            path = os.path.join(sRoot, uri.replace(sUrl, ""))
                    else:
                            return uri

            # make sure that file exists
            if not os.path.isfile(path):
                    raise Exception(
                            'media URI must start with %s or %s' % (sUrl, mUrl)
                    )
            return path

def export_customer(request):
    current_id = request.GET.get('current_id')
    print(current_id)
    batch = firestoreDB.collection(u'visuals').document(current_id)
    customer = batch.collection('customer').get()

    template_path = 'upload_form/export_customer.html'
    context = {'customers': [data.to_dict() for data in customer]}
    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="output.pdf"'
    # find the template and render it.
    template = get_template(template_path)
    html = template.render(context)

    # create a pdf
    pisa_status = pisa.CreatePDF(
       html, dest=response, link_callback=link_callback)
    # if error then show some funy view
    if pisa_status.err:
       return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response

def total_churns(request):
    is_ajax = request.headers.get('X-Requested-With') == 'XMLHttpRequest'

    if is_ajax:
        if request.method == 'POST':
            data = json.load(request)
            current_id = data.get('batch_id')
            customers = firestoreDB.collection(u'visuals').document(current_id).collection('customer').get()
            total_churns = 0
            partner = 0
            dependents = 0
            senior_citizen = 0
            for doc in customers:
                if doc.to_dict()['Churn_Label'] == "Yes":
                    total_churns += 1
                if doc.to_dict()['Partner'] == "2":
                    partner += 1
                if doc.to_dict()['Dependents'] == "2":
                    dependents += 1
                if doc.to_dict()['Senior_Citizen'] == "2":
                    senior_citizen += 1
            return JsonResponse({'total_churns': total_churns,"partner":partner,"dependents":dependents,"senior_citizen":senior_citizen})
        return JsonResponse({'status': 'Invalid request'}, status=400)
    else:
        return HttpResponseBadRequest('Invalid request')
     
def get_services(request):
    is_ajax = request.headers.get('X-Requested-With') == 'XMLHttpRequest'

    if is_ajax:
        if request.method == 'POST':
            data = json.load(request)
            current_id = data.get('batch_id')
            customers = firestoreDB.collection(u'visuals').document(current_id).collection('customer')
            multiple_lines_no = customers.get()
            return JsonResponse({'multiple_lines': [doc.to_dict() for doc in multiple_lines_no]})
        return JsonResponse({'status': 'Invalid request'}, status=400)
    else:
        return HttpResponseBadRequest('Invalid request')