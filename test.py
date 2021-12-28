import main as m

def test_hi():
    if len(m.hi()) > 0:
        print('Pass: hi function')
    else:
        assert False, 'hi function is not working'

def test_bye():
    if len(m.bye()) > 0:
        print('Pass: bye function')
    else:
        assert False, 'bye function is not working'

def test_hello_again():
    if len(m.hello_again()) < 0:
        print('Pass: hello_again function')
    else:
        assert False, 'hello_again function is not working'


test_hi()
test_bye()
test_hello_again()