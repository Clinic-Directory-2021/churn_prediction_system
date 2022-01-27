import this
from typing import Any
def rule_set(customer_id, Tenure, MonthlyCharges, TotalCharges, Senior_Citizen, Partner, Dependents, Multiple_Lines, 
    Internet_Service, Online_Security, Online_Backup, Device_Protection, Tech_Support, Streaming_TV, Streaming_Movies, Contract, Paperless_Billing, Payment_Method):
    global churn_label  
    if Contract == 3 and MonthlyCharges <=  '92.4' and Senior_Citizen == 1:
        churn_label = 'Yes'
    elif Contract == 3 and Streaming_TV == 3 and Multiple_Lines == 1:
        churn_label = 'Yes'
    elif Contract ==  3 and Streaming_TV ==  3 and Multiple_Lines == 1:
        churn_label = 'Yes'
    elif Contract == 3 and Multiple_Lines == 3 and Streaming_TV == 1:
        churn_label = 'Yes'
    elif Contract == 3 and Streaming_TV == 3 and Multiple_Lines == 3 and Paperless_Billing == 1 and Dependents == 1:
        churn_label = 'Yes'
    elif Contract == 2 and Streaming_TV == 2:
        churn_label = 'Yes'
    elif Contract == 3 and Streaming_TV == 3 and Multiple_Lines == 3 and Streaming_Movies == 3 and Payment_Method == 2 and Online_Backup == 3:
        churn_label = 'Yes'
    elif Contract == 3 and Streaming_TV == 3 and Multiple_Lines == 3 and Streaming_Movies == 3 and Payment_Method == 2 and Online_Backup == 3:
        churn_label = 'Yes'
    elif Contract == 3 and Streaming_TV == 3 and Multiple_Lines == 3 and Streaming_Movies == 1:
        churn_label = 'Yes'
    elif Contract == 2 and Streaming_Movies == 1 and Payment_Method == 1:
        churn_label = 'Yes'
    elif Contract == 3 and Streaming_TV == 2:
        churn_label = 'Yes'
    else:
        churn_label = 'No'
    

def get_churn():
    return churn_label
