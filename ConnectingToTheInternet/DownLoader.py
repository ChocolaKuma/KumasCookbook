def DownloadIMG(URL,FileName,FileType):
    import urllib.request
    filename=FileName+FileType
    urllib.request.urlretrieve(URL, filename)