from antlr4 import InputStream, CommonTokenStream
from Cond1Lexer import Cond1Lexer
from Cond1Parser import Cond1Parser
from EvalVisitor1 import EvalVisitor1


def ejecutar(codigo):
    lexer = Cond1Lexer(InputStream(codigo))
    tokens = CommonTokenStream(lexer)
    parser = Cond1Parser(tokens)
    tree = parser.prog()
    EvalVisitor1().visit(tree)


if __name__ == "__main__":
    print("Caso 1: if 2 < 3 / imprime 8 / else imprime 5  -> esperado: 8")
    ejecutar("if 2 < 3\nimprime 8\nelse imprime 5")

    print("\nCaso 2: if 5 < 8 / imprime 6  -> esperado: 6")
    ejecutar("if 5 < 8\nimprime 6")

    print("\nCaso 3: if 8 < 5 / imprime 6  -> esperado: (nada)")
    ejecutar("if 8 < 5\nimprime 6")
