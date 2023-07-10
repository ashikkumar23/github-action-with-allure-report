import pytest
from assertpy import assert_that, soft_assertions
from pytest_bdd import when, scenarios, then

from helpers.environment import Env
from step_definitions.test_common import get_request

scenarios("get_user_data.feature")


@pytest.fixture(scope="session")
def context():
    return {}


@when("I send a GET HTTP request")
def send_get_request(set_headers, context):
    get_response = get_request(headers=set_headers)
    context["get_response"] = get_response.json()
    context["get_status_code"] = get_response.status_code


@then("I expect response body to contain all user data")
def validate_all_user_data(context):
    with soft_assertions():
        assert_that(len(context["get_response"]["data"])).is_greater_than(1)
        assert_that(len(context["get_response"]["data"])).is_equal_to(6)


@then("I expect response body to contain a single user data")
def validate_single_user_data(context):
    with soft_assertions():
        assert_that(context["get_response"]["data"]["id"]).is_equal_to(
            int(pytest.globalDict["user_id"])
        )
        assert_that(context["get_response"]["data"]["email"]).is_equal_to(
            Env.get_email()
        )
        assert_that(context["get_response"]["data"]["first_name"]).is_equal_to(
            Env.get_first_name()
        )
        assert_that(context["get_response"]["data"]["last_name"]).is_equal_to(
            Env.get_last_name()
        )
        assert_that(context["get_response"]["data"]["avatar"]).is_equal_to(
            Env.get_avatar()
        )
