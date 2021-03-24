import logging
from django import http
from functools import wraps
from django.views import defaults
from jsonschema import validate
from TechBaseVN_Lib.jsonutils import to_json, from_json
from TechBaseVN_Lib.constants import Result
from TechBaseVN_Lib.manager import token_manager
import re


REGEX_VALIDATE_EMAIL = re.compile(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)")

def api_response_data(result, data=None):
    response = http.HttpResponse(to_json({"result": result, "reply": data}, ensure_ascii=False))
    response['content-type'] = 'application/json; charset=utf-8'
    response['X_CCS_RESULT_CODE'] = result
    return response

def response_http_404(request):
    return defaults.page_not_found(request)

def api_response_error_params(*args):
    return api_response_data(Result.ERROR_PARAMS)

def parse_params(form, error_handler=response_http_404):
    def _parse_params(func):
        @wraps(func)
        def _func(request, *args, **kwargs):
            try:
                formdata = from_json(request.body) if request.body else {}
                validate(formdata, form)
                data = formdata
            except Exception as ex:
                logging.warning("error_body_params|body_param=%s" % request.body)
                return error_handler(request)

            return func(request, data, *args, **kwargs)

        return _func

    return _parse_params

def pre_process_header():
    def _pre_process_header(func):
        def _func(request, *args, **kwargs):
            data = {}
            if len(args) > 0:
                data = args[0]

            headers = request.META
            try:
                data["access_token"] = headers['HTTP_X_ACCESS_TOKEN']

            except Exception as err:
                logging.exception("header_invalid|headers=%s" % headers)
                return api_response_data(Result.ERROR_HEADER)

            if len(args) > 0:
                return func(request, *args, **kwargs)
            else:
                return func(request, data, *args, **kwargs)

        return _func

    return _pre_process_header

def verify_access_token():
    def _verify_access_token(func):
        def _func(request, data, *args, **kwargs):
            if not data.get("access_token"):
                return api_response_data(Result.ERROR_ACCESS_TOKEN_NOT_FOUND)

            if "Bearer" not in data["access_token"]:
                return api_response_data(Result.ERROR_ACCESS_TOKEN_WRONG_FORMAT)

            is_valid, result_code, object_data = token_manager.check_access_token(data["access_token"])
            if not is_valid or result_code != Result.SUCCESS:
                return api_response_data(result_code)

            data["_session"] = object_data
            return func(request, data, *args, **kwargs)
        return _func
    return _verify_access_token

def validate_email(email):
    is_valid = False
    if not email:
        return is_valid
    if REGEX_VALIDATE_EMAIL.match(email):
        is_valid = True
    return is_valid

def validate_phone_number(phone_number):
    if not phone_number:
        return None

    count_plus = phone_number.count("+")

    if count_plus > 1:
        return None

    if count_plus == 1:
        phone_number = phone_number.replace("+", "")

    if not phone_number.isdigit():
        return None

    if len(phone_number) > 15 or len(phone_number) < 5:
        return None

    return phone_number

def required_roles(required_list_groups):
    def _required_roles(func):
        def _func(request, data, *args, **kwargs):
            user_role = data["_session"]["role"]
            if not user_role:
                return api_response_data(Result.ERROR_ROLE_IS_NOT_SET)
            if user_role not in required_list_groups:
                return api_response_data(Result.ERROR_PERMISSION_DENIED)
            return func(request, data, *args, **kwargs)
        return _func
    return _required_roles
