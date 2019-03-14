from PageObjects.EscolheProdutoObject import MainPageLocators
from selenium import webdriver
import unittest
from selenium.webdriver.common.by import By
import time
import random



class MainPage:

    def __init__(self, driver):
        self.driver = driver

    def click_go_button(self):

        test = MainPageLocators(self.driver)

        test.get_go_button().click()

        test.Add_cart().click()

        self.driver.get_screenshot_as_file('Produto')

        time.sleep(5)
        test.Proceed_Checkout1().click()

        test.Proceed_Checkout1().click()

        email = random.randrange(10000)
        test.Email_Address().send_keys(email,"@dbserver.com.br")
        self.driver.get_screenshot_as_file('Email')
        test.Email_Address_Click().click()

        time.sleep(5)
        test.Radio_Button().click()

        test.First_Name().send_keys("Marcio")

        test.Last_Name().send_keys("Dutra")

        test.Password().send_keys("12345")

        test.Day().send_keys(5)

        test.Month().send_keys("May")

        test.Year().send_keys("1980")

        test.Address().send_keys("Rua Primeiro de Setembro, 76")

        test.City().send_keys("Porto Alegre")

        test.State().send_keys("Alaska")

        test.Postal_Code().send_keys("00000")

        test.Country().send_keys("United States")

        test.Mobile_Phone().send_keys("993786915")

        test.My_Address().clear()
        test.My_Address().send_keys("professormarciodutra@gmail.com")

        test.Confirm_Cadastro().click()

        test.Proceed_Checkout2().click()

        self.driver.get_screenshot_as_file('Cadastro')

        self.driver.find_element_by_id("cgv").click()

        self.driver.find_element_by_xpath("/html/body/div/div[2]/div/div[3]/div/div/form/p/button").click()

        test.Form_Pagamento().click()

        self.driver.find_element_by_xpath("/html/body/div/div[2]/div/div[3]/div/form/p/button").click()
        test.Form_Pagamento().click()

        self.driver.get_screenshot_as_file('Compra')






