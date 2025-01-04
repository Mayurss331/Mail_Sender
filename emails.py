# mail.py
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from random import*
from email.mime.application import MIMEApplication



def start_session(message):
            # Create SMTP session
    session = smtplib.SMTP("smtp.titan.email", 587)
    session.starttls()  # Upgrade to secure connection

    # Login to Gmail account
    session.login("info.elementis@onlyformachinelearning.in", "@gendu_generation_2024")  # Avoid storing passwords in plaintext

    # Send the email
    session.sendmail(message["From"], message["To"], message.as_string())
    session.quit()  # Cleanly close the SMTP session

    return

# Function to send a assessment emails
def send_aptitude_assessment_mail(to,role='',sub='',link='',date='',time='',name="Candidate"):

    try:
        # Create a multi-part message to include both plain text and HTML content
        message = MIMEMultipart("alternative")
        assessment_link = link
        logo = "https://buikzohejfkxouarmyni.supabase.co/storage/v1/object/sign/assets/Elementis-01.png?token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1cmwiOiJhc3NldHMvRWxlbWVudGlzLTAxLnBuZyIsImlhdCI6MTczNTg4NzkxMiwiZXhwIjoyMTY3ODg3OTEyfQ.JonG5NOKKZkLZWT6Fmf5VusAUgFIQaNvY4t4l3KCfmY&t=2025-01-03T07%3A05%3A12.250Z"
        
        # Email subject and sender information
        message["Subject"] = sub
        message["From"] = "info.elementis@onlyformachinelearning.in"
        message["To"] = to

        # PDF Attachment
        with open(r"CompanyProfile.pdf", 'rb') as f:
            pdf_attachment = MIMEApplication(f.read(), _subtype='pdf')
            pdf_attachment.add_header('Content-Disposition', 'attachment', filename='CompanyProfile.pdf')
            message.attach(pdf_attachment)

        # HTML content styled for design
        html_content = f"""
        <html>
        <head>
            <style>
                body {{
                    font-family: Arial, sans-serif;
                    background-color: #f9f9f9;
                    margin: 0;
                    padding: 0;
                }}
                .email-container {{
                    max-width: 600px;
                    margin: 20px auto;
                    background: #ffffff;
                    padding: 20px;
                    border: 4px solid #18def3;
                    border-radius: 10px;
                }}
                .header-logo {{
                    text-align: center;
                    margin-bottom: 20px;
                }}
                .instructions {{
                    font-size: 14px;
                    text-align: left;
                    margin-bottom: 20px;
                    line-height: 1.6;
                }}
                .content {{
                    font-size: 14px;
                    text-align: left;
                    margin-bottom: 20px;
                    line-height: 1.6;
                }}
                .action-button{{
                    display: inline-block;
                    background-color: #004aad;
                    color: white;
                    font-weight: bold;
                    text-decoration: none;
                    padding: 12px 20px;
                    font-size: 16px;
                    border-radius: 5px;
                    text-align: center;
                    margin: 20px auto;
                    cursor: pointer;
                    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.2);
                    transition: background-color 0.3s ease, transform 0.2s ease;
                }}
                .action-button:hover{{
                    background-color: #003580;
                    color: white;
                    transform: scale(1.05);
                }}
                .fallback-link {{
                    font-size: 14px;
                    margin-top: 20px;
                    text-align: center;
                    word-wrap: break-word;
                }}
                .footer {{
                    font-size: 12px;
                    color: #888;
                    text-align: center;
                    margin-top: 20px;
                }}
            </style>
        </head>
        <body>
            <div class="email-container">
                <div class="header-logo">
                    <img src={logo} width="250">
                </div>
                <h2 style="text-align: center;">Elementis SoftTech || {role}</h2>
                <p class="instructions">
                    Hii {name},<br><br>
                    Thank you for your interest in joining our team. Please read the following instructions carefully before starting your assessment:<br>
                    - Test Content: 20 questions of Aptitude.<br>
                    - Time: 30 minutes to complete the 20 questions.<br>
                    - The link will be <b>Open From {date} {time}</b>.
                    <br><br>
                    A couple of things to keep in mind while taking the assessment:<br>
                    1. Ensure you have a stable internet connection.<br>
                    2. Use a desktop or laptop to take the test.<br>
                    3. Find a quiet place where you won't be interrupted.<br>
                </p>
                <div style="text-align: center;height:60px;justify-content: center;">
                    <a href="{assessment_link}" class="action-button" style="color:white;">Start Assessment</a>
                </div>
                <p class="fallback-link">If the button above doesn't work, use the following link: </p> <br> 
                <a href="{assessment_link}">{assessment_link}</a>
                <p class="content">
                    If you have any query write an email to : support@elementissofttech.com 
                </p>
                <div class="footer">
                    Best regards,<br>
                    Team Elementis SoftTech
                </div>
            </div>
        </body>
        </html>
        """

        content = MIMEText(html_content, "html")
        message.attach(content)

        start_session(message)

        print("Email Sent to -",name)


    except Exception as e:
        print(f"Error sending email: {e}")  # Provide more detailed error information

    return

