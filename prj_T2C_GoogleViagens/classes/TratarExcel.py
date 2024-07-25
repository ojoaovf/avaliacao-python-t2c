from prj_T2C_GoogleViagens.classes_t2c.utils.T2CMaestro import T2CMaestro, LogLevel, ErrorType

import pandas as pd
from babel.numbers import parse_decimal

class TratarExcel:
    """
    Classe responsável pelo processamento dos dados no Excel.

    Parâmetros:
    
    Retorna:
    """
    def __init__(self, arg_dictConfig:dict, arg_clssMaestro:T2CMaestro):
        """
        Inicializa a classe TratarExcel.

        Parâmetros:
        - arg_dictConfig (dict): dicionário de configuração.
        - arg_clssMaestro (T2CMaestro): instância de T2CMaestro.

        Retorna:

        Raises:
        """
        self.var_dictConfig = arg_dictConfig
        self.var_clssMaestro = arg_clssMaestro

    def inserir_e_tratar_excel(self, arg_listDadosViagem: list, arg_strCaminhoPlanilha: str):
        """
        Recebe uma lista de dicionários contendo dados de viagem, converte para um DataFrame do pandas
        e exporta esses dados para um arquivo Excel. Além disso, ordena os dados pelo valor da viagem
        para identificar os 10 destinos mais baratos e exporta esses destinos para uma segunda planilha
        no mesmo arquivo Excel.

        Parâmetros:
        - arg_listDadosViagem (list): Lista de dicionários contendo dados de viagem, onde cada dicionário possui 
        as chaves 'cidade' e 'valorviagem'.

        - arg_strCaminhoPlanilha (str): String onde a planilha será salva.
        """
        try:
            self.var_clssMaestro.write_log(f"Criando e tratando da planilha...")

            for viagem in arg_listDadosViagem:
                viagem['valorviagem'] = parse_decimal(viagem['valorviagem'], locale='pt_BR')

            var_dfDadosViagem = pd.DataFrame(arg_listDadosViagem)

            with pd.ExcelWriter(arg_strCaminhoPlanilha) as writer:
                var_dfDadosViagem.to_excel(writer, index=False, sheet_name='Todos')

            var_dfDadosViagemOrdenados = var_dfDadosViagem.sort_values(by='valorviagem').head(10)
            with pd.ExcelWriter(arg_strCaminhoPlanilha, mode='a', engine='openpyxl') as writer:  # 'a' para append
                var_dfDadosViagemOrdenados.to_excel(writer, index=False, sheet_name='Baratos')

            self.var_clssMaestro.write_log(f"Criação e tratamento finalizados com sucesso")

        except Exception as exception:
            raise Exception(f"Houve um erro ao processar o método 'inserir_e_tratar_excel' na classe 'TratarExcel' : {exception}")