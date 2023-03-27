import ply.lex as lex

tokens = ( "COMMENT_ML", "COMMENT_L",
          "L_BRACKET", "R_BRACKET", "L_PARENTHESES", "R_PARENTHESES", "L_SQRBRACKET", "R_SQRBRACKET",
          "ASSIGN", "GREATER", "LESS", "MULT", "ADD", "SUB",
          "COMMA", "SEMICOLON",
          "FUNCTION", "PROGRAM", 
          "INT", "CHAR", "FLOAT",
          "WHILE", "FOR", "IF", "PRINT", "IN", "RANGE",
          "VAR"
          )


t_COMMENT_ML = r'\/\*[\w\W]*\*\/'
t_COMMENT_L = r'\/\/.*'
t_L_BRACKET = r'\{'
t_R_BRACKET = r'\}'
t_L_PARENTHESES = r'\('
t_R_PARENTHESES = r'\)'
t_L_SQRBRACKET = r'\['
t_R_SQRBRACKET = r'\]'
t_ASSIGN = r'\='
t_GREATER = r'\>'
t_LESS = r'\<'
t_MULT = r'\*'
t_ADD = r'\+'
t_SUB = r'-'
t_COMMA = r'\,'
t_SEMICOLON = r'\;'


def t_FUNCTION(t):
    r'function\s'
    return t

def t_PROGRAM(t):
    r'program\s'
    return t

def t_INT(t):
    r'int\s'
    return t

def t_CHAR(t):
    r'char\s'
    return t

def t_FLOAT(t):
    r'float\s'
    return t

def t_WHILE(t):
    r'while'
    return t

def t_FOR(t):
    r'for'
    return t

def t_IF(t):
    r'if'
    return t

def t_PRINT(t):
    r'print'
    return t

def t_IN(t):
    r'in'
    return t

def t_RANGE(t):
    r'\[\d+..\d+\]'
    return t

def t_VAR(t):
    r'[\w|_*]+'
    return t

t_ignore = ' \t\n'

def t_error(t):
    print(f'Token invalido: {t.value}')
    t.lexer.skip(1)

data1 = '''/* factorial.p
-- 2023-03-20 
-- by jcr
*/

int i;

// Função que calcula o factorial dum número n
function fact(n){
  int res = 1;
  while res > 1 {
    res = res * n;
    res = res - 1;
  }
}

// Programa principal
program myFact{
  for i in [1..10]{
    print(i, fact(i));
  }
}'''

data2 = '''/* max.p: calcula o maior inteiro duma lista desordenada
-- 2023-03-20 
-- by jcr
*/

int i = 10, a[10] = {1,2,3,4,5,6,7,8,9,10};

// Programa principal
program myMax{
  int max = a[0];
  for i in [1..9]{
    if max < a[i] {
      max = a[i];
    }
  }
  print(max);
}
'''

lexer = lex.lex()

print("\n\n»» data 1\n")

lexer.input(data1)

while token:=lexer.token():
    print(token)
    
print()

print("\n\n»» data 2\n")

lexer.input(data2)

while token:=lexer.token():
    print(token)

print()