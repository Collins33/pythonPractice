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

    def __init__(self,first_name,last_name,number,email):

      # docstring removed for simplicity

        self.first_name = first_name
        self.last_name = last_name
        self.number = number
        self.email = email
