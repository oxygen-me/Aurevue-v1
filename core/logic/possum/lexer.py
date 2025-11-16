class Lexer:
    KEYWORDS = {
        "probably", "with", "means",
        "politely", "decide", "beg",
        "ask", "sleep", "in", "as",
        "using", "poke", "plead",
        "require", "awaken", "behead",
    }

    SINGLE_CHAR = {

    "{": "LBRACE",
    "}": "RBRACE",
    "[": "LBRACKET",
    "]": "RBRACKET",
    "(": "LPAREN",
    ")": "RPAREN",
    ",": "COMMA",
    ":": "COLON",
    ";": "SEMICOLON",
    "/": "SLASH",
    }

    def __init__(self, source):
        self.source = source
        self.position = 0
        self.length = len(source)

    def _peek(self):
        if self.position >= self.length:
            return '\0'
        return self.source[self.position]

    def _advance(self):
        ch = self._peek()
        self.position += 1
        return ch

    def tokenize(self):
        tokens = []

        while self.position < self.length:
            ch = self._peek()

            if ch.isspace():
                self._advance()
                continue

            if ch in self.SINGLE_CHAR:
                tokens.append((self.SINGLE_CHAR[ch], ch))
                self._advance()
                continue

            if ch.isalpha():
                ident = self._consume_identifier()
                if ident in self.KEYWORDS:
                    tokens.append(("KEYWORD", ident))
                else:
                    tokens.append(("IDENT", ident))
                continue

            if ch.isdigit():
                num = self._consume_number()
                tokens.append(("NUMBER", num))
                continue

            if ch == '"':
                string = self._consume_string()
                tokens.append(("STRING", string))
                continue

            raise Exception(f"[Lexer] Unknown character: {ch}")
        tokens.append(("EOF", None))
        return tokens

    def _consume_identifier(self):
        start = self.position
        while self._peek().isalnum() or self._peek() in ["_", "-"]:
            self._advance()
        return self.source[start:self.position]

    def _consume_number(self):
        start = self.position
        while self._peek().isdigit():
            self._advance()
        return self.source[start:self.position]

    def _consume_string(self):
        self._advance()
        start = self.position

        while True:
            ch = self._peek()
            if ch == '\0':
                raise Exception("[Lexer] Unterminated string")
            if ch == '"':
                text = self.source[start:self.position]
                self._advance()
                return text
            self._advance()