from django.core.files import File
from django.core.files.uploadedfile import TemporaryUploadedFile
from django.shortcuts import render
from rest_framework.request import Request
from rest_framework.response import Response
from django.http.response import HttpResponse
from rest_framework.views import APIView
from .models import (RoleMaster, UserRoleAssociation, MappingIngestMaster)
import json
from .role_mapping_util import *
from datetime import datetime
import uuid

class RoleCRUDView(APIView):
    def get(self, request: Request) -> Response:
        """Lists all roles"""
        role_ids = []
        if request.data:
            """there is some content coming from UI"""
            role_ids.append(request.data)
            # this is a hack, avoid using the append method in this manner
        resp = RoleMaster.objects.values_list()
        return Response(resp)

    def post(self, request: Request) -> Response:
        """ adds a new role """

        return None


class UploadView(APIView):
    def post(self, request: Request) -> Response:
        """ allows for Excel files to be uploaded
        Args:
            request: Request
        """
        uploaded_file = request.FILES['file_to_upload']
        file_name = request.data['file_name']
        mapping_master = MappingIngestMaster()
        mapping_master.file_blob = uploaded_file
        mapping_master.ingest_date = datetime.now()
        mapping_master.file_name = file_name

        mapping_master.save()

        excel_file = File(uploaded_file)
        path: str = f'/tmp/{uuid.uuid4()}'
        with open(path, 'wb+') as dest:
            for chunks in excel_file.chunks():
                dest.write(chunks)

        resp = process_excel(path)

        RoleMaster.objects.update(status='N')
        UserRoleAssociation.objects.update(status='N')
        for entry in resp:
            role_master = RoleMaster()
            role = entry['role_name']
            users = entry['uNumbers']
            role_master.role_name = role
            role_master.status = 'Y'
            role_master.mapping_id = mapping_master
            role_master.save()
            for user_unumber in users:
                ura = UserRoleAssociation()
                ura.role_id = role_master
                ura.user_id = user_unumber
                ura.mapping_id = mapping_master
                ura.status = 'Y'
                ura.save()

        return Response(data=resp)
