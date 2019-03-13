from selenium.webdriver.common.by import By


class Validacoes:

    def __init__(self, driver):
        self.driver = driver

    def Produto_Carrinho(self, driver):

        produto = self.driver.find_element(By.PARTIAL_LINK_TEXT, "Product successfully added to your shopping cart")
        self.assertEqual(produto, "Blouse")

    def Endereco(self, driver):

        endereco = self.driver.find_element(By.PARTIAL_LINK_TEXT, "Product successfully added to your shopping cart")
        self.assertEqual(endereco, "Product successfully added to your shopping cart")

    def Compra(self, driver):

        compra = self.driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div[3]/div/div/p/strong")
        self.assertEqual(compra, "Your order on My Store is complete.")






