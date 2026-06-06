from ops_study_kit.cli import check_text, create_report


def test_check_text_pass(tmp_path):
    log = tmp_path / "app.log"
    log.write_text("INFO ok\nERROR database failed\n", encoding="utf-8")
    assert check_text(str(log), "ERROR") == 0


def test_check_text_fail(tmp_path):
    log = tmp_path / "app.log"
    log.write_text("INFO ok\n", encoding="utf-8")
    assert check_text(str(log), "ERROR") == 1


def test_create_report(tmp_path):
    output = tmp_path / "report.md"
    create_report("Linux Practice", str(output))
    assert output.exists()
    assert "# Linux Practice" in output.read_text(encoding="utf-8")
