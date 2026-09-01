def test_emoticon(capsys):
    import emoticon

    captured = capsys.readouterr()

    assert captured.out.strip() == ":-)"
