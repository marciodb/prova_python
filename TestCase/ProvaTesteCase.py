import unittest
from selenium import webdriver
import PageObjects
import time
from selenium.webdriver.support.ui import WebDriverWait
from PageTasks.EscolheProdutoTask import MainPage
import PageTasks.EscolheProdutoTask
import Screenshot.screenshot
import VerificationPoints

class ProvaTesteCase(unittest.TestCase):


    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.get("http://automationpractice.com/index.php?")

    def Print(self):
        self.Print()
    def test_search_in_python_org(self):
        main_page = MainPage(self.driver)
        main_page.click_go_button()

    def Add_button(self):
        main_page = MainPage(self.driver)
        main_page.Add_Cart()

    def Verification_Produto(self):
        Validacoes = MainPage(self.driver)
        Validacoes.Produto_Carrinho()


    def Proceed_To_Checkout1(self):

        main_page = MainPage(self.driver)
        main_page.Proceed_Checkout1()

    def Proceed_Checkout4(self):
        main_page = MainPage(self.driver)
        main_page.Proceed_Checkout4()


    def Email_Address(self):

        main.page = MainPage(self.driver)
        main_page.Email_Address()

    def Email_Address_CLICK(self):

        main.page = MainPage(self.driver)
        main_page.Email_Address_Click()

    def Radio_Button(self):
        main.page = MainPage(self.driver)
        main_page.Radio_Button()

    def First_Name(self):
        main.page = MainPage(self.driver)
        main_page.First_Name()

    def Last_Name(self):
        main.page = MainPage(self.driver)
        main_page.Last_Name()

    def Password(self):
        main.page = MainPage(self.driver)
        main_page.Password()

    def Day(self):
        main.page = MainPage(self.driver)
        main_page.Day()

    def Month(self):
        main.page = MainPage(self.driver)
        main_page.Month()

    def Year(self):
        main.page = MainPage(self.driver)
        main_page.Year()

    def Address(self):
        main.page = MainPage(self.driver)
        main_page.Address()

    def City(self):
        main.page = MainPage(self.driver)
        main_page.City()

    def State(self):
        main.page = MainPage(self.driver)
        main_page.State()

    def Postal_Code(self):
        main.page = MainPage(self.driver)
        main_page.Postal_Code()

    def Country(self):
        main.page = MainPage(self.driver)
        main_page.Country()

    def Mobile_Phone(self):
        main.page = MainPage(self.driver)
        main_page.Mobile_Phone()

    def My_Address(self):
        main.page = MainPage(self.driver)
        main_page.My_Address()

    def Confirm_Cadastro(self):
        main.page = MainPage(self.driver)
        main_page.Confirm_Cadastro()

    def Proceed_Checkout2(self):
        main.page = MainPage(self.driver)
        main_page.Proceed_Checkout2()

    def Term_Service(self):
        main.page = MainPage(self.driver)
        main_page.Term_Service()

    def Proceed_Checkout3(self):
        main.page = MainPage(self.driver)
        main_page.Proceed_Checkout()

    def Form_Pagamento(self):
        main.page = MainPage(self.driver)
        main_page.Form_Pagamento()

    def Confirm_Pagagmento(self):
        main.page = MainPage(self.driver)
        main_page.Confirm_Pagagmento()

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()



