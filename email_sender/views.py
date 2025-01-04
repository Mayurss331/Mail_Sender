# I have created this file - Dhaneshwar
from django.http import HttpResponse
from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
import pandas as pd
from emails import*

def send_email_to_candidate(data,email_type,role,subject,link,date,time):

    # Check if required columns are present
    required_columns = ['First Name', 'Last Name', 'Email']
    missing_columns = [col for col in required_columns if col not in data.columns]
    if missing_columns:
        return f"Missing columns in CSV: {missing_columns}"
    else:
        # Fetch the required data
        extracted_data = data[required_columns].dropna()
        records = extracted_data.to_dict('records')
        for record in records:
                name = record['First Name']+" "+record['Last Name']
                email = record['Email']

                if email_type == 'send_aptitude_assessment_mail':
                     
                     send_aptitude_assessment_mail(email,role,subject,link,date,time,name)

                elif email_type == 'send_aptitude_assessment_reminder_mail':

                     send_aptitude_assessment_reminder_mail(email,role,subject,link,date,time,name)

                elif email_type == 'send_aptitude_assessment_feedback_mail':

                     send_aptitude_assessment_feedback_mail(email,role,subject,link,date,time,name)

                elif email_type == 'send_GD1_mail':
                     
                     send_GD1_mail(email,role,subject,link,date,time,name)

                elif email_type == 'send_GD1_reminder_mail':

                     send_GD1_reminder_mail(email,role,subject,link,date,time,name)

                elif email_type == 'send_GD2_mail':

                     send_GD2_mail(email,role,subject,link,date,time,name)

                elif email_type == 'send_GD2_reminder_mail':

                     send_GD2_reminder_mail(email,role,subject,link,date,time,name)

                elif email_type == 'send_technical_assessment_register_mail':

                     send_technical_assessment_register_mail(email,role,subject,link,date,time,name)

                elif email_type == 'send_technical_assessment_mail':

                     send_technical_assessment_mail(email,role,subject,link,date,time,name)

                elif email_type == 'send_process_feedback_mail':

                     send_process_feedback_mail(email,role,subject,link,date,time,name)

                elif email_type == 'send_selection_mail':

                     send_selection_mail(email,role,subject,link,date,time,name)


        return f"Email sent to <br><br> {name}"

def index(request):
    if request.method == "POST":
        uploaded_file = request.FILES.get('fileUpload', None) #Get File
        submit_value = request.POST.get("action") # Get Button value
        email_type = request.POST.get("email_type") # Get the selected mail type dropdown value
        role = request.POST.get("role") # Get the selected role dropdown value
        subject = request.POST.get("subject") # Get the subject
        link = request.POST.get("link") # Get the link
        time = request.POST.get("time") # Get the time
        date = request.POST.get("date") # Get the date
        
        if submit_value == 'test':
            data = pd.read_csv("company.csv")
            response = send_email_to_candidate(data,email_type,role,subject,link,date,time)
            return HttpResponse(response)
        
        elif submit_value == 'send' and uploaded_file:
            data = pd.read_csv(uploaded_file)
            response = send_email_to_candidate(data,email_type,role,subject,link,date,time)
            return HttpResponse(response)  # Just an example, can redirect or display message
        else:
             return HttpResponse('''<div style="display: flex; justify-content: center; align-items: center; height: 100vh; background-color: #f8f8f8; color: white; font-family: Arial, sans-serif; font-weight: bold; text-align: center;"><div style="background-color: red; padding: 15px 20px; border-radius: 10px; box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);">Please Upload File</div></div>
''')

    return render(request, 'index.html')  # If not POST, just show the form

def about(request):
    return render(request,'about.html')