# Generated from main/bkit/parser/BKIT.g4 by ANTLR 4.8
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .BKITParser import BKITParser
else:
    from BKITParser import BKITParser

# This class defines a complete generic visitor for a parse tree produced by BKITParser.

class BKITVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by BKITParser#program.
    def visitProgram(self, ctx:BKITParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#exp.
    def visitExp(self, ctx:BKITParser.ExpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#expint.
    def visitExpint(self, ctx:BKITParser.ExpintContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#expint1.
    def visitExpint1(self, ctx:BKITParser.Expint1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#expint2.
    def visitExpint2(self, ctx:BKITParser.Expint2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#expint3.
    def visitExpint3(self, ctx:BKITParser.Expint3Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#expint4.
    def visitExpint4(self, ctx:BKITParser.Expint4Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#expint5.
    def visitExpint5(self, ctx:BKITParser.Expint5Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#atomint.
    def visitAtomint(self, ctx:BKITParser.AtomintContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#call.
    def visitCall(self, ctx:BKITParser.CallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#listexp.
    def visitListexp(self, ctx:BKITParser.ListexpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#index.
    def visitIndex(self, ctx:BKITParser.IndexContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#indexele.
    def visitIndexele(self, ctx:BKITParser.IndexeleContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#var.
    def visitVar(self, ctx:BKITParser.VarContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#listid.
    def visitListid(self, ctx:BKITParser.ListidContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#index_var.
    def visitIndex_var(self, ctx:BKITParser.Index_varContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#indexele_var.
    def visitIndexele_var(self, ctx:BKITParser.Indexele_varContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#assign_var.
    def visitAssign_var(self, ctx:BKITParser.Assign_varContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#assign.
    def visitAssign(self, ctx:BKITParser.AssignContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#retur.
    def visitRetur(self, ctx:BKITParser.ReturContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#contin.
    def visitContin(self, ctx:BKITParser.ContinContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#br.
    def visitBr(self, ctx:BKITParser.BrContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#st.
    def visitSt(self, ctx:BKITParser.StContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#ifst.
    def visitIfst(self, ctx:BKITParser.IfstContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#whilest.
    def visitWhilest(self, ctx:BKITParser.WhilestContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#dowhilest.
    def visitDowhilest(self, ctx:BKITParser.DowhilestContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#forst.
    def visitForst(self, ctx:BKITParser.ForstContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#parameter.
    def visitParameter(self, ctx:BKITParser.ParameterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#listpar.
    def visitListpar(self, ctx:BKITParser.ListparContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#array.
    def visitArray(self, ctx:BKITParser.ArrayContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#array1.
    def visitArray1(self, ctx:BKITParser.Array1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#function.
    def visitFunction(self, ctx:BKITParser.FunctionContext):
        return self.visitChildren(ctx)



del BKITParser