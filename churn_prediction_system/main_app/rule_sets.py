import this
from typing import Any
def rule_set(customer_id, Tenure, MonthlyCharges, TotalCharges, Senior_Citizen, Partner, Dependents, Multiple_Lines, 
    Internet_Service, Online_Security, Online_Backup, Device_Protection, Tech_Support, Streaming_TV, Streaming_Movies, Contract, Paperless_Billing, Payment_Method):
    global churn_label  
    if Contract == 3 and MonthlyCharges <=  92.4 and Senior_Citizen == 1:
        churn_label = 'No'
    elif Contract == 3 and Streaming_TV == 3 and Multiple_Lines == 1:
        churn_label = 'No'
    elif Contract ==  3 and Streaming_TV ==  3 and Multiple_Lines == 1:
        churn_label = 'No'
    elif Contract == 3 and Multiple_Lines == 3 and Streaming_TV == 1:
        churn_label = 'No'
    elif Contract == 3 and Streaming_TV == 3 and Multiple_Lines == 3 and Paperless_Billing == 1 and Dependents == 1:
        churn_label = 'No'
    elif Contract == 2 and Streaming_TV == 2:
        churn_label = 'No'
    elif Contract == 3 and Streaming_TV == 3 and Multiple_Lines == 3 and Streaming_Movies == 3 and Payment_Method == 2 and Online_Backup == 3:
        churn_label = 'No'
    elif Contract == 3 and Streaming_TV == 3 and Multiple_Lines == 3 and Streaming_Movies == 3 and Payment_Method == 2 and Online_Backup == 3:
        churn_label = 'No'
    elif Contract == 3 and Streaming_TV == 3 and Multiple_Lines == 3 and Streaming_Movies == 1:
        churn_label = 'No'
    elif Contract == 2 and Streaming_Movies == 1 and Payment_Method == 1:
        churn_label = 'No'
    elif Contract == 3 and Streaming_TV == 2:
        churn_label = 'No'
    elif Contract == 3 and Streaming_TV == 2:
        churn_label = "No"
    elif Contract == 2 and Streaming_Movies == 1 and Payment_Method == 2 and Internet_Service == 2:
        churn_label = "No"
    elif Contract == 2 and Internet_Service == 1 and Online_Security == 3 and Senior_Citizen == 1 and Device_Protection == 1:
        churn_label = "No"
    elif Tenure > 17 and Internet_Service == 3:
        churn_label = "No"
    elif Contract == 3 and Multiple_Lines == 3 and Payment_Method == 3 and Senior_Citizen == 1 and Partner == 2:
        churn_label = "No"
    elif Contract == 3 and Multiple_Lines == 3 and Payment_Method == 1 and Online_Security == 3 and Tenure > 59:
        churn_label = "No"
    elif Contract == 2 and Internet_Service == 1 and Paperless_Billing == 1 and Online_Security == 1 and Payment_Method == 2:
        churn_label = "No"
    elif Contract == 2 and Streaming_TV == 1 and Device_Protection == 3 and Senior_Citizen == 1 and Online_Backup == 1 and Paperless_Billing == 1:
        churn_label = "No"
    elif Contract == 2 and Internet_Service == 1 and Streaming_Movies == 1 and Dependents == 2 and Online_Security == 3: 
        churn_label = 'No'
    elif Contract == 2 and Streaming_TV == 1 and Partner == 1 and Internet_Service == 2:
        churn_label = 'No'
    elif Contract == 2 and Internet_Service == 1 and Device_Protection == 3 and Payment_Method == 1 and Online_Backup == 1:
        churn_label = 'No'
    elif Contract == 3 and Multiple_Lines == 2:
        churn_label = 'No'
    elif Tenure > 17 and Internet_Service == 1 and Senior_Citizen == 1 and Multiple_Lines == 1 and Contract == 1 and Tech_Support == 3 and Payment_Method == 4:
        churn_label = 'No'
    elif Tenure > 5 and Internet_Service == 3 and Senior_Citizen == 1 and Payment_Method == 4 and Partner == 1:
        churn_label = 'No'
    elif Tenure > 17 and Internet_Service == 1 and Senior_Citizen == 1 and Multiple_Lines == 3 and Payment_Method == 4:
        churn_label = "No"
    elif Contract == 2 and Internet_Service == 1 and Payment_Method == 3 and Multiple_Lines == 1:
        churn_label = "No"
    elif Tenure > 17 and Internet_Service == 1 and Senior_Citizen == 1 and Multiple_Lines == 1 and Contract == 1 and Payment_Method == 1 and Online_Security == 1:
        churn_label = "No"
    elif Contract == 2 and Streaming_Movies == 1 and Payment_Method == 4:
        churn_label = "No"
    elif Tenure > 17 and Internet_Service == 1 and Senior_Citizen == 1 and Tech_Support == 3 and Multiple_Lines == 2 and Device_Protection == 3 and Partner == 1:
        churn_label = "No"
    elif Tenure > 17 and Internet_Service == 1 and Multiple_Lines == 3 and Online_Backup == 3 and Streaming_TV == 3 and Senior_Citizen == 1:
        churn_label = "No"
    elif Tenure > 177 and Internet_Service == 1 and Senior_Citizen == 1 and Paperless_Billing == 1 and Payment_Method == 4:
        churn_label = "No"
    elif Tenure > 22 and Internet_Service == 1 and Senior_Citizen == 1 and Multiple_Lines == 1 and Contract == 1 and Payment_Method == 2:
        churn_label = "No"
    elif Tenure > 25 and Internet_Service == 1 and Streaming_TV == 1 and Payment_Method == 3 and Paperless_Billing == 1:
        churn_label = "No"
    elif Contract == 3 and Multiple_Lines == 1:
        churn_label = "No"
    elif Contract == 2 and Payment_Method == 2 and Multiple_Lines == 2:
        churn_label = "No"
    elif Online_Security == 2 and Tenure > 1 and Senior_Citizen == 1 and Payment_Method == 2 and Multiple_Lines == 1:
        churn_label = "No"
    elif Contract == 2 and Dependents == 2 and Tenure <= 68 and Senior_Citizen ==1 and Device_Protection == 3 and Streaming_Movies == 3 and Online_Backup == 3 and Tenure <= 64:
        churn_label = "No"
    elif Tenure > 17 and Tenure > 50 and Streaming_TV == 1 and Tech_Support == 3 and Paperless_Billing == 1:
        churn_label = "No"
    elif Tenure > 17 and Tenure > 49 and Payment_Method == 4:
        churn_label = "No"
    elif Online_Security == 2 and Tenure > 1 and Payment_Method == 4:
        churn_label = "No"
    elif Tenure > 10 and Internet_Service == 1 and Dependents == 2 and Senior_Citizen == 2:
        churn_label = "No"  
    elif Tenure > 10 and Internet_Service == 1 and Dependents == 2 and Senior_Citizen == 2:
        churn_label = "No"
    elif Tenure > 10 and Internet_Service == 1 and Dependents == 2 and Contract == 1 and Payment_Method == 1 and Multiple_Lines == 1:
        churn_label = "No"
    if Tenure > 16 and Internet_Service == 1 and Senior_Citizen == 1 and Contract == 1 and Payment_Method == 4 and Multiple_Lines == 1 and Paperless_Billing == 2 and Dependents == 1:
        churn_label = "No"
    elif Tenure > 16 and Internet_Service == 1 and Senior_Citizen == 1 and Online_Backup == 1 and Tenure <= 55 and Dependents == 2 and Paperless_Billing == 2 and Streaming_Movies == 1:
        churn_label = "No"
    elif Tenure > 17 and Tenure > 50 and Streaming_Movies == 1 and Payment_Method == 1 and Streaming_Movies == 1:
        churn_label = "No"
    elif Tenure > 6 and Internet_Service == 3 and Dependents == 2:
        churn_label = "No"
    elif Tenure > 16 and Tenure > 55 and Online_Security == 3 and Contract == 1 and Dependents == 1 and Streaming_TV == 3 and Streaming_Movies == 3:
        churn_label = "No"
    elif Contract == 3 and Online_Security == 1 and Payment_Method == 3 and Senior_Citizen == 2:
        churn_label = "No"
    elif Contract == 2 and Payment_Method == 1 and Senior_Citizen == 2:
        churn_label = "No"
    elif Tenure > 16 and Internet_Service == 1 and Multiple_Lines == 3 and Senior_Citizen == 2:
        churn_label = "No"
    elif Tenure > 6 and Internet_Service == 1 and Senior_Citizen == 1 and Online_Backup == 3 and Contract == 1 and Payment_Method == 1 and Tech_Support == 3:
        churn_label = "No"
    elif Contract == 2 and Tenure > 70 and TotalCharges <= 8046.85:
        churn_label = "No"
    elif Tenure > 6 and Internet_Service == 1 and Senior_Citizen == 1 and Multiple_Lines == 1 and Streaming_TV == 3 and Dependents == 1 and Partner == 1 and Device_Protection == 3:
        churn_label = "No"
    elif Tenure <= 5 and MonthlyCharges > 65.65 and Online_Security == 1 and Internet_Service == 2 and Tenure <= 1 and Tech_Support == 1 and Payment_Method == 3 and Device_Protection == 1 and Online_Backup == 1 and Dependents == 1:
        churn_label = "Yes"
    elif Contract == 3 and Online_Security == 1 and Senior_Citizen == 1 and Payment_Method == 1 and Paperless_Billing == 2 and Online_Backup == 3 and Dependents == 1:
        churn_label = "No"
    elif Tenure > 16 and Tech_Support == 3 and Streaming_TV == 1 and Senior_Citizen == 1 and Payment_Method == 1 and Dependents == 1:
        churn_label = "No"
    elif Contract == 2 and Payment_Method == 2 and Senior_Citizen == 1 and Tech_Support == 1 and Multiple_Lines == 1 and Streaming_TV == 3:
        churn_label = "No"
    elif Online_Security == 2 and Senior_Citizen == 1 and Payment_Method == 3 and Multiple_Lines == 1 and Dependents == 1:
        churn_label = "No"
    elif Tenure > 16 and Tech_Support == 3 and Dependents == 2 and Tenure > 50:
        churn_label = "No"
    elif Online_Security == 3 and Streaming_TV == 1 and Dependents == 2 and Senior_Citizen == 1 and Streaming_Movies == 3 and Tenure <= 55:
        churn_label = "No"
    elif Online_Security == 2 and Senior_Citizen == 1 and Paperless_Billing == 1 and Payment_Method  == 2:
        churn_label = "No"
    elif Tenure > 16 and Internet_Service == 1 and Senior_Citizen == 1 and Multiple_Lines == 3 and Online_Security == 1 and Paperless_Billing == 2 and Payment_Method == 2:
        churn_label = "No"
    elif Tenure > 16 and Internet_Service == 1 and Senior_Citizen == 1 and Tech_Support == 1 and Multiple_Lines == 3 and Online_Security == 1 and Tenure <= 40:
        churn_label = "No"
    elif Tenure <= 5 and Internet_Service == 2 and Online_Security == 1 and Multiple_Lines == 3 and Dependents == 1 and Payment_Method == 3 and Paperless_Billing == 2 and Streaming_Movies == 3:
        churn_label = "Yes"
    elif Online_Security == 3 and Paperless_Billing == 1 and Online_Backup == 3 and Contract == 1 and Device_Protection == 1:
        churn_label = "No"
    elif Tenure > 17 and Online_Security == 3 and Streaming_TV == 1 and Tech_Support == 3 and Internet_Service == 2:
        churn_label = "No"
    elif Contract == 2 and Online_Backup == 1 and Payment_Method == 1 and Internet_Service == 2 and Streaming_TV == 3 and Paperless_Billing == 1:
        churn_label = "No"
    elif Contract == 2 and Dependents == 1 and Online_Backup == 1 and Device_Protection == 1 and Multiple_Lines == 1:
        churn_label = "No"
    else:
        churn_label = 'Yes'
    

def get_churn():
    return churn_label
