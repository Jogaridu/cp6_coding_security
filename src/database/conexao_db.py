import pymongo
from urllib.parse import quote_plus

import dns.resolver
dns.resolver.default_resolver=dns.resolver.Resolver(configure=False)
dns.resolver.default_resolver.nameservers=['8.8.8.8'] 

# REMOTO
username = quote_plus('guardian')
password = quote_plus('03I71bq05qC8OQp4')
cluster = 'cluster0.fgcgcg7.mongodb.net'
authSource = '<authSource>'
authMechanism = '<authMechanism>'
uri = f"mongodb+srv://{username}:{password}@{cluster}/?authMechanism=DEFAULT"

# LOCAL
# uri = "localhost"

def instanciar_usuarios():
    client = pymongo.MongoClient(uri, 27017)
    db = client["guardian_packet_com_br"]
    colecao = db["usuarios"]
    return colecao
