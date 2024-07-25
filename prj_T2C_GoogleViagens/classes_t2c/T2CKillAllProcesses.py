from botcity.web import WebBot, Browser
from botcity.core import DesktopBot
import psutil
from prj_T2C_GoogleViagens.classes_t2c.utils.T2CMaestro import T2CMaestro, LogLevel, ErrorType
from prj_T2C_GoogleViagens.classes_t2c.utils.T2CExceptions import BusinessRuleException

class T2CKillAllProcesses:
    """
    Classe para finalizar todos os processos necessários.
    Feita para ser invocada em casos de system exceptions no processamento, para resetar o processamento.
    Pode ser usado em outras partes do processo também, dependendo de como a automação for programada.

    Parâmetros:

    Retorna:
    """

    def __init__(self, arg_dictConfig:dict, arg_clssMaestro:T2CMaestro, arg_botWebbot:WebBot=None, arg_botDesktopbot:DesktopBot=None):
        """
        Inicializa a classe T2CKillAllProcesses, pedindo um dicionário config e o bot que vai ser usado e enviando uma exceção caso nenhum for informado.

        Parâmetros:
        - arg_dictConfig (dict): dicionário de configuração.
        - arg_clssMaestro (T2CMaestro): objeto T2CMaestro.
        - arg_botWebbot (WebBot): objeto WebBot. (opcional, default=None)
        - arg_botDesktopbot (DesktopBot): objeto DesktopBot. (opcional, default=None)

        Retorna:
        """

        if(arg_botWebbot is None and arg_botDesktopbot is None): raise Exception("Não foi possível inicializar a classe, forneça pelo menos um bot")
        else:
            self.var_botWebbot = arg_botWebbot
            self.var_botDesktopbot = arg_botDesktopbot
            self.var_dictConfig = arg_dictConfig
            self.var_clssMaestro = arg_clssMaestro

    def execute(self):
        """
        Executa o método para finalizar os processos necessários, apenas com a estrutura em código.

        Parâmetros:
    
        Retorna:
        
        Raises:
            - BusinessRuleException: Se ocorrer um erro de regra de negócio durante o processamento.
            - Exception: Se ocorrer um erro não tratado durante o processamento.
        """

        #Edite o valor dessa variável a no arquivo Config.xlsx
        var_intMaxTentativas = self.var_dictConfig["MaxRetryNumber"]

        for var_intTentativa in range(var_intMaxTentativas):
            try:
                self.var_clssMaestro.write_log("Finalizando processos, tentativa " + (var_intTentativa+1).__str__())
                #Insira aqui seu código para finalizar processos

                nomes_processos = ['MicrosoftEdge.exe', 'EXCEL.EXE']
                
                # Lista de nomes de processos a serem finalizados
                nomes_processos = ['MicrosoftEdge.exe', 'EXCEL.EXE']

                # Itera sobre os processos em execução
                for var_strNomeProcesso in psutil.process_iter(['pid', 'name']):
                    if var_strNomeProcesso.info['name'] in nomes_processos:
                        print(f"Finalizando processo {var_strNomeProcesso.info['name']} (PID {var_strNomeProcesso.info['pid']})")
                        var_strNomeProcesso.kill()
           
            except BusinessRuleException as exception:
                self.var_clssMaestro.write_log(arg_strMensagemLog="Erro de negócio: " + str(exception), arg_enumLogLevel=LogLevel.ERROR, arg_enumErrorType=ErrorType.BUSINESS_ERROR)

                raise
            except Exception as exception:
                self.var_clssMaestro.write_log(arg_strMensagemLog="Erro, tentativa " + (var_intTentativa+1).__str__() + ": " + str(exception), arg_enumLogLevel=LogLevel.ERROR, arg_enumErrorType=ErrorType.APP_ERROR)
                
                if(var_intTentativa+1 == var_intMaxTentativas): raise
                else: 
                    #Incluir aqui seu código para tentar novamente
                    
                    continue
            else:
                self.var_clssMaestro.write_log("Aplicativos finalizados, continuando processamento...")
                break
            