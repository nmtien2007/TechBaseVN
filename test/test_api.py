import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

import unittest
from test.test_common import *
from TechBaseVN_Lib.constants import *
from TechBaseVN_Lib.date_utils import get_timestamp


class LoginSmokeTest(unittest.TestCase):
    def test_login(self):
        data = {
            "username": "user_1",
            "password": "123"
        }

        result_code, reply = request_service_api(API_LOGIN, data, Method.POST, set_client_token=False)
        self.assertIn(result_code, [Result.SUCCESS, Result.ERROR_USER_NOT_EXISTED, Result.ERROR_PASSWORD_INCORRECT])

class AdminSmokeTest(unittest.TestCase):
    def test_create_user(self):
        data = {
            "username": "user_5",
            "password": "123",
            "email": "user_5@abc.com",
            "phone": "0702468097"
        }
        result_code, reply = request_service_api(API_ADMIN_CREATE_USER, data, Method.POST, set_client_token=True)
        self.assertIn(result_code, [Result.SUCCESS, Result.ERROR_EMAIL_WRONG_FORMAT, Result.ERROR_EMAIL_IS_EXISTED,
                                    Result.ERROR_PHONE_WRONG_FORMAT, Result.ERROR_PHONE_IS_EXISTED,
                                    Result.ERROR_USERNAME_IS_EXISTED])

    def test_get_user_info(self):
        data = {}
        result_code, reply = request_service_api(API_ADMIN_GET_USER_IDS, data, Method.POST, set_client_token=True)
        self.assertIn(result_code, [Result.SUCCESS])

        if result_code == Result.SUCCESS and reply["user_ids"]:
            data = {
                "user_ids": reply["user_ids"]
            }
            result_code, reply = request_service_api(API_ADMIN_GET_USER_INFOS, data, Method.POST)
            self.assertIn(result_code, [Result.SUCCESS])

    def test_user_mapping_group(self):
        data = {
            "user_id": 2,
            "group_id": 1
        }
        result_code, reply = request_service_api(API_ADMIN_SET_USER_MAPPING_GROUP, data, Method.POST, set_client_token=True)
        self.assertIn(result_code, [Result.SUCCESS, Result.ERROR_USER_NOT_EXISTED, Result.ERROR_GROUP_NOT_EXISTED,
                                    Result.ERROR_USER_IS_SET_GROUP, Result.ERROR_GROUP_IS_MAPPING_WITH_USER])

    def test_group_mapping_team(self):
        data = {
            "group_id": 1,
            "team_id": 1
        }
        result_code, reply = request_service_api(API_ADMIN_SET_GROUP_MAPPING_TEAM, data, Method.POST, set_client_token=True)
        self.assertIn(result_code, [Result.SUCCESS, Result.ERROR_GROUP_NOT_EXISTED, Result.ERROR_TEAM_NOT_EXISTED,
                                    Result.ERROR_TEAM_IS_MAPPING_WITH_GROUP])

    def test_user_mapping_team(self):
        data = {
            "user_id": 5,
            "team_id": 1
        }
        result_code, reply = request_service_api(API_ADMIN_SET_USER_MAPPING_TEAM, data, Method.POST, set_client_token=True, is_manger=False)
        self.assertIn(result_code, [Result.SUCCESS, Result.ERROR_TEAM_NOT_EXISTED, Result.ERROR_TEAM_INCORRECT,
                                    Result.ERROR_USER_IS_MAPPING_TEAM])

    def test_create_group(self):
        data = {
            "group_name": "Group_%s" % str(get_timestamp())
        }
        result_code, reply = request_service_api(API_ADMIN_CREATE_GROUP, data, Method.POST, set_client_token=True)
        self.assertIn(result_code, [Result.SUCCESS])

    def test_create_team(self):
        data = {
            "team_name": "Team_%s" % str(get_timestamp())
        }
        result_code, reply = request_service_api(API_ADMIN_CREATE_TEAM, data, Method.POST, set_client_token=True)
        self.assertIn(result_code, [Result.SUCCESS])

    def test_set_user_role(self):
        data = {
            "user_id": 2,
            "role_id": 2
        }
        result_code, reply = request_service_api(API_ADMIN_SET_USER_ROLE, data, Method.POST, set_client_token=True)
        self.assertIn(result_code, [Result.SUCCESS, Result.ERROR_USER_NOT_EXISTED, Result.ERROR_ROLE_IS_NOT_EXISTED,
                                    Result.ERROR_USER_IS_MAPPING_ROLE])

if __name__ == '__main__':
    unittest.main()