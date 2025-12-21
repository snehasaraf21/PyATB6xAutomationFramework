#commom verifications
#HTTP status code
#json schema
#headers
#data verification


def verify_http_status_code(response_data_status,expected_data):
    assert response_data_status == expected_data, "Failed to match the Status code"

def verify_response_key(key,expected_data):
    assert key == expected_data

def verify_json_key_for_not_null(key):
    assert key != 0 , "Failed-key is not empty"+ key
    assert key > 0 , "Failed-key is greater than 0"

def verify_json_key_not_null_token(key):
    assert key != 0 , "Failed-key is not empty"+ key

def verify_response_delete(response):
    assert "Created" in response