import email
import imaplib
import os
import subprocess
from config import ConfigEmail

mail = imaplib.IMAP4_SSL(ConfigEmail.imap_server)
mail.login(ConfigEmail.email_user, ConfigEmail.email_pass)

mail.select("inbox")

result, data = mail.uid("search", None, '(UNSEEN)')
email_ids = data[0].split()

for num in email_ids:
    result, data = mail.uid("fetch", num, "(BODY.PEEK[])")
    raw_email = data[0][1]
    raw_email_string = raw_email.decode("utf-8")
    email_message = email.message_from_string(raw_email_string)

    for part in email_message.walk():
        if part.get_content_maintype() == "multipart":
            continue
        if part.get("Content-Disposition") is None:
            continue
        filename = part.get_filename()

        if bool(filename):
            filePath = os.path.join("../data", filename)
            if not os.path.isfile(filePath):
                with open(filePath, "wb") as file:
                    file.write(part.get_payload(decode=True))
    subprocess.run(["lpr", "-P nombre_impresora", filePath])