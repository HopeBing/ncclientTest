from string import Template
from ncclient import manager
template = Template('''
        <config>
            <ospfv2 xmlns="http://www.huawei.com/netconf/vrp" format-version="1.0" content-version="1.0">
                <ospfv2comm>
                    <ospfSites>
                        <ospfSite>
                            <processId>${processId}</processId>
                            <areas>
                                <area>
                                    <areaId>${areaId}</areaId>
                                    <descriptionArea>${descriptionArea}</descriptionArea>
                                </area>
                            </areas>
                        </ospfSite>
                    </ospfSites>
                </ospfv2comm>
            </ospfv2>
        </config>
''')

# config = template.substitute(vlanId=106, vlanName='vlan106',vlanDesc='VLAN106')
mapping = {'processId':200, 'routerId':'10.10.10.10','areaType': 'common',
           'description':'ospf200', 'areaId':'0.0.0.0','descriptionArea':'area0',
           'ipAddress':'192.168.10.0','wildcardMask':'0.0.0.255'
           }
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
