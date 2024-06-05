from sly import Lexer

class MyLexer(Lexer):
    # Set of token names. This is always required
    tokens = { NOT_EQUAL, FALSE, TRUE, MOD, INCREMENT, DECREMENT, ID, NUMBER }

    # String containing ignored characters between tokens
    ignore = ' \t'

    # Regular expression rules for tokens
    NOT_EQUAL = r'!='
    FALSE = r'falso'
    TRUE = r'vdd'
    MOD = r'mod'
    INCREMENT = r'\+\+'
    DECREMENT = r'--'

    # Identifiers and numbers
    ID = r'[a-zA-Z_][a-zA-Z0-9_]*'
    NUMBER = r'\d+'

    # Ignore newline characters and track line numbers
    ignore_newline = r'\n+'
    def ignore_newline(self, t):
        self.lineno += t.value.count('\n')

    # Additional action for tracking line numbers
    def newline(self, t):
        self.lineno += 1

if __name__ == '__main__':
    data = '''
    falso vdd mod != ++ -- 123 abc
    '''
    lexer = MyLexer()
    for token in lexer.tokenize(data):
        print(token)
