import xmlrpc.client
proxy = xmlrpc.client.ServerProxy("http://localhost:8080")
with xmlrpc.client.ServerProxy("http://localhost:8000/") as proxy:
    print("le résultat est %s" % str(proxy.calculatrice(142,40,-)))
