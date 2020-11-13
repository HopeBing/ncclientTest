from string import Template
from ncclient import manager
template = Template('''
    <config>
            <ifmtrunk xmlns="http://www.huawei.com/netconf/vrp" format-version="1.0" content-version="1.0">
                <TrunkIfs>
                    <TrunkIf>
                        <ifName>Eth-Trunk1</ifName>
                        <minUpNum>10</minUpNum>
                        <maxUpNum>32</maxUpNum>
                        <trunkType>EthTrunk</trunkType>
                        <workMode>Manual</workMode>
                        <TrunkMemberIfs>
                            <TrunkMemberIf>
                                <memberIfName>GE1/0/7</memberIfName>
                                <weight>2</weight>
                            </TrunkMemberIf>
                        </TrunkMemberIfs>
                    </TrunkIf>
                </TrunkIfs>
            </ifmtrunk>
    </config>
''')
mapping = {}
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
