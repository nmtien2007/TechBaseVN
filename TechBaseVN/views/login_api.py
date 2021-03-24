from TechBaseVN_Lib.utils import parse_params, api_response_data, api_response_error_params
from TechBaseVN_Lib.constants import Result
from TechBaseVN.views.form_schema import LoginSchema
from TechBaseVN_Lib.manager import user_manager

@parse_params(LoginSchema, error_handler=api_response_error_params)
def login(request, data):
    username = data["username"]
    password = data["password"]

    user_info = user_manager.get_user_info_by_filter(username)
    if not user_info:
        return api_response_data(Result.ERROR_USER_NOT_EXISTED)

    if not user_manager.check_password_user(password, user_info.password):
        return api_response_data(Result.ERROR_PASSWORD_INCORRECT)

    token_obj = user_manager.login_user(user_info)

    return api_response_data(Result.SUCCESS, token_obj)
