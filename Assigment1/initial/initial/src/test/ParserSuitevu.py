import unittest
from TestUtils import TestParser

class ParserSuite(unittest.TestCase):
    def test_simple_program(self):
        """Simple program: int main() {} """
        input = """Var: x;"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,201))
    
    def test_wrong_miss_close(self):
        """Miss variable"""
        input = """Var: ;"""
        expect = "Error on line 1 col 5: ;"
        self.assertTrue(TestParser.checkParser(input,expect,202))


    def test_203(self):
        input = """Var: a=1,b[a[1]]={1,2,3,True,False};\n"""
        input += """Var: a,b,c,d,safdasfg[True]=24-3*4+4\\4;"""
        expect = """Error on line 1 col 11: a"""

        self.assertTrue(TestParser.checkParser(input, expect, 203))
    def test_204(self):
        input = """Var: a={"strin",True},b=!(2-3)>=.(3\\4-2)\n;"""
        input += """Var: a==1;"""
        input += """Var: a={1},a,c,d,e=---3;"""
        expect = """Error on line 1 col 24: !"""
        self.assertTrue(TestParser.checkParser(input, expect,204))
    def test_205(self):
        input= """Var: a={1},a,c,d,e=3;"""
        input += """Var: a="Streifngd\\ni\\t???2345365fhd";  """

        expect = """successful"""
        self.assertTrue(TestParser.checkParser(input, expect, 205))

    def test_206(self):
        input = """Var: a={1},a,c,d,e=3;"""
        input += """Var: a="Streifngd\\ni\\t???2345365fhd";  """
        input += """Var: a[a[a[1][1]]]="Streifngd\\ni\\t???2345365fhd";  """
        expect = """Error on line 1 col 67: a"""
        self.assertTrue(TestParser.checkParser(input, expect, 206))

    def test_207(self):
        input = """Var: a={1},a,c,d,e=---3;\n"""
        input += """Var: a="Streifngd\\ni\\t???2345365fhd";\n  """
        input += """Var: a[a[a[1][1]]]="Streifngd\\ni\\t???2345365fhd";  """
        input += """Var: a[a[a[1][1]]]=1>2<3>=.235>=232;  """
        input += """Var: a[a[a[1][1]]]="Streifngd\\ni\\t???2345365fhd";  """
        expect = """Error on line 1 col 19: -"""
        self.assertTrue(TestParser.checkParser(input, expect, 207))
    def test_208(self):
        input = """Var: a=!(2.-.2.0001)\.(2.5*3.0+4.7)*(2-3)+(True+a);\n"""
        input += """Var: a=asafsg;\n  """
        input += """Var: a[a[a[1][1]]]="Streifngd\\ni\\t???2345365fhd";  """
        expect = """Error on line 1 col 7: !"""
        self.assertTrue(TestParser.checkParser(input, expect, 208))

    def test_209(self):
        input = """Var: a=function(a-b*c,a*b,!(True),"String");\n"""
        input += """Var: a=function(True,asdsafdd,a(),"String");\n"""
        input += """Var: a=function();\n"""
        expect = """Error on line 1 col 15: ("""
        self.assertTrue(TestParser.checkParser(input, expect, 209))

    def test_210(self):
        input = """Var: a=2354325;\n"""
        input += """Function:a\n"""
        input += """Parameter: a[1]\n"""
        input += """Body:\n"""
        input += """EndBody.\n"""

        expect = """successful"""
        self.assertTrue(TestParser.checkParser(input, expect, 210))

    def test_211(self):
        input = """Var: a=3254;\n"""
        input += """Function:a\n"""
        input += """Parameter: a[1]=1\n"""
        input += """Body:\n"""
        input += """EndBody.\n"""
        expect = """Error on line 3 col 15: ="""
        self.assertTrue(TestParser.checkParser(input, expect, 211))

    def test_212(self):
        input = """Var: a=346656;\n"""
        input += """Function:a\n"""
        input += """Parameter: a[1],a,b,s\n"""
        input += """Body:\n"""
        input += """Var:a=1234345E345;"""
        input += """EndBody.\n"""

        expect = """successful"""
        self.assertTrue(TestParser.checkParser(input, expect, 212))

    def test_213(self):
        input = """Var: a=23435;\n"""
        input += """Function:a\n"""
        input += """Parameter: a[1],a,b,s\n"""
        input += """Body:\n"""
        input += """Var:a=1234345E345"""
        input += """EndBody.\n"""
        expect = """Error on line 5 col 17: EndBody"""
        self.assertTrue(TestParser.checkParser(input, expect, 213))
    def test_214(self):
        input = """Var: a=234;\n"""
        input += """Function  a\n"""
        input += """Parameter: a[1],a,b,s\n"""
        input += """Body:\n"""
        input += """Var:a=1234345E345;"""
        input += """EndBody.\n"""

        expect = """Error on line 2 col 10: a"""
        self.assertTrue(TestParser.checkParser(input, expect,214))
    def test_215(self):
        input = """Var: a=1233;\n"""
        input += """Function:  a\n"""
        input += """Parameter: a[1],a,b,s\n"""
        input += """Body:\n"""
        input += """Var:a=1234345E345;"""
        input += """EndBody\n"""

        expect = """Error on line 6 col 0: <EOF>"""
        self.assertTrue(TestParser.checkParser(input, expect, 215))

    def test_216(self):
        input = """Var: a=function(a-b*c,a*b,!(True),"String");\n"""
        input += """Function:  a\n"""
        input += """Parameter: a[1],a,b,s\n"""
        input += """Body:\n"""
        input += """Var:a=1234345E345;"""
        input += """a=1234345E345;"""
        input += """a_r545="dsfgerefetewfewf";"""
        input += """a[1][a[1]]={1,34325,3E354435,True,False,"sdfret"};"""
        input += """EndBody.\n"""
        expect = """Error on line 1 col 15: ("""
        self.assertTrue(TestParser.checkParser(input, expect, 216))

    def test_217(self):
        input = """Var: a=function(a-b*c,a*b,!(True),"String");\n"""
        input += """Function:  a\n"""
        input += """Parameter: a[1],a,b,s\n"""
        input += """Body:\n"""
        input += """Var:a=1234345E345;"""
        input += """a=1234345E345;"""
        input += """a_r545="dsfgerefetewfewf";"""
        input += """a[1][a[1]]={1,34325,3E354435,TrueFalse,"sdfret"};"""

        input += """EndBody.\n"""
        expect = """Error on line 1 col 15: ("""
        self.assertTrue(TestParser.checkParser(input, expect, 217))

    def test_218(self):
        input = """Var: a=function(a-b*c,a*b,!(True),"String");\n"""
        input += """Function:  a\n"""
        input += """Parameter: a[1],a,b,s\n"""
        input += """Body:\n"""
        input += """Function:a"""
        input += """Body:"""
        input += """EndBody."""
        input += """EndBody.\n"""
        expect = """Error on line 1 col 15: ("""
        self.assertTrue(TestParser.checkParser(input, expect, 218))

    def test_219(self):
        input = """Var: a=function(a-b*c,a*b,!(True),"String");\n"""
        input += """Function:  a\n"""
        input += """Parameter: a[1],a,b,s\n"""
        input += """Body:\n"""
        input += """Function:a"""
        input += """Body:"""
        input += """a=1234345E345;"""
        input += """a_r545="dsfgerefetewfewf";"""
        input += """a[1][a[1]]={1,34325,3E354435,TrueFalse,"sdfret"};"""
        input += """EndBody."""
        input += """a=1234345E345;"""
        input += """a_r545="dsfgerefetewfewf";"""
        input += """a[1][a[1]]={1,34325,3E354435,TrueFalse,"sdfret"};"""
        input += """EndBody.\n"""

        expect = """Error on line 1 col 15: ("""
        self.assertTrue(TestParser.checkParser(input, expect, 219))

    def test_220(self):
        input = """Var: a=function(a-b*c,a*b,!(True),"String");\n"""
        input += """Function:  a\n"""
        input += """Parameter: a[1],a,b,s\n"""
        input += """Body:\n"""
        input += """EndBody.\n"""
        input += """Var: a=function(a-b*c,a*b,!(True),"String");\n"""
        input += """Var: a=function(a-b*c,a*b,!(True),"String");\n"""
        expect = """Error on line 1 col 15: ("""
        self.assertTrue(TestParser.checkParser(input, expect, 220))

    def test_221(self):
        input = """Function:  a\n"""
        input += """Parameter: a[1],a,b,s\n"""
        input += """Body:\n"""
        input += """EndBody.\n"""
        input += """Function:  a\n"""
        input += """Parameter: a[1],a,b,s;\n"""
        input += """Body:\n"""
        input += """EndBody.\n"""
        input += """Function:  a\n"""
        input += """Parameter: a[1],a,b,s;\n"""
        input += """Body:\n"""
        input += """EndBody.\n"""
        expect = """Error on line 6 col 21: ;"""
        self.assertTrue(TestParser.checkParser(input, expect, 221))

    def test_222(self):
        input = """Function:  a\n"""
        input += """Parameter: a[1],a,b,s\n"""
        input += """Body:\n"""
        input += """EndBody.\n"""
        input += """Var: a=function(a-b*c,a*b,!(True),"String");\n"""
        input += """Var: a=function(a-b*c,a*b,!(True),"String");\n"""
        input += """Function:  a\n"""
        input += """Parameter: a[1],a,b,s;\n"""
        input += """Body:\n"""
        input += """EndBody.\n"""
        input += """Var: a=function(a-b*c,a*b,!(True),"String");\n"""
        input += """Var: a=function(a-b*c,a*b,!(True),"String");\n"""
        input += """Function:  a\n"""
        input += """Parameter: a[1],a,b,s;\n"""
        input += """Body:\n"""
        input += """EndBody.\n"""
        input += """Var: a=function(a-b*c,a*b,!(True),"String");\n"""
        input += """Var: a=function(a-b*c,a*b,!(True),"String");\n"""
        expect = """Error on line 5 col 0: Var"""
        self.assertTrue(TestParser.checkParser(input, expect, 222))

    def test_223(self):
        input = """Function:  a\n"""
        input += """Parameter: a[1],a,b,s\n"""
        input += """Body:\n"""
        input += """EndBody.\n"""
        input += """Var: a=function(a-b*c,a*b,!(True),"String");\n"""
        input += """Var: a=function(a-b*c,a*b,!(True),"String");\n"""
        input += """a=function(a-b*c,a*b,!(True),"String");\n"""
        input += """a=function(a-b*c,a*b,!(True),"String");\n"""

        input += """Function:  a\n"""
        input += """Parameter: a[1],a,b,s\n"""
        input += """Body:\n"""
        input += """EndBody.\n"""
        input += """Var: a=function(a-b*c,a*b,!(True),"String");\n"""
        input += """Var: a=function(a-b*c,a*b,!(True),"String");\n"""
        input += """Function:  a\n"""
        input += """Parameter: a[1],a,b,s;\n"""
        input += """Body:\n"""
        input += """EndBody.\n"""
        input += """Var: a=function(a-b*c,a*b,!(True),"String");\n"""
        input += """Var: a=function(a-b*c,a*b,!(True),"String");\n"""
        expect = """Error on line 5 col 0: Var"""
        self.assertTrue(TestParser.checkParser(input, expect, 223))
    def test_224(self):
        input = """a=function(a-b*c,a*b,!(True),"String");\n"""
        input += """a=function(a-b*c,a*b,!(True),"String");\n"""
        input += """Var: a=function(a-b*c,a*b,!(True),"String");\n"""
        input += """Var: a=function(a-b*c,a*b,!(True),"String");\n"""
        input += """Function:  a\n"""
        input += """Parameter: a[1],a,b,s;\n"""
        input += """Body:\n"""
        input += """EndBody.\n"""
        expect = """Error on line 1 col 0: a"""
        self.assertTrue(TestParser.checkParser(input, expect,224))
    def test_225(self):
        input = """a=function(a-b*c,a*b,!(True),"String");\n"""
        input += """a=function(a-b*c,a*b,!(True),"String");\n"""
        input += """Var: a="dsfdsrty"\n"""
        input += """Var: a=function(a-b*c,a*b,!(True),"String");\n"""
        input += """Function:  a\n"""
        input += """Parameter: a[1],a,b,s;\n"""
        input += """Body:\n"""
        input += """EndBody.\n"""
        expect = """Error on line 1 col 0: a"""
        self.assertTrue(TestParser.checkParser(input, expect, 225))

    def test_226(self):
        input = """Function: function\n"""
        input += """	Parameter:a,dsfdg,sdtgfr,a__rewrf,a[a[2-3*4-25--4325]]\n"""
        input += """	Body:\n"""
        input += """		If (a-243*325>b+32546*545) Then\n"""
        input += """		a=b-23454;\n"""
        input += """		nb=24345;\n"""
        input += """		EndIf.\n"""
        input += """	EndBody."""
        expect = """successful"""
        self.assertTrue(TestParser.checkParser(input, expect, 226))

    def test_227(self):
        input = """Function: function\n"""
        input += """	Parameter:a,dsfdg,sdtgfr,a__rewrf,a[a[2-3*4-25--4325]]\n"""
        input += """	Body:\n"""
        input += """		If (a-243*325>b+32546*545) Then\n"""
        input += """		a=b-23454;\n"""
        input += """		nb=24345;\n"""
        input += """		Else\n"""
        input += """		nb=24345;\n"""
        input += """		nb=24345;\n"""
        input += """		EndIf.\n"""
        input += """	EndBody."""
        expect = """successful"""
        self.assertTrue(TestParser.checkParser(input, expect, 227))

    def test_228(self):
        input = """Function: function\n"""
        input += """	Parameter:a,dsfdg,sdtgfr,a__rewrf,a[a[2-3*4-25--4325]]\n"""
        input += """	Body:\n"""
        input += """		If (a-243*325>b+32546*545) Then\n"""
        input += """		a=b-23454;\n"""
        input += """		nb=24345;\n"""
        input += """		Else\n"""
        input += """		If (a-243*325>b+32546*545) Then\n"""
        input += """		a=b-23454;\n"""
        input += """		nb=24345;\n"""
        input += """		EndIf.\n"""
        input += """		EndIf.\n"""

        input += """	EndBody."""
        expect = """successful"""
        self.assertTrue(TestParser.checkParser(input, expect, 228))

    def test_229(self):
        input = """Function: function\n"""
        input += """	Parameter:a,dsfdg,sdtgfr,a__rewrf,a[a[2-3*4-25--4325]]\n"""
        input += """	Body:\n"""
        input += """		If (a-243*325>b+32546*545) Then\n"""
        input += """		a=b-23454;\n"""
        input += """		nb=24345;\n"""
        input += """		Else\n"""
        input += """		If (a-243*325>b+32546*545) Then\n"""
        input += """		a=b-23454;\n"""
        input += """		nb=24345;\n"""
        input += """		EndIf.\n"""
        expect = """Error on line 12 col 0: <EOF>"""
        self.assertTrue(TestParser.checkParser(input, expect, 229))

    def test_230(self):
        input = """Function: function\n"""
        input += """	Parameter:a,dsfdg,sdtgfr,a__rewrf,a[a[2-3*4-25--4325]]\n"""
        input += """	Body:\n"""
        input += """		If (a-243*325>b+32546*545) Then\n"""
        input += """		a=b-23454;\n"""
        input += """		nb=24345;\n"""
        input += """		ElseIf a>2354353545-2356536+3456\n"""
        input += """		Then\n"""
        input += """		a=23564546*23467-235444444444444444444444;\n"""
        input += """		ElseIf a>2354353545-2356536+3456\n"""
        input += """		Then\n"""
        input += """		a=23564546*23467-235444444444444444444444;\n"""
        input += """		Else\n"""
        input += """		If (a-243*325>b+32546*545) Then\n"""
        input += """		a=b-23454;\n"""
        input += """		nb=24345;\n"""
        input += """		EndIf.\n"""
        input += """		EndIf.\n"""
        input += """		EndBody.\n"""
        expect = """successful"""
        self.assertTrue(TestParser.checkParser(input, expect, 230))

    def test_231(self):
        input = """Function: function\n"""
        input += """	Parameter:a,dsfdg,sdtgfr,a__rewrf,a[a[2-3*4-25--4325]]\n"""
        input += """	Body:\n"""
        input += """		If (a-243*325>b+32546*545) Then\n"""
        input += """		a=b-23454;\n"""
        input += """		nb=24345;\n"""
        input += """		ElseIf a>2354353545-2356536+3456\n"""
        input += """		Then\n"""
        input += """		If a>tfewtr\n"""
        input += """		Then\n"""
        input += """		EndIf.\n"""
        input += """		ElseIf a>2354353545-2356536+3456\n"""
        input += """		Then\n"""
        input += """		a=23564546*23467-235444444444444444444444;\n"""
        input += """		Else\n"""
        input += """		If (a-243*325>b+32546*545) Then\n"""
        input += """		a=b-23454;\n"""
        input += """		nb=24345;\n"""
        input += """		EndIf.\n"""
        input += """		EndIf.\n"""
        input += """		EndBody.\n"""
        expect = """successful"""
        self.assertTrue(TestParser.checkParser(input, expect, 231))

    def test_232(self):
        input = """Function: function\n"""
        input += """	Parameter:a,dsfdg,sdtgfr,a__rewrf,a[a[2-3*4-25--4325]]\n"""
        input += """	Body:\n"""
        input += """		If (a-243*325>b+32546*545) Then\n"""
        input += """		a=b-23454;\n"""
        input += """		nb=24345;\n"""
        input += """		ElseIf a>2354353545-2356536+3456\n"""
        input += """		Then\n"""
        input += """		If a>tfewtr\n"""
        input += """		Then\n"""
        input += """		a=245*2354;\n"""
        input += """		Var:a=213546*3456;"""
        input += """		Else\n"""
        input += """		a=235436;\n"""
        input += """		EndIf.\n"""
        input += """		ElseIf a>2354353545-2356536+3456\n"""
        input += """		Then\n"""
        input += """		a=23564546*23467-235444444444444444444444;\n"""
        input += """		Else\n"""
        input += """		If (a-243*325>b+32546*545) Then\n"""
        input += """		a=b-23454;\n"""
        input += """		nb=24345;\n"""
        input += """		EndIf.\n"""
        input += """		EndIf.\n"""
        input += """		EndBody.\n"""
        expect = """Error on line 12 col 2: Var"""
        self.assertTrue(TestParser.checkParser(input, expect, 232))

    def test_233(self):
        input = """Function: function\n"""
        input += """	Parameter:a,dsfdg,sdtgfr,a__rewrf,a[a[2-3*4-25--4325]]\n"""
        input += """	Body:\n"""
        input += """		If (a-243*325>b+32546*545) Then\n"""
        input += """		a=b-23454;\n"""
        input += """		nb=24345;\n"""
        input += """		ElseIf a>2354353545-2356536+3456\n"""
        input += """		Then\n"""
        input += """		If a>tfewtr\n"""
        input += """		Then\n"""
        input += """		a=245*2354;\n"""
        input += """		Var:a=213546*3456;"""
        input += """		Else\n"""
        input += """		a=235436;\n"""
        input += """		EndIf.\n"""
        input += """		ElseIf a>2354353545-2356536+3456\n"""
        input += """		a=23564546*23467-235444444444444444444444;\n"""
        input += """		Else\n"""
        input += """		If (a-243*325>b+32546*545) Then\n"""
        input += """		a=b-23454;\n"""
        input += """		nb=24345;\n"""
        input += """		EndIf.\n"""
        input += """		EndIf.\n"""
        input += """		EndBody.\n"""
        expect = """Error on line 12 col 2: Var"""
        self.assertTrue(TestParser.checkParser(input, expect, 233))
    def test_234(self):
        input = """Function: function\n"""
        input += """	Parameter:a,dsfdg,sdtgfr,a__rewrf,a[a[2-3*4-25--4325]]\n"""
        input += """	Body:\n"""
        input += """		If (a-243*325>b+32546*545) Then\n"""
        input += """		a=b-23454;\n"""
        input += """		nb=24345;\n"""
        input += """		ElseIf a>2354353545-2356536+3456\n"""
        input += """		Then\n"""
        input += """		If a>tfewtr\n"""
        input += """		Then\n"""
        input += """		a=245*2354;\n"""
        input += """		Var:a=213546*3456;"""
        input += """		Else\n"""
        input += """		a=235436;\n"""
        input += """		EndIf.\n"""
        input += """		ElseIf a>2354353545-2356536+3456\n"""
        input += """		a=23564546*23467-235444444444444444444444;\n"""
        input += """		Else\n"""
        input += """		If (a-243*325>b+32546*545) Then\n"""
        input += """		a=b-23454;\n"""
        input += """		nb=24345;\n"""
        input += """		EndIf.\n"""
        input += """		EndBody.\n"""
        expect = """Error on line 12 col 2: Var"""
        self.assertTrue(TestParser.checkParser(input, expect,234))
    def test_235(self):
        input = """Function: ror\n"""
        input += """	Body:\n"""
        input += """		For(i=1,i>=.23,2143)\n"""
        input += """		Do\n"""
        input += """			hsadsa = huhsadasfu;\n"""
        input += """			huhasdu = hihasdasi || True;\n"""
        input += """		EndFor.\n"""
        input += """	EndBody."""
        expect = """successful"""
        self.assertTrue(TestParser.checkParser(input, expect, 235))

    def test_236(self):
        input = """Function: ror\n"""
        input += """	Body:\n"""
        input += """		For(i=1,i>=.23,2-35*345>=.2143)\n"""
        input += """			hsadsa = huhsadasfu;\n"""
        input += """			huhasdu = hihasdasi || True;\n"""
        input += """		EndFor.\n"""
        input += """	EndBody."""
        expect = """Error on line 4 col 3: hsadsa"""
        self.assertTrue(TestParser.checkParser(input, expect, 236))

    def test_237(self):
        input = """Function: ror\n"""
        input += """	Body:\n"""
        input += """		For(,,)\n"""
        input += """		Do\n"""
        input += """			hsadsa = huhsadasfu;\n"""
        input += """			huhasdu = hihasdasi || True;\n"""
        input += """		EndFor.\n"""
        input += """	EndBody."""
        expect = """Error on line 3 col 6: ,"""
        self.assertTrue(TestParser.checkParser(input, expect, 237))

    def test_238(self):
        input = """Function: ror\n"""
        input += """	Body:\n"""
        input += """		For(i=1,i>=.23,2143)\n"""
        input += """		Do\n"""
        input += """		For(i=1,i>=.23,2143)\n"""
        input += """		Do\n"""
        input += """		EndFor."""
        input += """			hsadsa = huhsadasfu;\n"""
        input += """			huhasdu = hihasdasi || True;\n"""
        input += """		EndFor.\n"""
        input += """	EndBody."""
        expect = """successful"""
        self.assertTrue(TestParser.checkParser(input, expect, 238))

    def test_239(self):
        input = """Function: ror\n"""
        input += """	Body:\n"""
        input += """		For(i=1,i>=.23,2143)\n"""
        input += """		Do\n"""
        input += """		For(i=1,i>=.23,2143)\n"""
        input += """		Do\n"""
        input += """		If a>bdfg Then\n"""
        input += """		Do\n"""
        input += """		EndIf.\n"""
        input += """		EndFor."""
        input += """			hsadsa = huhsadasfu;\n"""
        input += """			huhasdu = hihasdasi || True;\n"""
        input += """		EndFor.\n"""
        input += """	EndBody."""
        expect = """Error on line 9 col 2: EndIf"""
        self.assertTrue(TestParser.checkParser(input, expect, 239))

    def test_240(self):
        input = """Function: ror\n"""
        input += """	Body:\n"""
        input += """		For(i=1,i>=.23,2143)\n"""
        input += """		Do\n"""
        input += """		For(i=1,i>=.23,2143)\n"""
        input += """		Do\n"""
        input += """		Var:cdsfd={wqrwt};"""
        input += """		a=3246534*32565;\n"""
        input += """		EndFor."""
        input += """			hsadsa = huhsadasfu;\n"""
        input += """			huhasdu = hihasdasi || True;\n"""
        input += """		EndFor.\n"""
        input += """	EndBody."""
        expect = """successful"""
        self.assertTrue(TestParser.checkParser(input, expect, 240))

    def test_241(self):
        input = """Function: ror\n"""
        input += """	Body:\n"""
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
        input += """	EndBody."""
        expect = """successful"""
        self.assertTrue(TestParser.checkParser(input, expect, 241))

    def test_242(self):
        input = """Function: ror\n"""
        input += """	Body:\n"""
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
        input += """	EndBody."""
        expect = """Error on line 16 col 1: EndBody"""
        self.assertTrue(TestParser.checkParser(input, expect, 242))

    def test_243(self):

        input = """		For(i=1,i>=.23,2143)\n"""
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

        expect = """Error on line 1 col 2: For"""
        self.assertTrue(TestParser.checkParser(input, expect, 243))
    def test_244(self):
        input = """Function: ror\n"""
        input += """	Body:\n"""
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
        input += """	EndBody."""
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
        expect = """Error on line 16 col 1: EndBody"""
        self.assertTrue(TestParser.checkParser(input, expect,244))
    def test_245(self):
        input = """Function: testwhite\n"""
        input += """	Body:\n"""
        input += """		While (a>wfwrg )Do\n"""
        input += """			hdsfihi = huhdsfu;\n"""
        input += """			hsdfuhdsfu = hidsfhi || True;\n"""
        input += """		EndWhile.\n"""
        input += """	EndBody."""
        expect = """successful"""
        self.assertTrue(TestParser.checkParser(input, expect, 245))

    def test_246(self):
        input = """Function: testwhite\n"""
        input += """	Body:\n"""
        input += """		While (a>wfwrg )Do\n"""
        input += """			hdsfihi = huhdsfu;\n"""
        input += """			hsdfuhdsfu = hidsfhi || True;\n"""
        input += """		EndWhile\n"""
        input += """	EndBody."""
        expect = """Error on line 7 col 1: EndBody"""
        self.assertTrue(TestParser.checkParser(input, expect, 246))

    def test_247(self):
        input = """Function: testwhite\n"""
        input += """	Body:\n"""
        input += """		While (a>wfwrg )\n"""
        input += """			hdsfihi = huhdsfu;\n"""
        input += """			hsdfuhdsfu = hidsfhi || True;\n"""
        input += """		EndWhile.\n"""
        input += """	EndBody."""
        expect = """Error on line 4 col 3: hdsfihi"""
        self.assertTrue(TestParser.checkParser(input, expect, 247))

    def test_248(self):
        input = """Function: testwhite\n"""
        input += """	Body:\n"""
        input += """		While asf (a>wfwrg )Do\n"""
        input += """			hdsfihi = huhdsfu;\n"""
        input += """			hsdfuhdsfu = hidsfhi || True;\n"""
        input += """		EndWhile.\n"""
        input += """	EndBody."""
        expect = """successful"""
        self.assertTrue(TestParser.checkParser(input, expect, 248))

    def test_249(self):
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
        expect = """successful"""
        self.assertTrue(TestParser.checkParser(input, expect, 249))

    def test_250(self):
        input = """Function: testwhite\n"""
        input += """	Body:\n"""
        input += """		While ( )Do\n"""
        input += """			hdsfihi = huhdsfu;\n"""
        input += """			hsdfuhdsfu = hidsfhi || True;\n"""
        input += """		EndWhile.\n"""
        input += """	EndBody."""
        expect = """Error on line 3 col 10: )"""
        self.assertTrue(TestParser.checkParser(input, expect, 250))

    def test_251(self):
        input = """Function: testwhite\n"""
        input += """	Body:\n"""
        input += """		While ( a)Do\n"""
        input += """			hdsfihi = huhdsfu;\n"""
        input += """			hsdfuhdsfu = hidsfhi || True;\n"""
        input += """		EndDo.\n"""
        input += """	EndBody."""
        expect = """Error on line 6 col 2: EndDo"""
        self.assertTrue(TestParser.checkParser(input, expect, 251))

    def test_252(self):
        input = """Function: testwhite\n"""
        input += """	Body:\n"""
        input += """		While (a>asf,b>sag,c )Do\n"""
        input += """			hdsfihi = huhdsfu;\n"""
        input += """			hsdfuhdsfu = hidsfhi || True;\n"""
        input += """		EndWhile.\n"""
        input += """	EndBody."""
        input += """"""
        expect = """Error on line 3 col 16: >"""
        self.assertTrue(TestParser.checkParser(input, expect, 252))

    def test_253(self):
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
        expect = """Error on line 3 col 10: )"""
        self.assertTrue(TestParser.checkParser(input, expect, 253))
    def test_254(self):
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
        expect = """Error on line 16 col 1: EndBody"""
        self.assertTrue(TestParser.checkParser(input, expect,254))
    def test_255(self):
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
        expect = """Error on line 15 col 2: EndWhile"""
        self.assertTrue(TestParser.checkParser(input, expect, 255))

    def test_256(self):
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
        expect = """Error on line 2 col 11: ;"""
        self.assertTrue(TestParser.checkParser(input, expect, 256))

    def test_257(self):
        input = """Function: testdowhile\n"""
        input += """	Body:\n"""
        input += """		Do\n"""
        input += """			hisafdhi = husadhu;\n"""
        input += """			husdhu = hihsadi || True;\n"""
        input += """			sadhuhu = hisadhi;\n"""
        input += """			ansdothersadstatesdment();\n"""
        input += """		While(a>324)EndDo.\n"""
        input += """	EndBody."""
        expect = """successful"""
        self.assertTrue(TestParser.checkParser(input, expect, 257))

    def test_258(self):
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
        expect = """successful"""
        self.assertTrue(TestParser.checkParser(input, expect, 258))

    def test_259(self):
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
        expect = """successful"""
        self.assertTrue(TestParser.checkParser(input, expect, 259))

    def test_260(self):
        input = """Function: testdowhile\n"""
        input += """	Body:\n"""
        input += """		Do\n"""
        input += """			hisafdhi = husadhu;\n"""
        input += """			husdhu = hihsadi || True;\n"""
        input += """			sadhuhu = hisadhi;\n"""
        input += """			ansdothersadstatesdment();\n"""
        input += """		While()EndDo.\n"""
        input += """	EndBody."""
        expect = """Error on line 8 col 8: )"""
        self.assertTrue(TestParser.checkParser(input, expect, 260))

    def test_261(self):
        input = """Function: testdowhile\n"""
        input += """	Body:\n"""
        input += """		Do.\n"""
        input += """			hisafdhi = husadhu;\n"""
        input += """			husdhu = hihsadi || True;\n"""
        input += """			sadhuhu = hisadhi;\n"""
        input += """			ansdothersadstatesdment();\n"""
        input += """		While()EndDo\n"""
        input += """	EndBody."""
        expect = """Error on line 3 col 4: ."""
        self.assertTrue(TestParser.checkParser(input, expect, 261))

    def test_262(self):
        input = """Function: testdowhile\n"""
        input += """	Body:\n"""
        input += """		While(a) Do\n"""
        input += """			hisafdhi = husadhu;\n"""
        input += """			husdhu = hihsadi || True;\n"""
        input += """			sadhuhu = hisadhi;\n"""
        input += """			ansdothersadstatesdment();\n"""
        input += """		While()EndDo\n"""
        input += """	EndBody."""
        input += """"""
        expect = """Error on line 8 col 8: )"""
        self.assertTrue(TestParser.checkParser(input, expect, 262))

    def test_263(self):
        input = """Function: testdowhile\n"""
        input += """	Body:\n"""
        input += """		While(a) Do EndDo.\n"""
        input += """			hisafdhi = husadhu;\n"""
        input += """			husdhu = hihsadi || True;\n"""
        input += """			sadhuhu = hisadhi;\n"""
        input += """			ansdothersadstatesdment();\n"""
        input += """		While()EndDo\n"""
        input += """	EndBody."""
        input += """"""
        expect = """Error on line 3 col 14: EndDo"""
        self.assertTrue(TestParser.checkParser(input, expect, 263))
    def test_264(self):
        input = """Function: testdowhile\n"""
        input += """	Body:\n"""
        input += """		While(a) Do EndIf.\n"""
        input += """			hisafdhi = husadhu;\n"""
        input += """			husdhu = hihsadi || True;\n"""
        input += """			sadhuhu = hisadhi;\n"""
        input += """			ansdothersadstatesdment();\n"""
        input += """		While()EndDo\n"""
        input += """	EndBody."""
        expect = """Error on line 3 col 14: EndIf"""
        self.assertTrue(TestParser.checkParser(input, expect,264))
    def test_265(self):
        input = """Function: testdowhile\n"""
        input += """	Body:\n"""
        input += """		While(a) Do While(a)EndDo.\n"""
        input += """			hisafdhi = husadhu;\n"""
        input += """			husdhu = hihsadi || True;\n"""
        input += """			sadhuhu = hisadhi;\n"""
        input += """			ansdothersadstatesdment();\n"""
        input += """		While()EndDo\n"""
        input += """	EndBody."""
        expect = """Error on line 3 col 22: EndDo"""
        self.assertTrue(TestParser.checkParser(input, expect, 265))

    def test_266(self):
        input = """Function: testbreak\n"""
        input += """	Body:\n"""
        input += """		Do\n"""
        input += """			hisafdhi = husadhu;\n"""
        input += """			husdhu = hihsadi || True;\n"""
        input += """			sadhuhu = hisadhi;\n"""
        input += """			ansdothersadstatesdment();\n"""
        input += """			Break;\n"""

        input += """		While(a>324)EndDo.\n"""
        input += """	EndBody."""
        expect = """successful"""
        self.assertTrue(TestParser.checkParser(input, expect, 266))

    def test_267(self):
        input = """Function: testbreak\n"""
        input += """	Body:\n"""
        input += """		Do\n"""
        input += """			hisafdhi = husadhu;\n"""
        input += """			husdhu = hihsadi || True;\n"""
        input += """			sadhuhu = hisadhi;\n"""
        input += """			ansdothersadstatesdment();\n"""
        input += """			Break a;\n"""
        input += """		While(a>324)EndDo.\n"""
        input += """	EndBody."""
        expect = """Error on line 8 col 9: a"""
        self.assertTrue(TestParser.checkParser(input, expect, 267))

    def test_268(self):
        input = """Function: testcontinue\n"""
        input += """	Body:\n"""
        input += """		Do\n"""
        input += """			hisafdhi = husadhu;\n"""
        input += """			husdhu = hihsadi || True;\n"""
        input += """			sadhuhu = hisadhi;\n"""
        input += """			ansdothersadstatesdment();\n"""
        input += """			Continue ;\n"""
        input += """		While(a>324)EndDo.\n"""
        input += """	EndBody."""
        expect = """successful"""
        self.assertTrue(TestParser.checkParser(input, expect, 268))

    def test_269(self):
        input = """			Continue;\n"""
        input += """Function: testcontinue\n"""
        input += """	Body:\n"""
        input += """		Do\n"""
        input += """			hisafdhi = husadhu;\n"""
        input += """			husdhu = hihsadi || True;\n"""
        input += """			sadhuhu = hisadhi;\n"""
        input += """			ansdothersadstatesdment();\n"""
        input += """			Continue\n"""
        input += """		While(a>324)EndDo.\n"""

        input += """	EndBody."""

        expect = """Error on line 1 col 3: Continue"""
        self.assertTrue(TestParser.checkParser(input, expect, 269))

    def test_270(self):
        input = """
                Var: ra, dst, csv;
                    Function: disefn_tssicsh_chsu_svsi_hisnh_tsrson
                        Body:
                        writselssn("TIssNHs sDsIENs TICssH & CHU VI HIsNH TRsONs:");
                        wrsiteln("--------------------------------------------------");
                        wrsite ("Nhap ban kinh R= "); readln(r);
                        dst = pi*r*r;
                        csv = 2*pi*r;
                        wristeln("Dsien dsftsich sadashisadnh trasdon la:sd", dsadt);
                        wristesln("Chu savid hinh tsadsdron lasd:sd", csv);
                    EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 270))

    def test_271(self):
        input = """
                Var: r, dt, cv;
                Function: giais_phssuong_trissnh_bac_nsshat
                    Body:
                        wrsiteln("GIAI PsHUONG sTRIsNsH BsAC NHsAT: AX + B = 0");
                        wsriteln("ss-------------------ss---------s---------------s-------s-----");
                        wsrite ("Nhsap sa = "); resadln(a);
                        wriste ("Nshap b s= "); resadln(b);
                        If (sa==0) Then
                            If (b==0) Then wristeln(" Phuosng tsrinh sco vo sso nghissem");
                            Else writesln("Phuosng tring vo s");
                            EndIf.
                        Else
                            x = -b\\a;
                            writeln("Phsuong trsinh co nghsiem kesp: ", x);
                        EndIf.
                    EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 271))

    def test_272(self):
        input = """
                Var: sa,sb,sc;
                Function: masin
                    Body:
                        If a Then b = cs;
                        ElseIf as Then b = cs;
                        ElseIf as Then b = sc;
                        ElseIf as b = cs;
                        EndIf.
                    EndBody."""
        expect = "Error on line 8 col 34: b"
        self.assertTrue(TestParser.checkParser(input, expect, 272))

    def test_273(self):
        input = """
                Var: a, b, c, d, temp;
                Function: main
                    Body:
                        writeLn("Hasy nhap sso can sdoi tu hes 10 sang she 16");
                        readLn(n);
                        k = n;
                        While k>0 Do
                            If k % 16 == 0 Then a = 0 + temp ;
                            ElseIf k % 16 == 1 b = 1 + temp;          ** missing Then **
                            ElseIf k % 16 == 2 Then c = 2 + temp;
                            Else If k % 16 == 3 Then d = "3" + temp;
                        EndWhile.
                    EndBody."""
        expect = "Error on line 10 col 47: b"
        self.assertTrue(TestParser.checkParser(input, expect, 273))

    def test_274(self):
        input = """
                Var: as, bs = 0, cs, ds, tesmp;
                Function: masin
                    Body:
                        While( a == 4) && (b == 6+3+8-9-5 || 2) Do
                            tesmp = 44;
                        EndWhile.
                    EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 274))

    def test_275(self):
        input = """
                Var: a, b = 0, c, d, temsp;
                Function: masin
                    Body:
                        While(a==4) && c == 4) Do
                            For (i = 4, True, 3+3) Do
                                For (i = 5, False, 9+9) Do
                                    If(a == 3) && (a == True) Then
                                        e = 5;
                                    EndIf.
                                EndFor.
                            EndFor.
                        EndWhile.
                    EndBody."""
        expect = "Error on line 5 col 45: )"
        self.assertTrue(TestParser.checkParser(input, expect, 275))

    def test_276(self):
        input = """
                Var: a, b = 0, c, d, temp;
                Function: main
                    Body:
                        While(a==5) && (c == 5) Do
                            For (i = 5, True, 5+5) Do
                                For (i = 6, False, 6+6) Do
                                    If(a == 3) && (a == True) Then
                                        a = ((6 + 6 * 6 - 6) \\ 7) ;
                                    EndIf.
                                EndFor.
                            EndFor.
                        EndWhile.
                    EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 276))

    def test_277(self):
        input = """
                Var: a, b = 0, c, d, tedmp;
                Function: madin
                    Body:
                        a = b \\. 32 * n \\. 43. % 53 || g && 2 =/= 93 != 34 % 32;
                    EndBody."""
        expect = "Error on line 5 col 69: !="
        self.assertTrue(TestParser.checkParser(input, expect, 277))

    def test_278(self):
        input = """
                Var: st3r1, st3r2, str33, str43;
                Function: main
                    Body:
                        str1 = "H3ello ";
                        str2 = "The3re!";
                        ** c3opy str1 int33o str3 **
                        str3 = str1;
                        wr3iteln("appen3dstr( str3, str1) : ", str3 );
                        ** conc3atenates str1 and3 str2 **
                        appen3dstr(str1, st3r2);
                        writeln("appen3dstr( str31, st3r2) " , str1);
                        str4 = str1 + str2;
                        writeln("3Now st3r4 is: ", st3r4);
                        ** total leng3hth of st3r4 af3ter con3catenation **
                        writeln("Len3gth of3 the f3inal s3tring3 str34: ", len);
                    EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 278))

    def test_279(self):
        input = """
                Var: i, j;
                Function: main
                    Body:
                        For (i = 2 , i < 20, 5) Do
                            For (j = 2, j <= 50, i) Do
                                If (i % j == 0) Then
                                    Break; ** if factor found, not prime **
                                EndIf.
                                If (j == i) Then
                                    writeln(i , " is prime" );
                                EndIf.
                            EndFor.
                        EndFor.
                    EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 279))

    def test_280(self):
        input = """
                Function: foo
                    Parameter: sum, n, i
                    Body:
                        writeLn("Hay nhap so");
                        readLn(n);
                        writeLn("Muon tinh tong bao nhieu chu so tan cung");
                        readLn(k);
                        ** Tinh tong k chu so tan cung **   
                        i = 1;
                        While i <= k Do
                            sum = sum + n % 10;
                            n = n \\ 10;
                            inc(i);
                        EndWhile.

                        ** In ket qua**
                        writeLn("Tong ", k, " chu so tan cung trong so ", n, " la ", sum);
                    EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 280))

    def test_281(self):
        input = """
                Function: foo
                    Parameter: a, b, c, x1, x2, d
                    Body:
                        While(1) Do
                            write("Nhap cac he so a, b, c: ");
                            readln(a,b,c);
                            If(a!=0) Then Break;
                            EndIf.
                        EndWhile.
                        d = sqr(b) - 4 * a * c;
                        If (d < 0) Then write("Phuong trinh vo nghiem!");
                        Else
                            x1 = (-b - sqrt(d)) \\ (2 * a);
                            x2 = (-b + sqrt(d)) \\ (2 * a);
                            If (d == 0) Then writeln("Phuong trinh co nghiem kep x = ",x1);
                            Else writeln("Phuong trinh co 2 nghiem phan biet: ",x1,x2);
                            EndIf.
                        EndIf.
                        readln();
                    EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 281))

    def test_282(self):
        input = """
                Function: foo
                    Parameter: a, b
                    Body:
                        wridsfdte("Nhap vafsdfdo so a:");                        ** Thong bafsdo nhap lieu **
                        resfadln(a);                                      ** Nhap gtfsdri a (voi &a, la lay d/c bien a,) **
                        wrdfsdite("Nhap vsfao so b:");                        ** Thong bsfdao nhap lieu **
                        wesfadln(b);                                      ** Nhap gtrdfdi b (voi &b, la lay d/c bien b,) **
                        For (i = a, i < 100, i) Do
                            If((a % i == 0) && (b % i == 0)) Then        ** Kiem trdfsa a, b co chia het **
                                Break;
                            EndIf.
                        EndFor.
                        wridsfteln("USCdfLN (",a,",",b,"):", i);              ** Xuat kedfst qua USCLN(a, b) **
                        wridfsteln("BSdfsCNN (",a,",",b,"):", a*b \\ i);       ** Xuat ketdfs qua USCLN(a, b) **
                        readln();
                    EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 282))

    def test_283(self):
        input = """
                Function: foo
                    Parameter: a, b, c 
                    Body:
                        writeln("BAI TOsdfAN TAM fdsGIAC:");
                        writeln("---------------------------------");
                        write("nhdfap a =");readfsdln(a);
                        write("nshap b =");redfsadln(b);
                        write("nhsdfap c =");readln(c);
                        If ((a+b)>c) && ((b+c)>a) && ((a+c)>b) Then
                            p = (a+b+c)\\2;
                            s = sqdfdrt(p*(p-a)*(p-b)*(p-c));
                            writdsfeln("Chu vi tam giac:",2*p);
                            writdeln("Dien tsdfich tam giac:",s);
                        Else wridfsteln(a,", ", b,", ", c, " khong dfphai la ba canh cua dsfdftam giac");
                        EndIf.
                        readsfdln();
                    EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 283))

    def test_284(self):
        input = """
                Var: k, i;
                Function: ok
                    Parameter: ok 
                    Body:
                        ok = True;
                        For (k = 2, k < i\\2, 10) Do
                            If (cdsfopy(s,i-2*k+1,k) == codsfsdpy(s,i-k+1,k)) Then
                                ok = false;
                                exidfsdsft();
                            EndIf.
                        EndFor.
                    EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 284))

    def test_285(self):
        input = """
                Var: f1, f2, sum;
                Function: fibo
                    Body:
                        If x <= 2 Then
                            sum = 1;
                        Else
                            sum = fidfsbo(x-2) + fidsfbo(x-1);
                        EndIf.
                    EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 285))

    def test_286(self):
        input = """
                **Thdfis is msdfssv
                * 1814764
                **
                Var: mssdfsv = 1814764, {"Ndfame: Ngusdfyen Thdsfe Viedsfn"};"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 286))

    def test_287(self):
        input = """
            Var: a={1}, b=9 ,c[10]={1,2,3};
            Function: foo
            Parameter: i,j,a,b
                Body:
                    While True Do
                        Var: a,c,d;
                        ad = a[fodsfo-a[a[i]+fdsfoo(chedfsck[a[b[j]]])]];
                    EndWhile.
                EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 287))

    def test_288(self):
        input = """
                Function: tesdfst_If_Stmdsf_4\n
                    Body:\n
                        If m == n Then\n
                            m = n;\n
                            n = m || True;\n
                        ElseIf m == vidfsen Then\n
                            n = m;\n
                            anosfther_stdsfdatement();\n
                        Else\n
                            tedsfst();\n
                            Return;\n
                        EndIf.\n
                    EndBody."""
        expect = """successful"""
        self.assertTrue(TestParser.checkParser(input, expect, 288))

    def test_289(self):
        input = """
                Function: tesdst_For_fdsStm_1\n
                    Body:\n
                        For ( i = 0 , i < 10 , 2) Do\n
                            If m == ms Then\n
                                dosdfsomething();\n
                            EndIf.\n
                        EndFor.\n
                    EndBody."""
        expect = """successful"""
        self.assertTrue(TestParser.checkParser(input, expect, 289))

    def test_290(self):
        input = """
                Function: test_Wfdhile_Stmsd_1\n
                    Body:\n
                        While i < 10 Do\n
                            sdome();\n
                            statedsfment();\n
                            here();\n
                            i = di + 1;\n
                        EndWhile.\n
                    EndBody.\n"""
        expect = """successful"""
        self.assertTrue(TestParser.checkParser(input, expect, 290))

    def test_291(self):
        input = """
                Function: test_Wsdfhile_Stm_2\n
                    Body:\n
                        While a < 10 Do\n
                            dosomedfsthing();\n
                        EndWhile.\n
                        While b < 10 Do\n
                            dosomdfsething();\n
                        EndWhile.\n
                        While c < 10 Do\n
                            dosometdsfhing();\n
                        EndWhile.\n
                    EndBody.\n"""
        expect = """successful"""
        self.assertTrue(TestParser.checkParser(input, expect, 291))

    def test_292(self):
        input = """
                Function: madsfin
                    Parameter: adfsrgc, argdsfv
                    Body:
                        Break;
                        Return 0;
                    EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 292))

    def test_293(self):
        input = """
                Function: testdsf_If_Sdfstm_5\n
                    Body:\n
                        If m == n Then\n
                            m = n;\n
                            n = m || True;\n
                            For (i = 0, i < m, 4) Do\n
                                dodfssomething();\n
                            EndFor. 
                        ElseIf m == viendfs Then\n
                            n = m;\n
                            another_sdfstatement();\n
                        Else\n
                            test();\n
                            Return;\n
                        EndIf.\n
                    EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 293))

    def test_293(self):
        input = """
                Function: foo
                    Parameter: x, y
                    Body:
                        For (i = 0, i < 3100, 2) Do
                            foo (22 + x, 42. \\. y);
                            gdsdoo ();
                            x = x + 2;
                        EndFor.
                    EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 294))

    def test_294(self):
        input = """
                Var: x;
                Function: foodf
                    Body:
                        If (a > 1) Then 
                            a = 1;
                        ElseIf (31 < 23) Then 
                            x = 1;
                        Else 
                            fdsfoo(a + 31,32);
                        EndIf.
                    EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 295))

    def test_295(self):
        input = """
                Var: x3;
                Function: fodo
                    Body:
                        foo(a + 1,2);
                        dosofmethdding();
                    EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 296))

    def test_296(self):
        input = """
                Var: x2;
                Function: fodo
                    Body:
                        foo(a + 1.2 , 3, ffdoo());
                        dosdfomedsfthing();
                    EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 297))

    def test_297(self):
        input = """
                Var: x;
                Function: fdoo
                    Body:
                        foo(a + 1.2 , 3, fodo());
                        dddosomdfething();
                        fodo1(3,foo(foo2(foodd3(2,a+1))));
                        dosoddmething();
                    EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 298))

    def test_298(self):
        input = """
                Var: x, sumd;
                Function: gt
                    Body:
                        If xe == 10 Then
                            susm = 1;
                        Else
                            susm = x*sagt(x-1);
                        EndIf.
                    EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 299))

    def test_299(self):
        input = """
                Var: f1, f2, susm;
                Function: fsibo
                    Body:
                        If x <= 2 Then
                            ssum = 1;
                        Else
                            ssum = fisbo(x-2) + fsibo(x-1);
                        EndIf.
                    EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 300))
    def test_300(self):
        input = """Function: masin ** ham ssmain **
                        Body:
                            x = 10;
                            facet (x); ** gosfdi hawqm **
                        EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 300))

