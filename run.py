#!/usr/bin/env python3.6

from contact import Contact
import pyperclip
#creating the contact
def createContact(fname,lname,phone,email):
    new_contact=Contact(fname,lname,phone,email)
    return new_contact
#save contacts
def saveContact(contact):
    contact.save()
#delete contact
def deleteContact(contact):
    contact.delete()
#find contact
def findContact(number):
    Contact.find_by_number(number)
def check_existing_contacts(number):
    '''
    Function that check if a contact exists with that number and return a Boolean
    '''
    return Contact.contact_exist(number)
def display_contacts():
    '''
    Function that returns all the saved contacts
    '''
    return Contact.display_contacts()
def copy_number(number):
    Contact_found=Contact.findContact(number)
    pyperclip.copy(Contact_found.number)
#the main Function
def main():
    print("Hello welcome to your contact list.What is your name?")
    user_name=input()
    print(f"Hello {user_name}.What would you like to do?")
    print("\n")

    while True:
        print("Use these short codes : cc - create a new contact, dc - display contacts, fc -find a contact, ex -exit the contact list ")
        short_code=input().lower()
        if short_code =='cc':
            print("New Contact")
            print("-"*10)

            print ("First name ....")
            f_name = input()

            print("Last name ...")
            l_name = input()

            print("Phone number ...")
            p_number = input()

            print("Email address ...")
            e_address = input()
            saveContact(createContact(f_name,l_name,p_number,e_address))#createcontact then save it

if __name__ == '__main__':

    main()