# Function to send a aptitude assessment reminder emails
def send_aptitude_assessment_reminder_mail(to,role='',sub='',link='',date='',time='',name="Candidate"):

    try:
        # Create a multi-part message to include both plain text and HTML content
        message = MIMEMultipart("alternative")
        assessment_link = link
        logo = "https://buikzohejfkxouarmyni.supabase.co/storage/v1/object/sign/assets/Elementis-01.png?token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1cmwiOiJhc3NldHMvRWxlbWVudGlzLTAxLnBuZyIsImlhdCI6MTczNTg4NzkxMiwiZXhwIjoyMTY3ODg3OTEyfQ.JonG5NOKKZkLZWT6Fmf5VusAUgFIQaNvY4t4l3KCfmY&t=2025-01-03T07%3A05%3A12.250Z"
        
        # Email subject and sender information
        message["Subject"] = sub
        message["From"] = "info.elementis@onlyformachinelearning.in"
        message["To"] = to

        # HTML content styled for design
        html_content = f"""
        <html>
        <head>
            <style>
                body {{
                    font-family: Arial, sans-serif;
                    background-color: #f9f9f9;
                    margin: 0;
                    padding: 0;
                }}
                .email-container {{
                    max-width: 600px;
                    margin: 20px auto;
                    background: #ffffff;
                    padding: 20px;
                    border: 4px solid #18def3;
                    border-radius: 10px;
                }}
                .header-logo {{
                    text-align: center;
                    margin-bottom: 20px;
                }}
                .instructions {{
                    font-size: 14px;
                    text-align: left;
                    margin-bottom: 20px;
                    line-height: 1.6;
                }}
                .reminder {{
                    font-size: 16px;
                    font-weight: bold;
                    margin-bottom: 20px;
                }}
                .content {{
                    font-size: 14px;
                    text-align: left;
                    margin-bottom: 20px;
                    line-height: 1.6;
                }}
                .action-button{{
                    display: inline-block;
                    background-color: #004aad;
                    color: white;
                    font-weight: bold;
                    text-decoration: none;
                    padding: 12px 20px;
                    font-size: 16px;
                    border-radius: 5px;
                    text-align: center;
                    margin: 20px auto;
                    cursor: pointer;
                    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.2);
                    transition: background-color 0.3s ease, transform 0.2s ease;
                }}
                .action-button:hover{{
                    background-color: #003580;
                    color: white;
                    transform: scale(1.05);
                }}
                .fallback-link {{
                    font-size: 14px;
                    margin-top: 20px;
                    text-align: center;
                    word-wrap: break-word;
                }}
                .footer {{
                    font-size: 12px;
                    color: #888;
                    text-align: center;
                    margin-top: 20px;
                }}
            </style>
        </head>
        <body>
            <div class="email-container">
                <div class="header-logo">
                    <img src={logo} width="250">
                </div>
                <h2 style="text-align: center;">Elementis SoftTech || {role}</h2>
                <p class="instructions">
                    Hi {name},<br><br>
                    This is a friendly reminder to complete the Elementis SoftTech Aptitude Assessment as part of the application process. Below are the details for your reference:<br><br>
                    <b>Test Content:</b> 20 questions (Aptitude).<br>
                    <b>Time Limit:</b> 30 minutes.<br>
                    <b>Availability:</b> The assessment link is open on <Br> 
                    <b>Date:{date}</b>.<br>
                    <b>Time:{time}</b>.<br><br>
                    To successfully complete the test, please keep the following in mind:<br>
                    1. Ensure you have a stable internet connection.<br>
                    2. Use a desktop or laptop for the best experience.<br>
                    3. Find a quiet place where you won't be interrupted.<br><br>
                </p>
                <div style="text-align: center;height:60px;justify-content: center;">
                    <a href="{assessment_link}" class="action-button" style="color:white;">Start Assessment</a>
                </div>
                <p class="fallback-link">If the button above doesn't work, use the following link: </p> <br> 
                <a href="{assessment_link}">{assessment_link}</a>
                <p class="content">
                    If you have any query write an email to : support@elementissofttech.com 
                </p>
                <div class="footer">
                    Best regards,<br>
                    Team Elementis SoftTech
                </div>
            </div>
        </body>
        </html>
        """


        content = MIMEText(html_content, "html")
        message.attach(content)

        start_session(message)

        print("Email Sent to -",name)


    except Exception as e:
        print(f"Error sending email: {e}")  # Provide more detailed error information
        
    return

# Function for sending aptitude assessment feedback mail
def send_aptitude_assessment_feedback_mail(to,role='',sub='',link='',date='',time='',name="Candidate"):
    try:
        # Create a multi-part message to include both plain text and HTML content
        message = MIMEMultipart("alternative")
        feedback_link = link
        logo = "https://buikzohejfkxouarmyni.supabase.co/storage/v1/object/sign/assets/Elementis-01.png?token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1cmwiOiJhc3NldHMvRWxlbWVudGlzLTAxLnBuZyIsImlhdCI6MTczNTg4NzkxMiwiZXhwIjoyMTY3ODg3OTEyfQ.JonG5NOKKZkLZWT6Fmf5VusAUgFIQaNvY4t4l3KCfmY&t=2025-01-03T07%3A05%3A12.250Z"
        
        # Email subject and sender information
        message["Subject"] = sub
        message["From"] = "info.elementis@onlyformachinelearning.in"
        message["To"] = to

        # HTML content styled for design
        html_content = f"""
        <html>
        <head>
            <style>
                body {{
                    font-family: Arial, sans-serif;
                    background-color: #f9f9f9;
                    margin: 0;
                    padding: 0;
                }}
                .email-container {{
                    max-width: 600px;
                    margin: 20px auto;
                    background: #ffffff;
                    padding: 20px;
                    border: 4px solid #18def3;
                    border-radius: 10px;
                }}
                .header-logo {{
                    text-align: center;
                    margin-bottom: 20px;
                }}
                .content {{
                    font-size: 14px;
                    text-align: left;
                    margin-bottom: 20px;
                    line-height: 1.6;
                }}
                .action-button{{
                    display: inline-block;
                    background-color: #004aad;
                    color: white;
                    font-weight: bold;
                    text-decoration: none;
                    padding: 12px 20px;
                    font-size: 16px;
                    border-radius: 5px;
                    text-align: center;
                    margin: 20px auto;
                    cursor: pointer;
                    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.2);
                    transition: background-color 0.3s ease, transform 0.2s ease;
                }}
                .action-button:hover{{
                    background-color: #003580;
                    color: white;
                    transform: scale(1.05);
                }}
                .fallback-link {{
                    font-size: 14px;
                    margin-top: 20px;
                    text-align: center;
                    word-wrap: break-word;
                }}
                .footer {{
                    font-size: 12px;
                    color: #888;
                    text-align: center;
                    margin-top: 20px;
                }}
            </style>
        </head>
        <body>
            <div class="email-container">
                <div class="header-logo">
                    <img src={logo} width="250">
                </div>
                <h2 style="text-align: center;">Elementis SoftTech || {role} </h2>
                <p class="instructions">
                    Hi {name},<br><br>
                    Thank you for successfully submitting your assessment. We appreciate your effort and time in completing it.
                    <br>
                    <br>
                    <b>If you encountered any issues during the submission process or have any feedback to share, please let us know by filling out the form linked below. Your input is invaluable in helping us improve our processes.<br><br>
                    <br>
                    <br>
                    <b>If you encountered any issues we will reschedule the Test for you.You need to fill the form.</b>
                </p>
                <div style="text-align: center;height:60px;justify-content: center;">
                    <a href="{feedback_link}" class="action-button" style="color:white;">Raise Issue</a>
                </div>
                <p class="fallback-link">If the button above doesn't work, use the following link: </p> <br> 
                <a href="{feedback_link}">{feedback_link}</a>
                <p class="content">
                    If you have any query write an email to : support@elementissofttech.com 
                </p>
                <div class="footer">
                    Best regards,<br>
                    Team Elementis SoftTech
                </div>
            </div>
        </body>
        </html>
        """


        content = MIMEText(html_content, "html")
        message.attach(content)

        start_session(message)

        print("Email Sent to -",name)


    except Exception as e:
        print(f"Error sending email: {e}")  # Provide more detailed error information

    return

