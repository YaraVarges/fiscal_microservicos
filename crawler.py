import requests
import json
from time import sleep

LISTAGEM_CFOP = "/home/yara/Área de trabalho/DDI/projAval_IUni_Yara/lista/cfop.json"
LISTAGEM_CSOSN = "/home/yara/Área de trabalho/DDI/projAval_IUni_Yara/lista/csosn.json"
LISTAGEM_CST = "/home/yara/Área de trabalho/DDI/projAval_IUni_Yara/lista/cst.json"

URL_CFOP = "http://localhost:5001/gravar/"
URL_CSOSN = "http://localhost:5002/gravar/"
URL_CST = "http://localhost:5003/gravar/"

def enviar (url, json_lista):
    with open(json_lista, "r") as arquivo:
        listagem = json.load(arquivo)
        arquivo.close()

        resposta = requests.post(url, json=json.dumps(listagem))
        if resposta.ok:
            resposta = "LISTAGENS ENVIADAS COM SUCESSO"
        else:
            resposta = "ERRO NO ENVIO DAS LISTAGENS: " + resposta.text
        
        return resposta


if __name__ == "__main__":
    while True:
        resposta = enviar(URL_CFOP, LISTAGEM_CFOP)
        print("Enviado serviço CFOP. Resposta: " + resposta)

        resposta = enviar(URL_CSOSN, LISTAGEM_CSOSN)
        print("Enviado serviço CSOSN. Resposta: " + resposta)

        resposta = enviar(URL_CST, LISTAGEM_CST)
        print("Enviado serviço CST. Resposta: " + resposta)

        sleep(10)