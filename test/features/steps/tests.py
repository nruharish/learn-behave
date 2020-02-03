from behave import *
from application.maths import add

@given( 'two numbers {number1} and {number2}')
def step_impl(context,number1, number2):
    context.number1 = number1
    context.number2 = number2

@when('we add the numbers')
def step_impl(context):
    context.result = add(float(context.number1), float(context.number2))

@then('we should get {result}')
def step_impl(context, result):
    print(context.result)
    assert context.result == float(result)