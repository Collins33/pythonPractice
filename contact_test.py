import unittest # Importing the unittest module
from contact import Contact # Importing the contact class
import pyperclip#import pyperclip module

class TestContact(unittest.TestCase):


# Items up here .......

    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_contact = Contact("James","Muriuki","0712345678","james@ms.com") # create contact object
    def tearDown(self):
        '''
        tearDown method that does clean up after each test case has run.
        '''
        Contact.contact_list=[]#clear the list after every test

    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''

        self.assertEqual(self.new_contact.first_name,"James")
        self.assertEqual(self.new_contact.last_name,"Muriuki")
        self.assertEqual(self.new_contact.number,"0712345678")
        self.assertEqual(self.new_contact.email,"james@ms.com")

    def test_save_contact(self):
        self.new_contact.saveContact()
        self.assertEqual(len(Contact.contact_list),1)
        #save multiple contacts
    def test_saveMultiple_contact(self):
        self.new_contact.saveContact()#save the setup object
        test_contact=Contact("Test","user","0712345678","test@user.com")#second object
        test_contact.saveContact()#save second object into the array
        self.assertEqual(len(Contact.contact_list),2)
        #test to delete contact_list
    def test_deleteContact_contact(self):
        self.new_contact.saveContact()#save the setup object
        test_contact=Contact("Test","user","0712345678","test@user.com")#second object
        test_contact.saveContact()#save second object into the array
        test_contact.deleteContact()
        self.assertEqual(len(Contact.contact_list),1)
    #find contact by number
    def test_findContact_contact(self):
        self.new_contact.saveContact()
        test_contact = Contact("Test","user","0711223344","test@user.com") # new contact
        test_contact.saveContact()
        found_contact=Contact.findContact("0711223344")
        self.assertEqual(found_contact.number,test_contact.number)
    #check if a contact exists after passing a number
    def test_contact_exists(self):
        self.new_contact.saveContact()
        test_contact = Contact("Test","user","0711223344","test@user.com") # new contact
        test_contact.saveContact()
        contact_exists=Contact.contactExists("0711223344")
        self.assertTrue(contact_exists)
    #return all contacts
    def test_allContacts_exists(self):
        self.assertEqual(Contact.displayContact(),Contact.contact_list)
    #copies number to the clipboard
    def test_copy_email(self):
        '''
        Test to confirm that we are copying the email address from a found contact
        '''

        self.new_contact.saveContact()
        Contact.copy_email("0712345678")

        self.assertEqual(self.new_contact.email,pyperclip.paste())


if __name__ == '__main__':
    unittest.main()
