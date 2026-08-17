from infrahealth.tcp import check_tcp


def test_tcp_result_shape():
    result = check_tcp("127.0.0.1", 9, timeout=1)
    assert result.check == "tcp:9"
    assert result.target == "127.0.0.1"
    assert isinstance(result.ok, bool)
