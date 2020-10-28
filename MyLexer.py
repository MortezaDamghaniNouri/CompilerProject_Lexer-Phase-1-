from ply import lex


class Lexer:
    tokens = ["ID", "INTEGERNUMBER", "FLOATNUMBER", "INTEGER", "FLOAT",
              "BOOLEAN", "FUNCTION", "TRUE", "FALSE", "PRINT", "RETURN",
              "MAIN", "IF", "ELSE", "ELSEIF", "WHILE", "ON", "WHERE", "FOR",
              "AND", "OR", "NOT", "IN", "ASSIGN", "SUM", "SUB", "MUL", "DIV",
              "MOD", "GT", "GE", "LT", "LE", "EQ", "NE", "LCB", "RCB",
              "LRB", "RRB", "LSB", "RSB", "SEMICOLON", "COLON", "COMMA", "ERROR!"]

    t_INTEGER = r"int"
    t_FLOAT = r"float"
    t_BOOLEAN = r"bool"
    t_FUNCTION = r"fun"
    t_TRUE = r"True"
    t_FALSE = r"False"
    t_PRINT = r"print"
    t_RETURN = r"return"
    t_MAIN = r"main"
    t_IF = r"if"
    t_ELSE = r"else"
    t_ELSEIF = r"elseif"
    t_WHILE = r"while"
    t_ON = r"on"
    t_WHERE = r"where"
    t_FOR = r"for"
    t_AND = r"and"
    t_OR = r"or"
    t_NOT = r"not"
    t_IN = r"in"
    t_ASSIGN = r"\="
    t_SUM = r"\+"
    t_SUB = r"\-"
    t_MUL = r"\*"
    t_DIV = r"\/"
    t_MOD = r"\%"
    t_GT = r"\>"
    t_GE = r"\>="
    t_LT = r"\<"
    t_LE = r"\<="
    t_EQ = r"\=="
    t_NE = r"!="
    t_LCB = r"\{"
    t_RCB = r"\}"
    t_LRB = r"\("
    t_RRB = r"\)"
    t_LSB = r"\["
    t_RSB = r"\]"
    t_SEMICOLON = r";"
    t_COLON = r":"
    t_COMMA = r","

    def t_ID(self, t):
        reserved = ["Int", "Float", "Bool", "Fun", "True", "False", "Print",
                    "Return", "Main", "If", "Else", "Elseif", "While",
                    "On", "Where", "For", "And", "Or", "Not", "In", "Error"]
        r"[a-z_][0-9A-Za-z_]*"
        if t.value in reserved:
            t.type = "ERROR!"
        return t

    def t_INTEGERNUMBER(self, t):
        r"([1-9]?[1-9]?[1-9]?[1-9]?[1-9]?[1-9]?[1-9]?[1-9]?[1-9]?[1-9])|[0]"
        return t

    def t_FLOATNUMBER(self, t):
        r"(([1-9]?[1-9]?[1-9]?[1-9]?[1-9]?[1-9]?[1-9]?[1-9]?[1-9]?[1-9])(\.)([0-9]*[1-9]))|[0]"
        return t

    def t_ERROR(self, t):
        r"([*/+-%][\n\t ]*[*/+-%][\n\t ])+"
        t.type = "ERROR!"
        return t

    def t_newline(self, t):
        r'\n+'
        t.lexer.lineno += len(t.value)

    t_ignore = '\n \t'

    def t_error(self, t):
        raise Exception('Error at', t.value)

    def build(self, **kwargs):
        self.lexer = lex.lex(module=self, **kwargs)
        return self.lexer




