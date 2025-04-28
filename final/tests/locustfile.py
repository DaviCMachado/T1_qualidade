from locust import HttpUser, task, between
from bs4 import BeautifulSoup

class SiteUser(HttpUser):
    wait_time = between(1, 3)
    host = "http://127.0.0.1:5000"

    def on_start(self):
        """
        Executa a primeira ação ao iniciar o teste: acessar a página de login.
        """
        csrf_token = self.obter_csrf_token("/login")
        if not csrf_token:
            return

    def obter_csrf_token(self, url):
        """
        Função que acessa uma página e retorna o CSRF token.
        """
        response = self.client.get(url)
        if response.status_code != 200:
            return None
        
        soup = BeautifulSoup(response.text, "html.parser")
        csrf_token = soup.find('input', {'name': 'csrf_token'})  
        if csrf_token:
            return csrf_token['value']
        else:
            return None

    @task(3)
    def acessar_home(self):
        """
        Realiza o GET na página inicial para obter CSRF token.
        """
        csrf_token = self.obter_csrf_token("/")
        if not csrf_token:
            return

    @task(2)
    def acessar_login(self):
        """
        Realiza o GET na página de login para obter CSRF token.
        """
        csrf_token = self.obter_csrf_token("/login")
        if not csrf_token:
            return
