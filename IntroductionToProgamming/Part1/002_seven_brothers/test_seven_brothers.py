def test_emoticon(capsys):
    import seven_brothers

    captured = capsys.readouterr()
    lines = captured.out.strip().splitlines()

    assert lines[0] == "Aapo"
    assert lines[1] == "Eero"
    assert lines[2] == "Juhani"
    assert lines[3] == "Lauri"
    assert lines[4] == "Simeoni"
    assert lines[5] == "Timo"
    assert lines[6] == "Tuomas"
