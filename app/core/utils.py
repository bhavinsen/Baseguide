import boto3
from django.conf import settings
from django.core.mail import EmailMessage
from django.template.loader import render_to_string, get_template

def send_booking_confirmation_email(customer_email, template, context):
    # email_data = get_template(template)
    email_body = render_to_string(template, context)
    # email_body = email_data.render(context)

    ses_client = boto3.client('ses', region_name=settings.AWS_SES_REGION_NAME,aws_access_key_id=settings.AWS_ACCESS_KEY_ID,aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY)

    email = EmailMessage(
        subject='Booking Confirmation',
        body=email_body,
        from_email=settings.DEFAULT_FROM_EMAIL,
        to=[customer_email],
        reply_to=[settings.DEFAULT_FROM_EMAIL],
    )
    email.content_subtype = 'html'
    
    try:
        ses_client.send_raw_email(RawMessage={'Data': email.message().as_string()})
        return True
    except Exception as e:
        print("Error sending email:", e)
        return False    