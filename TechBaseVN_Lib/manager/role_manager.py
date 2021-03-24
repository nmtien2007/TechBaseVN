import logging
from db_model.models import TBVN_DB
from TechBaseVN_Lib.date_utils import get_timestamp


def get_role_info_by_user_id(user_id):
    role_mapping_model = TBVN_DB.UserRoleTab.objects.filter(user_id=user_id).first()
    if not role_mapping_model:
        return None
    # role_info = TBVN_DB.RoleTab.objects.filter(id=role_mapping_model.role_id).first()
    role_info = get_role_info_by_id(role_mapping_model.role_id)
    return role_info.alias

def get_role_info_by_id(role_id):
    model = TBVN_DB.RoleTab.objects.filter(id=role_id).first()
    return model

def check_user_role_mapping(user_id, role_id):
    return TBVN_DB.UserRoleTab.objects.filter(user_id=user_id, role_id=role_id).first()

def set_user_role(user_id, role_id):
    created_ts = get_timestamp()
    try:
        TBVN_DB.UserRoleTab.objects.create(
            user_id=user_id,
            role_id=role_id,
            created_time=created_ts
        )
        return 1
    except Exception as ex:
        logging.warning("set_user_role_fail|error=%s" % ex)
        return 0
