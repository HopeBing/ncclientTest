from string import Template
from ncclient import manager
template = Template('''
        <config>
            <vlan xmlns = "http://www.huawei.com/netconf/vrp" content-version="1.0" format-version="1.0" >
                <vlans>
                <vlan>
                <vlanId>${vlanId}</vlanId>
                <vlanType>common</vlanType>
                <vlanName>${vlanName}</vlanName>
                <vlanDesc>${vlanDesc}</vlanDesc>
                <adminStatus>up</adminStatus>
                <subVlans/>
                <superVlan/>
                <vlanif>
                <ifName></ifName>
                <cfgBand>1000</cfgBand>
                <dampTime>0</dampTime>
                </vlanif>
                <muxVlan>
                    <separateVlan/>
                    <groupVlans/>
                </muxVlan>
                </vlan>
                </vlans>
            </vlan>
        </config>
''')

# config = template.substitute(vlanId=106, vlanName='vlan106',vlanDesc='VLAN106')
mapping = {'vlanId':106, 'vlanName':'vlan106','vlanDesc':'VLAN106'}
config = template.substitute(mapping)
# print(config)
# print(config)
huawei_connect = manager.connect(host='192.168.100.200', port=22, username='client001',
                                 password='Admin@wlx@2017', hostkey_verify=False,
                                 device_params={'name': "huawei"},
                                 allow_agent=False, look_for_keys=False)
rpc_obj = None
with huawei_connect as m:
    rpc_obj = m.edit_config(target='running', config=config)
    print(rpc_obj)
