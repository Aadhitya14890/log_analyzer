from file_handler import read_log_file


def test_read_log_file(tmp_path):
    log_file = tmp_path / "test.log"

    log_file.write_text("INFO: Test message\nERROR: Test error\n")

    result = read_log_file(log_file)

    assert len(result) == 2
    assert "INFO: Test message\n" in result
    assert "ERROR: Test error\n" in result