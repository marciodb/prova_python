from selenium.webdriver.common.by import By


class Validacoes:
    def __init__(self, driver):
        self.driver = driver

    def Produto_Carrinho(self, driver):

        produto = self.driver.find_element(By.XPATH, "/html/body/div/div/div[2]/h1")
        self.assertEqual(produto, "Blouse")





