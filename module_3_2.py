def send_email (message, recipient, *, sender):
    if (("@" and (".com" or ".ru" or ".net")) not in (recipient or sender) or
            ("@" or (".com" or ".ru" or ".net")) not in (recipient or sender)):
        print(f"Невозможно отправить письмо с адреса {sender} на адрес {recipient}")
    elif recipient == sender:
        print("Нельзя отправить письмо самому себе!")
    elif sender == "university.help@gmail.com":
        print(f"Письмо успешно отправлено с адреса {sender} на адрес {recipient}.")
    # else:
    elif sender != "university.help@gmail.com":
        print(f"НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}.")

send_email('message','universi@.com', sender = "university.help@gmail.com")
send_email('message','university.help@gmail.com', sender='123456@gmail.com')
send_email('message','urban.student@mail.ru', sender = "rban.teacher@mail.uk")
send_email('message','university.help@gmail.com', sender = "university.help@gmail.com")