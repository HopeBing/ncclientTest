from string import Template
from ncclient import manager
template = Template('''
<config>
            <ifm xmlns="http://www.huawei.com/netconf/vrp" content-version="1.0" format-version="1.0">
                <interfaces>
                    <interface operation="delete">
                        <ifName>${ifName}</ifName>
                        <ifDescr>${ifDescr}</ifDescr>
                        <ifAdminStatus>${ifAdminStatus}</ifAdminStatus>
                       
                    </interface>
                </interfaces>
            </ifm>
        </config>
''')
mapping = {'ifName': "LoopBack1",
           'ifDescr': "lb1",
           'ifAdminStatus': "up",
           'ifIpAddr': "4.4.4.4",
           'subnetMask': "255.255.255.255"}

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
