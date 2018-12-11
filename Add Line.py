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

callforward = 'CSS-Internal'
css = 'lCSS-LongDistance'

# E164 numbers need to have two backslashes
dn_pattern = '\\+05555531808'
dn_short = dn_pattern[-4:]
line_data = {'pattern': dn_pattern,
             'routePartitionName': 'PT-OnNet',
             'description': 'User Line' + ' - ' + dn_short,
             'usage': 'Device',
             'alertingName': 'vacant',
             'asciiAlertingName': 'vacant',
             'voiceMailProfileName': 'Default',
             'shareLineAppearanceCssName': css,
             'active': 'false',
             'callForwardAll': ({'forwardToVoiceMail': 'False', 'callingSearchSpaceName': callforward}),
             'callForwardBusy': ({'forwardToVoiceMail': 'True', 'callingSearchSpaceName': callforward}),
             'callForwardBusyInt': ({'forwardToVoiceMail': 'True', 'callingSearchSpaceName': callforward}),
             'callForwardNoAnswer': ({'forwardToVoiceMail': 'True', 'callingSearchSpaceName': callforward}),
             'callForwardNoAnswerInt': ({'forwardToVoiceMail': 'True', 'callingSearchSpaceName': callforward}),
             'callForwardNoCoverage': ({'forwardToVoiceMail': 'True', 'callingSearchSpaceName': callforward}),
             'callForwardNoCoverageInt': ({'forwardToVoiceMail': 'True', 'callingSearchSpaceName': callforward}),
             'callForwardOnFailure': ({'forwardToVoiceMail': 'True', 'callingSearchSpaceName': callforward}),
             'callForwardNotRegistered': ({'forwardToVoiceMail': 'True', 'callingSearchSpaceName': callforward}),
             'callForwardNotRegisteredInt': ({'forwardToVoiceMail': 'True', 'callingSearchSpaceName': callforward})}
resp = service.addLine(line_data)
print(resp)
