import re

tokens = [
    ('KEYWORD', r'fi|rof|tnirp|fed|esle|file'),
    ('NUMBER', r'\d+'),
    ('IDENTIFIER', r'[a-zA-Z_]\w*'),
    ('PUNCTUATION', r'[\(\)\[\]\{\},;:\']'),
    ('OPERATOR', r'[+\-*/=%]'),
    ('TAB', r'\t'),
    ('NEWLINE', r'\n'),
    ('SPACE', r'\s+'), 
]

def lexer(code):
    token_regex = '|'.join(f'(?P<{t[0]}>{t[1]})' for t in tokens)
    pos = 0
    while pos < len(code):
        match = re.match(token_regex, code[pos:])
        if match:
            token_type = match.lastgroup
            token_value = match.group()
            if token_type == 'WHITESPACE':
                if pos + len(token_value) < len(code) and code[pos + len(token_value)] == '\n':
                    yield 'NEWLINE', '\n'
            else:
                yield token_type, token_value
            pos += len(token_value)
        else:
            pos += 1

def parse(tokens):
    idx = 0
    parsed_code = ""
    while idx < len(tokens):
        token_type, token_value = tokens[idx]
        if token_type == 'KEYWORD' and token_value == 'rof':
            parsed_code += 'for'
        elif token_type == 'KEYWORD' and token_value == 'fi':
            parsed_code += 'if'
        elif token_type == 'KEYWORD' and token_value == 'tnirp':
            parsed_code += 'print'
        elif token_type == 'KEYWORD' and token_value == 'esle':
            parsed_code += 'else'
        elif token_type == 'KEYWORD' and token_value == 'file':
            parsed_code += 'elif'
        elif token_type == 'KEYWORD' and token_value == 'fed':
            parsed_code += 'def'
        elif token_type == 'TAB':
            parsed_code += '\t'
        elif token_type == 'NEWLINE':
            parsed_code += '\n'
        else:
            parsed_code += token_value

        idx += 1
    return parsed_code.strip()

def translate(input_code):
    tokens = list(lexer(input_code))
    parsed_code = parse(tokens)
    return parsed_code