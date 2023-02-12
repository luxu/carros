import json
from pathlib import Path

from requests import get

line = "-"*50

def get_model_car():
    url = "https://www.webmotors.com.br/api/category"

    response = get(url)

    result = response.json()
    list_models = []
    for modelo in result:
        nome = modelo['Nome'].lower()
        list_models.append(nome)
    return list_models

def crawl_cars(list_models):
    headers = {
        'authority': 'www.webmotors.com.br',
        'cookie': 'at_check=true; AMCVS_3ADD33055666F1A47F000101%40AdobeOrg=1; '
                  'WebMotorsVisitor=1; WMLastFilterSearch=%7B%22car%22%3A%22suvs%2Fcarros%2F%22%2C%22bike%22%3A%22motos'
                  '%2Festoque%22%2C%22estadocidade%22%3A%22estoque%22%2C%22lastType%22%3A%22car%22%2C%22cookie%22%3A%22v3%22'
                  '%2C%22ano%22%3A%7B%7D%2C%22preco%22%3A%7B%7D%2C%22marca%22%3A%22%22%2C%22modelo%22%3A%22%22%7D; '
                  'WebMotorsSearchDataLayer=%7B%22search%22%3A%7B%22location%22%3A%7B%7D%2C%22ordination%22%3A%7B%22name'
                  '%22%3A%22Mais%20relevantes%22%2C%22id%22%3A1%7D%2C%22pageNumber%22%3A1%2C%22totalResults%22%3A81392%2C%22'
                  'vehicle%22%3A%7B%22type%22%3A%7B%22id%22%3A1%2C%22name%22%3A%22carro%22%7D%7D%2C%22'
                  'cardExhibition%22%3A%7B%22id%22%3A%221%22%2C%22name%22%3A%22Cards%20Grid%22%7D%2C%22eventType%22%3A%22'
                  'buscaRealizada%22%7D%7D; WebMotorsDataFormLeads=%7B%22dataForm%22%3A%7B%22uniqueId%22%3A45085051%2C%22'
                  'listingType%22%3A%22U%22%2C%22vehicleType%22%3A%22car%22%2C%22'
                  'idGuid%22%3A%220c2d1ff9-113a-473c-86e3-273ad2dca01a%22%2C%22make%22%3A%22PEUGEOT%22%2C%22'
                  'makeId%22%3A28%2C%22model%22%3A%222008%22%2C%22modelId%22%3A3515%2C%22version%22%3A%221.6%2016V%20'
                  'FLEX%20ALLURE%20PACK%204P%20AUTOM%C3%81TICO%22%2C%22versionId%22%3A348026%2C%22yearModel%22%3A2022%2C%22'
                  'yearFabrication%22%3A2021%2C%22price%22%3A77490%2C%22storeName%22%3A%22Movida%20Seminovos%20Feira%20de%20'
                  'Santana%22%2C%22storeDocument%22%3A%2207976147000918%22%2C%22sellerId%22%3A3878771%2C%22'
                  'sellerType%22%3A%22PJ%22%2C%22city%22%3A%22Feira%20de%20Santana%22%2C%22hyundaiGroup%22%3Afalse%7D%7D; '
                  'mbox=session#8a00cf65489240caab8008ec2dec11fe#1676129029|PC#8a00cf65489240caab8008ec2dec11fe.34_0'
                  '#1739371777; AMCV_3ADD33055666F1A47F000101%40AdobeOrg=1176715910%7CMCIDTS%7C19400%7CMCMID%7C346228617967'
                  '81007867246275422075936572%7CMCOPTOUT-1676134368s%7CNONE%7CvVersion%7C5.4.0',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36'
    }
    index = 1
    results = []
    for model in list_models:
        url = f'https://www.webmotors.com.br/api/search/car?url=https://www.webmotors.com.br/{model}'
        response = get(url, headers=headers)
        for cars in response.json()['NewSearchResults']:
            id = cars['id']
            fabricante = cars['make']
            model = cars['model']
            version = cars['version']
            price = cars['price']
            year = cars['year']
            travelledDistance = cars['travelledDistance']
            location = cars['location']
            photos = cars['photos']
            print(f'ID..:{id} - Fabricante..:{fabricante} - Model..:{model} - Version..:{version}'
                  f' - Price..:{price} - Year..:{year} - Distância..:{travelledDistance} - Location..:{location}')
            index += 1
            item = {
                'id': id,
                'fabricante': fabricante,
                'modelo': model,
                'versao': version,
                'preco': price,
                'ano': year,
                'distancia': travelledDistance,
                'localizacao': location,
                'foto': photos
            }
            results.append(item)
    return results


def save_in_json(results):
    file_to_save_json = "cars.json"
    local_filename_json = Path.joinpath(Path.home(), Path('desktop'), file_to_save_json)
    dict_salvar = json.dumps(results, indent=4, ensure_ascii=False)
    try:
        with open(local_filename_json, "w", encoding="utf8") as file:
            file.write(dict_salvar)
    except Exception as erro:
        print(f"O erro é: {erro}")

def main():
    list_models = get_model_car()
    results = crawl_cars(list_models)
    save_in_json(results)

if __name__ == '__main__':
    main()
