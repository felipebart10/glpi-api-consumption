import glpi_api
import json
import configparser as cp

parser = cp.ConfigParser()
parser.read('config.ini')
URL = str(parser['Config']['URL'])
APPTOKEN = str(parser['Config']['APPTOKEN'])
USERTOKEN = str(parser['Config']['USERTOKEN'])

con = glpi_api.GLPI(url=URL,apptoken=APPTOKEN,auth=USERTOKEN, use_headers=True,verify_certs=False)
arquivo_json = open('dump.json', 'w', encoding="utf-8")
con.set_active_entities(0, True)
dados_json = con.get_all_items("Entity",range='0-1000')
lista_entidades = [x["name"] for x in dados_json]
print(sorted(lista_entidades))

json.dump(con.get_all_items("Entity"), arquivo_json,ensure_ascii=False)
arquivo_json.close()