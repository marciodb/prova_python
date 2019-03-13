from typing import Tuple
import PageTasks
from selenium import webdriver
import unittest
from selenium.webdriver.common.by import By
import time

class MainPageLocators:

    def __init__(self, driver):
        self.driver = driver

    def get_go_button(self):
        return self.driver.find_element(By.XPATH, '/html/body/div/div[2]/div/div[2]/div/div[1]/ul[1]/li[2]/div/div[1]/div/a[1]/img')

    def Add_cart(self):
        return self.driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div[3]/div/div/div/div[4]/form/div/div[3]/div[1]/p/button")

    def Proceed_Checkout1(self):
        return self.driver.find_element(By.PARTIAL_LINK_TEXT, "Proceed to checkout")

    def Proceed_Checkout1(self):
        return self.driver.find_element_by_partial_link_text("Proceed to checkout")

    def Email_Address(self):
        return self.driver.find_element(By.ID,"email_create")

    def Email_Address_Click(self):
        return self.driver.find_element(By.ID, "SubmitCreate")

    def Radio_Button(self):
        return  self.driver.find_element(By.ID, "id_gender2")

    def First_Name(self):
        return  self.driver.find_element(By.ID, "customer_firstname")

    def Last_Name(self):
        return  self.driver.find_element(By.ID, "customer_lastname")

    def Password(self):
        return self.driver.find_element(By.ID, "passwd")

    def Day(self):
        return  self.driver.find_element(By.ID, "days")

    def Month(self):
        return  self.driver.find_element(By.ID, "months")

    def Year(self):
        return  self.driver.find_element(By.ID, "years")

    def Address(self):
        return self.driver.find_element(By.ID, "address1")

    def City(self):
        return  self.driver.find_element(By.ID, "city")

    def State(self):
        return  self.driver.find_element(By.ID, "id_state")

    def Postal_Code(self):
        return  self.driver.find_element(By.ID, "postcode")

    def Country(self):
        return  self.driver.find_element(By.ID, "id_country")

    def Mobile_Phone(self):
        return  self.driver.find_element(By.ID, "phone_mobile")

    def My_Address(self):
        return  self.driver.find_element(By.ID, "alias")

    def Confirm_Cadastro(self):
        return  self.driver.find_element(By.ID, "submitAccount")

    def Proceed_Checkout2(self):
        return  self.driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div[3]/div/form/p/button")

    def Term_Service(self):
        return  self.driver.find_element("cgv")

    def Proceed_Checkout3(self):
        return  self.driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div[3]/div/div/form/p/button")

    def Form_Pagamento(self):
        return  self.driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div[3]/div/div/div[3]/div[1]/div/p/a")



