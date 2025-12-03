import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import os

def send_individual_emails(subject, body, recipients, pdf_path=None):

    # Email settings
    sender_email = 'jaiswaladi246@gmail.com'
    sender_password = 'tpzk olai omuk vhol'  # Use App Password

    # HTML Email Template
    html_body_template = """
    <html>
    <body style="font-family: 'Segoe UI', sans-serif; background-color: #f4f4f4; padding: 20px;">
        <div style="max-width: 600px; margin: 0 auto; background-color: white; padding: 20px; border-radius: 10px; box-shadow: 0 0 10px rgba(0,0,0,0.1);">
            
            <h2 style="color: #4CAF50; text-align: center;">Welcome to Batch-7!</h2>

            <p style="font-size: 18px; color: #555;">Hello <b>{name}</b>,</p>

            <p style="font-size: 16px; color: #555;">
            We are excited to announce that <b>Batch-7</b> of our 
            <b>DevSecOps & Cloud DevOps Bootcamp</b> is starting soon!
            <br><br>
            Secure your spot now and learn the most in-demand DevOps & DevSecOps skills:
            </p>

            <ul style="font-size: 16px; color: #333; line-height: 1.8;">
                <li>CI/CD Tools (Jenkins, GitHub Actions, GitLab CI/CD)</li>
                <li>Infrastructure as Code (Ansible, Terraform)</li>
                <li>Security Tools (Trivy, OWASP Dependency Check, Vault)</li>
                <li>Cloud Platforms (Azure DevOps, Kubernetes, Docker)</li>
                <li>Hands-on Projects (NodeJS, Python, Java, Microservices)</li>
                <li>Linux & Shell Scripting</li>
                <li>Resume Building & LinkedIn Profile Optimization</li>
            </ul>

            <p style="text-align: center; margin: 30px 0;">
                <a href="https://devopsshack.com"
                   style="text-decoration: none; background-color: #4CAF50; color: white; padding: 12px 25px; border-radius: 5px; font-size: 18px;">
                   Enroll Now
                </a>
            </p>

            <p style="font-size: 16px; color: #555; text-align: center;">
                Don't miss this opportunity to become a DevOps expert!
            </p>

            <p style="font-size: 16px; color: #555;">Best Regards,<br><b>DevOps Shack Team</b></p>
        </div>

        <footer style="text-align: center; margin-top: 20px;">
            <p style="font-size: 14px; color: #888;">© 2024 DevOps Shack</p>
        </footer>
    </body>
    </html>
    """

    # Send email to each recipient
    for recipient in recipients:

        # Extract name from email
        name = recipient.split('@')[0].capitalize()
        html_body = html_body_template.format(name=name)

        # Prepare mail message
        msg = MIMEMultipart()
        msg['Subject'] = subject
        msg['From'] = sender_email
        msg['To'] = recipient

        # Attach HTML content
        msg.attach(MIMEText(html_body, 'html'))

        # Attach PDF if exists
        if pdf_path and os.path.exists(pdf_path):
            with open(pdf_path, 'rb') as pdf_file:
                pdf_part = MIMEBase('application', 'octet-stream')
                pdf_part.set_payload(pdf_file.read())
                encoders.encode_base64(pdf_part)
                pdf_part.add_header('Content-Disposition',
                                    f'attachment; filename={os.path.basename(pdf_path)}')
                msg.attach(pdf_part)

        # Send email
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
            server.login(sender_email, sender_password)
            server.sendmail(sender_email, recipient, msg.as_string())


# -------------------------
# Example usage
# -------------------------

recipients_list = [
    'jaiswaladi246@gmail.com',
    'recipient1@example.com',
    'recipient2@example.com'
]

send_individual_emails(
    subject='Enroll Now: Batch-7 Starting Soon!',
    body='Batch-7 is starting soon, enroll now to book your seat!',
    recipients=recipients_list,
    pdf_path='Batch-7-Syllabus.pdf'
)
