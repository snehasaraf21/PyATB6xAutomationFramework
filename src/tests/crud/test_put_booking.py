import allure
import pytest
import requests
from src.modules.wrappers.api_requests_wrappers import *
from src.endpoints.api_constants import *
from src.utilities.util import utils
from src.modules.payload_manager.payload_manager import *
from src.modules.verifications.common_verification import *

class TestPutBooking:

    @pytest.mark.positive
    @allure.title("Verify that existing booking ID with existing token can be updated using PUT")
    @allure.description("Create a booking, generate token, and update the booking using PUT")
    class TestPUTBooking:

        @pytest.mark.positive
        @allure.title("Verify that the existing booking ID with existing token update is happening")
        @allure.description("")
        class TestPUTBooking:

            @pytest.mark.positive
            @allure.title("Verify that the existing booking ID with existing token update is happening")
            @allure.description("")
            def test_verify_existing_booking_update_put(self):
                bookingId = 1
                tokne = "ox232m3m23kl"
                pass

            @pytest.mark.negative
            @allure.title("Verify that if you try to update without the token, you get an error.")
            @allure.description("")
            def test_verify_existing_booking_update_put_with_auth(self):
                bookingId = 1
                tokne = "ox232m3m23kl"
                pass

