from TechBaseVN_Lib.form_schema import *

LoginSchema = {
    'type': 'object',
    'properties': {
        'username': StringSchema,
        "password": StringSchema,
    },
    'required': ['username', 'password']
}

AdminCreateGroupSchema = {
    'type': 'object',
    'properties': {
        'group_name': StringSchema,
    },
    'required': ['group_name']
}

AdminCreateTeamSchema = {
    'type': 'object',
    'properties': {
        'team_name': StringSchema,
    },
    'required': ['team_name']
}

AdminCreateUserLoginSchema = {
    'type': 'object',
    'properties': {
        'username': StringSchema,
        "password": StringSchema,
        "email": StringSchema,
        "phone": StringSchema
    },
    'required': ['username', 'password']
}

AdminGetUserIdsSchema = {
    'type': 'object',
    'properties': {
        'group_id': Int32Schema,
        "team_id": Int32Schema,
    },
}

AdminGetUserInfosSchema = {
    'type': 'object',
    'properties': {
        "user_ids": {
            "type": "array",
            "minItems": 1,
            "maxItems": 1500,
            "items": UInt32Schema
        }
    },
    'required': ['user_ids']
}

AdminSetUserMappingGroupSchema = {
    'type': 'object',
    'properties': {
        'user_id': Int32Schema,
        "group_id": Int32Schema,
    },
    'required': ['user_id', "group_id"]
}

AdminSetGroupMappingTeamSchema = {
    'type': 'object',
    'properties': {
        'group_id': Int32Schema,
        "team_id": Int32Schema,
    },
    'required': ['group_id', "team_id"]
}

AdminSetUserMappingTeamSchema = {
    'type': 'object',
    'properties': {
        'user_id': Int32Schema,
        "team_id": Int32Schema,
    },
    'required': ['user_id', "team_id"]
}

AdminSetUserRoleSchema = {
    'type': 'object',
    'properties': {
        'user_id': Int32Schema,
        "role_id": Int32Schema,
    },
    'required': ['user_id', "role_id"]
}