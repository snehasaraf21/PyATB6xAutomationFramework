import allure
import pytest
import requests
from src.modules.wrappers.api_requests_wrappers import post_request , put_request,delete_request
from src.endpoints.api_constants import APIConstants
from src.utilities.util import utils
from src.modules.payload_manager.payload_manager import payload_create_token , paylaod_create_booking , paylaod_update_booking
from src.modules.verifications.common_verification import *



# FLOW of the E2E
# Create a token
# Create a booking ID.
# We need to update the booking ID. With token
# We are going to delete the booking ID.
# We are going to verify that booking ID does not exist after delete.
#CONFTEST-`**conftest.py**`** = central place for test configuration and shared logic**

class TestCRUDBooking(object):


    @allure.title("Test CRUD operation(PUT)")
    @allure.description("Verify that Full Update with the booking ID and Token is working.")

    def test_update_booking_id_token(self, create_token, get_booking_id):
        put_url = APIConstants().url_put_patch_delete(booking_id = get_booking_id)
        print(put_url)
        print(create_token)


        response = put_request(
            url = put_url,
            headers = utils().common_headers_put_delete_patch_cookie(token=create_token),
            payload = paylaod_update_booking(),
            auth = None,
            in_json = False,

        )
        verify_http_status_code(response_data_status=response.status_code,expected_data=200)
        verify_response_key(response.json()["firstname"],expected_data="Jim")
        verify_response_key(response.json()["lastname"],expected_data="Brown")

    def test_delete_booking_id(self, create_token, get_booking_id):
        delete_url = APIConstants().url_put_patch_delete(booking_id=get_booking_id)
        response = delete_request(
            url=delete_url,
            headers=utils().common_headers_put_delete_patch_cookie(token=create_token),
            auth=None,
            in_json=False
        )
        verify_response_delete(response=response.text)
        verify_http_status_code(response_data_status=response.status_code, expected_data=201)


