import unittest
from TestUtils import TestLexer

class LexerSuite(unittest.TestCase):
    # Comment tests
    def test_normal_comment(self):
        """test normal comment"""
        self.assertTrue(TestLexer.checkLexeme("** abcdef **","<EOF>",101))

    def test_unterminated_comment(self):
        """test unterminated comment"""
        self.assertTrue(TestLexer.checkLexeme("** abcdef","Unterminated Comment", 102))

    def test_empty_comment(self):
        """test empty comment"""
        self.assertTrue(TestLexer.checkLexeme("**** ** ** ****** **** **","<EOF>",103))

    def test_special_char_in_comment(self):
        """test special char in comment"""
        self.assertTrue(TestLexer.checkLexeme("** * \t \\ \\ *e ~1!3    \b\r \n ' \" \f \\f \\r **", "<EOF>", 104))

    def test_multi_line_comment(self):
        """test multi-line comment"""
        self.assertTrue(TestLexer.checkLexeme(
            "** abcdef \
            ghilkm \
            *ewkljrwe \
            jlkewr \
            rwerjl**",
            "<EOF>", 105))

    # Identifier tests
    def test_normal_identifier(self):
        """test normal identifier"""
        self.assertTrue(TestLexer.checkLexeme("aTelkj_03479AA", "aTelkj_03479AA,<EOF>",106))

    def test_single_character_identifier(self):
        """test single character identifier"""
        self.assertTrue(TestLexer.checkLexeme("a", "a,<EOF>", 107))

    def test_uppercase_first_identifier(self):
        """test uppercase first identifier"""
        self.assertTrue(TestLexer.checkLexeme("Asa", "Error Token A",108))

    def test_number_first_identifier(self): #Not sure
        """test number first identifier"""
        self.assertTrue(TestLexer.checkLexeme("5alskdjfEE", "5,alskdjfEE,<EOF>", 109))

    def test_number_first_identifier2(self): #Not sure
        """test number first identifier2"""
        self.assertTrue(TestLexer.checkLexeme("5ElskdjfEE", "5,Error Token E", 110))

    # Keywords and operators
    def test_keyword_and_operator1(self):
        """test keyword and operator1"""
        self.assertTrue(TestLexer.checkLexeme("Break", "Break,<EOF>", 111))

    def test_keyword_and_operator2(self): #Not sure
        """test keyword and operator2"""
        self.assertTrue(TestLexer.checkLexeme("EndDoElseIf", "EndDo,ElseIf,<EOF>", 112))

    def test_keyword_and_operator3(self):
        """test keyword and operator3"""
        self.assertTrue(TestLexer.checkLexeme("+.", "+.,<EOF>", 113))

    def test_keyword_and_operator4(self): #Not sure
        """test keyword and operator4"""
        self.assertTrue(TestLexer.checkLexeme("+.EndDo", "+.,EndDo,<EOF>", 114))

    def test_keyword_and_operator5(self):
        """test keyword and operator5"""
        self.assertTrue(TestLexer.checkLexeme("EndD", "Error Token E", 115))

    # Seperators
    def test_seperator(self):
        """test seperator"""
        self.assertTrue(TestLexer.checkLexeme("[()]}[{;:,.", "[,(,),],},[,{,;,:,,,.,<EOF>", 116))
    
    # Integer literals
    def test_normal_integer1(self):
        """test_normal_integer1"""
        self.assertTrue(TestLexer.checkLexeme("0",'0,<EOF>',117))
    
    def test_normal_integer2(self):
        """test_normal_integer2"""
        self.assertTrue(TestLexer.checkLexeme("4",'4,<EOF>',118))

    def test_normal_integer3(self):
        """test_normal_integer3"""
        self.assertTrue(TestLexer.checkLexeme("17",'17,<EOF>',119))

    def test_0_first_integer(self): #Not sure
        """test 0 first integer"""
        self.assertTrue(TestLexer.checkLexeme("0123",'0,123,<EOF>',120 ))
    
    def test_normal_hexa1(self):
        """test normal hexa1"""
        self.assertTrue(TestLexer.checkLexeme("0xABC","0xABC,<EOF>",121))

    def test_normal_hexa2(self):
        """test normal hexa2"""
        self.assertTrue(TestLexer.checkLexeme("0x102304560789ABCDEF","0x102304560789ABCDEF,<EOF>",122))

    def test_0_first_hexa(self): #Not sure
        """test 0 first hexa"""
        self.assertTrue(TestLexer.checkLexeme("0x0","0,x0,<EOF>",123))

    def test_0_first_hexa2(self): #Not sure
        """test 0 first hexa2"""
        self.assertTrue(TestLexer.checkLexeme("0x012AA","0,x012AA,<EOF>",124))

    def test_normal_hexa3(self):
        """test normal hexa3"""
        self.assertTrue(TestLexer.checkLexeme("0XAAAAA","0XAAAAA,<EOF>",125))
    
    def test_middle_x_hexa1(self):
        """test middle x hexa 1"""
        self.assertTrue(TestLexer.checkLexeme("0X12000xAA","0X12000,xAA,<EOF>",126))

    def test_normal_octal1(self):
        """test normal octal 1"""
        self.assertTrue(TestLexer.checkLexeme("0o12345067", "0o12345067,<EOF>", 127))

    def test_normal_octal2(self):
        """test normal octal 2"""
        self.assertTrue(TestLexer.checkLexeme("0O764051", "0O764051,<EOF>", 128))

    def test_normal_octal3(self):
        """test normal octal 3"""
        self.assertTrue(TestLexer.checkLexeme("0O1", "0O1,<EOF>", 129))

    def test_0_first_octal(self):
        """test 0 first octal"""
        self.assertTrue(TestLexer.checkLexeme("0O01", "0,Error Token O", 130))

    def test_double_O_octal(self):
        """test double O octal"""
        self.assertTrue(TestLexer.checkLexeme("0OO1", "0,Error Token O", 131))

    def test_middle_o_octal(self):
        """test middle o octal"""
        self.assertTrue(TestLexer.checkLexeme("0o2370o33","0o2370,o33,<EOF>",132))

    # Boolean literals
    def test_boolean_literal(self):
        """test boolean literal"""
        self.assertTrue(TestLexer.checkLexeme("True False", "True,False,<EOF>",133))

    # Float literals
    def test_normal_float1(self):
        """test normal float 1"""
        self.assertTrue(TestLexer.checkLexeme("0.0e0", "0.0e0,<EOF>",134))

    def test_normal_float2(self):
        """test normal float 2"""
        self.assertTrue(TestLexer.checkLexeme("53234.89230E21983", "53234.89230E21983,<EOF>",135))

    def test_missing_decimal_float1(self):
        """test missing_decimal_float1"""
        self.assertTrue(TestLexer.checkLexeme("53234E+21983", "53234E+21983,<EOF>",136))

    def test_missing_decimal_float2(self):
        """test missing_decimal_float2"""
        self.assertTrue(TestLexer.checkLexeme("864E-0", "864E-0,<EOF>",137))

    def test_missing_exponent_float1(self):
        """test missing exponent float 1"""
        self.assertTrue(TestLexer.checkLexeme("0.34","0.34,<EOF>",138))

    def test_missing_exponent_float2(self):
        """test missing exponent float 2"""
        self.assertTrue(TestLexer.checkLexeme("32.46","32.46,<EOF>",139))

    def test_zeros_float(self):
        """test zeros float"""
        self.assertTrue(TestLexer.checkLexeme("000.000e-000", "000.000e-000,<EOF>",140))

    def test_omitted_float1(self):
        """test omitted float 1"""
        self.assertTrue(TestLexer.checkLexeme("1.", "1.,<EOF>",141))

    def test_omitted_float2(self):
        """test omitted float 2"""
        self.assertTrue(TestLexer.checkLexeme("2.e13454", "2.e13454,<EOF>",142))

    def test_omitted_float3(self):
        """test omitted float 3"""
        self.assertTrue(TestLexer.checkLexeme("0042.E999", "0042.E999,<EOF>",143))

    def test_abnormal_float2(self):
        """test abnormal float 2"""
        self.assertTrue(TestLexer.checkLexeme("1e", "1,e,<EOF>",144))

    def test_abnormal_float3(self):
        """test abnormal float 3"""
        self.assertTrue(TestLexer.checkLexeme("1E", "1,Error Token E",145))

    def test_abnormal_float4(self):
        """test abnormal float 4"""
        self.assertTrue(TestLexer.checkLexeme("E13", "Error Token E",146))

    def test_abnormal_float5(self):
        """test abnormal float 5"""
        self.assertTrue(TestLexer.checkLexeme("e013", "e013,<EOF>",147))

    def test_abnormal_float6(self):
        """test abnormal float 6"""
        self.assertTrue(TestLexer.checkLexeme(".013", ".,0,13,<EOF>",148))

    def test_abnormal_float8(self):
        """test abnormal float 8"""
        self.assertTrue(TestLexer.checkLexeme("0042.E", "0042.,Error Token E",149))

    def test_abnormal_float10(self):
        """test abnormal float 10"""
        self.assertTrue(TestLexer.checkLexeme("0e", "0,e,<EOF>",150))

    def test_normal_float3(self):
        """test normal float 3"""
        self.assertTrue(TestLexer.checkLexeme("0012.1200", "0012.1200,<EOF>", 151))

    def test_normal_float4(self):
        """test normal float 4"""
        self.assertTrue(TestLexer.checkLexeme("1200.0012", "1200.0012,<EOF>", 152))

    def test_normal_float5(self):
        """test normal float 5"""
        self.assertTrue(TestLexer.checkLexeme("0001.0001e0001", "0001.0001e0001,<EOF>", 153))

    def test_normal_float6(self):
        """test normal float 6"""
        self.assertTrue(TestLexer.checkLexeme("1000.1000e-1000", "1000.1000e-1000,<EOF>", 154))
    
    def test_normal_float7(self):
        """test normal float 7"""
        self.assertTrue(TestLexer.checkLexeme("000.1000E+1000", "000.1000E+1000,<EOF>", 155))
    
    # String literals

    def test_normal_string(self):
        """test normal string"""
        self.assertTrue(TestLexer.checkLexeme(""" "sfdje3343ljvcxslkk" ""","sfdje3343ljvcxslkk,<EOF>",156))

    def test_unterminated_string(self):
        """test unclosed string"""
        self.assertTrue(TestLexer.checkLexeme(""" "abc def  ""","""Unclosed String: abc def  """,157))

    def test_unterminated_string2(self):
        """test unclosed string2"""
        self.assertTrue(TestLexer.checkLexeme(""" "abc def\n" ""","""Unclosed String: abc def""",158))


    def test_illegal_escape1(self):
        """test illegal escape1"""
        self.assertTrue(TestLexer.checkLexeme(""" "abc\\h def"  ""","""Illegal Escape In String: abc\\h""",159))

    def test_illegal_escape2(self):
        """test illegal escape2"""
        self.assertTrue(TestLexer.checkLexeme(""" "abcdef\\\"  """, "Illegal Escape In String: abcdef\\\"",160))

    def test_illegal_escape3(self):
        """test illegal escape3"""
        self.assertTrue(TestLexer.checkLexeme(""" "abcdeggg\\4erer" """, "Illegal Escape In String: abcdeggg\\4", 161))

    def test_normal_string_with_escape1(self):
        """test normal string with escape 1"""
        self.assertTrue(TestLexer.checkLexeme(""" "ab'"c\\n def"  ""","""ab'"c\\n def,<EOF>""",162))

    def test_normal_string_with_escape2(self):
        """test normal string with escape 2"""
        self.assertTrue(TestLexer.checkLexeme(""" "ab'"c\\n \\b \\f \\r \\t \\' \\\\ def"  ""","""ab'"c\\n \\b \\f \\r \\t \\' \\\\ def,<EOF>""",163))

    def test_single_quote_in_string1(self):
        """test single quote in string 1"""
        self.assertTrue(TestLexer.checkLexeme(""" "abcdef'" """, """Unclosed String: abcdef'" """, 164))

    def test_single_quote_in_string2(self):
        """test single quote in string 2"""
        self.assertTrue(TestLexer.checkLexeme(""" "abcdef'welkjf" """, """Illegal Escape In String: abcdef'w""", 165))

    def test_single_quote_in_string3(self):
        """test single quote in string 3"""
        self.assertTrue(TestLexer.checkLexeme(""" "'abcdefwelkjf" """, """Illegal Escape In String: 'a""", 166))    

    def test_normal_string_with_escape3(self):
        """test string in string"""
        self.assertTrue(TestLexer.checkLexeme(""" "abcsd '"baks'" sdklfj"  """, """abcsd '"baks'" sdklfj,<EOF>""", 167))

    def test_comment_in_string(self):
        """test comment in string"""
        self.assertTrue(TestLexer.checkLexeme(""" "sdfkj** sdkfj **skdjf" ""","""sdfkj** sdkfj **skdjf,<EOF>""", 168))

    def test_multiple_string(self):
        """test multiple string"""
        self.assertTrue(TestLexer.checkLexeme(""" "   slkdfj   "   ab   ekj "    fsklj  " sjf  kdf""", """   slkdfj   ,ab,ekj,    fsklj  ,sjf,kdf,<EOF>""", 169))
    
    def test_empty_string(self):
        """test empty string"""
        self.assertTrue(TestLexer.checkLexeme(" \"\" \"\" \"\"\"\" \"\"\"\"\"\"\"\"  ", ",,,,,,,,<EOF>" , 170))

    def test_real_escape_character(self):
        """test newline character"""
        self.assertTrue(TestLexer.checkLexeme(""" "abcdef 
        ghiklm" ""","Unclosed String: abcdef ", 171))

    def test_array1(self):
        self.assertTrue(TestLexer.checkLexeme("{1,2,3,{4,5,6,{7,8,9,{1,2,3,5,4,333333,\"sfjks\"}}}}", "{,1,,,2,,,3,,,{,4,,,5,,,6,,,{,7,,,8,,,9,,,{,1,,,2,,,3,,,5,,,4,,,333333,,,sfjks,},},},},<EOF>", 172))

    def test_array2(self):
        self.assertTrue(TestLexer.checkLexeme("{}{{{}{{}{}{43,34,6,24,,{}{}[..,,][][{}}{}{}{{}}}{}\"jrejrjkkkw33@@##\"", "{,},{,{,{,},{,{,},{,},{,43,,,34,,,6,,,24,,,,,{,},{,},[,.,.,,,,,],[,],[,{,},},{,},{,},{,{,},},},{,},jrejrjkkkw33@@##,<EOF>", 173))

    def test_array3(self):
        self.assertTrue(TestLexer.checkLexeme("""{{1,1.1, "abcdef\r", True }, {True, 1.3, 00, "aa"}}""", "{,{,1,,,1.1,,,Unclosed String: abcdef", 174))

    def test_normal_string_with_escape4(self):
        self.assertTrue(TestLexer.checkLexeme(""" "wueryTTTa\\\'""sdjfvvvv """, "wueryTTTa\\\',Unclosed String: sdjfvvvv ", 175))

    def test_if_else_keyword(self):
        self.assertTrue(TestLexer.checkLexeme("IfIfElseElseIfElseElseIfIfIfElseElseElseElseIfIfElseIfElseElseIfIf", "If,If,Else,ElseIf,Else,ElseIf,If,If,Else,Else,Else,ElseIf,If,ElseIf,Else,ElseIf,If,<EOF>", 176))

    def test_all_keyword(self):
        self.assertTrue(TestLexer.checkLexeme("BodyElseIfElseIfVarWhileTrueFalseEndDoDoEndBodyBodyReturnFunctionThenDoParameterBreakContinueEndForEndWhileReturn", "Body,ElseIf,ElseIf,Var,While,True,False,EndDo,Do,EndBody,Body,Return,Function,Then,Do,Parameter,Break,Continue,EndFor,EndWhile,Return,<EOF>", 177))

    def test_large_equal_operator(self):
        self.assertTrue(TestLexer.checkLexeme(">>>>=>.>>>=>=>....=====.....>>>=.=..==>>..=>", ">,>,>,>=,>.,>,>,>=,>=,>.,.,.,.,==,==,=,.,.,.,.,.,>,>,>=.,=,.,.,==,>,>.,.,=,>,<EOF>", 178))

    def test_less_equal_operator(self):
        self.assertTrue(TestLexer.checkLexeme("<=.<=.=.===....==<<<<===...<<<====......===<..<=<=...", "<=.,<=.,=,.,==,=,.,.,.,.,==,<,<,<,<=,==,.,.,.,<,<,<=,==,=,.,.,.,.,.,.,==,=,<.,.,<=,<=.,.,.,<EOF>", 179))
    
    def test_all_operator(self):
        self.assertTrue(TestLexer.checkLexeme("+-* *.+.!==%!&&<===>.<=.>=.<.>||\\.-.-\\!==/=", "+,-,*,*.,+.,!=,=,%,!,&&,<=,==,>.,<=.,>=.,<.,>,||,\\.,-.,-,\\,!=,=/=,<EOF>", 180))

    def test_all_operator2(self):
        self.assertTrue(TestLexer.checkLexeme("+-+.!==%!&&**.<===>.<=.>=.<.>||\\.-.-\\!==/=", "+,-,+.,!=,=,%,!,&&,Unterminated Comment", 181))

    def test_long_identifier(self):
        self.assertTrue(TestLexer.checkLexeme("alksjlksjbkfjsfkdslfjsdklfjksldfjkdsljfksdfjdkljfklsdfjdkslfjdkslfjnweriuywerkj43t324728rnrhir2y3ewrhwerkhrjk32hr8746", "alksjlksjbkfjsfkdslfjsdklfjksldfjkdsljfksdfjdkljfklsdfjdkslfjdkslfjnweriuywerkj43t324728rnrhir2y3ewrhwerkhrjk32hr8746,<EOF>", 182))

    def test_asterik1(self):
        self.assertTrue(TestLexer.checkLexeme("** ***** *** * * *** 8** 8** 8**** **** 8**8****", "*,*,*,8,8,<EOF>", 183))
    
    def test_asterik2(self):
        self.assertTrue(TestLexer.checkLexeme("* * *** *** * * * * * * * *** *** *** * *** * ***** * ******* * *** ***** ****** *********", "*,*,*,*,*,*,*,*,*,*,*,*,*,*,*,*,*,Unterminated Comment", 184))

    def test_quote1(self):
        self.assertTrue(TestLexer.checkLexeme("\"\"\" \"\"\"\"\" \"\"\"\"\"\" \"\" \"\" \" \"", ", ,,,,,,,, ,<EOF>", 185))

    def test_quote2(self):
        self.assertTrue(TestLexer.checkLexeme("\"\'\"\"\'\" \"\'\" \"\'\"\"\'\" ", "\'\",Error Token \'", 186))

    def test_random_number(self):
        self.assertTrue(TestLexer.checkLexeme("023497e43e34e43e43o0o340o439284o900234o003240O943", "023497e43,e34e43e43o0o340o439284o900234o003240O943,<EOF>", 187))

    def test_long_number(self):
        self.assertTrue(TestLexer.checkLexeme("0XABCDEFFDDEDFAAAAFFaFEEEF", "0XABCDEFFDDEDFAAAAFF,aFEEEF,<EOF>",188))

    def test_keyword_in_id(self):
        self.assertTrue(TestLexer.checkLexeme("abcdTrueFalse", "abcdTrueFalse,<EOF>", 189))

    def test_string_and_comment(self):
        self.assertTrue(TestLexer.checkLexeme("\"\"***\"\"\"\"\"** * *** \"\" \" *** ******* \" * \" * ** \" * \" ** \" *", ",*,*, * ,Unterminated Comment", 190))

    def test_string_and_comment2(self):
        self.assertTrue(TestLexer.checkLexeme("\"\"***\"\"\"\"\"** * *** \"\" \" *** ******* \" * \" * ** \" * \" ** \" *\"", ",*,*, * ,Unterminated Comment", 191)) 

    def test_negative_int(self):
        self.assertTrue(TestLexer.checkLexeme("-12443", "-,12443,<EOF>", 192))
    
    def test_simple_program(self):
        self.assertTrue(TestLexer.checkLexeme("""Var : x, y, z = -4;
                                                Function x
                                                Parameter: x, y, z
                                                Body:
                                                Break;
                                                Continue; Return 3-4;
                                                EndBody....""", "Var,:,x,,,y,,,z,=,-,4,;,Function,x,Parameter,:,x,,,y,,,z,Body,:,Break,;,Continue,;,Return,3,-,4,;,EndBody,.,.,.,.,<EOF>", 193))
    
    def test_unary_operator(self):
        self.assertTrue(TestLexer.checkLexeme("""1-----++++!!!!--..-.-.-.+.+.2""", "1,-,-,-,-,-,+,+,+,+,!,!,!,!,-,-.,.,-.,-.,-.,+.,+.,2,<EOF>", 194))

    def test_real_escape_character2(self):
        self.assertTrue(TestLexer.checkLexeme(""" "\b\f\r" """, "Unclosed String: \b\f", 195))

    def test_real_escape_character3(self):
        self.assertTrue(TestLexer.checkLexeme(""" "\f\t\b\'\\\"" """, "Illegal Escape In String: \f\t\b\'\\", 196))

    def test_real_escape_character4(self):
        self.assertTrue(TestLexer.checkLexeme(""" "\\b\\r\\f\\n\\\'\'\"" \t \b "  """, """\\b\\r\\f\\n\\\''",Error Token \b""", 197))

    def test_real_escape_character_in_comment(self):
        self.assertTrue(TestLexer.checkLexeme(""" ** abcc \r \t \n \r \b \f \\ \' \" ** """, "<EOF>", 198))

    def test_unclosed_string_in_comment(self):
        self.assertTrue(TestLexer.checkLexeme("""** \" *""", "Unterminated Comment", 199))

    def test_long_float(self):
        self.assertTrue(TestLexer.checkLexeme(""" 00000000000000.00000000000000000e-00000000000000000 """, "00000000000000.00000000000000000e-00000000000000000,<EOF>", 200))
