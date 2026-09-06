def test_name_twice(capsys):
    import name_twice

    captured = capsys.readouterr()

    assert captured.out.strip().splitlines() == ["What is your name"]
