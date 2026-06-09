from ops_study_kit.cli import (
    build_evidence_pack,
    check_text,
    create_evidence_pack,
    create_report,
    get_resource_list,
)


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


def test_get_resource_list():
    resources = get_resource_list()
    assert "Available resources:" in resources
    assert "Korean beginner quickstart" in resources
    assert "Linux grep/find lab" in resources
    assert "AWS S3 beginner lab template" in resources
    assert "Japanese study report template" in resources


def test_build_evidence_pack():
    evidence = build_evidence_pack("Linux grep/find practice", "linux")
    assert "# Linux grep/find practice" in evidence
    assert "## Area" in evidence
    assert "linux" in evidence
    assert "## Commands Run" in evidence
    assert "## Portfolio Summary" in evidence
    assert "## Next Practice" in evidence


def test_create_evidence_pack(tmp_path):
    output = tmp_path / "evidence-pack.md"
    create_evidence_pack("Linux grep/find practice", "linux", str(output))
    text = output.read_text(encoding="utf-8")
    assert output.exists()
    assert "# Linux grep/find practice" in text
    assert "## Area" in text
    assert "linux" in text
    assert "## Commands Run" in text
    assert "## Portfolio Summary" in text
    assert "## Next Practice" in text
