from django.db import models

class MappingIngestMaster(models.Model):
    id = models.BigAutoField(primary_key=True, auto_created=True, db_column="id")
    ingest_date = models.DateTimeField(db_column="ingest_date")
    file_blob = models.FileField(db_column="file_content_as_blob")
    file_name = models.CharField(db_column="file_name", max_length=200)

    class META:
        db_table = 'mapping_master'


class RoleMaster(models.Model):
    role_id = models.BigAutoField(primary_key=True, db_column="role_id", auto_created=True)
    role_name = models.CharField(db_column="role_name", max_length=100)
    status = models.CharField(db_column="status", max_length=1)
    mapping_id = models.ForeignKey(to=MappingIngestMaster, db_column="mapping_id", on_delete=models.CASCADE)

    class META:
        db_table = 'role_master'

class UserRoleAssociation(models.Model):
    id = models.BigAutoField(primary_key=True, auto_created=True, db_column="id")
    user_id = models.CharField(db_column="user_id", max_length=7)
    role_id = models.ForeignKey(to=RoleMaster, db_column="role_id", on_delete=models.CASCADE)
    mapping_id = models.ForeignKey(to=MappingIngestMaster, db_column="mapping_id", on_delete=models.CASCADE)
    status = models.CharField(db_column="status", max_length=1)

    class META:
        db_table = 'user_role_assoc'