# Function for sending  GD-1 mail
def send_GD1_mail(to,role='',sub='',link='',date='',time='',name="Candidate"):
    try:
        # Create a multi-part message to include both plain text and HTML content
        message = MIMEMultipart("alternative")
        gd1_link = link
        logo = "https://buikzohejfkxouarmyni.supabase.co/storage/v1/object/sign/assets/Elementis-01.png?token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1cmwiOiJhc3NldHMvRWxlbWVudGlzLTAxLnBuZyIsImlhdCI6MTczNTg4NzkxMiwiZXhwIjoyMTY3ODg3OTEyfQ.JonG5NOKKZkLZWT6Fmf5VusAUgFIQaNvY4t4l3KCfmY&t=2025-01-03T07%3A05%3A12.250Z"
        
        # Email subject and sender information
        message["Subject"] = sub
        message["From"] = "info.elementis@onlyformachinelearning.in"
        message["To"] = to

        # HTML content styled for design
        html_content = f"""
        <html>
        <head>
            <style>
                body {{
                    font-family: Arial, sans-serif;
                    background-color: #f9f9f9;
                    margin: 0;
                    padding: 0;
                }}
                .email-container {{
                    max-width: 600px;
                    margin: 20px auto;
                    background: #ffffff;
                    padding: 20px;
                    border: 4px solid #18def3;
                    border-radius: 10px;
                }}
                .header-logo {{
                    text-align: center;
                    margin-bottom: 20px;
                }}
                .instructions {{
                    font-size: 14px;
                    text-align: left;
                    margin-bottom: 20px;
                    line-height: 1.6;
                }}
                .content {{
                    font-size: 14px;
                    text-align: left;
                    margin-bottom: 20px;
                    line-height: 1.6;
                }}
                .action-button{{
                    display: inline-block;
                    background-color: #004aad;
                    color: white;
                    font-weight: bold;
                    text-decoration: none;
                    padding: 12px 20px;
                    font-size: 16px;
                    border-radius: 5px;
                    text-align: center;
                    margin: 20px auto;
                    cursor: pointer;
                    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.2);
                    transition: background-color 0.3s ease, transform 0.2s ease;
                }}
                .action-button:hover{{
                    background-color: #003580;
                    color: white;
                    transform: scale(1.05);
                }}
                .fallback-link {{
                    font-size: 14px;
                    margin-top: 20px;
                    text-align: center;
                    word-wrap: break-word;
                }}
                .footer {{
                    font-size: 12px;
                    color: #888;
                    text-align: center;
                    margin-top: 20px;
                }}
            </style>
        </head>
        <body>
            <div class="email-container">
                <div class="header-logo">
                    <img src={logo} width="250">
                </div>
                <h2 style="text-align: center;">Elementis SoftTech || {role}</h2>
                <p class="instructions">
                    Dear {name},<br><br>
                    Congratulations! We are pleased to inform you that you have been shortlisted from Aptitude round for the next stage of our joining process.
                    <br><br>
                    Your performance in the Aptitude was impressive, and we are excited to move forward with your application. The next step will be a Group Discussion(GD-1) , which will assess your Communication skills.<br>
                    <br>
                    Here are the details for the Group Discussion:<br>
                    <b>Date: {date}<br>
                    Time: {time}<br>
                    Venue: Google Meet
                    </b>
                    <br><br>
                    <b>
                    We look forward to your participation in this round of the selection process.
                    <br>
                </p>
                <div style="text-align: center;height:60px;justify-content: center;">
                    <a href="{gd1_link}" style:"color:white;" class="action-button">Join Meet</a>
                </div>
                <p class="fallback-link">If the button above doesn't work, use the following link: </p> <br> 
                <a href="{gd1_link}">{gd1_link}</a>
                <p class="content">
                    If you have any query write an email to : support@elementissofttech.com 
                </p>
                <div class="footer">
                    Best regards,<br>
                    Team Elementis SoftTech
                </div>
            </div>
        </body>
        </html>
        """


        content = MIMEText(html_content, "html")
        message.attach(content)

        start_session(message)

        print("Email Sent to -",name)


    except Exception as e:
        print(f"Error sending email: {e}")  # Provide more detailed error information
        
    return

