import allure
import pytest
import requests
from src.modules.wrappers.api_requests_wrappers import post_request
from src.endpoints.api_constants import APIConstants
from src.utilities.util import utils
from src.modules.payload_manager.payload_manager import paylaod_create_booking
from src.modules.verifications.common_verification import *
import logging









class TestCreateBooking:
    @pytest.mark.positve
    @allure.title("Verify that create booking status and booking ID should not be null")
    @allure.description("Create a Booking from the paylaod and verify that booking id should not be null and status code be 200 for the correct payload")
    LOGGER= logging.getLogger(__name__)
    LOGGER.info("Starting test......")
    def test_create_booking_positive(self):
        LOGGER = logging.getLogger(__name__)
        LOGGER.info("Starting test......")
        LOGGER.info("POST request to create booking")


        response = post_request(
            url = APIConstants().create_booking(),
            auth = None,
            headers = utils().common_headers_json(),
            payload = paylaod_create_booking(),
            in_json = False,

        )
        LOGGER.info("POST request for create booking done")
        LOGGER.info("Verify the status code")

        verify_http_status_code(response_data_status = response.status_code,expected_data = 200)
        verify_json_key_for_not_null(response.json()["bookingid"])
        LOGGER.info("Status code verification done")


    def test_create_booking_negative_tc1(self):
        response = post_request(
            url=APIConstants().create_booking(),
            auth=None,
            headers=utils().common_headers_json(),
            payload={},
            in_json=False
        )
        verify_http_status_code(response_data_status=response.status_code, expected_data=500)

    def test_create_booking_negative_tc2(self):
        response = post_request(
            url=APIConstants().create_booking(),
            auth=None,
            headers=utils().common_headers_json(),
            payload={"firstname":"pramod"},
            in_json=False,

        )
        verify_http_status_code(response_data_status=response.status_code, expected_data=500)




