def test_name_twice(monkeypatch, capsys):
    monkeypatch.setattr("builtins.input", lambda _: "Mike O'hearn")

    import name_twice

    captured = capsys.readouterr()

    assert captured.out.strip().splitlines() == [
        "Mike O'hearn",
        "Mike O'hearn",
    ]
