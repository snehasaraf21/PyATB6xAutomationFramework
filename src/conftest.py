import allure
import pytest
import requests
from src.modules.wrappers.api_requests_wrappers import post_request
from src.endpoints.api_constants import APIConstants
from src.utilities.util import utils
from src.modules.payload_manager.payload_manager import payload_create_token , paylaod_create_booking
from src.modules.verifications.common_verification import *

@pytest.fixture
def setup():
    print("setup is started!!!")
    yield
    print("TC execution is finished!!!")

#all the common code will be executed before running other tc
#ex db connection

@pytest.fixture
def db_connection():
    print("db_connection is started!!!")
    yield
    print("db_connection is finished!!!")

#pytest.fixture
#def browser():
 #   driver= launch_browser()
  #  yield driver
   # driver.quit()

#create token
##booking id
@pytest.fixture(scope="session")
def create_token():
    response =post_request(
        url = APIConstants().url_create_token(),
        headers = utils().common_headers_json(),
        auth=None,
        payload=payload_create_token(),
        in_json = False,
    )
    verify_http_status_code(response_data_status=response.status_code, expected_data=200)
    verify_json_key_not_null_token(response.json()["token"])
    return response.json()["token"]


@pytest.fixture(scope="session")
def get_booking_id():
    response = post_request(
        url=APIConstants().create_booking(),
        auth=None,
        headers=utils().common_headers_json(),
        payload=paylaod_create_booking(),
        in_json=False,

    )
    booking_id = response.json()["bookingid"]
    verify_http_status_code(response_data_status=response.status_code, expected_data=200)
    verify_json_key_for_not_null(booking_id)
    return booking_id
