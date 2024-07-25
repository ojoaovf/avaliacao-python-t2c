from clicknium import clicknium as cc, locator, ui
from pywinauto.keyboard import send_keys
import time
import pyautogui
import pandas as pd

var_listPaises = []
var_tabNav = cc.edge.open("https://www.dadosmundiais.com/turismo.php")

for i in range(2, 5):
    var_strPais = var_tabNav.find_element_by_xpath(f'//*[@id="main"]/div[3]/div[2]/table/tbody/tr[{i}]/td[2]/a').get_text()
    var_listPaises.append(var_strPais)

# print(var_listPaises)

# cc.edge.browsers[0].close()

var_listDadosViagem = []

for destino in var_listPaises:
    var_tabNav.goto("https://www.google.com/travel/explore")

    var_tabNav.find_element(locator.chrome.google.combobox_de_onde).click()
    cc.send_text("São Paulo")
    send_keys('{ENTER}')
    var_tabNav.find_element(locator.chrome.google.combobox_para_onde).click()
    cc.send_text(destino)
    time.sleep(2)
    var_dictLocatorDinamico = {"Destino": destino}
    var_tabNav.find_element(locator.chrome.google.option_frança_img, var_dictLocatorDinamico).click()






    # var_tabNav.find_element(locator.chrome.google.combobox_de_onde).click()
    var_tabNav.find_element(locator.chrome.google.button_kn4yub_zsbbeb).click()
    time.sleep(5)

    var_tabNav.find_element(locator.chrome.google.tab_snlbpb).click()
    time.sleep(2)
    
    var_tabNav.find_element(locator.chrome.google.text_partida).set_text("20/04/2025")
    send_keys('{TAB}')

    time.sleep(2)
    var_tabNav.find_element(locator.chrome.google.text_volta).set_text("23/04/2025")
    time.sleep(2)
    var_tabNav.find_element(locator.chrome.google.text_volta).click()
    send_keys('{TAB}')

    time.sleep(5)

    for i in range(1,5):
        var_strCidade = var_tabNav.find_element_by_xpath(f'//*[@id="yDmH0d"]/c-wiz[2]/div/div[2]/div/c-wiz/div[2]/div/div/div[1]/main/div/div[2]/div/ol/li[{i}]/div/div[2]/div[1]/h3').get_text()
        var_strValorViagem = var_tabNav.find_element_by_xpath(f'//*[@id="yDmH0d"]/c-wiz[2]/div/div[2]/div/c-wiz/div[2]/div/div/div[1]/main/div/div[2]/div/ol/li[{i}]/div/div[2]/div[2]/div[1]/div[1]/span').get_text()    

        var_dictDadosViagem = {
        'cidade': var_strCidade,
        'valorviagem': var_strValorViagem.replace('\xa0', '')
        }
        var_listDadosViagem.append(var_dictDadosViagem)
    
df = pd.DataFrame(var_listDadosViagem)
df.to_excel('viagens.xlsx', index=False, sheet_name="Todos")
print(df)

#Ordenar pelo valor da viagem para encontrar os 10 destinos mais baratos
df_ordenado = df.sort_values(by='valorviagem').head(10)

# Exportar para um arquivo Excel com duas planilhas
with pd.ExcelWriter('viagens.xlsx') as writer:
    df.to_excel(writer, index=False, sheet_name='Todos')
    df_ordenado.to_excel(writer, index=False, sheet_name='Barato')

# Exibir os DataFrames
print("Todos os destinos:")
print(df)
print("\nOs 10 destinos mais baratos:")
print(df_ordenado)