# Function to send a GD1 reminder email
def send_GD1_reminder_mail(to,role='',sub='',link='',date='',time='',name="Candidate"):
    try:
        # Create a multi-part message to include both plain text and HTML content
        message = MIMEMultipart("alternative")
        gd1_link = link 
        logo = "https://buikzohejfkxouarmyni.supabase.co/storage/v1/object/sign/assets/Elementis-01.png?token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1cmwiOiJhc3NldHMvRWxlbWVudGlzLTAxLnBuZyIsImlhdCI6MTczNTg4NzkxMiwiZXhwIjoyMTY3ODg3OTEyfQ.JonG5NOKKZkLZWT6Fmf5VusAUgFIQaNvY4t4l3KCfmY&t=2025-01-03T07%3A05%3A12.250Z"  # Update with the correct logo URL
        
        # Email subject and sender information
        message["Subject"] = sub
        message["From"] = "info.elementis@onlyformachinelearning.in"
        message["To"] = to

        # HTML content styled for design
        html_content = f"""
        <html>
        <head>
            <style>
                body {{
                    font-family: Arial, sans-serif;
                    background-color: #f9f9f9;
                    margin: 0;
                    padding: 0;
                }}
                .email-container {{
                    max-width: 600px;
                    margin: 20px auto;
                    background: #ffffff;
                    padding: 20px;
                    border: 4px solid #18def3;
                    border-radius: 10px;
                }}
                .header-logo {{
                    text-align: center;
                    margin-bottom: 20px;
                }}
                .instructions {{
                    font-size: 14px;
                    text-align: left;
                    margin-bottom: 20px;
                    line-height: 1.6;
                }}
                .reminder {{
                    font-size: 16px;
                    font-weight: bold;
                    margin-bottom: 20px;
                }}
                .content {{
                    font-size: 14px;
                    text-align: left;
                    margin-bottom: 20px;
                    line-height: 1.6;
                }}
                .action-button {{
                    display: inline-block;
                    background-color: #004aad;
                    color: white; /* Ensures the text is white */
                    font-weight: bold;
                    text-decoration: none;
                    padding: 12px 20px;
                    font-size: 16px;
                    border-radius: 5px;
                    text-align: center;
                    margin: 20px auto;
                    cursor: pointer; /* Makes it look clickable */
                    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.2); /* Adds a subtle shadow */
                    transition: background-color 0.3s ease, transform 0.2s ease; /* Smooth hover effect */
                }}
                .action-button:hover {{
                    background-color: #003580; /* Darker blue on hover */
                    color: white; /* Ensures the text stays white on hover */
                    transform: scale(1.05); /* Slight zoom effect */
                }}
                .fallback-link {{
                    font-size: 14px;
                    margin-top: 20px;
                    text-align: center;
                    word-wrap: break-word;
                }}
                .footer {{
                    font-size: 12px;
                    color: #888;
                    text-align: center;
                    margin-top: 20px;
                }}
            </style>
        </head>
        <body>
            <div class="email-container">
                <div class="header-logo">
                    <img src="{logo}" width="250" alt="Elementis SoftTech Logo">
                </div>
                <h2 style="text-align: center;">Elementis SoftTech || {role}</h2>
                <p class="instructions">
                    Dear {name},<br><br>
                    This is a friendly reminder about your upcoming Group Discussion Round 2 (GD-1) as part of the selection process for the Associate Web Developer role.
                    <br><br>
                    <b>Details for GD-1:</b>
                    <br><b>Date:</b> {date}
                    <br><b>Time:</b> {time}
                    <br><b>Venue:</b> Google Meet
                    <br><br>
                    Please ensure you:<br>
                    1. Join the session at least 10 minutes before the scheduled time.<br>
                    2. Are well-prepared, as the evaluation will focus on your performance during the discussion.<br><br>
                    If you have any questions or need further assistance, feel free to reach out to us.
                </p>
                <div style="text-align: center;height:60px;justify-content: center;">
                    <a href="{gd1_link}" class="action-button" style="color:white;">Join Meet</a>
                </div>
                <p class="fallback-link">If the button above doesn't work, use the following link: </p> <br> 
                <a href="{gd1_link}">{gd1_link}</a>
                <p class="content">
                    If you have any query write an email to : support@elementissofttech.com 
                </p>
                <div class="footer">
                    Best regards,<br>
                    Team Elementis SoftTech
                </div>
            </div>
        </body>
        </html>
        """

        content = MIMEText(html_content, "html")
        message.attach(content)

        start_session(message)

        print("Email Sent to -", name)

    except Exception as e:
        print(f"Error sending email: {e}")  # Provide more detailed error information

    return

