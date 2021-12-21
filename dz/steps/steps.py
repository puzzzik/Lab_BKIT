from test import TestBot
from behave import given, when, then


@given("Entered data")
def start_up(context):
    context.a = TestBot()


@when("Check Tula Russia")
def test1(context):
    context.a.test_1()


@when("Check None")
def test2(context):
    context.a.test_2()


@when("Check Istanbul Turkey")
def test3(context):
    context.a.test_3()


@then("Completed")
def check_result(context):
    pass
