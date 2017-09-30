#build the contact class
class Contact:
    """
    Class that generates new instances of contacts.
    """

    contact_list = [] # Empty contact list

    #method to save contacts to the list
    def saveContact(self):
        #appends the object to the list
        Contact.contact_list.append(self)
    #method to delete contacts
    def deleteContact(self):
        Contact.contact_list.remove(self)

    @classmethod#decorator that says the method belongs to the whole classmethod
    def findContact(cls,number):
            #cls refers to the class
        for contact in cls.contact_list:
            if contact.number == number:
                return contact

    @classmethod
    def contactExists(cls,number):
        for contact in cls.contact_list:
            if contact.number == number:
                return True
        return False
    @classmethod
    def displayContact(cls):
       return cls.contact_list





    def __init__(self,first_name,last_name,number,email):

      # docstring removed for simplicity

        self.first_name = first_name
        self.last_name = last_name
        self.number = number
        self.email = email
