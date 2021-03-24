import logging
import bcrypt
from db_model.models import TBVN_DB
from TechBaseVN_Lib.constants import SYSTEM_ID, GrandType
from TechBaseVN_Lib.date_utils import get_timestamp
from TechBaseVN_Lib.manager import auth_manager
from TechBaseVN_Lib.manager.cache_manager import simple_cache_data, CACHE_KEY_FUNC_GET_USER_INFOS_BY_IDS
from config import SECRET_KEY

def create_user(username, password, email, phone, created_by=SYSTEM_ID):
    password = password
    salt_key = bcrypt.gensalt()
    hash_password = bcrypt.hashpw(password.encode("utf-8"), salt_key)
    is_deleted = 0
    created_time = updated_time = get_timestamp()

    try:
        TBVN_DB.UserTab.objects.create(
            username=username,
            password=hash_password.decode("utf-8"),
            email=email,
            phone=phone,
            created_by=created_by,
            is_deleted=is_deleted,
            created_time=created_time,
            updated_time=updated_time
        )
        return 1
    except Exception as ex:
        logging.warning("error_create_user|error=%s", ex)
        return 0

def get_all_user_infos_models(is_deleted=0):
    models = TBVN_DB.UserTab.objects.filter(is_deleted=is_deleted).all()
    return models

def convert_user_info_data(user_info):
    return {
        "user_id": user_info.id,
        "username": user_info.username,
        "email": user_info.email,
        "phone": user_info.phone
    }

@simple_cache_data(**CACHE_KEY_FUNC_GET_USER_INFOS_BY_IDS)
def get_user_infos_by_ids(user_ids):
    models = get_all_user_infos_models()
    results = []
    models = models.filter(id__in=user_ids)
    for model in models:
        results.append(convert_user_info_data(model))

    return results

def get_user_info_by_filter(username=None, email=None, phone=None, is_deleted=0):
    models = get_all_user_infos_models(is_deleted=is_deleted)
    if username is not None:
        models = models.filter(username=username)
    if email is not None:
        models = models.filter(email=email)
    if phone is not None:
        models = models.filter(phone=phone)

    return models.first()

def check_password_user(pass1, pass2):
    try:
        if bcrypt.checkpw(pass1.encode("utf-8"), pass2.encode("utf-8")):
            return True
    except Exception as err:
        return False

def login_user(user_info, secret_key=SECRET_KEY, algorithm="HS256", grand_type=GrandType.PASSWORD):
    token_obj = auth_manager.generate_token_obj(
        user_info, secret_key, algorithm, grand_type=grand_type
    )
    return token_obj

def get_all_user_mapping_group_infos():
    models = TBVN_DB.UserGroupTab.objects.all()
    return models

def get_user_mapping_group_infos_by_filter(user_id=None, group_id=None):
    models = get_all_user_mapping_group_infos()
    if user_id is not None:
        models = models.filter(user_id=user_id)

    if group_id is not None:
        models = models.filter(group_id=group_id)

    return models

def set_user_mapping_group(user_id, group_id):
    created_ts = get_timestamp()
    try:
        TBVN_DB.UserGroupTab.objects.create(
            user_id=user_id,
            group_id=group_id,
            created_time=created_ts
        )
        return 1
    except Exception as ex:
        logging.warning("create_user_mapping_group_fail|error=%s" % ex)
        return 0

def get_all_group_team_infos():
    models = TBVN_DB.GroupTeamTab.objects.all()
    return models

def get_group_team_infos_by_filter(group_id=None, team_id=None):
    models = get_all_group_team_infos()

    if group_id is not None:
        models = models.filter(group_id=group_id)

    if team_id is not None:
        models = models.filter(team_id=team_id)

    return models

def set_group_mapping_team(group_id, team_id):
    created_ts = get_timestamp()
    try:
        TBVN_DB.GroupTeamTab.objects.create(
            group_id=group_id,
            team_id=team_id,
            created_time=created_ts
        )
        return 1
    except Exception as ex:
        logging.warning("create_group_mapping_team_fail|error=%s" % ex)
        return 0

def check_user_mapping_team(user_id, team_id):
    model = TBVN_DB.UserTeamTab.objects.filter(user_id=user_id, team_id=team_id).first()

    if model:
        return True

    return False

def set_user_mapping_team(user_id, team_id):
    created_ts = get_timestamp()
    try:
        TBVN_DB.UserTeamTab.objects.create(
            user_id=user_id,
            team_id=team_id,
            created_time=created_ts
        )
        return 1
    except Exception as ex:
        logging.warning("create_user_mapping_team_fail|error=%s" % ex)
        return 0
