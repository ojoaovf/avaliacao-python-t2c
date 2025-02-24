from botcity.web import WebBot, Browser
from botcity.core import DesktopBot

from prj_T2C_GoogleViagens.classes.TravelExplore import TravelExplore
from prj_T2C_GoogleViagens.classes_t2c.utils.T2CMaestro import T2CMaestro, LogLevel, ErrorType
from prj_T2C_GoogleViagens.classes_t2c.utils.T2CExceptions import BusinessRuleException
import datetime

#Classe responsável pelo processamento principal, necessário preencher com o seu código no método execute
class T2CProcess:
    """
    Classe responsável pelo processamento principal.

    Parâmetros:
    
    Retorna:
    """
    #Iniciando a classe, pedindo um dicionário config e o bot que vai ser usado e enviando uma exceção caso nenhum for informado
    def __init__(self, arg_dictConfig:dict, arg_clssMaestro:T2CMaestro, arg_botWebbot:WebBot=None, arg_botDesktopbot:DesktopBot=None):
        """
        Inicializa a classe T2CProcess.

        Parâmetros:
        - arg_dictConfig (dict): dicionário de configuração.
        - arg_clssMaestro (T2CMaestro): instância de T2CMaestro.
        - arg_botWebbot (WebBot): instância de WebBot (opcional, default=None)
        - arg_botDesktopbot (DesktopBot): instância de DesktopBot (opcional, default=None)

        Retorna:

        Raises:
        - Exception: caso nenhum bot seja fornecido.
        """
        if(arg_botWebbot is None and arg_botDesktopbot is None): raise Exception("Não foi possível inicializar a classe, forneça pelo menos um bot")
        else:
            self.var_botWebbot = arg_botWebbot
            self.var_botDesktopbot = arg_botDesktopbot
            self.var_dictConfig = arg_dictConfig
            self.var_clssMaestro = arg_clssMaestro
            self.var_listDadosViagem = []
            
    #Parte principal do código, deve ser preenchida pelo desenvolvedor
    #Acesse o item a ser processado pelo arg_tplQueueItem
    def execute(self, arg_tplQueueItem:tuple):
        """
        Método principal para execução do código.

        Parâmetros:
        - arg_tplQueueItem (tuple): item da fila a ser processado.

        Retorna:
        """
        var_clssTravelExplore = TravelExplore(arg_dictConfig=self.var_dictConfig, 
        arg_clssMaestro=self.var_clssMaestro)
        var_strPais = arg_tplQueueItem[7]
        
        var_listDadosViagem = var_clssTravelExplore.pesquisar_viagem(arg_listDadosViagem = self.var_listDadosViagem,
                                                                     arg_strOrigem = "São Paulo",
                                                                     arg_strDestino = var_strPais, 
                                                                     arg_strDataPartida = "20/08/2025", 
                                                                     arg_strDataVolta = "23/08/2025")

        return var_listDadosViagem
