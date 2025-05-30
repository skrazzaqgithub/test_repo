import pytest
import requests

def test_getRequest_Validation():
    header = {'content-Type': 'application/json'}
    base_url = 'https://reqres.in/'
    response = requests.get(url= base_url + '/api/users/', headers=header)
    assert 200 == response.status_code
    print(response.text)
# output = test_getRequest_Validation()
# print(output)

# @pytest.fixture()
# def log_on_failure(request):
#     yield
#     item = request.node
#     if item.rep_call.failed:
#         allure.attach(driver.get_screenshot_as_png().name="failed_test", attachment_tye=AttachmentType.PNG)

@pytest.fixture()
def something(request):
    if request.function.failed:
        print("I failed")