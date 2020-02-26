# Generated from main/mc/parser/MC.g4 by ANTLR 4.7.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .MCParser import MCParser
else:
    from MCParser import MCParser

# This class defines a complete generic visitor for a parse tree produced by MCParser.

class MCVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by MCParser#program.
    def visitProgram(self, ctx:MCParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#decls.
    def visitDecls(self, ctx:MCParser.DeclsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#vardecl.
    def visitVardecl(self, ctx:MCParser.VardeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#lstvar.
    def visitLstvar(self, ctx:MCParser.LstvarContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#primitype.
    def visitPrimitype(self, ctx:MCParser.PrimitypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#var.
    def visitVar(self, ctx:MCParser.VarContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#arrayvar.
    def visitArrayvar(self, ctx:MCParser.ArrayvarContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#fundecl.
    def visitFundecl(self, ctx:MCParser.FundeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#typefun.
    def visitTypefun(self, ctx:MCParser.TypefunContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#out_array_pointer_type.
    def visitOut_array_pointer_type(self, ctx:MCParser.Out_array_pointer_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#in_array_pointer_type.
    def visitIn_array_pointer_type(self, ctx:MCParser.In_array_pointer_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#paradecl.
    def visitParadecl(self, ctx:MCParser.ParadeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#block_statement.
    def visitBlock_statement(self, ctx:MCParser.Block_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#var_stm.
    def visitVar_stm(self, ctx:MCParser.Var_stmContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#if_statement.
    def visitIf_statement(self, ctx:MCParser.If_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#do_while_statement.
    def visitDo_while_statement(self, ctx:MCParser.Do_while_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#for_statement.
    def visitFor_statement(self, ctx:MCParser.For_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#break_statement.
    def visitBreak_statement(self, ctx:MCParser.Break_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#continue_statement.
    def visitContinue_statement(self, ctx:MCParser.Continue_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#return_statement.
    def visitReturn_statement(self, ctx:MCParser.Return_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#exp_statement.
    def visitExp_statement(self, ctx:MCParser.Exp_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#statement.
    def visitStatement(self, ctx:MCParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#exp.
    def visitExp(self, ctx:MCParser.ExpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#exp1.
    def visitExp1(self, ctx:MCParser.Exp1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#exp2.
    def visitExp2(self, ctx:MCParser.Exp2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#exp3.
    def visitExp3(self, ctx:MCParser.Exp3Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#exp4.
    def visitExp4(self, ctx:MCParser.Exp4Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#exp5.
    def visitExp5(self, ctx:MCParser.Exp5Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#exp6.
    def visitExp6(self, ctx:MCParser.Exp6Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#exp7.
    def visitExp7(self, ctx:MCParser.Exp7Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#exp8.
    def visitExp8(self, ctx:MCParser.Exp8Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#exp9.
    def visitExp9(self, ctx:MCParser.Exp9Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#operand.
    def visitOperand(self, ctx:MCParser.OperandContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#literal.
    def visitLiteral(self, ctx:MCParser.LiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#funcall.
    def visitFuncall(self, ctx:MCParser.FuncallContext):
        return self.visitChildren(ctx)



del MCParser