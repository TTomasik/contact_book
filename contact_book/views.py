from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.views import View
from mysql.connector import connect


from contact_book.models import Contact


class NewContact(View):
    
    def get(self, request):
        return render(request, "new_contact.html")
        
    def post(self, request):
        new_contact_name = request.POST.get("contact_name")
        new_contact_surname = request.POST.get("contact_surname")
        new_contact_mail = request.POST.get("contact_mail")
        new_contact_phone_number = request.POST.get("contact_phone_number")
        
        query = """
        INSERT INTO Contacts (id, name, surname, mail, phone_number)
        VALUES (0, '%s', '%s', '%s', '%s')
                """ % (new_contact_name, new_contact_surname, new_contact_mail, new_contact_phone_number)
                
        cnx = connect(
        user="root",
        password="coderslab",
        host="localhost",
        database="contacts"
        )

    
        try:
            cursor = cnx.cursor()
            cursor.execute(query)
            cnx.commit()
        
        except:
            raise
            
               
        cursor.close()
        cnx.close()
        
        return HttpResponseRedirect("/")

    
class DeleteContact(View):
    
    def get(self, request):        
        sql = "SELECT id, name, surname, mail, phone_number FROM Contacts;"
        cnx = connect(
        user="root",
        password="coderslab",
        host="localhost",
        database="contacts"
        )
    
        try:
            cursor = cnx.cursor()
            cursor.execute(sql)
        
        except:
            raise
        
        contacts = []
        for row in cursor:
            contact = Contact(row[0], row[1], row[2], row[3], row[4])
            contacts.append(contact)
        
        ctx = {'contact_list': contacts}
        
        
        
        return render(request, "delete_contact.html", ctx)
        
    def post(self, request):                   
                
        delete_contact_id = request.POST.get("name")                      
        delete_contact_id == "" 
            
        query = """DELETE FROM Contacts WHERE id=%s;""" % int(delete_contact_id)
        
        cnx = connect(
        user="root",
        password="coderslab",
        host="localhost",
        database="contacts"
        )

    
        try:
            cursor = cnx.cursor()
            cursor.execute(query)
            cnx.commit()
        
        except:
            raise
            
               
        cursor.close()
        cnx.close()
        
        return HttpResponseRedirect("/delete")        
                     
        
class ShowContact(View):
    
    def get(self, request, contact_id):      
                
        sql = "SELECT id, name, surname, mail, phone_number FROM Contacts WHERE id=%s;" % contact_id
        cnx = connect(
        user="root",
        password="coderslab",
        host="localhost",
        database="contacts"
        )

    
        try:
            cursor = cnx.cursor()
            cursor.execute(sql)
        
        except:
            raise
            
        contact_from_cursor = cursor.fetchone()
        contact = Contact(
            contact_from_cursor[0],
            contact_from_cursor[1],
            contact_from_cursor[2],
            contact_from_cursor[3],
            contact_from_cursor[4])
        
        cursor.close()
        cnx.close()
        
#         ctx = {'name': contact.name,
#                'surname': contact.surname,
#                'mail': contact.mail,
#                'phone_number': contact.phone_number
#             
#             }
        
        ctx = {'contact' : contact}     # to jest alternatywa dla tego co na gorze, reszte zalatwiamy w show_contact.html poprzez dodanie contact. przed name surname itd...
        
        return render(request, "show_contact.html", ctx)

    def post(self, request, contact_id):  

        edit_contact = request.POST.get("editContact")
        edit_contact == "Edit contact"
                 
        sql = "SELECT id, name, surname, mail, phone_number FROM Contacts WHERE id=%s;" % contact_id
        cnx = connect(
        user="root",
        password="coderslab",
        host="localhost",
        database="contacts"
        )
 
     
        try:
            cursor = cnx.cursor()
            cursor.execute(sql)
         
        except:
            raise
             
        contact_from_cursor = cursor.fetchone()
        contact = Contact(
            contact_from_cursor[0],
            contact_from_cursor[1],
            contact_from_cursor[2],
            contact_from_cursor[3],
            contact_from_cursor[4])
         
        cursor.close()
        cnx.close()
         
#         ctx = {'name': contact.name,
#                'surname': contact.surname,
#                'mail': contact.mail,
#                'phone_number': contact.phone_number
#             
#             }
         
        ctx = {'contact' : contact}     # to jest alternatywa dla tego co na gorze, reszte zalatwiamy w show_contact.html poprzez dodanie contact. przed name surname itd...
         
        return render(request, "edit_contact.html", ctx)
    