# Function for sending  GD-2 selection mail
def send_GD2_mail(to,role='',sub='',link='',date='',time='',name="Candidate"):
    try:
        # Create a multi-part message to include both plain text and HTML content
        message = MIMEMultipart("alternative")
        gd2_link = link
        logo = "https://buikzohejfkxouarmyni.supabase.co/storage/v1/object/sign/assets/Elementis-01.png?token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1cmwiOiJhc3NldHMvRWxlbWVudGlzLTAxLnBuZyIsImlhdCI6MTczNTg4NzkxMiwiZXhwIjoyMTY3ODg3OTEyfQ.JonG5NOKKZkLZWT6Fmf5VusAUgFIQaNvY4t4l3KCfmY&t=2025-01-03T07%3A05%3A12.250Z"
        
        # Email subject and sender information
        message["Subject"] = sub
        message["From"] = "info.elementis@onlyformachinelearning.in"
        message["To"] = to

        # HTML content styled for design
        html_content = f"""
        <html>
        <head>
            <style>
                body {{
                    font-family: Arial, sans-serif;
                    background-color: #f9f9f9;
                    margin: 0;
                    padding: 0;
                }}
                .email-container {{
                    max-width: 600px;
                    margin: 20px auto;
                    background: #ffffff;
                    padding: 20px;
                    border: 4px solid #18def3;
                    border-radius: 10px;
                }}
                .header-logo {{
                    text-align: center;
                    margin-bottom: 20px;
                }}
                .instructions {{
                    font-size: 14px;
                    text-align: left;
                    margin-bottom: 20px;
                    line-height: 1.6;
                }}
                .content {{
                    font-size: 14px;
                    text-align: left;
                    margin-bottom: 20px;
                    line-height: 1.6;
                }}
                .action-button{{
                    display: inline-block;
                    background-color: #004aad;
                    color: white;
                    font-weight: bold;
                    text-decoration: none;
                    padding: 12px 20px;
                    font-size: 16px;
                    border-radius: 5px;
                    text-align: center;
                    margin: 20px auto;
                    cursor: pointer;
                    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.2);
                    transition: background-color 0.3s ease, transform 0.2s ease;
                }}
                .action-button:hover{{
                    background-color: #003580;
                    color: white;
                    transform: scale(1.05);
                }}
                .fallback-link {{
                    font-size: 14px;
                    margin-top: 20px;
                    text-align: center;
                    word-wrap: break-word;
                }}
                .footer {{
                    font-size: 12px;
                    color: #888;
                    text-align: center;
                    margin-top: 20px;
                }}
            </style>
        </head>
        <body>
            <div class="email-container">
                <div class="header-logo">
                    <img src={logo} width="250">
                </div>
                <h2 style="text-align: center;">Elementis SoftTech || {role}</h2>
                <p class="instructions">
                    Dear {name},<br><br>
                    Congratulations! We are pleased to inform you that you have successfully cleared Group Discussion Round 1 and have been selected to proceed to the next round (GD-2) of the selection process.
                    <br>
                    Your performance in the Group Discussion was impressive, and we are excited to move forward with your application. The next step will be a Group Discussion(GD-2).<br>
                    <br>
                    <b>Details for GD-2 are as follows:</b>
                    <br><b>Date:</b> {date}
                    <br><b>Time:</b> {time}
                    <br><b>Venue:</b> Google Meet
                    <br><br>
                    <b>
                    Please make sure to:
                    <br>
                    1.Be punctual and join the session at least 10 minutes before the scheduled time.<br>
                    2.Prepare thoroughly, keeping in mind the evaluation will be based on your performance.
                    </b>
                    <br>
                    If you have any questions or require further assistance, feel free to reach out to us. <br>
                    <br>We wish you the very best for the next round and look forward to your continued participation.
                </p>
                <div style="text-align: center;height:60px;justify-content: center;">
                    <a href="{gd2_link}" style:"color:white;" class="action-button">Join Meet</a>
                </div>
                <p class="fallback-link">If the button above doesn't work, use the following link: </p> <br> 
                <a href="{gd2_link}">{gd2_link}</a>
                <p class="content">
                    If you have any query write an email to : support@elementissofttech.com 
                </p>
                <div class="footer">
                    Best regards,<br>
                    Team Elementis SoftTech
                </div>
            </div>
        </body>
        </html>
        """

        content = MIMEText(html_content, "html")
        message.attach(content)

        start_session(message)

        print("Email Sent to -",name)


    except Exception as e:
        print(f"Error sending email: {e}")  # Provide more detailed error information
        
    return

# Function for sending  GD-2 reminder mail
def send_GD2_reminder_mail(to,role='',sub='',link='',date='',time='',name="Candidate"):
    try:
        # Create a multi-part message to include both plain text and HTML content
        message = MIMEMultipart("alternative")
        gd2_link = link
        logo = "https://buikzohejfkxouarmyni.supabase.co/storage/v1/object/sign/assets/Elementis-01.png?token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1cmwiOiJhc3NldHMvRWxlbWVudGlzLTAxLnBuZyIsImlhdCI6MTczNTg4NzkxMiwiZXhwIjoyMTY3ODg3OTEyfQ.JonG5NOKKZkLZWT6Fmf5VusAUgFIQaNvY4t4l3KCfmY&t=2025-01-03T07%3A05%3A12.250Z"
        
        # Email subject and sender information
        message["Subject"] = sub
        message["From"] = "info.elementis@onlyformachinelearning.in"
        message["To"] = to

        # HTML content styled for design
        html_content = f"""
        <html>
        <head>
            <style>
                body {{
                    font-family: Arial, sans-serif;
                    background-color: #f9f9f9;
                    margin: 0;
                    padding: 0;
                }}
                .email-container {{
                    max-width: 600px;
                    margin: 20px auto;
                    background: #ffffff;
                    padding: 20px;
                    border: 4px solid #18def3;
                    border-radius: 10px;
                }}
                .header-logo {{
                    text-align: center;
                    margin-bottom: 20px;
                }}
                .instructions {{
                    font-size: 14px;
                    text-align: left;
                    margin-bottom: 20px;
                    line-height: 1.6;
                }}
                .reminder {{
                    font-size: 16px;
                    font-weight: bold;
                    margin-bottom: 20px;
                }}
                .content {{
                    font-size: 14px;
                    text-align: left;
                    margin-bottom: 20px;
                    line-height: 1.6;
                }}
                .action-button{{
                    display: inline-block;
                    background-color: #004aad;
                    color: white;
                    font-weight: bold;
                    text-decoration: none;
                    padding: 12px 20px;
                    font-size: 16px;
                    border-radius: 5px;
                    text-align: center;
                    margin: 20px auto;
                    cursor: pointer;
                    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.2);
                    transition: background-color 0.3s ease, transform 0.2s ease;
                }}
                .action-button:hover{{
                    background-color: #003580;
                    color: white;
                    transform: scale(1.05);
                }}
                .fallback-link {{
                    font-size: 14px;
                    margin-top: 20px;
                    text-align: center;
                    word-wrap: break-word;
                }}
                .footer {{
                    font-size: 12px;
                    color: #888;
                    text-align: center;
                    margin-top: 20px;
                }}
            </style>
        </head>
        <body>
            <div class="email-container">
                <div class="header-logo">
                    <img src="{logo}" width="250" alt="Elementis SoftTech Logo">
                </div>
                <h2 style="text-align: center;">Elementis SoftTech || {role}</h2>
                <p class="instructions">
                    Dear {name},<br><br>
                    This is a friendly reminder about your upcoming Group Discussion Round 2 (GD-2) as part of the selection process for the Associate Web Developer role.
                    <br><br>
                    <b>Details for GD-2:</b>
                    <br><b>Date:</b> {date}
                    <br><b>Time:</b> {time}
                    <br><b>Venue:</b> Google Meet
                    <br><br>
                    Please ensure you:<br>
                    1. Join the session at least 10 minutes before the scheduled time.<br>
                    2. Are well-prepared, as the evaluation will focus on your performance during the discussion.<br><br>
                    If you have any questions or need further assistance, feel free to reach out to us.
                </p>
                <div style="text-align: center;height:60px;justify-content: center;">
                    <a href="{gd2_link}" class="action-button" style="color:white;">Join Meet</a>
                </div>
                <p class="fallback-link">If the button above doesn't work, use the following link: 
                <a href="{gd2_link}">{gd2_link}</a></p>
                <p class="content">
                    If you have any query write an email to : support@elementissofttech.com 
                </p>
                <div class="footer">
                    Best regards,<br>
                    Team Elementis SoftTech
                </div>
            </div>
        </body>
        </html>
        """



        content = MIMEText(html_content, "html")
        message.attach(content)

        start_session(message)

        print("Email Sent to -",name)


    except Exception as e:
        print(f"Error sending email: {e}")  # Provide more detailed error information
        
    return

