from sodapy import Socrata

client = Socrata(
    "www.datos.gov.co",
    "83e223pn454ukslhkj7f622b9"
)

print(client.get("gt2j-8ykr", limit=5000))