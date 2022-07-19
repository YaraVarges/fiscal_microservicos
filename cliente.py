import json
import aiohttp
import asyncio

# rotas dos serviços
URL_SERVICO_CFOP = "http://localhost:5001/"
CFOP_IS_ALIVE = URL_SERVICO_CFOP + "isalive/"
CFOP = URL_SERVICO_CFOP + "lista/"

URL_SERVICO_CSOSN = "http://localhost:5002/"
CSOSN_IS_ALIVE = URL_SERVICO_CSOSN + "isalive/"
CSOSN = URL_SERVICO_CSOSN + "lista/"

URL_SERVICO_CST = "http://localhost:5003/"
CST_IS_ALIVE = URL_SERVICO_CST + "isalive/"
CST = URL_SERVICO_CST + "lista/"

async def acessar(url):
    dados = None

    async with aiohttp.ClientSession() as sessao:
        async with sessao.get(url) as resposta:
            dados = await resposta.text()
            
    return dados

async def CFOP_is_alive():
    alive = False

    if await acessar(CFOP_IS_ALIVE) == "yes":
        alive = True

    return alive

async def CSOSN_is_alive():
    alive = False

    if await acessar(CSOSN_IS_ALIVE) == "yes":
        alive = True

    return alive

async def CST_is_alive():
    alive = False

    if await acessar(CST_IS_ALIVE) == "yes":
        alive = True

    return alive

async def get_cfop():
    dados = await acessar(CFOP)
    dados = json.loads(dados)

    return dados["cfop"]

async def get_csons():
    dados = await acessar(CSOSN)
    dados = json.loads(dados)

    return dados["csosn"]

async def get_CST():
    dados = await acessar(CST)
    dados = json.loads(dados)

    return dados["cst"]

def imprimir(tipo_lista, listas):
    print("------------Listagem de " + tipo_lista)
    for lista in listas:
        print("Código: " + lista['data'] + " - " + lista['titulo'])

async def acessar_CFOP():
    while True:
        if await CFOP_is_alive():
            print("Listagem do serviço de CFOP estão disponiveis.")
            listas = await get_cfop()
            imprimir("CFOP: Devoluções---------", listas)
        else:
            print("Listagem do serviço de CFOP indisponiveis")
        await asyncio.sleep(10)

async def acessar_CSOSN():
    while True:
        if await CSOSN_is_alive():
            print("Listagem do serviço de CSOSN estão disponiveis.")
            listas = await get_csons()
            imprimir("CSOSN: Regime Simples Nacional----------", listas)
        else:
            print("Listagem do serviço de CSOSN indisponiveis")
            
        await asyncio.sleep(10)

async def acessar_CST():
    while True:
        if await CST_is_alive():
            print("Listagem do serviço de CST estão disponiveis.")
            listas = await get_CST()
            imprimir("CST: Regime Normal-----------", listas)
        else:
            print("Listagem do serviço de CST indisponiveis")
            
        await asyncio.sleep(10)

async def executar():
    await asyncio.gather(acessar_CFOP(), acessar_CSOSN(), acessar_CST())

if __name__ == "__main__":
    asyncio.run(executar())
