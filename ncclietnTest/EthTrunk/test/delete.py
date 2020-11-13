from string import Template
from ncclient import manager
template = Template('''
 <config>
            <ethernet xmlns="http://www.huawei.com/netconf/vrp" format-version="1.0" content-version="1.0">
                <ethernetIfs>
                    <ethernetIf>
                        <ifName>${ifName}</ifName>
                        <l2Enable>${l2Enable}</l2Enable>
                        <l2Attribute operation="delete">
                            <linkType>${linkType}</linkType>
                            <pvid>${pvid}</pvid>
                        </l2Attribute>
                    </ethernetIf>
                </ethernetIfs>
            </ethernet>
        </config>
''')
mapping = {'ifName': "GE1/0/8",
           'l2Enable': "enable",
           'linkType': "access",
           'pvid': "1",
           'trunkVlans': ""}

config = template.substitute(mapping)
print(config)
huawei_connect = manager.connect(host='192.168.100.201', port=22, username='client001',
                                 password='WLX@wlx2020', hostkey_verify=False,
                                 device_params={'name': "huawei"},
                                 allow_agent=False, look_for_keys=False)
rpc_obj = None
with huawei_connect as m:
    rpc_obj = m.edit_config(target='running', config=config)
    print(rpc_obj)
