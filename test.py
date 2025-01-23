from jwt import decode
from decoder import decodeMessage

def test_string_vazia():
  assert decodeMessage("") == ""

def test_vogais_duplicadas():
  assert decodeMessage("aa") == "a"
  assert decodeMessage("ee") == "e"
  assert decodeMessage("ii") == "i"
  assert decodeMessage("oo") == "o"
  assert decodeMessage("uu") == "u"

def test_vogais_duplicadas2():
  assert decodeMessage("a") == "a"
  assert decodeMessage("aaa") == "aa"
  assert decodeMessage("aaaa") == "aa"
  assert decodeMessage("aaaaa") == "aaa"
  
def test_caracteres_especiais():
  assert decodeMessage("*") == "@"
  assert decodeMessage("|") == "!"
  assert decodeMessage("$") == "?"
  assert decodeMessage("_") == " "
  assert decodeMessage("#") == ""
  assert decodeMessage("^") == ""
  assert decodeMessage("*$") == "@?"
  assert decodeMessage("*|$__#^") == "@!?  "
  
def test_decrementar_numeros():
  assert decodeMessage("0") == "9"
  assert decodeMessage("1") == "0"
  assert decodeMessage("2") == "1"
  assert decodeMessage("3") == "2"
  assert decodeMessage("4") == "3"
  assert decodeMessage("5") == "4"
  assert decodeMessage("6") == "5"
  assert decodeMessage("7") == "6"
  assert decodeMessage("8") == "7"
  assert decodeMessage("9") == "8"
  assert decodeMessage("0123456789") == "9012345678"
  
def test_inverter_consoantes():
  assert decodeMessage("b") == "z"
  assert decodeMessage("c") == "y"
  assert decodeMessage("palavra") == "maqagka"
  assert decodeMessage("peenjaaveep_xee_aaqiieen*234|") == "mensagem de alien@123!"