# Function for sending technical assessment registration mail
def send_technical_assessment_register_mail(to,role='',sub='',link='',date='',time='',name="Candidate"):

    try:
        # Create a multi-part message to include both plain text and HTML content
        message = MIMEMultipart("alternative")
        registration_link = link
        logo = "https://buikzohejfkxouarmyni.supabase.co/storage/v1/object/sign/assets/Elementis-01.png?token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1cmwiOiJhc3NldHMvRWxlbWVudGlzLTAxLnBuZyIsImlhdCI6MTczNTg4NzkxMiwiZXhwIjoyMTY3ODg3OTEyfQ.JonG5NOKKZkLZWT6Fmf5VusAUgFIQaNvY4t4l3KCfmY&t=2025-01-03T07%3A05%3A12.250Z"
        
        # Email subject and sender information
        message["Subject"] = sub
        message["From"] = "info.elementis@onlyformachinelearning.in"
        message["To"] = to

        # HTML content styled for design
        html_content = f"""
        <html>
        <head>
            <style>
                body {{
                    font-family: Arial, sans-serif;
                    background-color: #f9f9f9;
                    margin: 0;
                    padding: 0;
                }}
                .email-container {{
                    max-width: 600px;
                    margin: 20px auto;
                    background: #ffffff;
                    padding: 20px;
                    border: 4px solid #18def3;
                    border-radius: 10px;
                }}
                .header-logo {{
                    text-align: center;
                    margin-bottom: 20px;
                }}
                .content {{
                    font-size: 14px;
                    text-align: left;
                    margin-bottom: 20px;
                    line-height: 1.6;
                }}
                .content {{
                    font-size: 14px;
                    text-align: left;
                    margin-bottom: 20px;
                    line-height: 1.6;
                }}
                .action-button{{
                    display: inline-block;
                    background-color: #004aad;
                    color: white;
                    font-weight: bold;
                    text-decoration: none;
                    padding: 12px 20px;
                    font-size: 16px;
                    border-radius: 5px;
                    text-align: center;
                    margin: 20px auto;
                    cursor: pointer;
                    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.2);
                    transition: background-color 0.3s ease, transform 0.2s ease;
                }}
                .action-button:hover{{
                    background-color: #003580;
                    color: white;
                    transform: scale(1.05);
                }}
                .fallback-link {{
                    font-size: 14px;
                    margin-top: 20px;
                    text-align: center;
                    word-wrap: break-word;
                }}
                .footer {{
                    font-size: 12px;
                    color: #888;
                    text-align: center;
                    margin-top: 20px;
                }}
                ul {{
                    margin: 0 0 20px 20px;
                }}
                li {{
                    margin-bottom: 10px;
                }}
            </style>
        </head>
        <body>
            <div class="email-container">
                <div class="header-logo">
                    <img src="{logo}" width="250" alt="Elementis SoftTech Logo">
                </div>
                <h2 style="text-align: center;">Congratulations - Elementis SoftTech || {role}</h2>
                <p class="content">
                    Dear {name},<br><br>
                    Thank you for participating in Elementis SoftTech’s selection process. We value your enthusiasm and interest.<br><br>
                    To maintain a transparent and fair process, we charge a nominal fee for the technical round. This covers costs for using Coderbyte, a premium assessment platform that ensures high standards in evaluating technical skills.<br><br>
                    Passing this fee to candidates helps us manage resources responsibly and avoid unnecessary expenses for no-shows after registration.
                </p>
                <p class="content">
                    Here’s what this step ensures for all candidates:
                    <ul>
                        <li><b>Fair Opportunity:</b> By conducting an advanced technical evaluation, we aim to shortlist candidates who meet the technical standards we require for our projects.</li>
                        <li><b>Transparency:</b> The fee charged is entirely directed towards covering the costs associated with your assessment.</li>
                        <li><b>Career Development:</b> Every participant in this process, regardless of the outcome, will have an opportunity to gain valuable experience.</li>
                    </ul>
                </p>
                <p class="content">
                    After the technical round:<br>
                    <ul>
                        <li><b>Qualified Candidates:</b> Those who qualify will join as stipend interns (₹5000/month). Outstanding performers will also be eligible for a Pre-Placement Offer (PPO) with a starting salary of ₹4–6 LPA.</li>
                        <li><b>Candidates Who Couldn’t Qualify:</b> We believe learning is a journey. To support this, we will offer an unpaid internship where you can gain hands-on experience and earn a certificate of completion. This certificate will serve as a valuable addition to your résumé, reflecting relevant industry exposure.</li>
                    </ul>
                </p>
                <div style="text-align: center;height:60px;justify-content: center;">
                    <a href="{registration_link}" class="action-button" style="color:white;">Register</a>
                </div>
                <p class="fallback-link">If the button above doesn't work, use the following link:</p>
                <p style="word-wrap: break-word; text-align: center;"><a href="{registration_link}">{registration_link}</a></p><br>
                <p class="content">
                    To proceed further, please register for the Technical Round using the link below. After registration, you will receive the date and time slot for your technical round. <br>
                    If you have any query write an email to : support@elementissofttech.com 
                </p>
                <div class="footer">
                    Best regards,<br>
                    Elementis SoftTech
                </div>
            </div>
        </body>
        </html>
        """


        with open(r"Technical Round.pdf", 'rb') as f:
            pdf_attachment = MIMEApplication(f.read(), _subtype='pdf')
            pdf_attachment.add_header('Content-Disposition', 'attachment', filename='CompanyProfile.pdf')
            message.attach(pdf_attachment)

        content = MIMEText(html_content, "html")
        message.attach(content)

        start_session(message)

        print("Email Sent to -",name)


    except Exception as e:
        print(f"Error sending email: {e}")  # Provide more detailed error information

    return

