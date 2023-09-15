from smtplib import SMTP


try:
    subject     = "Test Python"
    message     = "seni çok seviyorum hihiih"
    content     = "Subject: {0}\n\n{1}".format(subject,message)

    email       = 'tolgaakalin@yandex.com'
    password    = "919281089230182093801923010298310928301"
    sendTo      = "beyzadalgatc@gmail.com"

    mail        =SMTP("smtp.yandex.com",587)
    mail.ehlo()
    mail.starttls()
    mail.login(email,password)
    mail.sendmail(email,sendTo,content.encode("utf-8"))
    
    print("mail gönderildi")
except Exception as e:
    
    print("Hata Oluştu\n {0}".format(e))

