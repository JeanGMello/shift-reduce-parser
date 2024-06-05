from sly import Parser

from MyLexer import MyLexer

class MyParser(Parser):
    # Get the token list from the lexer (required)
    tokens = MyLexer.tokens

    # Grammar rules and actions
    @_('expr NOT_EQUAL expr')
    def expr(self, p):
        return p.expr0 != p.expr1

    @_('FALSE')
    def expr(self, p):
        return False

    @_('TRUE')
    def expr(self, p):
        return True

    @_('expr MOD expr')
    def expr(self, p):
        return p.expr0 % p.expr1

    @_('ID INCREMENT')
    def expr(self, p):
        # increment variable
        print(f'Increment {p.ID}')
        return f'{p.ID} += 1'

    @_('ID DECREMENT')
    def expr(self, p):
        # decrement variable
        print(f'Decrement {p.ID}')
        return f'{p.ID} -= 1'

    @_('NUMBER')
    def expr(self, p):
        return int(p.NUMBER)

    @_('ID')
    def expr(self, p):
        # Placeholder action for identifiers
        return p.ID

if __name__ == '__main__':
    lexer = MyLexer()
    parser = MyParser()

    while True:
        try:
            text = input('input: ')
            if text.strip() == 'exit':
                break
            result = parser.parse(lexer.tokenize(text))
            print(result)
        except EOFError:
            break
        except Exception as e:
            print(e)
