import pytest

class StringProcessor:
    @staticmethod
    def process(text: str) -> str:
        if not text:
            return "."
        processed_text = text[0].upper() + text[1:]
        if not processed_text.endswith("."):
            processed_text += "."
        return processed_text

@pytest.mark.parametrize("text, result", [("Abc", "Abc."), ("abc.", "Abc."), ("abc def.", "Abc def."), ("ABC.", "ABC.")] )
def test_one_upper(text, result):
    StringProcessor()
    assert StringProcessor.process(text) == result

def test_empty_string():
    StringProcessor()
    res = StringProcessor.process("")
    assert res == "."

def test_space_string():
    StringProcessor()
    res = StringProcessor.process(" ")
    assert res == " ."