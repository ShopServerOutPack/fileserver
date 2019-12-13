
import os
from rest_framework import viewsets
from libs.core.decorator.response import Core_connector
from apps.utils import url_join
from rest_framework.decorators import list_route
import shutil

class FileAPIView(viewsets.ViewSet):

    @list_route(methods=['POST'])
    @Core_connector()
    def upload(self,request, *args, **kwargs):

        UPLOAD_FILE_PATH = '/var/nginx_upload/file/'

        endstr = request.data.get("file_name").split(".")[-1]

        print(endstr)

        if not os.path.exists(UPLOAD_FILE_PATH):
            os.makedirs(UPLOAD_FILE_PATH)

        new_file_name = request.data.get("file_md5") + '.{}'.format(endstr)
        new_file_path = ''.join([UPLOAD_FILE_PATH, new_file_name])

        print(new_file_path)

        shutil.copyfile(request.data.get('file_path'),new_file_path)
        url = url_join('/nginx_upload/file/%s'%(new_file_name))

        print(url)

        return {"data":{"path":url}}



