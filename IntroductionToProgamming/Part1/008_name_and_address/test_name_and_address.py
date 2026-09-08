def test_name_and_address(monkeypatch, capsys):
    inputs = iter(["Rich", "Piana", "91 Weighted Dips Dr", "Gainnesville 32937"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    import name_and_address

    captured = capsys.readouterr()

    assert captured.out.strip().splitlines() == [
        "Rich Piana",
        "91 Weighted Dips Dr",
        "Gainnesville 32937",
    ]
