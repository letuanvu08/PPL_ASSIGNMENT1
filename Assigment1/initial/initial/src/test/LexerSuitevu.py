import unittest
from TestUtils import TestLexer

class LexerSuite(unittest.TestCase):
      
    def test_lower_identifier(self):
        """test identifiers"""
        self.assertTrue(TestLexer.checkLexeme("abc","abc,<EOF>",101))

    def test_lower_upper_id(self):
        self.assertTrue(TestLexer.checkLexeme("Var","Var,<EOF>",102))

    def test_wrong_token(self):
        self.assertTrue(TestLexer.checkLexeme("ab?svn","ab,Error Token ?",103))

    def test_integer(self):
        """test integers"""
        self.assertTrue(TestLexer.checkLexeme("Var x;","Var,x,;,<EOF>",104))

    def test_illegal_escape(self):
        """test illegal escape"""
        self.assertTrue(TestLexer.checkLexeme(""" "abc\\n \\'""","""Unclosed String: abc\\n \\'""",105))

    def test_unterminated_string(self):
        """test unclosed string"""
        self.assertTrue(TestLexer.checkLexeme(""" "abc def  ""","""Unclosed String: abc def  """,106))

    def test_normal_string_with_escape(self):
        """test normal string with escape"""
        self.assertTrue(TestLexer.checkLexeme(""" "ab'"c\\n def"  ""","""ab'"c\\n def,<EOF>""",107))

    def test_108(self):
        """test identifiers"""
        self.assertTrue(TestLexer.checkLexeme("sdfdgregsdfsttrtfdert5ty5654657ab\saqwewqr", "sdfdgregsdfsttrtfdert5ty5654657ab,\,saqwewqr,<EOF>", 108))

    def test_lower_identifier_(self):
        """test identifiers"""
        self.assertTrue(TestLexer.checkLexeme("ab-nc", "ab,-,nc,<EOF>", 109))
    def test_110(self):
        """Identifier"""
        input = "test_01_Identifierssdfdsdsffds4655467"
        expect = "test_01_Identifierssdfdsdsffds4655467,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 110))

    def test_111(self):
        """Wrong Identifier"""
        input = "AaDDDbcdD"
        expect = "Error Token A"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 111))
    def test_112(self):
        """Identifier"""
        input = "aaDDDb.{}cdD"
        expect = "aaDDDb,.,{,},cdD,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 112))
    def test_113(self):
        """Identifier"""
        input = "Truesafsdfg2435_DDDbcdD_________"
        expect = "True,safsdfg2435_DDDbcdD_________,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 113))
    def test_114(self):
        """WrongIdentifier"""
        input = "+-*\\32445safsdfg2435_DDDbcdD_"
        expect = "+,-,*,\,32445,safsdfg2435_DDDbcdD_,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 114))
    def test_115(self):
        """WrongIdentifier"""
        input = "32445Asafsdfg2435_DDDbcdD_________"
        expect = "32445,Error Token A"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 115))
    def test_116(self):
        """WrongIdentifier"""
        input = "32445AAsa.fsdfg2435_DDDbcdD_________"
        expect = "32445,Error Token A"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 116))
    def test_117(self):
        """WrongIdentifier"""
        input = "Varasdfa"
        expect = "Var,asdfa,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 117))
    def test_118(self):
        """WrongIdentifier"""
        input = "Varasdfa"
        expect = "Var,asdfa,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 118))
    def test_119(self):
        """WrongIdentifier"""
        input = "Var#%~asdfa"
        expect = "Var,Error Token #"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 119))
    def test_120(self):
        """WrongIdentifier"""
        input = "####Var#%~asdfa"
        expect = "Error Token #"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 120))
    """ Keywords"""
    def test_121(self):
        """ Keywords"""
        input = "+ +. - -. * *. \ \. % ! && || == != < > <= >= =/= <. >. <=. >=."
        expect = "+,+.,-,-.,*,*.,\,\.,%,!,&&,||,==,!=,<,>,<=,>=,=/=,<.,>.,<=.,>=.,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 121))

    def test_122(self):
        """ Keywords"""
        input = "( ) [ ] : . , ; { }"
        expect = "(,),[,],:,.,,,;,{,},<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 122))

    def test_123(self):
        """ Keywords"""
        input = "Body Else EndFor If Var EndDo BreakElseIf EndWhile Parameter While Continue EndBodyForReturnTrueDoEndIfFunctionThenFalse"
        expect = "Body,Else,EndFor,If,Var,EndDo,Break,ElseIf,EndWhile,Parameter,While,Continue,EndBody,For,Return,True,Do,EndIf,Function,Then,False,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 123))

    def test_124(self):
        """ Keywords"""
        input = "body Else Endfor if var Enddo break Elseif Endwhile"
        expect = "body,Else,Error Token E"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 124))
    def test_125(self):
        """ Keywords"""
        input = "=--.++.* *.\\\\.&&||!!====/=%,.;:<><=>=<.>.<=.>=.()[]{}"
        expect = "=,-,-.,+,+.,*,*.,\,\.,&&,||,!,!=,==,=/=,%,,,.,;,:,<,>,<=,>=,<.,>.,<=.,>=.,(,),[,],{,},<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 125))
    def test_126(self):
        """ Keywords"""
        input = """Function: testIf\n"""
        input += """	Body:\n"""
        input += """		If hihi == huhu Then\n"""
        input += """			hihi = huhu;\n"""
        input += """			huhu = hihi || True;\n"""
        input += """		ElseIf hihi == haha Then\n"""
        input += """			huhu = hihi;\n"""
        input += """			anotherstatement();\n"""
        input += """		EndIf.\n"""
        input += """	EndBody."""
        expect = "Function,:,testIf,Body,:,If,hihi,==,huhu,Then,hihi,=,huhu,;,huhu,=,hihi,||,True,;,ElseIf,hihi,==,haha,Then,huhu,=,hihi,;,anotherstatement,(,),;,EndIf,.,EndBody,.,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 126))
    def test_127(self):
        """ Keywords"""
        input = """Function: testIf\n"""
        input += """	Body:\n"""
        input += """		If hihi == huhu Then\n"""
        input += """			hihi = huhu;\n"""
        input += """			huhu = hihi || True;\n"""
        input += """		ElseIf hihi == haha Then\n"""
        input += """			huhu = hihi;\n"""
        input += """			anotherstatement();\n"""
        input += """		Else\n"""
        input += """			test();\n"""
        input += """			Return;\n"""
        input += """		EndIf.\n"""
        input += """	EndBody."""
        expect = "Function,:,testIf,Body,:,If,hihi,==,huhu,Then,hihi,=,huhu,;,huhu,=,hihi,||,True,;,ElseIf,hihi,==,haha,Then,huhu,=,hihi,;,anotherstatement,(,),;,Else,test,(,),;,Return,;,EndIf,.,EndBody,.,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 127))

    def test_128(self):
        """ Keywords"""
        input = """Function: testFor\n"""
        input += """	Body:\n"""
        input += """		For ( i = 0 , i < 10 , 2) Do\n"""
        input += """			writeln(i);\n"""
        input += """		EndFor.\n"""
        input += """	EndBody."""
        expect = "Function,:,testFor,Body,:,For,(,i,=,0,,,i,<,10,,,2,),Do,writeln,(,i,),;,EndFor,.,EndBody,.,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 128))

    def test_129(self):
        """Literals"""
        input = "0 199 0xFF 0xABC 0o567 0O777"
        expect = "0,199,0xFF,0xABC,0o567,0O777,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 129))

    def test_130(self):
        """Literals"""
        input = "0.00e4 0.00 2.0 1e4 2.7e6"
        expect = "0.00e4,0.00,2.0,1e4,2.7e6,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 130))

    def test_131(self):
        """Literals"""
        input = "0.0e+3 0.1e-2 1e-2 1e+3 1.1e-1"
        expect = "0.0e+3,0.1e-2,1e-2,1e+3,1.1e-1,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 131))

    def test_intlit_132(self):
        self.assertTrue(TestLexer.checkLexeme("0", "0,<EOF>", 132))

    def test_intlit_133(self):
        self.assertTrue(TestLexer.checkLexeme("200", "200,<EOF>", 133))

    def test_intlit_134(self):
        self.assertTrue(TestLexer.checkLexeme("0254353", "0,254353,<EOF>", 134))

    def test_intlit_135(self):
        self.assertTrue(TestLexer.checkLexeme("-2325357", "-,2325357,<EOF>", 135))

    def test_floatlit_136(self):
        self.assertTrue(TestLexer.checkLexeme("000000000002.5", "000000000002.5,<EOF>", 136))

    def test_floatlit_137(self):
        self.assertTrue(TestLexer.checkLexeme("123.", "123.,<EOF>", 137))

    def test_floatlit_138(self):
        self.assertTrue(TestLexer.checkLexeme("0.", "0.,<EOF>", 138))

    def test_floatlit_139(self):
        self.assertTrue(TestLexer.checkLexeme("0.e-123", "0.e-123,<EOF>", 139))
    def test_floatlit_140(self):
        self.assertTrue(TestLexer.checkLexeme("-123E123", "-,123E123,<EOF>", 140))
    def test_floatlit_141(self):
        self.assertTrue(TestLexer.checkLexeme("-.0.", "-.,0.,<EOF>", 141))
    def test_floatlit_142(self):
        self.assertTrue(TestLexer.checkLexeme("0.000E-0", "0.000E-0,<EOF>", 141))
    def test_floatlit_143(self):
        self.assertTrue(TestLexer.checkLexeme("0.33E-", "0.33,Error Token E", 143))
    def test_floatlit_144(self):
        self.assertTrue(TestLexer.checkLexeme("00.0001E--22", "00.0001,Error Token E", 144))
    def test_floatlit_145(self):
        self.assertTrue(TestLexer.checkLexeme("0.1E+000", "0.1E+000,<EOF>", 145))
    def test_STRING_1(self):
        """Normal String"""
        self.assertTrue(TestLexer.checkLexeme(""" "True False Var Function" """, """True False Var Function,<EOF>""", 146))

    def test_STRING_2(self):
        """Normal String"""
        self.assertTrue(TestLexer.checkLexeme(""" "'"Le tuan vu'"" """, """'"Le tuan vu'",<EOF>""", 147))

    def test_STRING_3(self):
        """Normal String"""
        self.assertTrue(TestLexer.checkLexeme(""" "Le Tuan Vu\\n" """, """Le Tuan Vu\\n,<EOF>""", 148))
    def test_STRING_4(self):
        """Normal String"""
        self.assertTrue(TestLexer.checkLexeme(""" "Le\\f Tuan\\b Vu\\r" """, """Le\\f Tuan\\b Vu\\r,<EOF>""", 149))
    def test_STRING_5(self):
        """Normal String"""
        self.assertTrue(TestLexer.checkLexeme(""" "lam test case chan qua di" """, """lam test case chan qua di,<EOF>""", 150))
    def test_STRING_6(self):
        """Normal String"""
        self.assertTrue(TestLexer.checkLexeme(""" "" """, """,<EOF>""", 151))
    def test_STRING_7(self):
        """Normal String"""
        self.assertTrue(TestLexer.checkLexeme(""" "troi oi la troi'"tuc chet dc" """, """troi oi la troi'"tuc chet dc,<EOF>""", 152))
    def test_STRING_8(self):
        """Normal String"""
        self.assertTrue(TestLexer.checkLexeme(""" "chi mong\\n\\r\\t\\b\\f qua mon___ lay troi lay dat---" """, """chi mong\\n\\r\\t\\b\\f qua mon___ lay troi lay dat---,<EOF>""", 153))
    def test_STRING_9(self):
        """Normal String"""
        self.assertTrue(TestLexer.checkLexeme(""" "\\n cai nay la string dung'"'"'" nay\\r\\b\\r" """, """\\n cai nay la string dung'"'"'" nay\\r\\b\\r,<EOF>""", 154))
    def test_STRING_10(self):
        """Normal String"""
        self.assertTrue(TestLexer.checkLexeme(""" "Day la string dung cuoi cung hahaha.*-+=()* " """, """Day la string dung cuoi cung hahaha.*-+=()* ,<EOF>""", 155))
    def test_COMMENT_1(self):
        """commment"""
        input = "****"
        expect = "<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 156))
    def test_COMMENT_2(self):
        """commment"""
        input = "***weuhdsck2348473857344932urfjc,xmcv\n cnvn32!@#$%^&*)(&^%$fsvr345***"
        expect = "*,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 157))
    def test_COMMENT_3(self):
        """commment"""
        input = "***weuhdsck2348473857344932urfjc,x*********mcv cnvn32!@#$%^&*)(&^%$fsvr345***"
        expect = "*,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 158))
    def test_COMMENT_4(self):
        """commment"""
        input = "*************************************"
        expect = "*,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 159))
    def test_COMMENT_5(self):
        """commment"""
        input = "***weuhdsck2348473857344932urfjc,xmc\\n\\t\\***f**!@#$%^&*()v cnvn32!@#$%^&*)(&^%$fsvr345***"
        expect = "*,f,*,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 160))

    def test_array1(self):
        """Array"""
        self.assertTrue(TestLexer.checkLexeme("{1,2,3,4,5}", "{,1,,,2,,,3,,,4,,,5,},<EOF>", 161))

    def test_array2(self):
        """Array"""
        self.assertTrue(TestLexer.checkLexeme("{{1,2,3},{4,5,6},{7,8,9}}", "{,{,1,,,2,,,3,},,,{,4,,,5,,,6,},,,{,7,,,8,,,9,},},<EOF>", 162))
    def test_array3(self):
        """Array"""
        self.assertTrue(TestLexer.checkLexeme("{{ 1, 2, 3},{4,5,6},{7}}", "{,{,1,,,2,,,3,},,,{,4,,,5,,,6,},,,{,7,},},<EOF>", 163))
    def test_array4(self):
        """Array"""
        self.assertTrue(TestLexer.checkLexeme("{{1,2,3},{4.1,5.2,6.3},{7,8,9}}", "{,{,1,,,2,,,3,},,,{,4.1,,,5.2,,,6.3,},,,{,7,,,8,,,9,},},<EOF>", 164))
    def test_array5(self):
        """Array"""
        self.assertTrue(TestLexer.checkLexeme("{},{4,5,6},{7,8,9}}", "{,},,,{,4,,,5,,,6,},,,{,7,,,8,,,9,},},<EOF>", 165))
    def test_array6(self):
        """Array"""
        self.assertTrue(TestLexer.checkLexeme("{,{4,5,6},{7,8,9}}", "{,,,{,4,,,5,,,6,},,,{,7,,,8,,,9,},},<EOF>", 166))
    def test_array7(self):
        """Array"""
        self.assertTrue(TestLexer.checkLexeme("{1,2,3}{4,5,6}{7,8,9}", "{,1,,,2,,,3,},{,4,,,5,,,6,},{,7,,,8,,,9,},<EOF>", 167))
    def test_array8(self):
        """Array"""
        self.assertTrue(TestLexer.checkLexeme("{{1.0,2.0,3.0},,{7,8,9}}", "{,{,1.0,,,2.0,,,3.0,},,,,,{,7,,,8,,,9,},},<EOF>", 168))
    def test_array9(self):
        """Array"""
        self.assertTrue(TestLexer.checkLexeme("{{},{}}","{,{,},,,{,},},<EOF>", 169))
    def test_array10(self):
        """Array"""
        self.assertTrue(TestLexer.checkLexeme("  { { { 1 }   }   , { { 1 }  }  }  ", "{,{,{,1,},},,,{,{,1,},},},<EOF>", 170))

    """Illegal Escape In String"""
    def test_error_token_1(self):
        """error_token"""
        self.assertTrue(TestLexer.checkLexeme("aA#sVN", "aA,Error Token #", 171))

    def test_error_token_2(self):
        """error_token"""
        self.assertTrue(TestLexer.checkLexeme("Aaaaa", "Error Token A", 172))
    def test_error_token_3(self):
        """error_token"""
        self.assertTrue(TestLexer.checkLexeme("234AA", "234,Error Token A", 173))
    def test_error_token_4(self):
        """error_token"""
        self.assertTrue(TestLexer.checkLexeme("Var^^assd", "Var,Error Token ^", 174))
    def test_error_token_5(self):
        """error_token"""
        self.assertTrue(TestLexer.checkLexeme("~True", "Error Token ~", 175))

    def test_unclosed_string_1(self):
        """unclosed_string"""
        input = """ "Le Tuan Vu \\n"""
        expect = """Unclosed String: Le Tuan Vu \\n"""
        self.assertTrue(TestLexer.checkLexeme(input, expect, 176))
    def test_unclosed_string_2(self):
        """unclosed_string"""
        input = """ "Le Tuan Vu \\n'" """
        expect = """Unclosed String: Le Tuan Vu \\n'" """
        self.assertTrue(TestLexer.checkLexeme(input, expect, 177))
    def test_unclosed_string_3(self):
        """unclosed_string"""
        input = """ "'"Le Tuan Vu \\n\'" """
        expect = """Unclosed String: '"Le Tuan Vu \\n\'" """
        self.assertTrue(TestLexer.checkLexeme(input, expect, 178))
    def test_unclosed_string_4(self):
        """unclosed_string"""
        input = """ "sasarfsdewgwef'"'"'" """
        expect = """Unclosed String: sasarfsdewgwef'"'"'" """
        self.assertTrue(TestLexer.checkLexeme(input, expect, 179))
    def test_unclosed_string_5(self):
        """unclosed_string"""
        input = """ "asfdhsdsjfhsf\\n\\r\\f"""
        expect = """Unclosed String: asfdhsdsjfhsf\\n\\r\\f"""
        self.assertTrue(TestLexer.checkLexeme(input, expect, 180))

    def test_ILLEGAL_ESCAPE_1(self):
        """ILLEGAL_ESCAPE"""
        input = """ "cdsgregfvddsfgrf\n\r\t" """
        expect = """Illegal Escape In String: cdsgregfvddsfgrf\n"""
        self.assertTrue(TestLexer.checkLexeme(input, expect, 181))
    def test_ILLEGAL_ESCAPE_2(self):
        """ILLEGAL_ESCAPE"""
        input = """ "\\swtrfwdsgrerfvdsfdf" """
        expect = """Illegal Escape In String: \\s"""
        self.assertTrue(TestLexer.checkLexeme(input, expect, 182))
    def test_ILLEGAL_ESCAPE_3(self):
        """ILLEGAL_ESCAPE"""
        input = """ "safdgwdfe\\hsafewfcedfe """
        expect = """Illegal Escape In String: safdgwdfe\\h"""
        self.assertTrue(TestLexer.checkLexeme(input, expect, 183))
    def test_ILLEGAL_ESCAPE_4(self):
        """ILLEGAL_ESCAPE"""
        input = """ "??????" "saff\n"""
        expect = """??????,Illegal Escape In String: saff\n"""
        self.assertTrue(TestLexer.checkLexeme(input, expect, 184))
    def test_ILLEGAL_ESCAPE_5(self):
        """ILLEGAL_ESCAPE"""
        input = """ "saf\\tsadg\\n\\" """
        expect = """Illegal Escape In String: saf\\tsadg\\n\\"""
        self.assertTrue(TestLexer.checkLexeme(input, expect, 185))
    def test_MIX_1(self):
        """MIX"""
        input = """Function: testFor\n"""
        input += """	Body\n"""
        input += """		For ( i = 0  i < 10 , 2) Do\n"""
        input += """			writeln(i);\n"""
        input += """		EndFor.\n"""
        input += """	EndBody"""
        expect = """Function,:,testFor,Body,For,(,i,=,0,i,<,10,,,2,),Do,writeln,(,i,),;,EndFor,.,EndBody,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input, expect, 186))
    def test_MIX_2(self):
        """MIX"""
        input = """Function: testdowhile\n"""
        input += """	Body:\n"""
        input += """		Do\n"""
        input += """			hisafdhi = husadhu;\n"""
        input += """			hADusdhu = hihsadi || True;\n"""
        input += """			sadhuhu = hisadhi;\n"""
        input += """			ansdothersadstatesdment();\n"""
        input += """		For(i=1,i>=.23,2143)\n"""
        input += """		Do\n"""
        input += """		For(i=1,i>=.23,2143)\n"""
        input += """		Do\n"""
        input += """		Var:cdsfd={wqrwt};"""
        input += """		If a==b Then\n"""
        input += """		a=3246534*32565;\n"""
        input += """		Else\n"""
        input += """		a=3246534*32565;\n"""
        input += """		EndIf.\n"""
        input += """		a=3246534*32565;\n"""
        input += """		EndFor."""
        input += """			hsadsa = huhsadasfu;\n"""
        input += """			huhasdu = hihasdasi || True;\n"""
        input += """		EndFor.\n"""
        input += """		While(a>324)EndDo.\n"""
        input += """	EndBody."""
        expect="""Function,:,testdowhile,Body,:,Do,hisafdhi,=,husadhu,;,hADusdhu,=,hihsadi,||,True,;,sadhuhu,=,hisadhi,;,ansdothersadstatesdment,(,),;,For,(,i,=,1,,,i,>=.,23,,,2143,),Do,For,(,i,=,1,,,i,>=.,23,,,2143,),Do,Var,:,cdsfd,=,{,wqrwt,},;,If,a,==,b,Then,a,=,3246534,*,32565,;,Else,a,=,3246534,*,32565,;,EndIf,.,a,=,3246534,*,32565,;,EndFor,.,hsadsa,=,huhsadasfu,;,huhasdu,=,hihasdasi,||,True,;,EndFor,.,While,(,a,>,324,),EndDo,.,EndBody,.,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input, expect, 187))
    def test_MIX_3(self):
        """MIX"""
        input = """Function: testdowhile\n"""
        input += """	Body:\n"""
        input += """		Do\n"""
        input += """			hisafdhi = husadhu;\n"""
        input += """			husdhu = hihsadi || True;\n"""
        input += """			sadhuhu = hisadhi;\n"""
        input += """			ansdothersadstatesdment();\n"""
        input += """		While()EndDo.\n"""
        input += """	EndBody."""
        expect = """Function,:,testdowhile,Body,:,Do,hisafdhi,=,husadhu,;,husdhu,=,hihsadi,||,True,;,sadhuhu,=,hisadhi,;,ansdothersadstatesdment,(,),;,While,(,),EndDo,.,EndBody,.,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input, expect, 188))
    def test_MIX_4(self):
        """MIX"""
        input = """Function: testwhite\n"""
        input += """	Body:\n"""
        input += """		While (a>wfwrg )Do\n"""
        input += """			hdsfihi = huhdsfu;\n"""
        input += """			hsdfuhdsfu = hidsfhi || True;\n"""
        input += """		EndWhile\n"""
        input += """	EndBody."""
        expect = """Function,:,testwhite,Body,:,While,(,a,>,wfwrg,),Do,hdsfihi,=,huhdsfu,;,hsdfuhdsfu,=,hidsfhi,||,True,;,EndWhile,EndBody,.,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input, expect, 189))
    def test_MIX_5(self):
        """MIX"""
        input = """Function: testwhite\n"""
        input += """	Body:\n"""
        input += """		While (a>wfwrg )\n"""
        input += """			hdsfihi = huhdsfu;\n"""
        input += """			hsdfuhdsfu = hidsfhi || True;\n"""
        input += """		EndWhile.\n"""
        input += """	EndBody."""
        expect = """Function,:,testwhite,Body,:,While,(,a,>,wfwrg,),hdsfihi,=,huhdsfu,;,hsdfuhdsfu,=,hidsfhi,||,True,;,EndWhile,.,EndBody,.,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input, expect, 190))
    def test_MIX_6(self):
        """MIX"""
        input = """Function: testwhite\n"""
        input += """	Body:\n"""
        input += """		While (a>wfwrg )Do\n"""
        input += """		For(i=1,i>=.23,2143)\n"""
        input += """		Do\n"""
        input += """		For(i=1,i>=.23,2143)\n"""
        input += """		Do\n"""
        input += """		Var:cdsfd={wqrwt};"""
        input += """		If a==b Then\n"""
        input += """		a=3246534*32565;\n"""
        input += """		Else\n"""
        input += """		a=3246534*32565;\n"""
        input += """		EndIf.\n"""
        input += """		a=3246534*32565;\n"""
        input += """		"""
        input += """			hsadsa = huhsadasfu;\n"""
        input += """			huhasdu = hihasdasi || True;\n"""
        input += """		EndFor.\n"""
        input += """		EndFor.\n"""
        input += """			hdsfihi = huhdsfu;\n"""
        input += """			hsdfuhdsfu = hidsfhi || True;\n"""
        input += """		EndWhile.\n"""
        input += """	EndBody."""
        expect="""Function,:,testwhite,Body,:,While,(,a,>,wfwrg,),Do,For,(,i,=,1,,,i,>=.,23,,,2143,),Do,For,(,i,=,1,,,i,>=.,23,,,2143,),Do,Var,:,cdsfd,=,{,wqrwt,},;,If,a,==,b,Then,a,=,3246534,*,32565,;,Else,a,=,3246534,*,32565,;,EndIf,.,a,=,3246534,*,32565,;,hsadsa,=,huhsadasfu,;,huhasdu,=,hihasdasi,||,True,;,EndFor,.,EndFor,.,hdsfihi,=,huhdsfu,;,hsdfuhdsfu,=,hidsfhi,||,True,;,EndWhile,.,EndBody,.,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input, expect, 191))
    def test_MIX_7(self):
        """MIX"""
        input = """Function: testwhite\n"""
        input += """	Body:\n"""
        input += """		While ( )Do\n"""
        input += """			hdsfihi = huhdsfu;\n"""
        input += """			hsdfuhdsfu = hidsfhi || True;\n"""
        input += """		EndWhile.\n"""
        input += """	EndBody."""
        expect = """Function,:,testwhite,Body,:,While,(,),Do,hdsfihi,=,huhdsfu,;,hsdfuhdsfu,=,hidsfhi,||,True,;,EndWhile,.,EndBody,.,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input, expect, 192))
    def test_MIX_8(self):
        """MIX"""
        input = """Function: testFor\n"""
        input += """	Body:\n"""
        input += """		For ( i = 0 , i < 10 , 2) Do\n"""
        input += """			If hiih == haha Then\n"""
        input += """				dosomethin();\n"""
        input += """			Endif.\n"""
        input += """		EndFor.\n"""
        input += """	EndBody."""
        input = """Function: testFor\n"""
        input += """	Body:\n"""
        input += """		For ( i = 0 , i < 10 , 2) Do\n"""
        input += """			If hiih == haha Then\n"""
        input += """				dosomethin();\n"""
        input += """			Endif.\n"""
        input += """		EndFor.\n"""
        input += """	EndBody."""
        input = """Function: testFor\n"""
        input += """	Body:\n"""
        input += """		For ( i = 0 , i < 10 , 2) Do\n"""
        input += """			If hiih == haha Then\n"""
        input += """				dosomethin();\n"""
        input += """			Endif.\n"""
        input += """		EndFor.\n"""
        input += """	EndBody."""
        expect = """Function,:,testFor,Body,:,For,(,i,=,0,,,i,<,10,,,2,),Do,If,hiih,==,haha,Then,dosomethin,(,),;,Error Token E"""
        self.assertTrue(TestLexer.checkLexeme(input, expect, 193))
    def test_MIX_9(self):
        """MIX"""
        input = """Function: testwhite\n"""
        input += """	Body:\n"""
        input += """		While ( a)Do\n"""
        input += """			hdsfihi = huhdsfu;\n"""
        input += """			hsdfuhdsfu = hidsfhi || True;\n"""
        input += """		EndDo.\n"""
        input += """	EndBody."""
        expect = """Function,:,testwhite,Body,:,While,(,a,),Do,hdsfihi,=,huhdsfu,;,hsdfuhdsfu,=,hidsfhi,||,True,;,EndDo,.,EndBody,.,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input, expect, 194))
    def test_MIX_10(self):
        """MIX"""
        input = """Function: testwhite\n"""
        input += """	Body:\n"""
        input += """		While ( )Do\n"""
        input += """			hdsfihi = huhdsfu;\n"""
        input += """			hsdfuhdsfu = hidsfhi || True;\n"""
        input += """		While ( )Do\n"""
        input += """			hdsfihi = huhdsfu;\n"""
        input += """			hsdfuhdsfu = hidsfhi || True;\n"""
        input += """		EndWhile.\n"""
        input += """		While ( )Do\n"""
        input += """			hdsfihi = huhdsfu;\n"""
        input += """			hsdfuhdsfu = hidsfhi || True;\n"""
        input += """		EndWhile.\n"""
        input += """		EndWhile.\n"""
        input += """	EndBody."""
        expect = """Function,:,testwhite,Body,:,While,(,),Do,hdsfihi,=,huhdsfu,;,hsdfuhdsfu,=,hidsfhi,||,True,;,While,(,),Do,hdsfihi,=,huhdsfu,;,hsdfuhdsfu,=,hidsfhi,||,True,;,EndWhile,.,While,(,),Do,hdsfihi,=,huhdsfu,;,hsdfuhdsfu,=,hidsfhi,||,True,;,EndWhile,.,EndWhile,.,EndBody,.,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input, expect, 195))
    def test_MIX_11(self):
        """MIX"""
        input = """Function: testwhite\n"""
        input += """	Body:\n"""
        input += """		While ( a)Do\n"""
        input += """			hdsfihi = huhdsfu;\n"""
        input += """			hsdfuhdsfu = hidsfhi || True;\n"""
        input += """		While (a )Do\n"""
        input += """			hdsfihi = huhdsfu;\n"""
        input += """			hsdfuhdsfu = hidsfhi || True;\n"""
        input += """		EndWhile.\n"""
        input += """		While (a )Do\n"""
        input += """		While (a )Do\n"""
        input += """			hdsfihi = huhdsfu;\n"""
        input += """			hsdfuhdsfu = hidsfhi || True;\n"""
        input += """		EndWhile.\n"""
        input += """		EndWhile.\n"""
        input += """	EndBody."""
        expect = """Function,:,testwhite,Body,:,While,(,a,),Do,hdsfihi,=,huhdsfu,;,hsdfuhdsfu,=,hidsfhi,||,True,;,While,(,a,),Do,hdsfihi,=,huhdsfu,;,hsdfuhdsfu,=,hidsfhi,||,True,;,EndWhile,.,While,(,a,),Do,While,(,a,),Do,hdsfihi,=,huhdsfu,;,hsdfuhdsfu,=,hidsfhi,||,True,;,EndWhile,.,EndWhile,.,EndBody,.,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input, expect, 196))
    def test_MIX_12(self):
        """MIX"""
        input = """Function: testwhite\n"""
        input += """	Body:\n"""
        input += """		While ( a)Do\n"""
        input += """			hdsfihi = huhdsfu;\n"""
        input += """			hsdfuhdsfu = hidsfhi || True;\n"""
        input += """		While ( a)Do\n"""
        input += """			hdsfihi = huhdsfu;\n"""
        input += """			hsdfuhdsfu = hidsfhi || True;\n"""
        input += """		EndWhile.\n"""
        input += """		While ( a)Do\n"""
        input += """			hdsfihi = huhdsfu;\n"""
        input += """			hsdfuhdsfu = hidsfhi || True;\n"""
        input += """		EndWhile.\n"""
        input += """		EndWhile.\n"""
        input += """		EndWhile.\n"""
        input += """		EndWhile.\n"""
        input += """	EndBody."""
        expect ="""Function,:,testwhite,Body,:,While,(,a,),Do,hdsfihi,=,huhdsfu,;,hsdfuhdsfu,=,hidsfhi,||,True,;,While,(,a,),Do,hdsfihi,=,huhdsfu,;,hsdfuhdsfu,=,hidsfhi,||,True,;,EndWhile,.,While,(,a,),Do,hdsfihi,=,huhdsfu,;,hsdfuhdsfu,=,hidsfhi,||,True,;,EndWhile,.,EndWhile,.,EndWhile,.,EndWhile,.,EndBody,.,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input, expect, 197))
    def test_MIX_13(self):
        """MIX"""
        input = """Function: testdowhile\n"""
        input += """Parameter:a;"""
        input += """Parameter:a;"""
        input += """Parameter:a"""
        input += """Function: testdowhile\n"""

        input += """	Body:\n"""
        input += """		If hihi == huhu Then\n"""
        input += """			hihi = huhu;\n"""
        input += """			huhu = hihi || True;\n"""
        input += """		Else\n"""
        input += """			huhu = hihi;\n"""
        input += """			anotherstatement();\n"""
        input += """		EndIf.\n"""
        input += """	EndBody."""
        expect = """Function,:,testdowhile,Parameter,:,a,;,Parameter,:,a,;,Parameter,:,aFunction,:,testdowhile,Body,:,If,hihi,==,huhu,Then,hihi,=,huhu,;,huhu,=,hihi,||,True,;,Else,huhu,=,hihi,;,anotherstatement,(,),;,EndIf,.,EndBody,.,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input, expect, 198))
    def test_MIX_14(self):
        """MIX"""
        input = """Function: testdowhile\n"""
        input += """	Body:\n"""
        input += """		Do\n"""
        input += """			hisafdhi = husadhu;\n"""
        input += """			husdhu = hihsadi || True;\n"""
        input += """			sadhuhu = hisadhi;\n"""
        input += """			ansdothersadstatesdment();\n"""
        input += """		While(a>324)EndDo.\n"""
        input += """	EndBody."""
        expect="""Function,:,testdowhile,Body,:,Do,hisafdhi,=,husadhu,;,husdhu,=,hihsadi,||,True,;,sadhuhu,=,hisadhi,;,ansdothersadstatesdment,(,),;,While,(,a,>,324,),EndDo,.,EndBody,.,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input, expect, 199))
    def test_MIX_15(self):
        """MIX"""
        input = """Function: testdowhile\n"""
        input += """	Body:\n"""
        input += """		Do\n"""
        input += """			hisafdhi = husadhu;\n"""
        input += """			hADusdhu = hihsadi || True;\n"""
        input += """			sadhuhu = hisadhi;\n"""
        input += """			ansdothersadstatesdment();\n"""
        input += """		For(i=1,i>=.23,2143)\n"""
        input += """		Do\n"""
        input += """		For(i=1,i>=.23,2143)\n"""
        input += """		Do\n"""
        input += """		Var:cdsfd={wqrwt};"""
        input += """		If a==b Then\n"""
        input += """		a=3246534*32565;\n"""
        input += """		Else\n"""
        input += """		a=3246534*32565;\n"""
        input += """		EndIf.\n"""
        input += """		a=3246534*32565;\n"""
        input += """		EndFor."""
        input += """			hsadsa = huhsadasfu;\n"""
        input += """			huhasdu = hihasdasi || True;\n"""
        input += """		EndFor.\n"""
        input += """		Do\n"""
        input += """			hisafdhi = husadhu;\n"""
        input += """			husdhu = hihsadi || True;\n"""
        input += """			sadhuhu = hisadhi;\n"""
        input += """			ansdothersadstatesdment();\n"""
        input += """		While(a>324)EndDo.\n"""
        input += """		While(a>324)EndDo.\n"""
        input += """	EndBody."""
        expect="""Function,:,testdowhile,Body,:,Do,hisafdhi,=,husadhu,;,hADusdhu,=,hihsadi,||,True,;,sadhuhu,=,hisadhi,;,ansdothersadstatesdment,(,),;,For,(,i,=,1,,,i,>=.,23,,,2143,),Do,For,(,i,=,1,,,i,>=.,23,,,2143,),Do,Var,:,cdsfd,=,{,wqrwt,},;,If,a,==,b,Then,a,=,3246534,*,32565,;,Else,a,=,3246534,*,32565,;,EndIf,.,a,=,3246534,*,32565,;,EndFor,.,hsadsa,=,huhsadasfu,;,huhasdu,=,hihasdasi,||,True,;,EndFor,.,Do,hisafdhi,=,husadhu,;,husdhu,=,hihsadi,||,True,;,sadhuhu,=,hisadhi,;,ansdothersadstatesdment,(,),;,While,(,a,>,324,),EndDo,.,While,(,a,>,324,),EndDo,.,EndBody,.,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input, expect, 200))
