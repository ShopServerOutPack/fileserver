
from education.settings import ServerUrl

def url_join(path=None):
    return "{}{}".format(ServerUrl,path) if path else ServerUrl