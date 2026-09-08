def test_name_and_address(monkeypatch, capsys):
    monkeypatch.setattr("builtins.input", lambda _: "Mike O'hearn")

    import name_and_address

    captured = capsys.readouterr()

    assert captured.out.strip().splitlines() == [
        "Mike O'hearn",
        "Mike O'hearn",
    ]
