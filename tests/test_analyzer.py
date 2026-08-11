from analyzer import analyze_logs


def test_analyze_logs():
    logs = [
        "INFO: Application started",
        "INFO: User logged in",
        "WARNING: Disk space is low",
        "ERROR: Database failed"
    ]

    log_levels = ["INFO", "WARNING", "ERROR"]
    result = analyze_logs(logs, log_levels)

    assert result["INFO"] == 2
    assert result["WARNING"] == 1
    assert result["ERROR"] == 1