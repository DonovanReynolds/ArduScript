grammar ArduScript;

start:  (NEWLINE | block | s | function)*  # EveryLine
;

function: 'function' ID '(' (ID (',' ID)*)? ')' block;

block: BEGIN start END #Compound
;
s:   ID '=' (a|b) # Assignment
   | 'skip' # Skip
   | 'if' b block (ELSE block)? # If
   | 'while' b block # While
   | 'loop' a block #For
   | 'setPin' a ',' b #SetPin
   | 'togglePin' a #TogglePin
   | 'wait' a #Wait
   | 'print(' (STRING | a)')' #Print 
   | ID '(' (ID (',' ID)*)? ')' #CallFunction
   | 'GLOBAL' ID '=' a #Global
   | 'pin' ID '=' a #Pin
   ;

b:   'true' # True
   | 'false' # False
   | 'not' b # Not
   | b 'and' b # And
   | b 'or' b # Or
   | a op=('<' | '<=' | '==' | '>' | '>=') (a|b) # ROp
   | '(' b ')' # BParen
   | 'high' #High
   | 'low' #Low
   ;

a:   ID # Var
   | NUM # Num
   | a op=('+' | '-' | '*' | '/' | '%' ) a # AOp
   | '(' a ')' # AParen
   | 'readPin' a #ReadPin
   ;

BEGIN: 'begin' ;
END: 'end' ;
COLON: ':';

ELSE: 'else';

TRUE: 'true' ;
FALSE: 'false' ;
AND: 'and' ;
OR: 'or' ;
NOT: 'not' ;

ID: [a-zA-Z] ([a-zA-Z] | [0-9])* ;
NUM: [0-9]+ ;

EQ: '=' ;
LT: '<' ;
LE: '<=' ;
GT: '>' ;
GE: '>=' ;

PLUS: '+' ;
MINUS: '-' ;
MULT: '*' ;
DIV: '/' ;

WS:   [ \t\n\r]+ -> skip ;
SL_COMMENT:   '//' .*? '\n' -> skip ;
NEWLINE: '\r'? '\n';
TAB: '\t';

StringLiteral: ~[\\\r\n'];

FOR: 'for';
STRING: ["] StringLiteral StringLiteral* ["];