class ShowContactList(View):
    
    def get(self, request):        
        sql = "SELECT id, name, surname, mail, phone_number FROM Contacts;"
        cnx = connect(
        user="root",
        password="coderslab",
        host="localhost",
        database="contacts"
        )
    
        try:
            cursor = cnx.cursor()
            cursor.execute(sql)
        
        except:
            raise
        
        contacts = []
        for row in cursor:
            contact = Contact(row[0], row[1], row[2], row[3], row[4])
            contacts.append(contact)
        
        ctx = {'contact_list': contacts}
        
        return render(request, "contact_list.html", ctx)
    
    def post(self, request):
    
        SORT = request.POST.get("sort")
             
        if SORT == "Sort by name":      
            sql2 = "SELECT id, name, surname, mail, phone_number FROM Contacts ORDER BY name;" 
            cnx = connect(
            user="root",
            password="coderslab",
            host="localhost",
            database="contacts"
            )
        
        
            try:
                cursor = cnx.cursor()
                cursor.execute(sql2)
                
            except:
                raise
            
            contacts = []
            for row in cursor:
                contact = Contact(row[0], row[1], row[2], row[3], row[4])
                contacts.append(contact)
            
            ctx = {'contact_list': contacts}
                    
            return render(request, "contact_list.html", ctx)
        
        elif SORT == "Sort by modification":      
            sql2 = "SELECT id, name, surname, mail, phone_number FROM Contacts ORDER BY id;" 
            cnx = connect(
            user="root",
            password="coderslab",
            host="localhost",
            database="contacts"
            )
        
        
            try:
                cursor = cnx.cursor()
                cursor.execute(sql2)
                
            except:
                raise
            
            contacts = []
            for row in cursor:
                contact = Contact(row[0], row[1], row[2], row[3], row[4])
                contacts.append(contact)
            
            ctx = {'contact_list': contacts}
                    
            return render(request, "contact_list.html", ctx)
        
    
class FindContact(View):    
    
    def get(self, request):
        return render(request, "find_contact.html")
        
    def post(self, request):
        
        find_contact_surname = request.POST.get("contact_surname")
        find_contact_phone_number = request.POST.get("contact_phone_number")
        
        find_contact_surname == "Find by surname"
        
        
        sql = "SELECT id, name, surname, mail, phone_number FROM Contacts WHERE surname='%s';" % find_contact_surname
        cnx = connect(
        user="root",
        password="coderslab",
        host="localhost",
        database="contacts"
        )

    
        try:
            cursor = cnx.cursor()
            cursor.execute(sql)
        
        except:
            raise
        
        contacts = []
        for row in cursor:
            contact = Contact(row[0], row[1], row[2], row[3], row[4])
            contacts.append(contact)
        
        ctx = {'contact_list': contacts}
        
        return render(request, "find_list.html", ctx)
    
    
class EditContact(View):
    
    def get(self, request, contact_id):      
                
        sql = "SELECT id, name, surname, mail, phone_number FROM Contacts WHERE id=%s;" % contact_id
        cnx = connect(
        user="root",
        password="coderslab",
        host="localhost",
        database="contacts"
        )

    
        try:
            cursor = cnx.cursor()
            cursor.execute(sql)
        
        except:
            raise
            
        contact_from_cursor = cursor.fetchone()
        contact = Contact(
            contact_from_cursor[0],
            contact_from_cursor[1],
            contact_from_cursor[2],
            contact_from_cursor[3],
            contact_from_cursor[4])
        
        cursor.close()
        cnx.close()
        
#         ctx = {'name': contact.name,
#                'surname': contact.surname,
#                'mail': contact.mail,
#                'phone_number': contact.phone_number
#             
#             }
        
        ctx = {'contact' : contact}     # to jest alternatywa dla tego co na gorze, reszte zalatwiamy w show_contact.html poprzez dodanie contact. przed name surname itd...
        
        return render(request, "edit_contact.html", ctx)
        
    def post(self, request, contact_id):
        edited_contact_name = request.POST.get("contact_name")
        edited_contact_surname = request.POST.get("contact_surname")
        edited_contact_mail = request.POST.get("contact_mail")
        edited_contact_phone_number = request.POST.get("contact_phone_number")
        
        query = """
        UPDATE Contacts SET name='%s', surname='%s', mail='%s', phone_number='%s' where id='%s';
                """ % (edited_contact_name, edited_contact_surname, edited_contact_mail, edited_contact_phone_number)
                
        cnx = connect(
        user="root",
        password="coderslab",       
        host="localhost",
        database="contacts"
        )

    
        try:
            cursor = cnx.cursor()
            cursor.execute(query)
            cnx.commit()
        
        except:
            raise
            
               
        cursor.close()
        cnx.close()
        
        return HttpResponseRedirect("http://www.onet.pl")
        
    
"""
TO NIE JEST JESZCZE SKONCZONE, TRZEBA PRZEMYSLEC EDYTOWANIE KONTAKTOW. POWINNO BYC PODOBNIE JAK
CONTACT LIST MA PODLINKOWANE DLA KAZDEGO KONTAKTU SHOW_CONTACT I TWORZY 127.0.0.1:8000/show/contact_id





"""
    

        

    
        
        


