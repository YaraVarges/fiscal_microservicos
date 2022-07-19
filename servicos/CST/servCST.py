from flask import Flask, request
from flask import jsonify
from pymemcache.client import base

servico = Flask(__name__)


IS_ALIVE = "yes" #no
VERSION = "0.1"
AUTHOR = "YARA"
EMAIL = "VARGES98@GMAIL.COM"
BANCO_VOLATIL = "banco_CST"
PORTA_BANCO = 11211


@servico.route("/isalive/")
def is_alive():
    return IS_ALIVE


@servico.route("/info/")
def get_info():
    info = jsonify(
        version=VERSION,
        author=AUTHOR,
        email=EMAIL
    )

    return info

@servico.route("/gravar/", methods=["post", "get"])
def gravar():
    listagem = request.get_json()
    if listagem:
        cliente = base.Client((BANCO_VOLATIL, PORTA_BANCO))
        cliente.set("cst", listagem)

        cliente.close()

    return "OK"


@servico.route("/lista/")
def get_cst():
    cliente = base.Client((BANCO_VOLATIL, PORTA_BANCO))
    listagem = cliente.get("cst")
    cliente.close()

    return listagem

if __name__ == "__main__":
    servico.run(
        host = "0.0.0.0",
        debug=True
    )


#PARA RODAR SERVIÇO CLICAR NO PLAY DO PYTHON
#Primeiro Rodar servicos.py em seguida rodar cliente.py e ver as noticias como saida no prompt
#Rodar em janelas do prompt separadamente
#Executado durante a aula na versao2 o comando docker build . (dentro de /versao2/)
#Iniciado montagem do arquivo docker-compose