from string import Template
from ncclient import manager
template = Template('''
        <filter type="subtree">
            <staticrt xmlns="http://www.huawei.com/netconf/vrp" content-version="1.0" format-version="1.0">
                <staticrtbase>
                    <srRoutes>
                        <srRoute>
                            <vrfName/>
                            <afType/>
                            <topologyName/>
                            <prefix/>
                            <maskLength/>
                            <ifName/>
                            <destVrfName/>
                            <nexthop/>
                            <tag/>
                            <description/>
                        </srRoute>
                    </srRoutes>
                </staticrtbase>
            </staticrt>
        </filter>
''')

config = template.substitute()
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