# Function for sending technical assessment mail
def send_technical_assessment_mail(to,role='',sub='',link='',date='',time='',name="Candidate"):
# def send_technical_mail(to,name="Candidate"):

    try:
        # Create a multi-part message to include both plain text and HTML content
        message = MIMEMultipart("alternative")
        assessment_link = link
        logo = "https://buikzohejfkxouarmyni.supabase.co/storage/v1/object/sign/assets/Elementis-01.png?token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1cmwiOiJhc3NldHMvRWxlbWVudGlzLTAxLnBuZyIsImlhdCI6MTczNTg4NzkxMiwiZXhwIjoyMTY3ODg3OTEyfQ.JonG5NOKKZkLZWT6Fmf5VusAUgFIQaNvY4t4l3KCfmY&t=2025-01-03T07%3A05%3A12.250Z"
        
        # Email subject and sender information
        message["Subject"] = sub
        # message["Subject"] = "Congratulations! Shortlisted for Technical Round || Associate Web Developer"
        message["From"] = "info.elementis@onlyformachinelearning.in"
        message["To"] = to

        # HTML content styled for design
        html_content = f"""
        <html>
        <head>
            <style>
                body {{
                    font-family: Arial, sans-serif;
                    background-color: #f9f9f9;
                    margin: 0;
                    padding: 0;
                }}
                .email-container {{
                    max-width: 600px;
                    margin: 20px auto;
                    background: #ffffff;
                    padding: 20px;
                    border: 4px solid #18def3;
                    border-radius: 10px;
                }}
                .header-logo {{
                    text-align: center;
                    margin-bottom: 20px;
                }}
                .instructions {{
                    font-size: 14px;
                    text-align: left;
                    margin-bottom: 20px;
                    line-height: 1.6;
                }}
                .content {{
                    font-size: 14px;
                    text-align: left;
                    margin-bottom: 20px;
                    line-height: 1.6;
                }}
                .action-button{{
                    display: inline-block;
                    background-color: #004aad;
                    color: white;
                    font-weight: bold;
                    text-decoration: none;
                    padding: 12px 20px;
                    font-size: 16px;
                    border-radius: 5px;
                    text-align: center;
                    margin: 20px auto;
                    cursor: pointer;
                    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.2);
                    transition: background-color 0.3s ease, transform 0.2s ease;
                }}
                .action-button:hover{{
                    background-color: #003580;
                    color: white;
                    transform: scale(1.05);
                }}
                .fallback-link {{
                    font-size: 14px;
                    margin-top: 20px;
                    text-align: center;
                    word-wrap: break-word;
                }}
                .footer {{
                    font-size: 12px;
                    color: #888;
                    text-align: center;
                    margin-top: 20px;
                }}
                 
            </style>
        </head>
        <body>
            <div class="email-container">
                <div class="header-logo">
                    <img src={logo} width="250">
                </div>
                <h2 style="text-align: center;">Elementis SoftTech Assessment || {role}</h2>
                <p class="instructions">
                    Hi {name},<br><br>
                    Welcome to Elementis SoftTech Campus Drive(Technical Round)<br>
                    - This is a 120-minute Assessment.<br>
                    - Make sure to take the assessment on your Desktop/Laptop.<br>
                    - Mute all notifications. Any popup or antivirus notification is treated as off-tab activity. Disable all notifications before starting the test.<br>
                    - Highly Important: Please clear browser cache and cookies before starting the test; otherwise, it can affect the test session.<br>
                    - Ensure that your laptop time zone is set to (UTC+05:30) Chennai, Kolkata, Mumbai, New Delhi, to avoid any timezone-related issues.<br>
                    - Any attempt to copy from the internet, copy from others, or impersonate would lead to outright rejection as all the submissions are monitored by AI.</b>.<br>
                    <br><br>
                    <b>A couple of things to keep in mind while taking the assessment:<br>
                    i) This invite is valid from: {date} {time}.<br>
                    ii) Please take the test on your desktop or laptop.<br>
                    iii) Choose a quiet location where you will not be interrupted.<br>
                    iv) Ensure you have a reliable internet connection before starting the test.<br></b>
                </p>
                <br>You can start the assessment by clicking here:</b>
                <div style="text-align: center;">
                    <a href="{assessment_link}" style="color:white"class="action-button">Start Assessment</a>
                </div>
                <p class="fallback-link">If the button above doesn't work, use the following link: </p> <br> 
                <a href="{assessment_link}">{assessment_link}</a><br>
                <p class="content">
                    If you have any query write an email to : support@elementissofttech.com 
                </p>
                <div class="footer">
                    Best regards,<br>
                    Team Elementis SoftTech
                </div>
            </div>
        </body>
        </html>
        """

        content = MIMEText(html_content, "html")
        message.attach(content)

        start_session(message)

        print("Email Sent to -",name)


    except Exception as e:
        print(f"Error sending email: {e}")  # Provide more detailed error information
    
    return

