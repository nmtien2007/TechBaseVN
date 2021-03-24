TYPE_UINT8_MAX = 255
TYPE_UINT16_MAX = 65535
TYPE_UINT32_MAX = 4294967295
TYPE_INT32_MIN = -2147483648
TYPE_INT32_MAX = 2147483647
TYPE_UINT64_MAX = 18446744073709551615


SYSTEM_ID = -1

class GrandType:
    PASSWORD = 1

class Method:
    POST = 1
    GET = 2
    PUT = 3
    DELETE = 4

class Result:
    SUCCESS = "success"
    ERROR_PARAMS = "error_params"
    ERROR_USER_NOT_EXISTED = "error_user_not_existed"
    ERROR_PASSWORD_INCORRECT = "error_password_incorrect"
    ERROR_HEADER = "error_header"
    ERROR_ACCESS_TOKEN_NOT_FOUND = "error_access_token_not_found"
    ERROR_ACCESS_TOKEN_WRONG_FORMAT = "error_access_token_wrong_format"
    ERROR_ACCESS_TOKEN_INCORRECT = "error_access_token_incorrect"
    ERROR_EMAIL_WRONG_FORMAT = "error_email_wrong_format"
    ERROR_PHONE_WRONG_FORMAT = "error_phone_wrong_format"
    ERROR_EMAIL_IS_EXISTED = "error_email_is_existed"
    ERROR_PHONE_IS_EXISTED = "error_phone_is_existed"
    ERROR_USERNAME_IS_EXISTED = "error_username_is_existed"
    ERROR_ROLE_IS_NOT_SET = "error_role_is_not_set"
    ERROR_PERMISSION_DENIED = "error_permission_denied"
    ERROR_GROUP_NOT_EXISTED = "error_group_not_existed"
    ERROR_USER_IS_SET_GROUP = "error_user_is_set_group"
    ERROR_GROUP_IS_MAPPING_WITH_USER = "error_group_is_mapping_with_user"
    ERROR_TEAM_NOT_EXISTED = "error_team_not_existed"
    ERROR_TEAM_IS_MAPPING_WITH_GROUP = "error_team_is_mapping_with_group"
    ERROR_TEAM_INCORRECT = "error_team_incorrect"
    ERROR_USER_IS_MAPPING_TEAM = "error_user_is_mapping_team"
    ERROR_ROLE_IS_NOT_EXISTED = "error_role_is_not_existed"
    ERROR_USER_IS_MAPPING_ROLE = "error_user_is_mapping_role"

class UserRole:
    MANAGER = "manager"
    GROUP_MANAGER = "group_manager"
    USER = "user"
