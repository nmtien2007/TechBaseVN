import requests
import json
import traceback
from TechBaseVN_Lib.constants import Method, Result

TEST_URL = "http://127.0.0.1:8000"

API_ADMIN_CREATE_USER = TEST_URL + "/admin/create_user"
API_ADMIN_CREATE_GROUP = TEST_URL + "/admin/create_group"
API_ADMIN_CREATE_TEAM = TEST_URL + "/admin/create_team"
API_ADMIN_GET_USER_IDS = TEST_URL + "/admin/get_user_ids"
API_ADMIN_GET_USER_INFOS = TEST_URL + "/admin/get_user_infos"
API_ADMIN_SET_USER_MAPPING_GROUP = TEST_URL + "/admin/set_user_mapping_group"
API_ADMIN_SET_GROUP_MAPPING_TEAM = TEST_URL + "/admin/set_group_mapping_team"
API_ADMIN_SET_USER_MAPPING_TEAM = TEST_URL + "/admin/set_user_mapping_team"
API_ADMIN_SET_USER_ROLE = TEST_URL + "/admin/set_user_role"


API_LOGIN = TEST_URL + "/login"

MANAGER_USER = "user_1"
MANAGER_PASS = "123"

MANAGER_GROUP_USER = "user_2"
MANAGER_GROUP_PASS = "123"

MANAGER_ACCESS_TOKEN = ""
MANAGER_GROUP_ACCESS_TOKEN = ""


def request_service_api(url, data, method, is_manger=True, set_client_token=True):

    global MANAGER_ACCESS_TOKEN

    global MANAGER_GROUP_ACCESS_TOKEN

    headers = {}

    if set_client_token:
        if is_manger:
            headers['x-access-token'] = MANAGER_ACCESS_TOKEN
        else:
            headers['x-access-token'] = MANAGER_GROUP_ACCESS_TOKEN

    try:
        response = None
        if method == Method.POST:
            response = requests.post(url, data=json.dumps(data), verify=False, headers=headers)
        if method == Method.GET:
            response = requests.get(url, data=json.dumps(data), verify=False, headers=headers)

        if response.status_code != 200:
            print("REQUEST HTTP ERROR CODE: %s" % response.status_code)
            return None, None
        result = response.json()
        result_code = result["result"]
        result_body = result.get("reply")

        return result_code, result_body
    except Exception as error:
        print("REQUEST EXCEPTION: %s" % str(error))
        return None, None

def get_access_token(is_manger=True):
    try:
        if is_manger:
            data = {
                "username": MANAGER_USER,
                "password": MANAGER_PASS
            }
        else:
            data = {
                "username": MANAGER_GROUP_USER,
                "password": MANAGER_GROUP_PASS
            }

        result_code, reply = request_service_api(API_LOGIN, data, Method.POST, is_manger=is_manger)
        if result_code in [Result.SUCCESS]:
           return reply["access_token"]
        else:
            print(result_code)
            return ""

    except Exception as error:
        error = traceback.format_exc()
        print(error)
        return None, None

MANAGER_ACCESS_TOKEN = get_access_token(is_manger=True)
MANAGER_GROUP_ACCESS_TOKEN = get_access_token(is_manger=False)
