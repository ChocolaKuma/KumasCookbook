def ConnectToSite(IPV4,POR)
    import socket
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((IPV4,PORT))