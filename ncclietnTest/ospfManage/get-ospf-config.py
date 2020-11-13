from string import Template
from ncclient import manager
template = Template('''
<filter type="subtree">
    <ospfv2 xmlns="http://www.huawei.com/netconf/vrp" format-version="1.0" content-version="1.0">
        <ospfv2comm>
            <ospfSites>
                <ospfSite>
                <processId></processId>
                <routerId/>
                <vrfName></vrfName>
                <description/>
                <areas>
                    <area>
                        <areaId></areaId>
                        <areaType></areaType>
                        <descriptionArea/>
                        <networks>
                            <network>
                                <ipAddress></ipAddress>
                                <wildcardMask></wildcardMask>
                                <description/>
                            </network>
                        </networks>
                        <interfaces>
                            <interface>
                                <ifName></ifName>
                                <networkType></networkType>
                            </interface>
                        </interfaces>
                    </area>
                </areas>
                </ospfSite>
            </ospfSites>
        </ospfv2comm>
    </ospfv2>
</filter>
''')

config = template.substitute(vlanId=106)
# print(config)
# print(config)
huawei_connect = manager.connect(host='192.168.100.200', port=22, username='client001',
                                 password='Admin@wlx@2017', hostkey_verify=False,
                                 device_params={'name': "huawei"},
                                 allow_agent=False, look_for_keys=False)
rpc_obj = None
with huawei_connect as m:
    rpc_obj = m.get_config(source='running', filter=config)
    print(rpc_obj)
