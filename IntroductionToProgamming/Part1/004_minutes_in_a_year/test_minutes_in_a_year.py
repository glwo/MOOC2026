def test_minutes_in_a_year(capsys):
    import minutes_in_a_year

    captured = capsys.readouterr()

    assert captured.out.strip() == "525600"
