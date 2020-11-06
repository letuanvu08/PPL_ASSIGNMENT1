grammar BKIT;

@lexer::header {
from lexererr import *
}

@lexer::members {
def emit(self):
    tk = self.type
    result = super().emit()
    if tk == self.UNCLOSE_STRING:
        raise UncloseString(result.text)
    elif tk == self.ILLEGAL_ESCAPE:

        for i in range(0,len(result.text)):
            if result.text[i] in "\n\r\"":
                result.text=result.text[0:i+1]
                break
            if result.text[i]=='\\':
                if i<(len(result.text)-1) and result.text[i+1]!='"':
                    if result.text[i+1] not in "tnbfr":
                        result.text=result.text[0:i+2]
                        break
                else:
                    result.text=result.text[0:i+1]
                    break
            if result.text[i]=='\'':
                if i<(len(result.text)-1):
                    if result.text[i+1] != '"':
                        result.text=result.text[0:i+2]
                        break
                else:
                    result.text=result.text[0:i+1]
                    break
        raise IllegalEscape(result.text)
    elif tk == self.ERROR_CHAR:
        raise ErrorToken(result.text)
    elif tk == self.UNTERMINATED_COMMENT:
        raise UnterminatedComment()
    else:
        return result;

}

options{
	language=Python3;
}

program  :. EOF;
exp             :expint;
expint
                :   expint1 (RL)  expint1
                |expint1;
expint1         :   expint1 (BOOL_OP) expint2
                |   expint2;
expint2         :expint2(AO1|SINGN)expint3
                |expint3;
expint3         :expint3(AO2)expint4
                |expint4;
expint4         :NOT expint4
                |expint5;
expint5         :SINGN expint5
                |atomint;
atomint
                :call
                |index
                |LP exp RP
                |   ID
                |array
                |STRING
                |BOOL
                |FLOAT
                |   INT;

call    : ID LP listexp? RP;
listexp :(exp|STRING)
        |(exp|STRING)(COMMA listexp);
index   : (INT|ID|FLOAT|STRING|call|LP exp RP)indexele ;
indexele: (LBR exp? RBR)+;


var     :VAR COLON listid SEMI;
listid  :(ID|ID index_var|assign_var)(COMMA listid)
        |ID|ID index_var|assign_var;
index_var   : indexele_var ;
indexele_var: (LBR INT RBR)+;
assign_var: (ID|ID index_var)ASSIGN (INT|FLOAT|array|STRING|BOOL);
assign      : (ID|index) ASSIGN (exp|STRING|array);
retur      :RETURN exp? SEMI;
contin    :CONTINUE SEMI;
br       :BREAK SEMI;

st       : assign SEMI|call SEMI|retur|contin|br|forst|ifst|whilest|dowhilest;

ifst          : IF  exp  THEN (var*st*) (ELSEIF exp THEN (var*st*))* (ELSE (var*st*))? ENDIF DOT;
whilest: WHILE exp DO (var*st*) ENDWHILE DOT;
dowhilest: DO (var*st*) WHILE exp ENDDO DOT;
forst: FOR LP ID ASSIGN exp COMMA exp COMMA exp RP DO (var*st*) ENDFOR DOT;

parameter       :PARAMETER COLON listpar;
listpar         :(ID|index)(COMMA listpar)
                |(ID|index);
array:  LB (array1 array2) RB
      |LB RB;
array1: LB array1 RB array2
       |(FLOAT|INT|BOOL|STRING|ID)array2
       |LB RB array2;
array2:','array1
      |;

//array1: LB RB
//       |LB array1 RB
//       |INT COMMA array1
//       |LB RB;
function        : FUNCTION_ COLON ID parameter? BODY_ COLON (var*st*) ENDBODY_ DOT;

//int_of_float:;
//float_of_int:;
//int_of_string:;
//float_of_string:;
//string_of_int:;
//string_of_float:;
//bool_of_string:;
//string_of_bool:;











