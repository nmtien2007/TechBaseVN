import logging
from db_model.models import TBVN_DB
from TechBaseVN_Lib.date_utils import get_timestamp


def get_user_id_by_team_ids(team_ids):
    models = TBVN_DB.UserTeamTab.objects.filter(team_id__in=team_ids).all()
    return list(models.values_list("user_id", flat=True))

def get_team_info_by_id(team_id):
    model = TBVN_DB.TeamTab.objects.filter(id=team_id, is_deleted=0).first()
    return model

def get_team_ids_by_group_id(group_id):
    models = TBVN_DB.GroupTeamTab.objects.filter(group_id=group_id).all()
    return list(models.values_list("team_id", flat=True))

def create_team(team_name):
    created_ts = updated_ts = get_timestamp()
    try:
        TBVN_DB.TeamTab.objects.create(
            team_name=team_name,
            is_deleted=0,
            created_time=created_ts,
            updated_time=updated_ts
        )
        return 1
    except Exception as ex:
        logging.warning("create_team_fail|error=%s" % ex)
        return 0
