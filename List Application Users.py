from requests import Session
from requests.auth import HTTPBasicAuth
from zeep import Client
from zeep.transports import Transport
from zeep.cache import SqliteCache
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

WSDL_URL = 'file://~/Python/axlToolkit/axlToolkit/schema/11.5/AXLAPI.wsdl'
CUCM_URL = 'https://FQDN:8443/axl/'
USERNAME = 'username'
PASSWD = 'password'

session = Session()
session.verify = False
session.auth = HTTPBasicAuth(USERNAME, PASSWD)
transport = Transport(session=session, timeout=10, cache=SqliteCache())

client = Client(WSDL_URL, transport=transport)
service = client.create_service("{http://www.cisco.com/AXLAPIService/}AXLAPIBinding", CUCM_URL)

# list tags that you want to see or else they return with None
tags = {'userid': '',
        'presenceGroupName': '',
        'acceptPresenceSubscription': '',
        'acceptOutOfDialogRefer': '',
        'acceptUnsolicitedNotification': '',
        'allowReplaceHeader': '',
        'isStandard': ''}

resp = service.listAppUser(searchCriteria={'userid': '%'}, returnedTags=tags)
print(resp)
