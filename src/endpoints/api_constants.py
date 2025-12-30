#api constants will have class with all the end points
#for restful booker end points are
#/bookingId,/auth,/ping

class APIConstants:
    def base_url(self):
        return "https://restful-booker.herokuapp.com/booking"

    def create_booking(self):
        return "https://restful-booker.herokuapp.com/booking"

    def url_create_token(self):
        return "https://restful-booker.herokuapp.com/auth"

    # for PUT,PATCH,DELETE - bookingID
    def url_put_patch_delete(self,booking_id):
        return "https://restful-booker.herokuapp.com/booking/" + str(booking_id)
