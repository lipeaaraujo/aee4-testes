from decoder import decodeMessage

def test_string_vazia():
  assert decodeMessage("") == ""

def test_vogais_duplicadas():
  assert decodeMessage("aa") == "a"

def test_vogais_duplicadas2():
  assert decodeMessage("a") == "a"
  assert decodeMessage("aaa") == "a"
  assert decodeMessage("aaaa") == "a"
  assert decodeMessage("ee") == "a"
