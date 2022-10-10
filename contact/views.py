from django.shortcuts import render
import smtplib
from email.mime.text import MIMEText

def contact(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        comment = request.POST.get('comment')
        # 발신자주소, 수신자주소, 메시지
        send_mail('nagyeomhan91@gmail.com', email, comment)
        return render(request, 'contact_success.html')
    return render(request, 'contact.html')

# SMTP 설정 - TTL 혹은 SSL 사용
# TLS : smtplib.SMTP()     | 포트 587
# SSL : smtplib.SMTP_SSL() | 포트 465
# SMPT 객체를 생성한 후에는 stmp.ehlo()
# 이후 TLS인 경우에는 starttls() 실행
def send_mail(to_email, from_email, msg):
    # SMTP 설정 - SSL
    smtp = smtplib.SMTP_SSL('stmp.gmail.com', 465)
    smtp.ehlo()
    smtp.starttls()
    # 인증정보 설정
    smtp.login(from_email, 'cofcuqsulcxfvjxu')
    msg = MIMEText(msg)
    # 제목
    msg['Subject'] = '[문의사항]' + to_email
    # 수신 이메일
    msg['To'] = from_email
    # sendmail(송신자, 수신자, 메시지)
    smtp.sendmail(from_email, from_email, msg.as_string())
    # SMTP와 연결 종료
    smtp.quit()