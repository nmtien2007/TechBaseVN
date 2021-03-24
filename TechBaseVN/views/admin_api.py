from TechBaseVN_Lib.utils import parse_params, api_response_data, api_response_error_params, pre_process_header, \
    verify_access_token, validate_email, validate_phone_number, required_roles
from TechBaseVN_Lib.constants import Result, UserRole
from TechBaseVN.views.form_schema import AdminCreateUserLoginSchema, AdminGetUserIdsSchema, AdminGetUserInfosSchema, \
    AdminSetUserMappingGroupSchema, AdminSetGroupMappingTeamSchema, AdminSetUserMappingTeamSchema, \
    AdminCreateGroupSchema, AdminCreateTeamSchema, AdminSetUserRoleSchema
from TechBaseVN_Lib.manager import user_manager, group_manager, team_manager, role_manager


@parse_params(AdminCreateUserLoginSchema, error_handler=api_response_error_params())
@pre_process_header()
@verify_access_token()
@required_roles([UserRole.MANAGER, UserRole.GROUP_MANAGER])
def create_user(request, data):
    username = data["username"]
    password = data["password"]
    email = data["email"]
    phone = data["phone"]

    # validate email
    if not validate_email(email):
        return api_response_data(Result.ERROR_EMAIL_WRONG_FORMAT)

    if user_manager.get_user_info_by_filter(email=email):
        return api_response_data(Result.ERROR_EMAIL_IS_EXISTED)

    # validate phone
    phone = validate_phone_number(phone)
    if not phone:
        return api_response_data(Result.ERROR_PHONE_WRONG_FORMAT)

    if user_manager.get_user_info_by_filter(phone=phone):
        return api_response_data(Result.ERROR_PHONE_IS_EXISTED)
    
    # validate username
    if user_manager.get_user_info_by_filter(username=username):
        return api_response_data(Result.ERROR_USERNAME_IS_EXISTED)

    affected_count = user_manager.create_user(username, password, email, phone)

    return api_response_data(Result.SUCCESS, {"affected_count": affected_count})

@parse_params(AdminGetUserIdsSchema, error_handler=api_response_error_params())
@pre_process_header()
@verify_access_token()
@required_roles([UserRole.MANAGER, UserRole.GROUP_MANAGER])
def get_user_ids(request, data):
    group_id = data.get("group_id", None)
    team_id = data.get("team_id", None)

    user_ids = []

    if not group_id:
        team_ids = group_manager.get_team_id_by_group_id()
        if team_ids:
            user_ids = team_manager.get_user_id_by_team_ids(team_ids)
    else:
        if not team_id:
            team_ids = group_manager.get_team_id_by_group_id(group_id)
            if team_ids:
                user_ids = team_manager.get_user_id_by_team_ids(team_ids)
        else:
            user_ids = team_manager.get_user_id_by_team_ids([team_id])

    if user_ids:
        user_ids = list(set(user_ids))
        user_ids = sorted(user_ids, reverse=True)

    return api_response_data(Result.SUCCESS, {"user_ids": user_ids})

@parse_params(AdminGetUserInfosSchema, error_handler=api_response_error_params())
@pre_process_header()
@verify_access_token()
def get_user_infos(request, data):
    user_ids = data["user_ids"]
    user_infos = user_manager.get_user_infos_by_ids(user_ids)
    return api_response_data(Result.SUCCESS, {"user_infos": user_infos})

@parse_params(AdminSetUserMappingGroupSchema, error_handler=api_response_error_params())
@pre_process_header()
@verify_access_token()
@required_roles([UserRole.MANAGER])
def set_user_mapping_group(request, data):
    user_id = data["user_id"]
    group_id = data["group_id"]

    user_infos = user_manager.get_user_infos_by_ids([user_id], force_query=True)
    if not user_infos:
        return api_response_data(Result.ERROR_USER_NOT_EXISTED)

    if not group_manager.get_group_info_by_id(group_id):
        return api_response_data(Result.ERROR_GROUP_NOT_EXISTED)

    if user_manager.get_user_mapping_group_infos_by_filter(user_id=user_id):
        return api_response_data(Result.ERROR_USER_IS_SET_GROUP)

    if user_manager.get_user_mapping_group_infos_by_filter(group_id=group_id):
        return api_response_data(Result.ERROR_GROUP_IS_MAPPING_WITH_USER)

    affected_count = user_manager.set_user_mapping_group(user_id, group_id)

    return api_response_data(Result.SUCCESS, {"affected_count": affected_count})

