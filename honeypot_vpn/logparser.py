import datetime



def logparser( data, **kwargs ):
    extradata = {}
    request_type = kwargs.get('request_type', None)
    protocol = kwargs.get('protocol', None)
    vpn_client_ip = kwargs.get('vpn_client_ip', None)
    vpn_client_port = kwargs.get('vpn_client_port', None)
    vpn_destination_ip = kwargs.get('vpn_destination_ip', None)
    vpn_destination_port = kwargs.get('vpn_destination_port', None)
    body_length = kwargs.get('body_length', None)
    addExtraData = False
    if request_type is not None:
        extradata['request_type'] = request_type
        addExtraData = True
    if protocol is not None:
        extradata['protocol'] = protocol
        addExtraData = True
    if vpn_client_ip is not None:
        extradata['vpn_client_ip'] = vpn_client_ip
        addExtraData = True
    if vpn_client_port is not None:
        extradata['vpn_client_port'] = vpn_client_port
        addExtraData = True
    if vpn_destination_ip is not None:
        extradata['vpn_destination_ip'] = vpn_destination_ip
        addExtraData = True
    if vpn_destination_port is not None:
        extradata['vpn_destination_port'] = vpn_destination_port
        addExtraData = True
    if body_length is not None:
        extradata['body_length'] = body_length
        addExtraData = True
    msg = ''
    if addExtraData:
        msg = str(extradata) + ' data=' + str(data)
    else:
        msg = 'data=' + str(data)
        extradata = None
    return msg, extradata


