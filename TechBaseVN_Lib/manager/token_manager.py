import jwt
import logging
from db_model.models import TBVN_DB
from TechBaseVN_Lib.date_utils import get_timestamp
from TechBaseVN_Lib.constants import Result
from config import SECRET_KEY
from TechBaseVN_Lib.manager import user_manager

def get_access_token_by_user_id(user_id):
    model = TBVN_DB.AccessTokenTab.objects.filter(user_id=user_id).first()
    return model

def update_access_token_by_user_id(user_id, access_token='', expiry_time=0):
    affected_count = TBVN_DB.AccessTokenTab.objects.filter(user_id=user_id).update(
        access_token=access_token,
        expiry_time=expiry_time,
        updated_time=get_timestamp()
    )
    return affected_count

def create_access_token(user_id, access_token, expiry_time):
    created_time = updated_time = get_timestamp()
    try:
        TBVN_DB.AccessTokenTab.objects.create(
            user_id=user_id,
            access_token=access_token,
            expiry_time=expiry_time,
            created_time=created_time,
            updated_time=updated_time
        )
        return 1
    except Exception as ex:
        logging.warning("create_access_token_fail|error=%s" % ex)
        return 0

def decrypt_access_token(access_token, secret_key=SECRET_KEY, algorithms="HS256"):
    if algorithms is None:
        algorithms = ['HS256']
    try:
        decrypted_access_token = jwt.decode(access_token, secret_key, algorithms=algorithms)
        return decrypted_access_token
    except Exception as err:
        logging.warning("error_decrypt_access_token_fail|error: %s, access_token: %s" % (err, access_token))
        return {}

def check_access_token(access_token, secret_key=SECRET_KEY, algorithm='HS256'):
    is_valid = True
    result_code = Result.SUCCESS
    object_data = decrypt_access_token(
        access_token[str(access_token).index(" ") + 1:], secret_key, algorithm
    )
    if not object_data:
        is_valid = False
        result_code = Result.ERROR_ACCESS_TOKEN_INCORRECT
    else:
        # check existed user
        user_info = user_manager.get_user_info_by_filter(username=object_data["user_name"])

        if not user_info:
            is_valid = False
            result_code = Result.ERROR_USER_NOT_EXISTED

    return is_valid, result_code, object_data