# Function for sending process feedback mail
def send_process_feedback_mail(to,role='',sub='',link='',date='',time='',name="Candidate"):
    try:
        # Create a multi-part message to include both plain text and HTML content
        message = MIMEMultipart("alternative")
        feedback_link = link
        telegram_link = 'https://t.me/ElementisSoftTech'
        linkedin_link = 'https://www.linkedin.com/company/elementis-softtech/'
        logo = "https://buikzohejfkxouarmyni.supabase.co/storage/v1/object/sign/assets/Elementis-01.png?token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1cmwiOiJhc3NldHMvRWxlbWVudGlzLTAxLnBuZyIsImlhdCI6MTczNTg4NzkxMiwiZXhwIjoyMTY3ODg3OTEyfQ.JonG5NOKKZkLZWT6Fmf5VusAUgFIQaNvY4t4l3KCfmY&t=2025-01-03T07%3A05%3A12.250Z"
        
        # Email subject and sender information
        message["Subject"] = sub
        message["From"] = "info.elementis@onlyformachinelearning.in"
        message["To"] = to

        # HTML content styled for design
        html_content = f"""
        <html>
        <head>
            <style>
                body {{
                    font-family: Arial, sans-serif;
                    background-color: #f9f9f9;
                    margin: 0;
                    padding: 0;
                }}
                .email-container {{
                    max-width: 600px;
                    margin: 20px auto;
                    background: #ffffff;
                    padding: 20px;
                    border: 4px solid #18def3;
                    border-radius: 10px;
                }}
                .header-logo {{
                    text-align: center;
                    margin-bottom: 20px;
                }}
                .instructions {{
                    font-size: 14px;
                    text-align: left;
                    margin-bottom: 20px;
                    line-height: 1.6;
                }}
                .content {{
                    font-size: 14px;
                    text-align: left;
                    margin-bottom: 20px;
                    line-height: 1.6;
                }}
                .action-button{{
                    display: inline-block;
                    background-color: #004aad;
                    color: white;
                    font-weight: bold;
                    text-decoration: none;
                    padding: 12px 20px;
                    font-size: 16px;
                    border-radius: 5px;
                    text-align: center;
                    margin: 20px auto;
                    cursor: pointer;
                    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.2);
                    transition: background-color 0.3s ease, transform 0.2s ease;
                }}
                .action-button:hover{{
                    background-color: #003580;
                    color: white;
                    transform: scale(1.05);
                }}
                .fallback-link {{
                    font-size: 14px;
                    margin-top: 20px;
                    text-align: center;
                    word-wrap: break-word;
                }}
                .footer {{
                    font-size: 12px;
                    color: #888;
                    text-align: center;
                    margin-top: 20px;
                }}
                .social-links {{
                    text-align: center;
                    margin-top: 20px;
                }}
                .social-links a {{
                    color: #004aad;
                    font-weight: bold;
                    text-decoration: none;
                    margin: 0 10px;
                }}
                .social-links a:hover {{
                    text-decoration: underline;
                }}
            </style>
        </head>
        <body>
            <div class="email-container">
                <div class="header-logo">
                    <img src="{logo}" width="250" alt="Elementis SoftTech Logo">
                </div>
                <h2 style="text-align: center;">Elementis SoftTech || {role}</h2>
                <p class="instructions">
                    Dear {name},<br><br>
                    Thank you for your interest in our opportunity and the effort you put into your application.<br><br>
                    After much consideration, we’ve decided not to proceed with your candidacy at this time. This decision was not easy, as we had many strong applicants, and it’s not a reflection of your skills or potential.<br><br>
                    We’ll keep your profile on file for future opportunities and encourage you to stay connected with us.<br><br>
                    We sincerely wish you the best in your career journey and thank you again for considering us.
                </p>
                <p class="instructions">
                    Thank you for participating in the hiring process for the Associate Web Developer role at Elementis SoftTech. We value your input and would like to hear your feedback on the overall hiring experience.
                </p>
                <div style="text-align: center;height:60px;justify-content: center;">
                    <a href="{feedback_link}" class="action-button" style="color:white;">Give Feedback</a>
                </div>
                <p class="instructions" style="text-align: center;">
                    Follow us to stay updated on this drive, as well as upcoming opportunities and hiring events.
                </p>
                <div class="social-links">
                    <a href="{linkedin_link}" target="_blank">LinkedIn</a> | 
                    <a href="{telegram_link}" target="_blank">Telegram</a>
                </div><br>
                <p class="content">
                    If you have any query write an email to : support@elementissofttech.com 
                </p>
                <div class="footer">
                    Best regards,<br>
                    Team Elementis SoftTech
                </div>
            </div>
        </body>
        </html>
        """




        content = MIMEText(html_content, "html")
        message.attach(content)

        start_session(message)

        print("Email Sent to -",name)


    except Exception as e:
        print(f"Error sending email: {e}")  # Provide more detailed error information
    
    return

def send_selection_mail(to,role='',sub='',link='',date='',time='',name="Candidate"):
    pass
    return