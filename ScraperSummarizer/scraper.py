from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.alert import Alert
from selenium.common.exceptions import NoSuchElementException
from time import sleep
from re import sub

class Scraper:
    def __init__(self) -> None:
        options = webdriver.ChromeOptions()
        options.add_experimental_option("useAutomationExtension", False)
        options.add_experimental_option("excludeSwitches",["enable-automation"])
        options.add_argument('--ignore-certificate-errors')
        options.add_argument('--ignore-ssl-errors')
        user_agent ="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36"
        options.add_argument(f"user-agent={user_agent}") #You need to add your user agent
        options.add_argument('headless')
        options.add_argument("--window-size=1920,1080")
        options.add_argument('log-level=3')

        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
        self.driver.maximize_window()
        
        self.driver.get('https://www.google.com/')
        self.driver.find_element(By.ID, 'L2AGLb').click() #Accept cookie

        #Switch language to english
        self.driver.get("https://www.google.com/preferences?hl=pl&fg=1#languages")
        self.driver.find_element(By.XPATH, '//*[@id="langten"]/div/span[1]').click()
        self.driver.find_element(By.XPATH, '//*[@id="form-buttons"]/div[1]').click()
        Alert(self.driver).dismiss()

        self.driver.get('https://www.google.com/')

        self.queries = []

    def enter_input(self, user_input: str) -> None:
        self.driver.find_element(By.CLASS_NAME, 'gLFyf.gsfi').send_keys(user_input)

        search = self.driver.find_element(By.CLASS_NAME, "FPdoLc.lJ9FBc")
        search.find_element(By.CLASS_NAME, "gNO89b").click()


    def get_google_queries(self) -> dict:
        google_queries = self.driver.find_element(By.CLASS_NAME, "Wt5Tfe")
        elements = google_queries.find_elements(By.CLASS_NAME, "r21Kzd")

        quries = google_queries.find_elements(By.CLASS_NAME,"iDjcJe.IX9Lgd.wwB5gf")

        answers = google_queries.find_elements(By.CLASS_NAME, 'hgKElc')

        for element, query, answer in zip(elements, quries, answers):
            element.click()
            self.queries.append(f'{query.text} - {answer.text}')
            sleep(.1)

        if self.queries != []:
            return "\n\n".join(self.queries)
        else:
            return 'There is not queries and ansewers from google'

    def google_summary(self) -> None:
        try:
            text = self.driver.find_element(By.CLASS_NAME, 'V3FYCf').text
            return text

        except NoSuchElementException:
            return 'There is no summary from google'

        
    
    def wikipedia_page(self, user_input: str) -> None:
        self.driver.get(f'https://en.wikipedia.org/')

        self.driver.find_element(By.CLASS_NAME, 'vector-search-box-input').send_keys(user_input)
        self.driver.find_element(By.ID, 'searchButton').click()

        #If the input isn't precise
        try:
            search_result = self.driver.find_element(By.CLASS_NAME, 'mw-search-result-heading')
            search_result.find_element(By.XPATH, f'//a[@title = "{search_result.text}"]').click()
        except NoSuchElementException:
            pass


    def get_text(self) -> str:
        #deleting infobox if it exists, because it has useless information
        try:
            info_table = self.driver.find_element(By.CLASS_NAME, 'infobox')
            self.driver.execute_script("var element = arguments[0]; element. parentNode. removeChild(element);", info_table)
        except NoSuchElementException:
            pass

        paragraphs = self.driver.find_elements(By.XPATH, '//p')
        text = ''

        for x in paragraphs:
            text += f'{x.text} '

        return text
        
    def clean_text(self, text: str) -> str:
        text = sub(r"\([^()]*\)", '', text) #remove brackets with content
        text = sub(r"\[.*?\]", '', text) #remove square brackets with content

        return text

    def close(self) -> None:
        self.driver.close()