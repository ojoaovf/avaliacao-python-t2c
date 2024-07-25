from prj_T2C_GoogleViagens.classes_t2c.utils.T2CMaestro import T2CMaestro, LogLevel, ErrorType

from clicknium import clicknium as cc, locator, ui

class ExtrairDadosMundiais:
    """
    Classe responsável pelo processamento da extração dos dados no site 'https://www.dadosmundiais.com/turismo.php'.

    Parâmetros:
    
    Retorna:
    """

    def __init__(self, arg_dictConfig:dict, arg_clssMaestro:T2CMaestro):
        """
        Inicializa a classe ExtrairDadosMundiais.

        Parâmetros:
        - arg_dictConfig (dict): dicionário de configuração.
        - arg_clssMaestro (T2CMaestro): instância de T2CMaestro.

        Retorna:

        Raises:
        """
        self.var_dictConfig = arg_dictConfig
        self.var_clssMaestro = arg_clssMaestro
            
    def execute(self):
        """
        Executa a extração de dados de países a partir de uma página web específica.
        Inicializa o navegador controlado pela biblioteca Clicknium e navega até a URL configurada
        em var_dictConfig['UrlSiteDadosMundiais']. Extrai o nome de países encontrados em uma tabela
        específica e retorna uma lista com esses nomes.

        Parâmetros:

        Retorna:
            list: Lista contendo os nomes dos países extraídos da página.
        """
        try:
            self.var_clssMaestro.write_log(f"Iniciando extração no site '{self.var_dictConfig['UrlSiteDadosMundiais']}'")

            var_listPaises = []
            var_tabNavegador = cc.edge.open(self.var_dictConfig['UrlSiteDadosMundiais'])

            for i in range(2, 4): 
                var_strPais = var_tabNavegador.find_element_by_xpath(f'//*[@id="main"]/div[3]/div[2]/table/tbody/tr[{i}]/td[2]/a').get_text()
                var_listPaises.append(var_strPais)

            var_tabNavegador.close() 

            self.var_clssMaestro.write_log(f"Extração finalizada com sucesso")   

            return var_listPaises
        
        except Exception as exception:
            raise Exception(f"Houve um erro ao processar o metodo 'execute' da classe 'ExtrairDadosMundiais' : {exception}")
