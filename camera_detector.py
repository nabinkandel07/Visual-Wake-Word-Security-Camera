import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import config

def send_alert(subject, body, recipient):
    cfg = config.load_config()
    msg = MIMEMultipart()
    msg['From'] = cfg['smtp_user']
    msg['To'] = recipient
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))
    
    try:
        server = smtplib.SMTP(cfg['smtp_server'], cfg['smtp_port'])
        server.starttls()
        server.login(cfg['smtp_user'], cfg['smtp_pass'])
        server.sendmail(cfg['smtp_user'], recipient, msg.as_string())
        server.quit()
        print("Alert sent successfully")
    except Exception as e:
        print(f"Failed to send alert: {e}")

# Example usage in camera_detector.py: after detection, call send_alert("Security Alert", f"Person detected at {timestamp}", cfg['alert_email'])
