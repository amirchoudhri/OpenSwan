import string
import random
import os
import subprocess
import smtplib

def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
     randomstring = ''.join(random.choice(chars) for _ in range(size))
     startstring = random.choice(string.ascii_uppercase)
     lowerstring = random.choice(string.ascii_lowercase)
     return startstring + lowerstring + randomstring

new_password = id_generator()
new_password = str(new_password)
print new_password
target = open("/tmp/update.xml", 'w')
target.write("<ns3:internaluser xmlns:ns3=\"identity.ers.ise.cisco.com\" name=\"officeguest\" id=\"83a91e40-0e62-11e4-8b76-005056b0261a\" description=\"Office Shared Password for Large Groups\">")
target.write("<link type=\"application/xml\" href=\"https://usb-ssise01.net.ef.com:9060/ers/config/internaluser/83a91e40-0e62-11e4-8b76-005056b0261a\" rel=\"self\"/>")
target.write("<identityGroups>f9d27b10-f42e-11e2-bd54-005056bf2f0a</identityGroups>")
target.write("<password>%s</password>" %(new_password))
target.write("</ns3:internaluser>")
target.close()


sender = 'officeguest@ef.com'
receivers = ['wifi.officeguest.subscribers@ef.com']

success_message = """From: officeguest@ef.com
To: wifi.officeguest.subscribers@ef.com
Subject: New "officeguest" password created

The officeguest password has been changed, the new password is: %s

This username and password should only be used for large group meetings, and users should be encouraged to use https://wifiguest.ef.com to register their guest.

If you encounter any issues please raise a Nemo ticket - https://nemo.ef.com.

Thank you,

Global IT
""" % new_password

error_message = """From: officeguest@ef.com
To: wifi.officeguest.subscribers@ef.com
Subject: New "officeguest" password failed to be created

The officeguest password was not changed successfully, please continue to use last weeks password. In case of any issues please raise a Nemo Ticket - https://nemo.ef.com.

Thank you,

Global IT
"""


try:
        subprocess.call("curl -v -X PUT -k -H 'Content-type: application/vnd.com.cisco.ise.identity.internaluser.1.0+xml' 'https://ERS:TopGuns&04@usb-ssise01.net.ef.com:9060/ers/config/internaluser/83a91e40-0e62-11e4-8b76-005056b0261a' -d @/tmp/update.xml", shell=True)
        smtpObj = smtplib.SMTP('ht.ef.com',25)
        smtpObj.sendmail(sender, receivers, success_message)
        print "The guest password was created"
except subprocess.CalledProcessError:
        smtpObj = smtplib.SMTP('ht.ef.com',25)
        smtpObj.sendmail(sender, receivers, error_message)
        print "The guest password was NOT created, an error occured."
except SMTPException:
    print "Error: unable to send email"
