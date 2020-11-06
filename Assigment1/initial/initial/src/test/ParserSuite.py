import unittest
from TestUtils import TestParser

class ParserSuite(unittest.TestCase):
    #program structure
    def test_empty_program(self):
        """test empty program"""
        input = """ """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,201))
    
    def test_simple_program(self):
        """simple program"""
        input = """Var: x;"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,202))

    def test_simple_program2(self):
        """simple program 2"""
        input = """Function: abc
                    Body:
                    EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,203))
    
    def test_simple_program3(self):
        """simple program 3"""
        input = """Var: x,y,z;
                Var: m,n,o;
                Function: a1
                Body:
                EndBody.
                Function: a2
                Body:
                EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,204))

    def test_wrong_variable_declaration_position(self):
        """test wrong variable declaration position"""
        input = """Var: x,y,z;
                Function: a1
                Body:
                EndBody.
                Var: m,n,o;
                Function: a2
                Body:
                EndBody."""
        expect = "Error on line 5 col 16: Var"
        self.assertTrue(TestParser.checkParser(input,expect,205))
    
    #global variable declaration part
    def test_global_variable_declaration(self):
        """test global variable declaration"""
        input = """Var: x,y,z;"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,206))

    def test_missing_colon_variable_declaration(self):
        """test missing colon variable declaration"""
        input = """Var x,y,z;"""
        expect = "Error on line 1 col 4: x"
        self.assertTrue(TestParser.checkParser(input,expect,207))

    def test_missing_semicolon_variable_declaration(self):
        """test missing semicolon variable declaration"""
        input = """Var: x,y,z"""
        expect = "Error on line 1 col 10: <EOF>"
        self.assertTrue(TestParser.checkParser(input,expect,208))

    def test_global_variable_declaration2(self):
        """test global variable declaration2"""
        input = """Var: x = 4;
                Var: x = 4, y, t=9;"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,209))

    def test_global_variable_declaration3(self):
        """test global variable declaration3"""
        input = """Var: x = 4, y, t= -9;"""
        expect = "Error on line 1 col 18: -"
        self.assertTrue(TestParser.checkParser(input,expect,210))

    def test_missing_init_value_variable_declaration(self):
        """test missing init value variable declaration"""
        input = """Var: x = 4, y =, t=9;"""
        expect = "Error on line 1 col 15: ,"
        self.assertTrue(TestParser.checkParser(input,expect,211))

    def test_composite_variable_declaration1(self):
        """test composite variable declaration1"""
        input = """Var: x[3] = {1,2,3};"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,212))

    def test_composite_variable_declaration2(self):
        """test composite variable declaration2"""
        input = """Var: x[3][5] = 4;
                Var: x[3][5][6][1] = True;"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,213))

    def test_composite_variable_declaration3(self):
        """test composite variable declaration3"""
        input = """Var: x[3][2] = {2, 3 + 4, 66}"""
        expect = "Error on line 1 col 21: +"
        self.assertTrue(TestParser.checkParser(input,expect,214))

    def test_composite_variable_declaration4(self):
        """test composite variable declaration4"""
        input = """Var: x[3][5][6][1] [6]   [9] [10     ] [    11];"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,215))

    def test_composite_variable_declaration_without_integer_literal(self):
        """test composite variable declaration without integer interal"""
        input = """Var: x[3 + 5] = 6;"""
        expect = "Error on line 1 col 9: +"
        self.assertTrue(TestParser.checkParser(input,expect,216))

    def test_composite_variable_declaration5(self):
        """test composite variable declaration5"""
        input = """Var: x[3][5][6][1] = 5;
                    Var: y[4][5] = 3, t = 7, z, w, q[3];
                    Var: q,w,e,r;"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,217))

    #function declaration part
    def test_function_declaration1(self):
        """test function declaration1"""
        input = """Function: ert
                    Parameter: i, x, a[4]
                    Body:
                        x = ert(i);
                    EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,218))
    
    def test_missing_body_function_declaration(self):
        """test missing body in function declaration"""
        input = """Function: ert
                    Parameter: i, x, a[4]"""
        expect = "Error on line 2 col 41: <EOF>"
        self.assertTrue(TestParser.checkParser(input,expect,219))

    def test_parameter_in_function_declaration(self):
        """test parameter in function declaration"""
        input = """Function: ert
                    Parameter: i, x = 7, a[4]
                    Body:
                        x = ert(i);
                    EndBody."""
        expect = "Error on line 2 col 36: ="
        self.assertTrue(TestParser.checkParser(input,expect,220))

    def test_parameter_in_function_declaration2(self):
        """test parameter in function declaration 2"""
        input = """Function: ert
                    Parameter:
                    Body:
                        x = ert(i);
                    EndBody."""
        expect = "Error on line 3 col 20: Body"
        self.assertTrue(TestParser.checkParser(input,expect,221))

    def test_name_in_function_declaration3(self):
        """test name in function declaration 3"""
        input = """Function: 123
                    Parameter: x,y,z
                    Body:
                        x = ert(i);
                    EndBody."""
        expect = "Error on line 1 col 10: 123"
        self.assertTrue(TestParser.checkParser(input,expect,222))

    def test_name_in_function_declaration4(self):
        """test name in function declaration 4"""
        input = """Function: 123
                    Parameter: x,y,z
                    Body:
                        x = ert(i);
                    EndBody."""
        expect = "Error on line 1 col 10: 123"
        self.assertTrue(TestParser.checkParser(input,expect,223))

    #array literal tests
    
    def test_array_literal1(self):
        """test array literal 1"""
        input = """Var: x = {{1,2}, {3,4}};"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,224))

    def test_array_literal2(self):
        """test array literal 2"""
        input = """Var: x = {{{1,  2 ,2e-124, "avc" , -1 }, {  4 , **erty**  5}  },  {{ 6  ,  7  },{ 8,9}}};"""
        expect = "Error on line 1 col 35: -"
        self.assertTrue(TestParser.checkParser(input,expect,225))

    def test_array_literal3(self):
        """test array literal 3"""
        input = """Var: x = {1, 1.5, True, {1,2,3,4}, "abcdef"};"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,226))

    def test_array_literal4(self):
        """test array literal 4"""
        input = """Var: x = {{1, 5.5}, {1, 9 ,{4}}};"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,227))

    def test_array_literal5(self):
        """test array literal 5"""
        input = """Var: x = {{1,2}, {3,4},
                    {4,5},
                    {7,6}
                    , **sldkjf**
                    {1,9}};"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,228))
    
    def test_array_literal6(self):
        """test array literal 6"""
        input = """Var: x = {{1,2}, {3,4} ,};"""
        expect = "Error on line 1 col 24: }"
        self.assertTrue(TestParser.checkParser(input,expect,229))

    def test_empty_array_literal(self):
        """test empty array literal"""
        input = """Var: x = {};"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,230))

    def test_empty_array_literal2(self):
        """test empty array literal 2"""
        input = """Var: x = {{}, {}, {{}, {}}};"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,231))

    #local variables

    def test_local_variable_declaration1(self):
        """test local variable declaration 1"""
        input = """Function: abc
                Parameter: x, y, z
                Body:
                    Var: x = 4, y, z = 8;
                    x = 1;
                    y = 7;
                EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,232))

    def test_local_variable_declaration2(self):
        """test local variable declaration 2"""
        input = """Function: abc
                Parameter: x, y, z
                Body:
                    Var: x = 4, y, z = 8;
                    Var: y = 1, x = 3, q;
                    x = 1;
                    y = 7;
                    z = 6;
                EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,233))

    def test_local_variable_declaration3(self):
        """test local variable declaration 3"""
        input = """Function: abc
                Parameter: x, y, z
                Body:
                    Var: x = 4, y, z = 8;
                    x = 1;
                    y = 7;
                    Var: y = 1, x = 3, q;
                    z = 6;
                EndBody."""
        expect = "Error on line 7 col 20: Var"
        self.assertTrue(TestParser.checkParser(input,expect,234))

    def test_local_variable_declaration4(self):
        """test local variable declaration 4"""
        input = """Function: abc
                Parameter: x, y, z
                Body:
                    Var: x = 4, y, z = 8;
                    z = 6;
                EndBody.
                Var: y = 1, x = 3, q;"""
        expect = "Error on line 7 col 16: Var"
        self.assertTrue(TestParser.checkParser(input,expect,235))

    #parameters
    def test_normal_parameter_declaration(self):
        """test normal parameter declaration"""
        input = """Function: abc
                Parameter: x, y[1][2], z[5]
                Body:
                    Var: x = 4, y, z = 8;
                    z = 6;
                EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,236))

    def test_comment_in_parameter_declaration(self):
        """test comment in parameter declaration"""
        input = """Function: abc
                Parameter: x, y[1][2],  **abce** z[5]
                Body:
                    Var: x = 4, y, z = 8;
                    z = 6;
                EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,237))

    def test_two_parameter_declaration(self):
        """test two parameter declaration"""
        input = """Function: abc
                Parameter: x, y[1][2], z[5]
                Parameter: a, c
                Body:
                    Var: x = 4, y, z = 8;
                    z = 6;
                EndBody."""
        expect = "Error on line 3 col 16: Parameter"
        self.assertTrue(TestParser.checkParser(input,expect,238))

    def test_missing_colon_parameter_declaration(self):
        """test missing colon in parameter declaration"""
        input = """Function: abc
                Parameter x, y[1][2], z[5]
                Body:
                    Var: x = 4, y, z = 8;
                    z = 6;
                EndBody."""
        expect = "Error on line 2 col 26: x"
        self.assertTrue(TestParser.checkParser(input,expect,239))

    ##expressions

    #binary operator
    def test_add_operator(self):
        """test add operator"""
        input = """Function: abc
                Body:
                    x = 5 + 6;
                EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,240))

    def test_association(self):
        """test association"""
        input = """Function: abc
                Body:
                    x = 5 + 6 + 7;
                    y = 5 +. 4 +. 1;
                    z = True && False || True;
                    w = 4 - 3 - 3;
                EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,241))

    def test_association2(self):
        input = """Function: abc
                Body:
                    x = 1 - 2 + 4 * 5 \\ 6;
                    y = 1.1 +. 3 -. 1.2 *. 8.0 \\. 9.23;
                EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,242))

    def test_non_association_operator(self):
        input = """Function: abc
                Body:
                    x = 1 != 2;
                    y = 1 != 2 < 3;
                EndBody."""
        expect = "Error on line 4 col 31: <"
        self.assertTrue(TestParser.checkParser(input,expect,243))

    def test_non_association_operator2(self):
        input = """Function: abc
                Body:
                    x = 1 != 2;
                    y = 1 == (2 < 3);
                EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,244))

    #index operator
    def test_index_operator1(self):
        input = """Function: abc
                Body:
                    x = {1,2,3,4} [5];
                EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,245))

    def test_index_operator2(self):
        input = """Function: abc
                Body:
                    x = {1,2,3,4} [5][7][9];
                EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,246))

    def test_index_operator3(self):
        input = """Function: abc
                Body:
                    x = 8[5][7][9];
                EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,247))

    def test_index_operator4(self):
        input = """Function: abc
                Body:
                    x = 2 + 8 + 4[5][7][9];
                EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,248))

    def test_index_operator5(self):
        input = """Function: abc
                Body:
                    x = abcdef[5][7][9];
                EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,249))

    def test_index_operator6(self):
        input = """Function: abc
                Body:
                    x = ((1 \\ 2 +. 4 - 4)[5][7])[9];
                EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,250))

    def test_index_operator7(self):
        input = """Function: abc
                Body:
                    x[3 + 4 + (5 * 8)] = 5 + 7;
                EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,251))

    def test_index_operator8(self):
        input = """Function: abc
                Body:
                    Var: x[3 + 2] = y[2 + 3];
                EndBody."""
        expect = "Error on line 3 col 29: +"
        self.assertTrue(TestParser.checkParser(input,expect,252))

    def test_index_operator9(self):
        input = """Function: abc
                Body:
                    x[3 + 2 + foo() + y[1 + 4 + 6]] = y[2 + 3];
                EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,253))

    def test_index_operator10(self):
        input = """Function: abc
                Body:
                    x[3 + 2 + foo() + [1 + 4 + 6]] = y[2 + 3];
                EndBody."""
        expect = "Error on line 3 col 38: ["
        self.assertTrue(TestParser.checkParser(input,expect,254))

    #unary operator
    def test_unary_operator1(self):
        input = """Function: abc
                Body:
                    x = -5 + -7;
                EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,255))

    def test_unary_operator2(self):
        input = """Function: abc
                Body:
                    x = -5 + -7 -!!!-----.- -8 - -9 - ---!-.--.-10;
                EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,256))

    def test_unary_operator3(self):
        input = """Function: abc
                Body:
                    x = -5 + -7 - -.7 + -.2 **skdljf** + -(-5 + 4) + -4[5] + (-4)[5];
                EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,257))

    def test_unary_operator4(self):
        input = """Function: abc
                Body:
                    x = True && !False || !!a && !!!bsdklf;
                    y = 5.5 -. -.3.3456 -. -.1.2345 +. -.12.e3 +. -.12.;
                EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,258))    

    def test_unary_operator5(self):
        input = """Function: abc
                Body:
                    x = -5 == -(s[4]) + -8;
                EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,259))

    #function calls
    def test_function_call1(self):
        input = """Function: abc
                Body:
                    x = foo() + goo() - too();
                EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,260))

    def test_nested_function_call(self):
        input = """Function: abc
                Body:
                    x = hoo(foo() + goo(too()) - too(goo() + foo() + qoo()));
                EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,261))

    def test_nested_function_call2(self):
        input = """Function: abc
                Body:
                    x = hoo(goo[1 + foo()], boo(1 * 4 == hoo({1,2,3}, {1}))) +. 5 -. 1;
                EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,262))

    def test_nested_function_call3(self):
        input = """Function: abc
                Body:
                    x = foo(1, {1, 2}) [1 + foo(4, 5 * too())] + yoo("abcdef foo()");
                EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,263))

    ##statements
    #if statement
    def test_if_statement(self):
        input = """Function: abc
                Parameter: x, y, z[4][5]
                Body:
                    If 1 + 3 == 5 Then
                        x = 6;
                        t = 7;
                    ElseIf 1 + 3 == 7 Then
                        y = 9;
                        z = 10;
                    Else z = 11;
                    EndIf.
                EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,264))

    def test_if_statement2(self):
        input = """Function: abc
                Parameter: x, y, z[4][5]
                Body:
                    If 1 + 3 == 5 Then
                        x = 6;
                        t = 7;
                    ElseIf 1 + 3 == 7 Then
                        y = 9;
                        z = 10;
                    Else z = 11;
                    Else z = 12;
                    EndIf.
                EndBody."""
        expect = "Error on line 11 col 20: Else"
        self.assertTrue(TestParser.checkParser(input,expect,265))

    def test_if_statement3(self):
        input = """Function: abc
                Parameter: x, y, z[4][5]
                Body:
                    If 1 + 3 == 5 Then
                        x = 6;
                        t = 7;
                    ElseIf 1 + 3 == 7 Then
                        y = 9;
                        z = 10;
                    ElseIf foo() > goo() Then
                        y = 9;
                        z = 10;
                    ElseIf 1 + 3 == 7 Then
                        y = 9;
                        z = 10;
                    Else z = 11;
                    EndIf.
                EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,266))

    def test_nested_if_statement(self):
        input = """Function: abc
                Parameter: x, y, z[4][5]
                Body:
                    If 1 + 3 == 5 Then
                        x = 6;
                        t = 7;
                    ElseIf 1 + 3 == 7 Then
                        If 2 + 5 == 6 Then
                        EndIf.
                    ElseIf foo() > goo() Then
                        y = 9;
                        z = 10;
                    Else z = 11;
                    EndIf.
                EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,267))

    def test_nested_if_statement2(self):
        input = """Function: abc
                Parameter: x, y, z[4][5]
                Body:
                    If a Then
                        If b Then
                        EndIf.
                        If c Then
                            If d Then
                            a = b;
                            EndIf.
                        EndIf.
                    EndIf.
                EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,268))

    def test_if_statement4(self):
        input = """Function: abc
                Parameter: x, y, z[4][5]
                Body:
                    If a Then a = 5;
                    Else a = 6;
                    ElseIf b == 5 Then c = 8;
                    EndIf.
                EndBody."""
        expect = "Error on line 6 col 20: ElseIf"
        self.assertTrue(TestParser.checkParser(input,expect,269))

    def test_if_statement5(self):
        input = """Function: abc
                Parameter: x, y, z[4][5]
                Body:
                    If a = 4 Then a = 5;
                    EndIf.
                EndBody."""
        expect = "Error on line 4 col 25: ="
        self.assertTrue(TestParser.checkParser(input,expect,270))

    #for statement
    def test_for_statement(self):
        input = """Function: abc
                Parameter: x, y, z[4][5]
                Body:
                    For (a = 4, a == 10, 1 + 2) Do
                        i = i + 1;
                    EndFor.
                EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,271))

    def test_for_statement_not_scalar_variable(self):
        input = """Function: abc
                Parameter: x, y, z[4][5]
                Body:
                    For (a[1] = 4, a[1] == 10, 1 + 2) Do
                        i = i + 1;
                    EndFor.
                EndBody."""
        expect = "Error on line 4 col 26: ["
        self.assertTrue(TestParser.checkParser(input,expect,272))

    def test_if_statement_in_for_statement(self):
        input = """Function: abc
                Parameter: x, y, z[4][5]
                Body:
                    For (a = 4, a == 10, 1 + 2) Do
                        If a == 4 Then a = 5;
                        EndIf.
                    EndFor.
                EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,273))

    def test_for_statement_wrong_expression(self):
        input = """Function: abc
                Parameter: x, y, z[4][5]
                Body:
                    For (a = 4, 10 + 20, a = a + 1) Do
                        a = 1;
                    EndFor.
                EndBody."""
        expect = "Error on line 4 col 43: ="
        self.assertTrue(TestParser.checkParser(input,expect,274))

    #while statement

    def test_while_statement(self):
        input = """Function: abc
                Parameter: x, y, z[4][5]
                Body:
                    While a != 1 Do
                        a = a + 1;
                        a = a + 2;
                    EndWhile.
                EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,275))

    def test_while_statement_empty_statement_list(self):
        input = """Function: abc
                Parameter: x, y, z[4][5]
                Body:
                    While a != 1 Do
                    EndWhile.
                EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,276))

    def test_while_statement_wrong_expression(self): # ????
        input = """Function: abc
                Parameter: x, y, z[4][5]
                Body:
                    a = 4;
                    While a = 5 Do
                    a = 6;
                    EndWhile.
                EndBody."""
        expect = "Error on line 5 col 28: ="
        self.assertTrue(TestParser.checkParser(input,expect,277))

    #Do while statement
    def test_do_while_statement(self):
        input = """Function: abc
                Parameter: x, y, z[4][5]
                Body:
                    Do
                        a = 1;
                        b = 2;
                        Break;
                        Continue;
                    While 2000 EndDo.
                EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,278))

    def test_do_while_statement2(self):
        input = """Function: abc
                Parameter: x, y, z[4][5]
                Body:
                    Do
                        23 + 24;
                    While 2000 EndDo.
                EndBody."""
        expect = "Error on line 5 col 27: +"
        self.assertTrue(TestParser.checkParser(input,expect,279))

    def test_do_while_statement3(self):
        input = """Function: abc
                Parameter: x, y, z[4][5]
                Body:
                    Do
                        q[2][3] = 10;
                        a[2 + foo(goo(a[10][11]))] = a != b;
                    While a = 4 EndDo.
                EndBody."""
        expect = "Error on line 7 col 28: ="
        self.assertTrue(TestParser.checkParser(input,expect,280))

    #nested variable declaration

    def test_nested_variable_declaration1(self):
        input = """Var : x, y, z = 5, t = {1,2,{3,4,5,{1,2,3}}};
                Var : y = 10., t = 6.e200;
                Function: abc
                Parameter: x, y, z[4][5]
                Body:
                    Var: x, y;
                    v = 2 + 3 + 4 \\. 5 +. 6.7e-1;
                    If (x + y + z) Then
                        Var: a, b, c;
                        Var: a[4], b[6], r[1];
                        a = 5.6;
                        b = 2[2][3];
                    ElseIf 2 + 3 Then
                        Var: r, t, r[5];
                        Var: q1, w2, e1;
                        q = 5 * 5 + 5;
                    Else a = 3;
                    EndIf.
                EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,281))

    def test_nested_variable_declaration2(self):
        input = """Var : x, y, z = 5, t = {1,2,{3,4,5,{1,2,3}}};
                Var : y = 10., t = 6.e200;
                Function: abc
                Parameter: x, y, z[4][5]
                Body:
                    Var: x, y;
                    v = 2 + 3 + 4 \\. 5 +. 6.7e-1;
                    If (x + y + z) Then
                        Var: a, b, c;
                        Var: a[4], b[6], r[1];
                        a = 5.6;
                        For (e = 1, 4, 6) Do
                            Var: d, e, f = 6789;
                            Var: e[4];
                            printf(i);
                            While
                                a + 4
                            Do
                                Var: x = 5, y, qqqq = 6;
                                Break;
                                Continue;
                                print(a);
                                Do
                                    Var: x, xx, xxx, xxxx;
                                    Break;
                                    Continue;
                                    print(abcdef);
                                While 2000
                                EndDo.
                            EndWhile.
                        EndFor.
                        b = 2[2][3];
                    ElseIf 2 + 3 Then
                        Var: r, t, r[5];
                        Var: q1, w2, e1;
                        q = 5 * 5 + 5;
                        writeln(fff);
                    Else a = 3;
                    EndIf.
                EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,282))

    def test_middle_variable_declaration(self):
        input = """Var : x, y, z = 5, t = {1,2,{3,4,5,{1,2,3}}};
                Var : y = 10., t = 6.e200;
                Function: abc
                Parameter: x, y, z[4][5]
                Body:
                    Var: x, y;
                    v = 2 + 3 + 4 \\. 5 +. 6.7e-1;
                    If (x + y + z) Then
                        Var: a, b, c;
                        Var: a[4], b[6], r[1];
                        a = 5.6;
                        For (e = 1, 4, 6) Do
                            Var: d, e, f = 6789;
                            Var: e[4];
                            printf(i);
                            While
                                a + 4
                            Do
                                Break;
                                Var: x = 5, y, qqqq = 6;
                                Continue;
                                print(a);
                                Do
                                    Var: x, xx, xxx, xxxx;
                                    Break;
                                    Continue;
                                    print(abcdef);
                                While 2000
                                EndDo.
                            EndWhile.
                        EndFor.
                        b = 2[2][3];
                    ElseIf 2 + 3 Then
                        Var: r, t, r[5];
                        Var: q1, w2, e1;
                        q = 5 * 5 + 5;
                        writeln(fff);
                    Else a = 3;
                    EndIf.
                EndBody."""
        expect = "Error on line 20 col 32: Var"
        self.assertTrue(TestParser.checkParser(input,expect,283))

    def test_nested_function_declaration1(self):
        input="""Var:x,y,z;
            Function: abc
            Parameter: a, x, z
            Body:
                Function: ert
                Body:
                EndBody.
            EndBody."""
        expect = "Error on line 5 col 16: Function"
        self.assertTrue(TestParser.checkParser(input,expect,284))

    def test_return_statement(self):
        input="""Var: x, y, z;
            Function: abc
            Parameter: a, x, z[5]
            Body:
                Return ;
                Return 3;
            EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,285))

    def test_return_statement2(self):
        input="""Var: x, y, z;
            Function: abc
            Parameter: a, x, z[5]
            Body:
                Return;
                Return Return 5;
            EndBody."""
        expect = "Error on line 6 col 23: Return"
        self.assertTrue(TestParser.checkParser(input,expect,286))

    def test_no_whitespace_program(self):
        input = """Function:abc Parameter:x,y,z[4][5]Body:If1+3==5Thenx=6;t=7;ElseIf1+3==7ThenIf2+5==6Then
                    EndIf.ElseIffoo()>goo()Theny=9;z=10;Elsez=11;EndIf.EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,287))

    def test_random(self):
        input = """Function: main
                Body:
                    a = !--.1;
                    a = 3----------------1;
                EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,288))

    def test_random2(self):
        input = """Var : x, y, z = 5, t = {1,2,{3,4,5,{1,2,3}}};
                Var : y = 10., t = 6.e200, q[1][2] = {2,3,4,5};
                Function: abc
                Parameter: x, y, z[4][5]
                Body:
                    Var: x, y;
                    Continue;
                    Break;Break;Continue;Return;Return 44444;
                    If 4 Then If 5 Then If 6 Then EndIf.EndIf.EndIf.
                EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,289))

    def test_random3(self):
        input = """Function: abc
                Parameter: x, y, z[4][5]
                Body:
                    a = 4 ! 5;
                EndBody."""
        expect = "Error on line 4 col 26: !"
        self.assertTrue(TestParser.checkParser(input,expect,290))

    def test_nested_statements(self):
        input = """Function: abc
                Body:
                If 4 Then While 4 Do EndWhile.
                For (q = 1, 2, 3) Do Do While 5 EndDo.
                EndFor.
                ElseIf 5 Then 
                    If 1 Then
                    ElseIf 2 Then While 1 Do EndWhile.
                        For (q = 1, 2, 3) Do  Do While 1 Do EndWhile. While 5 EndDo.
                            EndFor.
                        If 3 Then
                        Else
                            For (q = 1, 2, 3) Do
                            Do While 5 EndDo.
                            While 4 Do  Do While 1 Do EndWhile. While 5 EndDo. EndWhile.
                            EndFor.
                        EndIf.
                    ElseIf -4 Then
                    EndIf.
                    While 4 Do  Do While 5 EndDo. EndWhile.
                ElseIf 6 Then
                While 4 Do  Do While 5 EndDo. EndWhile.
                For (q = 1, 2, 3) Do
                EndFor.
                ElseIf 7 Then While 1 Do EndWhile.
                While 4 Do Do While 5 EndDo. EndWhile.
                For (q = 1, 2, 3) Do
                EndFor.
                ElseIf 8 Then While 4 Do While 1 Do EndWhile. Do While 5 EndDo. EndWhile.
                EndIf.
                EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,291))

    def test_nested_statements2(self):
        input = """Function: abc
                Body:
                If 4 Then While 4 Do EndWhile.
                For (q = 1, 2, 3) Do Do While 5 EndDo.
                EndFor.
                ElseIf 5 Then 
                    If 1 Then
                    ElseIf 2 Then While 1 Do EndWhile.
                        For (q = 1, 2, 3) Do  Do While 1 Do EndWhile. While 5 EndDo.
                            EndFor.
                        If 3 Then
                        Else
                            For (q = 1, 2, 3) Do
                            Do While 5 EndDo.
                            While 4 Do  Do While 1 Do EndWhile. While 5 EndDo. EndWhile.
                            EndFor.
                        EndIf.
                    ElseIf -4 Then
                    EndIf.
                    While 4 Do Do Do While 5 EndDo. EndWhile.
                ElseIf 6 Then
                While 4 Do  Do While 5 EndDo. EndWhile.
                For (q = 1, 2, 3) Do
                EndFor.
                ElseIf 7 Then While 1 Do EndWhile.
                While 4 Do Do While 5 EndDo. EndWhile.
                For (q = 1, 2, 3) Do
                EndFor.
                ElseIf 8 Then While 4 Do While 1 Do EndWhile. Do While 5 EndDo. EndWhile.
                EndIf.
                EndBody."""
        expect = "Error on line 20 col 52: EndWhile"
        self.assertTrue(TestParser.checkParser(input,expect,292))

    def test_statement_outside_function(self):
        input = """Var: x, y, z;
                Break;
                Continue;
                Return;"""
        expect = "Error on line 2 col 16: Break"
        self.assertTrue(TestParser.checkParser(input,expect,293))

    def test_assignable_expression(self):
        input = """Function: abc
                Body:
                5[5[5]] = 4;
                EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,294))

    def test_assignable_expression2(self):
        input = """Function: abc
                Body:
                (5 + 5 - 4)[(5+ 5)[5 - 4]] = (4 + 4 * 4)[4][3];
                EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,295))

    def test_assignable_expression3(self):
        input = """Function: abc
                Body:
                fun(fun(5)) = (4 + 4 * 4)[4][3];
                EndBody."""
        expect = "Error on line 3 col 28: ="
        self.assertTrue(TestParser.checkParser(input,expect,296))

    def test_nested_statements3(self):
        input = """Function:abc
                Body:
                DoDoDoDoDoDoDoDoDoDoWhile------------1EndDo.Whilefun(4,5,5,6,{1,2,3,4,6},6)EndDo.While3.4EndDo.While4444EndDo.While"abcdefjlksdj"EndDo.While6EndDo.While7EndDo.While8EndDo.While9EndDo.While000222e-11111EndDo.
                EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,297))
    
    def test_nested_statement4(self):
        input = """Function:abc
                Body:
                While1DoDoe=5;While2EndDo.EndWhile..
                EndBody."""
        expect = "Error on line 3 col 51: ."
        self.assertTrue(TestParser.checkParser(input,expect,298))

    def test_index_operator11(self):
        input = """Function:abc
                Body:
                aaaa[112234[1123][123]][2 + 3 + 1][!!!!!-fun()][thisisfun()][nahthisisnotfun(fun,fee,ee,thisisnotthelasttestcaseSS)] = q;
                EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,299))

    def test_assign_statement(self):
        input = """Function:abc
                Body:
                Var: a = fun();
                EndBody."""
        expect = "Error on line 3 col 25: fun"
        self.assertTrue(TestParser.checkParser(input,expect,300))