WS : [ \t\r\n]+ -> skip ; // skip spaces, tabs, newlines
/*  3.2 PROGRAM COMMENT */
SINGN:SUB|SUBF;
AO1:ADD|ADDF;
AO2:MULTIF|DIVF|MULTI|DIV|MOD;
BOOL_OP:         AND|OR|AND|OR;
RL        :EQUALF| LESS_F|LESSEF|GREATER_F|GREATEREF|EQUAL| LESS|LESS_E|GREATER_E|GREATER|NOT_E;
BOOL: TRUE|FALSE;
/*  3.3 KEY WORDS    */
BODY_                :   'Body';
BREAK               :   'Break';
CONTINUE            :   'Continue';
DO                  :   'Do';
ELSE                :   'Else';
ELSEIF              :   'ElseIf';
ENDBODY_             :   'EndBody';
ENDIF               :   'EndIf';
ENDFOR              :   'EndFor';
ENDWHILE            :   'EndWhile';
FOR                 :   'For';
FUNCTION_            :   'Function';
IF                  :   'If';
PARAMETER           :   'Parameter';
RETURN              :   'Return';
THEN                :   'Then';
VAR                 :   'Var';
WHILE               :   'While';
TRUE                :   'True';
FALSE               :   'False';
ENDDO               :   'EndDo';

/*  3.3 OPERATER */
// INTEGER TYPE
ASSIGN              :   '=';
ADD                 :   '+';
SUB                 :   '-';
MULTI               :   '*';
DIV                 :   '\\';
MOD                 :   '%';
EQUAL               :   '==';
NOT_E           :   '!=';
GREATER             :   '>';
LESS                :   '<';
GREATER_E     :   '>=';
LESS_E         :   '<=';

// FLOAT TYPE
ADDF           :   '+.';
SUBF           :   '-.';
MULTIF         :   '*.';
DIVF           :   '\\.';
EQUALF         :   '=/=';
GREATER_F       :   '>.';
LESS_F          :   '<.';
GREATEREF :   '>=.';
LESSEF    :   '<=.';

//BOOLEAN TYPE
NOT                 :   '!';
AND                 :   '&&';
OR                  :   '||';

/*  SEPARATORS */
LP      :'(';
RP      :')';
LB          :'{';
RB            :'}';
LBR          :'[';
RBR          :']';
DOT                 :'.';
COLON               : ':' ;
SEMI                : ';' ;
COMMA               : ',';


/*  LITERALS */
ID                  :   [a-z][a-zA-Z0-9]*;
INT                 : '0' | [1-9][0-9]* | '0'[Xx][1-9A-F][0-9A-F]* | '0'[Oo][1-7][0-7]*;

FLOAT               : [0-9]+
                    ((DOT[0-9]* ([Ee][+-]?(([0-9][0-9]*)))? )
                    |(DOT?[Ee][+-]?(([0-9][0-9]*) ) ));
fragment STRING_CONDITION
    :   (
            ~('\''|'\\'|'\n'|'\r'|'"') | '\\' ('\\'|'t'|'n'|'b'|'f'|'r'|'\'') | '\'"')*
    ;
COMMENT             :'**' .*? '**'(COMMENT* [\t\r\n]*)? -> skip;
STRING
        :   '"'
        STRING_CONDITION
        '"'
        {self.text=self.text[1:len(self.text)-1]}
        ;
//STRING: '""'  .*?  '""';
//fragment  ARRAY_INT: ('{' (WS* INT WS* (','WS*INT WS*)*| (WS*ARRAY_INT WS*(','WS*ARRAY_INT WS*)*)) '}');
//fragment ARRAY_FLOAT_INT:('{' (WS* (FLOAT|INT|BOOL|STRING|ID) WS* (','WS*(ID|FLOAT|INT|BOOL|STRING) WS*)*| (WS*ARRAY_FLOAT_INT WS*(','WS*ARRAY_FLOAT_INT WS*)*)) '}');
//ARRAY         :  ARRAY_FLOAT_INT;
ERROR_CHAR: .;
UNCLOSE_STRING: '"' STRING_CONDITION {self.text=self.text[1:len(self.text)]};
//ILLEGAL_ESCAPE: '"'STRING_CONDITION ('\''~('"')|('\''|'\n'|'\r'|'\\')|'\\'~('\\'|'t'|'n'|'b'|'f'|'r'|'\'')) '"'? {self.text=self.text[1:len(self.text)]};
ILLEGAL_ESCAPE:  '"' ( ~["\n\r]  |  (~[\\]  '\\'  ~[\n\r]))* '"'{self.text=self.text[1:len(self.text)]};
UNTERMINATED_COMMENT: '**' .*?;
expb: expb '?' expb1
    |expb1;
expb1:expb2  '^'expb2
    |expb2;
expb2:expb3 '@' expb2
     |expb3;
expb3:INT|'(' expb ')';