@parse_params(AdminSetGroupMappingTeamSchema, error_handler=api_response_error_params())
@pre_process_header()
@verify_access_token()
@required_roles([UserRole.MANAGER])
def set_group_mapping_team(request, data):
    group_id = data["group_id"]
    team_id = data["team_id"]

    if not group_manager.get_group_info_by_id(group_id):
        return api_response_data(Result.ERROR_GROUP_NOT_EXISTED)

    if not team_manager.get_team_info_by_id(team_id):
        return api_response_data(Result.ERROR_TEAM_NOT_EXISTED)

    if user_manager.get_group_team_infos_by_filter(team_id=team_id):
        return api_response_data(Result.ERROR_TEAM_IS_MAPPING_WITH_GROUP)

    affected_count = user_manager.set_group_mapping_team(group_id, team_id)

    return api_response_data(Result.SUCCESS, {"affected_count": affected_count})

@parse_params(AdminSetUserMappingTeamSchema, error_handler=api_response_error_params())
@pre_process_header()
@verify_access_token()
@required_roles([UserRole.GROUP_MANAGER])
def set_user_mapping_team(request, data):
    user_id = data["user_id"]
    team_id = data["team_id"]
    group_manger_id = data["_session"]["user_id"]

    user_infos = user_manager.get_user_infos_by_ids([user_id], force_query=True)
    if not user_infos:
        return api_response_data(Result.ERROR_USER_NOT_EXISTED)

    if not team_manager.get_team_info_by_id(team_id):
        return api_response_data(Result.ERROR_TEAM_NOT_EXISTED)

    # get allowed team ids
    group_obj = group_manager.get_group_id_by_user_id(group_manger_id)
    team_ids = team_manager.get_team_ids_by_group_id(group_obj.id)
    if team_id not in team_ids:
        return api_response_data(Result.ERROR_TEAM_INCORRECT)

    if user_manager.check_user_mapping_team(user_id, team_id):
        return api_response_data(Result.ERROR_USER_IS_MAPPING_TEAM)

    affected_count = user_manager.set_user_mapping_team(user_id, team_id)

    return api_response_data(Result.SUCCESS, {"affected_count": affected_count})

@parse_params(AdminCreateGroupSchema, error_handler=api_response_error_params())
@pre_process_header()
@verify_access_token()
@required_roles([UserRole.MANAGER])
def create_group(request, data):
    group_name = data["group_name"]
    affected_count = group_manager.create_group(group_name)
    return api_response_data(Result.SUCCESS, {"affected_count": affected_count})

@parse_params(AdminCreateTeamSchema, error_handler=api_response_error_params())
@pre_process_header()
@verify_access_token()
@required_roles([UserRole.MANAGER])
def create_team(request, data):
    team_name = data["team_name"]
    affected_count = team_manager.create_team(team_name)
    return api_response_data(Result.SUCCESS, {"affected_count": affected_count})

@parse_params(AdminSetUserRoleSchema, error_handler=api_response_error_params())
@pre_process_header()
@verify_access_token()
@required_roles([UserRole.MANAGER])
def set_user_role(request, data):
    user_id = data["user_id"]
    role_id = data["role_id"]

    user_infos = user_manager.get_user_infos_by_ids([user_id], force_query=True)
    if not user_infos:
        return api_response_data(Result.ERROR_USER_NOT_EXISTED)

    role_info = role_manager.get_role_info_by_id(role_id)
    if not role_info:
        return api_response_data(Result.ERROR_ROLE_IS_NOT_EXISTED)

    if role_manager.check_user_role_mapping(user_id, role_id):
        return api_response_data(Result.ERROR_USER_IS_MAPPING_ROLE)

    affected_count = role_manager.set_user_role(user_id, role_id)
    return api_response_data(Result.SUCCESS, {"affected_count": affected_count})