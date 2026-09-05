def test_print_some_code(capsys):
    import print_some_code

    captured = capsys.readouterr()

    assert captured.out.strip() == 'print("Hello there!")'
