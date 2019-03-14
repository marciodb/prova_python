import Screenshot.screenshot



class Print_telas:


   def Print(self):
        self.driver.get_screenshot_as_file('teste.jpeg')