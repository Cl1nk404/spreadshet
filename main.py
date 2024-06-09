# import requests
# from enum import Enum


# class DocumentType(Enum):
#     # Паспорт гражданина СССР
#     passport_ussr = "01"
#     # Свидетельство о рождении
#     birth_certificate = "03"
#     # Паспорт иностранного гражданина
#     passport_foreign = "10"
#     # Вид на жительство в России
#     residence_permit = "12"
#     # Разрешение на временное проживание в России
#     residence_permit_temp = "15"
#     # Свидетельство о предоставлении временного убежища на территории России
#     asylum_certificate_temp = "19"
#     # Паспорт гражданина России
#     passport_russia = "21"
#     # Свидетельство о рождении, выданное уполномоченным органом иностранного государства
#     birth_certificate_foreign = "23"
#     # Вид на жительство иностранного гражданина
#     residence_permit_foreign = "62"


# def suggest_inn(surname, name, patronymic, birthdate, doctype, docnumber, docdate):
#     url = "https://service.nalog.ru/inn-proc.do"
#     data = {
#         "fam": surname,
#         "nam": name,
#         "otch": patronymic,
#         "bdate": birthdate,
#         "bplace": "",
#         "doctype": doctype,
#         "docno": docnumber,
#         "docdt": docdate,
#         "c": "innMy",
#         "captcha": "",
#         "captchaToken": "",
#     }
#     resp = requests.post(url=url, data=data)
#     resp.raise_for_status()
#     return resp.json()


# if __name__ == "__main__":
#     response = suggest_inn(
#         surname="Юнко",
#         name="Игорь",
#         patronymic="Андреевич",
#         birthdate="10.04.2003",
#         doctype=DocumentType.passport_russia.value,
#         docnumber="29 23 171576",
#         docdate="18.07.2023",
#     )
#     print(response)

import tkinter as tk
from tkinter import ttk, messagebox
import requests
from enum import Enum

class DocumentType(Enum):
    passport_ussr = "01"
    birth_certificate = "03"
    passport_foreign = "10"
    residence_permit = "12"
    residence_permit_temp = "15"
    asylum_certificate_temp = "19"
    passport_russia = "21"
    birth_certificate_foreign = "23"
    residence_permit_foreign = "62"

def suggest_inn(surname, name, patronymic, birthdate, doctype, docnumber, docdate):
    url = "https://service.nalog.ru/inn-proc.do"
    data = {
        "fam": surname,
        "nam": name,
        "otch": patronymic,
        "bdate": birthdate,
        "bplace": "",
        "doctype": doctype,
        "docno": docnumber,
        "docdt": docdate,
        "c": "innMy",
        "captcha": "",
        "captchaToken": "",
    }
    resp = requests.post(url=url, data=data)
    resp.raise_for_status()
    return resp.json()

def check_inn():
    surname = entry_surname.get()
    name = entry_name.get()
    patronymic = entry_patronymic.get()
    birthdate = entry_birthdate.get()
    doctype = '21'
    docnumber = entry_docnumber.get()
    docdate = entry_docdate.get()

    print(surname)
    print(name)
    print(patronymic)
    print(birthdate)
    print(doctype)
    print(docnumber)
    print(docdate)



    try:
        response = suggest_inn(
            surname=surname,
            name=name,
            patronymic=patronymic,
            birthdate=birthdate,
            doctype=doctype,
            docnumber=docnumber,
            docdate=docdate
        )
        result_text.set(response)
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

app = tk.Tk()
app.title("Проверка паспорта")

# Создание меток и полей ввода
ttk.Label(app, text="Фамилия:").grid(column=0, row=0, padx=10, pady=5)
entry_surname = ttk.Entry(app)
entry_surname.grid(column=1, row=0, padx=10, pady=5)

ttk.Label(app, text="Имя:").grid(column=0, row=1, padx=10, pady=5)
entry_name = ttk.Entry(app)
entry_name.grid(column=1, row=1, padx=10, pady=5)

ttk.Label(app, text="Отчество:").grid(column=0, row=2, padx=10, pady=5)
entry_patronymic = ttk.Entry(app)
entry_patronymic.grid(column=1, row=2, padx=10, pady=5)

ttk.Label(app, text="Дата рождения (дд.мм.гггг):").grid(column=0, row=3, padx=10, pady=5)
entry_birthdate = ttk.Entry(app)
entry_birthdate.grid(column=1, row=3, padx=10, pady=5)

ttk.Label(app, text="Тип документа:").grid(column=0, row=4, padx=10, pady=5)
doc_type_var = tk.StringVar()
doc_type_combobox = ttk.Combobox(app, textvariable=doc_type_var)
doc_type_combobox['values'] = [f"{doc.value} - {doc.name}" for doc in DocumentType]
doc_type_combobox.grid(column=1, row=4, padx=10, pady=5)

ttk.Label(app, text="Номер документа:").grid(column=0, row=5, padx=10, pady=5)
entry_docnumber = ttk.Entry(app)
entry_docnumber.grid(column=1, row=5, padx=10, pady=5)

ttk.Label(app, text="Дата выдачи документа (дд.мм.гггг):").grid(column=0, row=6, padx=10, pady=5)
entry_docdate = ttk.Entry(app)
entry_docdate.grid(column=1, row=6, padx=10, pady=5)

# Кнопка для проверки ИНН
ttk.Button(app, text="Проверить", command=check_inn).grid(column=0, row=7, columnspan=2, padx=10, pady=10)

# Поле для отображения результата
result_text = tk.StringVar()
ttk.Label(app, textvariable=result_text).grid(column=0, row=8, columnspan=2, padx=10, pady=10)

app.mainloop()
