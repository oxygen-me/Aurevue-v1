class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.position = 0

    def _current(self):
        return self.tokens[self.position]

    def _at_end(self):
        tok_type, _ = self._current()
        return tok_type == "EOF"

    def _consume(self, expected_type, expected_value=None, ctx=""):
        tok_type, tok_val = self._current()
        if tok_type != expected_type:
            raise Exception(
                f"[Parser] Expected {expected_type} in {ctx}"
                f"got {tok_type}({tok_val!r})"
            )
        self.position += 1
        return tok_type, tok_val

    def parse(self):
        ast = []

        while not self._at_end():
            stmt = self._parse_statement()
            if stmt is not None:
                ast.append(stmt)

        return ast

    def _parse_statement(self):
        tok_type, tok_val = self._current()

        if tok_type == "KEYWORD" and tok_val == "awaken":
            return self._parse_awaken()

        if tok_type == "KEYWORD" and tok_val == "sleep":
            return self._parse_sleep()

        if tok_type == "KEYWORD" and  tok_val == "require":
            return self._parse_require()

        if tok_type == "KEYWORD" and tok_val == "ask":
            return self._parse_ask()

        raise Exception(f"[Parser] Unexpected token at statement start: {tok_type}({tok_val!r})")

    def _parse_awaken(self):
        self._consume("KEYWORD", "awaken", ctx="awaken")
        self._consume("LPAREN", ctx="awaken()")
        self._consume("RPAREN", ctx="awaken()")
        return ("AWAKEN", None)

    def _parse_sleep(self):
        self._consume("KEYWORD", "sleep", ctx="sleep")
        self._consume("LPAREN", ctx="sleep()")
        self._consume("RPAREN", ctx="sleep()")
        return ("SLEEP", None)

    def _parse_require(self):
        self._consume("KEYWORD", "require", ctx="require")

        _, kind = self._consume("IDENT", ctx="require kind")

        self._consume("LBRACE", ctx="require{...}")
        _, name = self._consume("IDENT", ctx="require name")
        self._consume("RBRACE", ctx="require {...}")

        return ("REQUIRE", {"kind": kind, "name": name})

    def _parse_ask(self):
        self._consume("KEYWORD", "ask", ctx="ask")

        _, target = self._consume("IDENT", ctx="ask target")

        self._consume("LPAREN", ctx="ask(...)")
        _, arg = self._consume("IDENT", ctx="ask arg")
        self._consume("RPAREN", ctx="ask(...)")

        self._consume("KEYWORD", "as", ctx="ask ... as ...")
        _, alias = self._consume("IDENT", ctx="ask alias")

        return ("ASK", {"target": target, "arg": arg, "alias": alias})