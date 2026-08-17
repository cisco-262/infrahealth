from unittest.mock import Mock, patch

from infrahealth.http import check_http


@patch("infrahealth.http.requests.get")
def test_http_200(mock_get):
    response = Mock()
    response.status_code = 200
    response.url = "https://example.com"
    mock_get.return_value = response

    result = check_http("https://example.com")

    assert result.ok is True
    assert result.status == "HTTP 200"
