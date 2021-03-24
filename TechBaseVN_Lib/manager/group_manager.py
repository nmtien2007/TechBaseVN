import logging
from db_model.models import TBVN_DB
from TechBaseVN_Lib.date_utils import get_timestamp

def get_all_group_team_models():
    models = TBVN_DB.GroupTeamTab.objects.all()
    return models

def get_team_id_by_group_id(group_id=None):
    models = get_all_group_team_models()
    if group_id is not None:
        models = models.filter(group_id=group_id)

    return list(models.values_list("team_id", flat=True))

def get_group_info_by_id(group_id):
    model = TBVN_DB.GroupTab.objects.filter(id=group_id, is_deleted=0).first()
    return model

def get_group_id_by_user_id(user_id):
    model = TBVN_DB.UserGroupTab.objects.filter(user_id=user_id).first()
    return model

def create_group(group_name):
    created_ts = updated_ts = get_timestamp()
    try:
        TBVN_DB.GroupTab.objects.create(
            group_name=group_name,
            is_deleted=0,
            created_time=created_ts,
            updated_time=updated_ts
        )
        return 1
    except Exception as ex:
        logging.warning("create_group_fail|error=%s" % ex)
        return 0
