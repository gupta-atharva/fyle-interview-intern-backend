from core.libs.exceptions import FyleError

def test_fyle_error_to_dict():
    error_message = "This is a test error"
    status_code = 404
    error = FyleError(status_code, error_message)

    result = error.to_dict()

    assert result == {'message': error_message}