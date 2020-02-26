/*
   **************************************
   * Student name: Dang Van Dung        *
   * Student ID: 1710853                *
   **************************************
*/

grammar MC;

@lexer::header {
from lexererr import *
}


@lexer::members {
def emit(self):
    tk = self.type
    if tk == self.UNCLOSE_STRING:
        result = super().emit();
        raise UncloseString(result.text);
    elif tk == self.ILLEGAL_ESCAPE:
        result = super().emit();
        raise IllegalEscape(result.text);
    elif tk == self.ERROR_CHAR:
        result = super().emit();
        raise ErrorToken(result.text);
    else:
        return super().emit();
}

options{
	language=Python3;
}


program: decls+ EOF;
decls: vardecl | fundecl;
vardecl: primitype lstvar SM; 
lstvar: var (CM var)*;
primitype: (BOOLEAN|INT|FLOAT|STRING);
var: ID | arrayvar;
arrayvar: ID LSB INTLIT RSB;
fundecl: typefun ID LB (paradecl (CM paradecl)*)? RB block_statement;
typefun: (primitype|VOID|out_array_pointer_type);
out_array_pointer_type: primitype LSB RSB;
in_array_pointer_type: primitype ID LSB RSB;
paradecl: primitype ID | in_array_pointer_type;
block_statement: LP var_stm* RP;
var_stm: vardecl|statement;
if_statement: IF LB exp RB statement (ELSE statement)?;
do_while_statement: DO statement+ WHILE exp SM;
for_statement: FOR LB exp SM exp SM exp RB statement;
break_statement: BREAK SM;
continue_statement: CONTINUE SM;
return_statement: RETURN (exp|) SM;
exp_statement: exp SM;
statement: if_statement
        |   do_while_statement
        |   for_statement
        |   break_statement
        |   continue_statement
        |   return_statement
        |   block_statement
        |   exp_statement;



INT: 'int' ;
FLOAT: 'float';
VOID: 'void' ;
BOOLEAN: 'boolean';
STRING: 'string';
BREAK: 'break';
CONTINUE: 'continue';
ELSE: 'else';
FOR: 'for';
IF: 'if';
RETURN: 'return';
DO: 'do';
WHILE: 'while';


exp: exp1 ASSIGN exp
    | exp1;
exp1: exp1 OR exp2
    | exp2 ;
exp2: exp2 AND exp3
    | exp3;
exp3: exp4 (EQ|NOTEQ) exp4
    | exp4;
exp4: exp5 (LESS|LESSEQ|GREA|GREAEQ) exp5
    | exp5;
exp5: exp5 (ADD|SUB) exp6
    | exp6;
exp6: exp6 (DIV|MUL|MOD) exp7
    | exp7;
exp7: (SUB|NOT) exp7 | exp8;
exp8: exp9 LSB exp RSB | exp9;
exp9: LB exp RB | operand;
operand: literal | ID | funcall;//indexexp;

literal: INTLIT|FLOATLIT|BOOLLIT|STRINGLIT;
//indexexp: funcall (LSB exp RSB)?;
funcall: ID LB (exp (CM exp)*)? RB;
ADD: '+';
MUL: '*';
NOT:'!';
OR: '||';
NOTEQ: '!=';
LESS: '<';
LESSEQ: '<=';
ASSIGN: '=';
SUB:'-';
DIV:'/';
MOD:'%';
AND:'&&';
EQ: '==';
GREA: '>';
GREAEQ: '>=';

INTLIT: [0-9]+;
FLOATLIT: DIGIT* Dot? DIGIT+ Exponent? | DIGIT+ Dot? (DIGIT* Exponent?)? ;
fragment Exponent: ('e'|'E') ('-')? DIGIT+;
fragment Dot: '.';
fragment DIGIT: [0-9];
BOOLLIT: TRUE | FALSE;
TRUE: 'true';
FALSE: 'false';
COMMENT: ( '/*'.*?'*/' | '//' (~('\n' | '\r'))* ) -> skip ;
LB: '(' ;
RB: ')' ;
LP: '{';
RP: '}';
LSB: '[';
RSB:']';
SM: ';' ;
CM: ',';
WS : [ \t\r\n]+ -> skip ; // skip spaces, tabs, newlines
ID: [a-zA-Z_][a-zA-Z0-9_]*;
STRINGLIT: '"'  ('\\' [bfrnt"\\] | ~["\\\r\n])*  '"'
{
   self.text=self.text[1:-1]
};
ILLEGAL_ESCAPE:  '"' ('\\' [bfrnt\\] | ~[\\"\r] )*   ('\\' ~[bfrnt"\\])
{
    raise IllegalEscape(self.text[1:])
};
UNCLOSE_STRING: '"'  ('\\' [bfrnt"\\] | ~["\\\r\n])* ('\\')?
{
   raise UncloseString(self.text[1:])
};
ERROR_CHAR: .
{
    raise ErrorToken(self.text);
};
