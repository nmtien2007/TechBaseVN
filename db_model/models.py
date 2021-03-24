from django.db import models

class TBVN_DB:
    class TBVN_DB_Config:
        class Config:
            db_for_read = 'tech_base_vn_slave'
            db_for_write = 'tech_base_vn_master'

    class AccessTokenTab(TBVN_DB_Config, models.Model):
        id = models.BigAutoField(primary_key=True)
        access_token = models.CharField(max_length=2000, blank=True, null=True, default="")
        expiry_time = models.PositiveIntegerField(default=0)
        user_id = models.PositiveIntegerField()
        created_time = models.PositiveIntegerField(blank=False, null=False)
        updated_time = models.PositiveIntegerField(blank=False, null=False)

        class Meta:
            managed = False
            db_table = 'access_token_tab'

    class GroupTab(TBVN_DB_Config, models.Model):
        id = models.BigAutoField(primary_key=True)
        group_name = models.CharField(max_length=200, blank=False, null=False)
        is_deleted = models.PositiveSmallIntegerField()
        created_time = models.PositiveIntegerField(blank=False, null=False)
        updated_time = models.PositiveIntegerField(blank=False, null=False)

        class Meta:
            managed = False
            db_table = 'group_tab'

    class TeamTab(TBVN_DB_Config, models.Model):
        id = models.BigAutoField(primary_key=True)
        team_name = models.CharField(max_length=200, blank=False, null=False)
        is_deleted = models.PositiveSmallIntegerField()
        created_time = models.PositiveIntegerField(blank=False, null=False)
        updated_time = models.PositiveIntegerField(blank=False, null=False)

        class Meta:
            managed = False
            db_table = 'team_tab'

    class RoleTab(TBVN_DB_Config, models.Model):
        id = models.BigAutoField(primary_key=True)
        role_name = models.CharField(max_length=50, blank=False, null=False)
        alias = models.CharField(max_length=50, blank=False, null=False)
        created_time = models.PositiveIntegerField(blank=False, null=False)
        updated_time = models.PositiveIntegerField(blank=False, null=False)

        class Meta:
            managed = False
            db_table = 'role_tab'

    class GroupTeamTab(TBVN_DB_Config, models.Model):
        id = models.BigAutoField(primary_key=True)
        group_id = models.PositiveIntegerField()
        team_id = models.PositiveIntegerField()
        created_time = models.PositiveIntegerField(blank=False, null=False)

        class Meta:
            managed = False
            db_table = 'group_team_tab'

    class UserTeamTab(TBVN_DB_Config, models.Model):
        id = models.BigAutoField(primary_key=True)
        user_id = models.PositiveIntegerField()
        team_id = models.PositiveIntegerField()
        created_time = models.PositiveIntegerField(blank=False, null=False)

        class Meta:
            managed = False
            db_table = 'user_team_tab'

    class UserRoleTab(TBVN_DB_Config, models.Model):
        id = models.BigAutoField(primary_key=True)
        user_id = models.PositiveIntegerField()
        role_id = models.PositiveIntegerField()
        created_time = models.PositiveIntegerField(blank=False, null=False)

        class Meta:
            managed = False
            db_table = 'user_role_tab'

    class UserGroupTab(TBVN_DB_Config, models.Model):
        id = models.BigAutoField(primary_key=True)
        user_id = models.PositiveIntegerField()
        group_id = models.PositiveIntegerField()
        created_time = models.PositiveIntegerField(blank=False, null=False)

        class Meta:
            managed = False
            db_table = 'user_group_tab'

    class UserTab(TBVN_DB_Config, models.Model):
        id = models.BigAutoField(primary_key=True)
        username = models.CharField(max_length=50, blank=False, null=False)
        password = models.CharField(max_length=200, blank=False, null=False)
        email = models.CharField(max_length=50, blank=False, null=False)
        phone = models.CharField(max_length=15, blank=False, null=False)
        is_deleted = models.PositiveSmallIntegerField()
        created_by = models.PositiveIntegerField()
        created_time = models.PositiveIntegerField(blank=False, null=False)
        updated_time = models.PositiveIntegerField(blank=False, null=False)

        class Meta:
            managed = False
            db_table = 'user_tab'
