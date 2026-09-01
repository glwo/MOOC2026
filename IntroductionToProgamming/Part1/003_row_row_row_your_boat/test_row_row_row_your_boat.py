def test_emoticon(capsys):
    import row_row_row_your_boat

    captured = capsys.readouterr()

    assert captured.out.strip().splitlines() == [
        "Row, row, row your boat,",
        "Gently down the stream.",
        "Merrily, merrily, merrily, merrily,",
        "Life is but a dream.",
    ]
