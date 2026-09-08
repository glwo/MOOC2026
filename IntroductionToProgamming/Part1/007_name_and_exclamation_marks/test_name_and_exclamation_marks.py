def test_name_twice(monkeypatch, capsys):
    monkeypatch.setattr("builtins.input", lambda _: "Mike O'hearn")

    import name_and_exclamation_marks

    captured = capsys.readouterr()

    assert captured.out.strip() == "!Mike O'hearn!Mike O'hearn!"
