import pandas as pd
from mail import*


def Loader(btn,path,sub,link,date,time):
    # Load the CSV file
    file_path = path  # Replace with the path to your CSV file
    # data = pd.read_excel(file_path)
    data = pd.read_csv(file_path)

    # Check if required columns are present
    required_columns = ['First Name', 'Last Name', 'Email']
    missing_columns = [col for col in required_columns if col not in data.columns]

    if missing_columns:
        print(f"Missing columns in CSV: {missing_columns}")
    else:
        # Fetch the required data
        extracted_data = data[required_columns].dropna()  # Drop rows with missing values

        # print("Extracted Data:")
        # print(extracted_data)
        # Convert to list of dictionaries (optional)
        records = extracted_data.to_dict('records')
        choice = input("You want to send emails to candidate? yes/no : ").lower()
        if choice=="yes":
            # print("\nExtracted Records:")
            for record in records:
                name = record['First Name']+" "+record['Last Name']
                email = record['Email']
                # print(name,email)
                if btn==1:
                    send_assessment_mail(email,sub,link,date,time,name)
                elif btn==2:
                    send_GD1_mail(email,sub,link,date,time,name)
                elif btn==3:
                    send_GD2_mail(email,sub,link,date,time,name)
                elif btn==4:
                    send_feedback(email,sub,link,date,time,name)
                elif btn==5:
                    send_technical_mail(email,sub,link,date,time,name)
        else:
            print('Ok')


