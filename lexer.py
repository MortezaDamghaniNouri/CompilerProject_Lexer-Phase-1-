from ply import lex

reserved = {"int": "INTEGER", "float": "FLOAT", "bool": "BOOLEAN", "fun": "FUNCTION", "print": "PRINT", "True": "TRUE",
            "return": "RETURN", "main": "MAIN", "if": "IF", "else": "ELSE", "False": "FALSE", "elseif": "ELSEIF",
            "while": "WHILE", "on": "ON", "where": "WHERE", "for": "FOR", "and": "AND", "or": "OR", "not": "NOT",
            "in": "IN", "=": "ASSIGN", "+": "SUM", "-": "SUB", "*": "MUL",
            "/": "DIV", "%": "MOD", ">": "GT", ">=": "GE", "<": "LT",
            "<=": "LE", "==": "EQ", "!=": "NE", "{": "LCB", "}": "RCB",
            "(": "LRB", ")": "RRB", "[": "LSB", "]": "RSB", ";": "SEMICOLON",
            ":": "COLON", ",": "COMMA"}


class Lexer:
    tokens = ["ID", "INTEGERNUMBER", "FLOATNUMBER", "INTEGER", "FLOAT",
              "BOOLEAN", "FUNCTION", "TRUE", "FALSE", "PRINT", "RETURN",
              "MAIN", "IF", "ELSE", "ELSEIF", "WHILE", "ON", "WHERE", "FOR",
              "AND", "OR", "NOT", "IN", "ASSIGN", "SUM", "SUB", "MUL", "DIV",
              "MOD", "GT", "GE", "LT", "LE", "EQ", "NE", "LCB", "RCB",
              "LRB", "RRB", "LSB", "RSB", "SEMICOLON", "COLON", "COMMA", "ERROR"]

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
    t_NE = r"\!="
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
        r"[a-z_][0-9A-Za-z_]*"
        if t.value in reserved:
            t.type = reserved[t.value]
        return t

    def t_ERROR_one(self, t):
        r"([0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9]*(\.)[0-9]+)|(([0-9]+(\.)[0-9]+(\.))([0-9]+(\.)?)*)"
        t.type = "ERROR"
        return t

    def t_ERROR_two(self, t):
        r"((([+*/%\-][ \t\n]*[+\-/%*][ \t\n]*)+)([+*/\-%][ \t\n]*)*|([0-9][0-9]*[A-Za-z_]+)|([A-Z][A-Za-z0-9_]+)|[0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9]*)"
        if t.value in reserved:
            t.type = reserved[t.value]
        else:
            t.type = "ERROR"
        return t

    def t_FLOATNUMBER(self, t):
        r"([0-9]?[0-9]?[0-9]?[0-9]?[0-9]?[0-9]?[0-9]?[0-9]?[0-9](\.)[0-9]+)"
        string = t.value
        string = string.lstrip("0")
        if string[0] == '.':
            string = "0" + string
        string = string.rstrip("0")
        size = len(string)
        if string[size - 1] == '.':
            string = string + "0"
        t.value = string
        return t

    def t_INTEGERNUMBER(self, t):
        r"([0-9]?[0-9]?[0-9]?[0-9]?[0-9]?[0-9]?[0-9]?[0-9]?[0-9])"
        string = t.value
        t.value = string.lstrip("0")
        if t.value == "":
            t.value = "0"
        return t

    def t_newline(self, t):
        r'\n+'
        t.lexer.lineno += len(t.value)

    t_ignore = '\n \t'

    def t_ERROR_three(self, t):
        r"[^\s+\-*/%\(\)\{\}\[\]=\>\<!;:,]+"
        if t.value in reserved:
            t.type = reserved[t.value]
        else:
            t.type = "ERROR"
        return t

    def t_error(self, t):
        raise Exception('Error at', t.value)

    def build(self, **kwargs):
        self.lexer = lex.lex(module=self, **kwargs)
        return self.lexer




