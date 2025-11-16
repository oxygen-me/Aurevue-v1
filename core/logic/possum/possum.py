from lexer import Lexer
from parser import Parser
from runtime import Runtime

def run_possum(source):
    lexer = Lexer(source)
    tokens = lexer.tokenize()

    parser = Parser(tokens)
    ast = parser.parse()

    runtime = Runtime()
    runtime.execute(ast)

if __name__ == "__main__":
    import sys
    source = open(sys.argv[1]).read()
    run_possum(source)