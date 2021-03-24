import uuid
import jwt
import config
from datetime import datetime, timedelta
from TechBaseVN_Lib.manager import token_manager, role_manager
from TechBaseVN_Lib.date_utils import get_timestamp, datetime_to_timestamp
from TechBaseVN_Lib.constants import GrandType


def get_expired_time_token():
    current_date = datetime.now()
    current_date = current_date + timedelta(minutes=config.EXPIRED_TIME_TOKEN)
    return datetime_to_timestamp(current_date)

class AuthorizationModel(object):
    def __init__(self, data):
        self.user_info = data["user_info"]
        self.algorithm = data["algorithm"]
        self.iss = data.get("iss", config.ISS)
        self.secret_key = data.get("secret_key", config.SECRET_KEY)
        self.user_token = self._get_user_token()
        self.access_token = None
        self.data_obj = self._generate_data_obj()

    def _get_user_token(self):
        user_token = token_manager.get_access_token_by_user_id(self.user_info.id)
        return user_token

    def update_user_token(self, expiry_time):
        if not self.user_token:
            # create user token
            token_manager.create_access_token(
                self.user_info.id, self.access_token, expiry_time
            )

        else:
            # update user token
            token_manager.update_access_token_by_user_id(
                self.user_info.id, self.access_token, expiry_time
            )

    def _generate_data_obj(self):
        data = {
            "iat": get_timestamp(),
            "jti": str(uuid.uuid1()),
            "iss": self.iss
        }
        return data

    def get_token_obj(self):
        token_obj = {
            "token_type": "Bearer",
        }

        if self.access_token:
            token_obj["access_token"] = "%s %s" % ("Bearer" , self.access_token)

        return token_obj

    def generate_access_token(self):
        raise NotImplementedError

class PasswordGrandModel(AuthorizationModel):
    def __init__(self, data):
        super().__init__(data)

    def get_access_token(self):
        current_ts = get_timestamp()
        if self.user_token and self.user_token.expiry_time >= current_ts:
            self.access_token = self.user_token.access_token
        else:
            self.generate_access_token()

    def generate_access_token(self):
        expiry_time = get_expired_time_token()
        email = self.user_info.email
        user_id = self.user_info.id
        data = self.data_obj
        data["subject"] = email[0: email.index("@")]
        data["email"] = self.user_info.email
        data["phone"] = self.user_info.phone
        data["user_id"] = user_id
        data["user_name"] = self.user_info.username
        role_alias = role_manager.get_role_info_by_user_id(user_id)
        data["role"] = role_alias

        self.access_token = jwt.encode(data, self.secret_key, algorithm=self.algorithm).decode('ascii')

        # Update the access token of user
        self.update_user_token(expiry_time)

GRANT_TYPE = {
    1: PasswordGrandModel,
}

def get_grant_type(grant_type, data):
    """
    :param data:
    :param grant_type:
    :return: Grant type Model
    """
    model = GRANT_TYPE.get(grant_type)
    return model(data)


def generate_token_obj(user_info, secret_key=config.SECRET_KEY, algorithm="HS256", grand_type=GrandType.PASSWORD):
    data = {
        "user_info": user_info,
        "algorithm": algorithm,
        "secret_key": secret_key,
    }

    authorization_model = get_grant_type(grand_type, data)
    authorization_model.get_access_token()
    return authorization_model.get_token_obj()
