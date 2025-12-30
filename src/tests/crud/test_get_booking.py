import allure
import pytest
import requests
from src.modules.wrappers.api_requests_wrappers import get_request , post_request
from src.endpoints.api_constants import APIConstants
from src.utilities.util import utils
from src.modules.payload_manager.payload_manager import paylaod_create_booking,paylaod_update_booking
from src.modules.verifications.common_verification import *
import logging


class TestGetBooking:
    @pytest.mark.positive
    @allure.title("Verify the existing booking id (1) exists")
    @allure.description(" Booking id exists")
    def test_verify_existing_booking_id_01(self):
        bookingid=1
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

    @pytest.mark.negative
    @allure.title("Verify the not existing booking id 9999 does not exists")
    @allure.description(" Booking id does not exists")
    def test_verify_booking_id_not_exists_negative01(self):
        invalid_booking_id = 9999

        response = post_request(
            url=APIConstants().create_booking(),
            auth=None,
            headers=utils().common_headers_json(),
            payload=paylaod_create_booking(),
            in_json=False,

        )
        booking_id = response.json()["bookingid"]
        verify_http_status_code(response_data_status=response.status_code, expected_data=400)
        verify_json_key_for_not_null(invalid_booking_id)
        return booking_id








