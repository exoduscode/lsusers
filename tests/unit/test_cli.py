from lsusers import cli
from lsusers.platforms import UnsupportedPlatformError


def test_cli_reports_unsupported_platform_without_traceback(monkeypatch, capsys):
    def unsupported_list_users():
        raise UnsupportedPlatformError("unsupported platform 'win32'; supported platforms: linux, darwin")

    monkeypatch.setattr(cli, "list_users", unsupported_list_users)

    assert cli.main([]) == 1
    assert capsys.readouterr().err == (
        "lsusers: error: unsupported platform 'win32'; supported platforms: linux, darwin\n"
    )


def test_cli_preserves_positional_commands():
    parser = cli.build_parser()

    assert parser.parse_args([]).command == "human"
    assert parser.parse_args(["human"]).command == "human"
    assert parser.parse_args(["system"]).command == "system"
    assert parser.parse_args(["all"]).command == "all"
    assert parser.parse_args(["count"]).command == "count"

