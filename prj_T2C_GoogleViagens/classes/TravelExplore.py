from prj_T2C_GoogleViagens.classes_t2c.utils.T2CMaestro import T2CMaestro, LogLevel, ErrorType

from clicknium import clicknium as cc, locator, ui 
from pywinauto.keyboard import send_keys
import time

class TravelExplore:
    """
    Classe responsável pelo processamento no site https://www.google.com/travel/explorer.

    Parâmetros:
    
    Retorna:
    """
    def __init__(self, arg_dictConfig:dict, arg_clssMaestro:T2CMaestro):
        """
        Inicializa a classe TravelExplore.

        Parâmetros:
        - arg_dictConfig (dict): dicionário de configuração.
        - arg_clssMaestro (T2CMaestro): instância de T2CMaestro.

        Retorna:

        Raises:
        """
        self.var_dictConfig = arg_dictConfig
        self.var_clssMaestro = arg_clssMaestro       

    def pesquisar_viagem(self, arg_listDadosViagem:list, arg_strOrigem:str, arg_strDestino:str, arg_strDataPartida:str, arg_strDataVolta:str):
        """
        Realiza uma pesquisa de viagem utilizando o navegador controlado pela biblioteca Clicknium.
        Inicializa a navegação até a página de pesquisa do Google Travel com os parâmetros especificados
        de origem, destino, data de partida e data de volta. Extrai informações das viagens encontradas
        e armazena em uma lista de dicionários.

        Parâmetros:
        - arg_listDadosViagem (list): Lista que será preenchida com dicionários contendo informações das viagens encontradas.
        - arg_strOrigem (str): Local de onde parte a viagem.
        - arg_strDestino (str): Destino da viagem.
        - arg_strDataPartida (str): Data de partida no formato 'dd/mm/aaaa'.
        - arg_strDataVolta (str): Data de volta no formato 'dd/mm/aaaa'.
        Retorna:

        Raises:
        """        
        try:
            var_tabNavegador = cc.edge.open(self.var_dictConfig['UrlSiteGoogleTravel'])
            
            self.var_clssMaestro.write_log(f"Pesquisando viagens com destino: '{arg_strDestino}'")

            var_tabNavegador.find_element(locator.edge.cbx_de_onde).click()
            cc.send_text(arg_strOrigem)

            send_keys('{ENTER}')
            time.sleep(5)

            var_tabNavegador.find_element(locator.edge.cbx_para_onde).double_click()
            time.sleep(2)
            cc.send_text(arg_strDestino)
            time.sleep(5)

            var_dictLocatorDinamico = {"paisdestino": arg_strDestino}
            var_tabNavegador.find_element(locator.edge.img_globo, var_dictLocatorDinamico).click()
            time.sleep(3)

            var_tabNavegador.find_element(locator.edge.fld_calendario).click()
            time.sleep(5)

            var_tabNavegador.find_element(locator.edge.fld_datas_especificas).click()
            time.sleep(2)

            var_tabNavegador.find_element(locator.edge.fld_partida).set_text(arg_strDataPartida)
            self.var_clssMaestro.write_log(f"Pesquisando data de partida: '{arg_strDestino}'")
            time.sleep(2)
            send_keys('{TAB}')
            time.sleep(5)

            var_tabNavegador.find_element(locator.edge.fld_volta).set_text(arg_strDataVolta)
            self.var_clssMaestro.write_log(f"Pesquisando data de volta: '{arg_strDataVolta}'")
            time.sleep(2)
            send_keys('{TAB}')
            time.sleep(5)

            self.var_clssMaestro.write_log("Iniciando extração das informações")

            try:
                self.var_clssMaestro.write_log(f"Extraindo informações de Cidade e Valor da viagem...")

                for i in range(1, 100):
                    var_strCidade = var_tabNavegador.find_element_by_xpath(f'//*[@id="yDmH0d"]/c-wiz[2]/div/div[2]/div/c-wiz/div[2]/div/div/div[1]/main/div/div[2]/div/ol/li[{i}]/div/div[2]/div[1]/h3').get_text()
                    var_strValorViagem = var_tabNavegador.find_element_by_xpath(f'//*[@id="yDmH0d"]/c-wiz[2]/div/div[2]/div/c-wiz/div[2]/div/div/div[1]/main/div/div[2]/div/ol/li[{i}]/div/div[2]/div[2]/div[1]/div[1]/span').get_text()    

                    var_dictDadosViagem = {
                    'cidade': var_strCidade,
                    'valorviagem': var_strValorViagem.replace('\xa0', '')
                    }
                    arg_listDadosViagem.append(var_dictDadosViagem)

                self.var_clssMaestro.write_log("Extração finalizada com sucesso")

            except Exception as exception:
                var_tabNavegador.close()

                self.var_clssMaestro.write_log(f"Informações extraidas com sucesso")
                return arg_listDadosViagem

        except Exception as exception:
            raise Exception(f"Houve um erro ao processar o metodo 'pesquisar_viagem' da classe 'TravelExplore' : {exception}")
