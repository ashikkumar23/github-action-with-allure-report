from assertpy import assert_that
from pytest_bdd import then, parsers


@then(parsers.parse('I expect HTTP response code to be "{status_code}" for GET'))
def validate_status_code(status_code, context):
    assert_that(context["get_status_code"]).is_equal_to(int(status_code))


@then(parsers.parse("I expect response body of GET to be non-empty"))
def validate_response_body(context):
    assert_that(context["get_response"]).is_not_equal_to(None)
