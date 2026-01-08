from library import printBooks

def test_lib():
    op=(
        "Book id:101\n"
        "Book title:The Lord\n"
        "Authour name:Dr. Raj\n"
        "Year of publication:2007"
    )

    assert printBooks(101,"The Lord","Dr. Raj",2007) == op

    