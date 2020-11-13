from ping3 import ping


def ping_host(ip_address):
    """
    获取节点的延迟的作用
    :param ip_address:
    :param node:
    :return:
    """
    response = ping(ip_address)
    print(response)
    if response is not None:
        delay = int(response * 1000)
        print(delay, "延迟")
        # 下面两行新增的


ping_host('192.168.100.200')