import os

import pytest
import requests
from pytest_bdd import given, when, parsers

from helpers.environment import Env


@given(parsers.parse("I set Req Res API URL to ${base_url}"))
def set_req_res_api_base_url(base_url):
    req_res_api_base_url = os.environ.get(base_url, None)
    if req_res_api_base_url is None:
        raise LookupError(f"Environment variable {req_res_api_base_url} is undefined")
    pytest.globalDict["req_res_api_base_url"] = req_res_api_base_url


@given(parsers.parse('I set Req Res API GET route to "{route}" for all users'))
def set_req_res_api_route_all_users(route):
    pytest.globalDict["api_endpoint"] = (
        pytest.globalDict["req_res_api_base_url"] + route
    )


@given(parsers.parse('I set Req Res API GET route to "{route}" for single user'))
def set_req_res_api_route_single_user(route):
    api_route = route.split("{")[0]
    emp_id = (route.split("{")[-1]).split("}")[0]
    pytest.globalDict["user_id"] = Env.get_user_id(emp_id)
    pytest.globalDict["api_endpoint"] = (
        pytest.globalDict["req_res_api_base_url"]
        + api_route
        + pytest.globalDict["user_id"]
    )


@pytest.fixture
@when(parsers.parse('I set Content-Type as "{content_type}" in headers'))
def set_headers(content_type):
    return {"Content-Type": content_type}


def get_request(headers):
    get_url = pytest.globalDict["api_endpoint"]
    response = requests.get(f"{get_url}", headers=headers)
    print(
        f"Request Method: GET \n"
        f"Request URL: {get_url} \n"
        f"Request Headers: {headers} \n"
        f"Response Status Code: {response.status_code}\nResponse Body: {response.json()}"
    )
    return response
