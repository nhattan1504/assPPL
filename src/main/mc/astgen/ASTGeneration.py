from MCVisitor import MCVisitor
from MCParser import MCParser
from AST import *

# MSSV: 1710853
class ASTGeneration(MCVisitor):
    def visitProgram(self,ctx:MCParser.ProgramContext):
        # program: decls+ EOF;
        lstDecl=[]
        for decl in ctx.decls():
            if (isinstance(self.visit(decl),list)):
                lstDecl+=self.visit(decl)
            else:
                lstDecl+=[self.visit(decl)]
        return Program(lstDecl) #return Program(list(map(lambda x:self.visit(x),ctx.decls())))
        
    def visitDecls(self,ctx:MCParser.DeclsContext):
        # decls: vardecl | fundecl;
        return self.visit(ctx.vardecl()) if ctx.vardecl() else self.visit(ctx.fundecl())
    def visitVardecl(self,ctx:MCParser.VardeclContext):
        # vardecl: primitype lstvar SM;
        lstVardecl=[]
        lstVar=self.visit(ctx.lstvar())
        nameType=self.visit(ctx.primitype())
        for var in lstVar:
            if (isinstance(var,list)==True):
                lstVardecl+=[VarDecl(var[0],ArrayType(int(var[1]),nameType))]
            else:
                lstVardecl+=[VarDecl(var,nameType)]
        return lstVardecl

    def visitLstvar(self,ctx:MCParser.LstvarContext):
        # lstvar: var (CM var)*
        return [self.visit(x) for x in ctx.var()]
    def visitVar(self,ctx:MCParser.VarContext):
        # var: ID | arrayvar;
        return ctx.ID().getText() if ctx.ID() else self.visit(ctx.arrayvar())
    def visitArrayvar(self,ctx:MCParser.ArrayvarContext):
        # arrayvar: ID LSB INTLIT RSB;
        return [ctx.ID().getText(),ctx.INTLIT().getText()]
    def visitPrimitype(self,ctx:MCParser.PrimitypeContext):
        # primitype: (BOOLEAN|INT|FLOAT|STRING);
        return BoolType() if ctx.BOOLEAN() else IntType() if ctx.INT() else FloatType() if ctx.FLOAT() else StringType()
    def visitFundecl(self,ctx:MCParser.FundeclContext):
        # fundecl: typefun ID LB (paradecl (CM paradecl)*)? RB block_statement;
        lstVarDecl=[]
        for para in ctx.paradecl():
            temp=self.visit(para)
            if (len(temp)==3):
                lstVarDecl+=[VarDecl(temp[1],ArrayPointerType(temp[0]))]
            else:
                lstVarDecl+=[VarDecl(temp[1],temp[0])]    
        return FuncDecl(Id(ctx.ID().getText()),lstVarDecl,self.visit(ctx.typefun()),self.visit(ctx.block_statement()))
    def visitParadecl(self,ctx:MCParser.ParadeclContext):
        # paradecl: primitype ID | in_array_pointer_type;
        return [self.visit(ctx.primitype()),ctx.ID().getText()] if ctx.ID() else self.visit(ctx.in_array_pointer_type())
    def visitIn_array_pointer_type(self,ctx:MCParser.In_array_pointer_typeContext):
        # in_array_pointer_type: primitype ID LSB RSB;
        flag=1
        return [self.visit(ctx.primitype()),ctx.ID().getText(),flag]
    def visitTypefun(self,ctx:MCParser.TypefunContext):
        # typefun: (primitype|VOID|out_array_pointer_type);
        return self.visit(ctx.primitype()) if ctx.primitype() else VoidType() if ctx.VOID() else self.visit(ctx.out_array_pointer_type())
    def visitOut_array_pointer_type(self,ctx:MCParser.Out_array_pointer_typeContext):
        # out_array_pointer_type: primitype LSB RSB;
        return ArrayPointerType(self.visit(ctx.primitype()))
    def visitBlock_statement(self,ctx:MCParser.Block_statementContext):
        # block_statement: LP var_stm* RP;
        lstBlockMember=[]
        lstVarStmt=ctx.var_stm()
        if (lstVarStmt!=[]):
            for item in lstVarStmt:
                temp=self.visit(item)
                if (isinstance(temp,list)):
                    lstBlockMember+=temp
                else:
                    lstBlockMember+=[temp]
        return Block(lstBlockMember)
    def visitVar_stm(self,ctx:MCParser.Var_stmContext):
        # var_stm: vardecl|statement;
        return self.visit(ctx.vardecl()) if ctx.vardecl() else self.visit(ctx.statement())
    def visitStatement(self,ctx:MCParser.StatementContext):
        # statement: if_statement
        # |   do_while_statement
        # |   for_statement
        # |   break_statement
        # |   continue_statement
        # |   return_statement
        # |   block_statement
        # |   exp_statement;
        if ctx.if_statement():
            return self.visit(ctx.if_statement())
        elif ctx.do_while_statement():
            return self.visit(ctx.do_while_statement())
        elif ctx.for_statement():
            return self.visit(ctx.for_statement())
        elif ctx.break_statement():
            return self.visit(ctx.break_statement())
        elif ctx.continue_statement():
            return self.visit(ctx.continue_statement())
        elif ctx.return_statement():
            return self.visit(ctx.return_statement())
        elif ctx.exp_statement():
            return self.visit(ctx.exp_statement())
        else:
            return self.visit(ctx.block_statement())
    def visitIf_statement(self,ctx:MCParser.If_statementContext):
        # if_statement: IF LB exp RB statement (ELSE statement)?;
        if (ctx.ELSE()):
            return If(self.visit(ctx.exp()),self.visit(ctx.statement(0)),self.visit(ctx.statement(1)))
        else:
            return If(self.visit(ctx.exp()),self.visit(ctx.statement(0)),None)
    def visitDo_while_statement(self,ctx:MCParser.Do_while_statementContext):
        # do_while_statement: DO statement+ WHILE exp SM;
        lstStatement=[self.visit(x) for x in ctx.statement()]
        return Dowhile(lstStatement,self.visit(ctx.exp()))
    def visitFor_statement(self,ctx:MCParser.For_statementContext):
        # for_statement: FOR LB exp SM exp SM exp RB statement;
        return For(self.visit(ctx.exp(0)),self.visit(ctx.exp(1)),self.visit(ctx.exp(2)),self.visit(ctx.statement()))
    def visitBreak_statement(self,ctx:MCParser.Break_statementContext):
        # break_statement: BREAK SM;
        return Break()
    def visitContinue_statement(self,ctx:MCParser.Continue_statementContext):
        # continue_statement: CONTINUE SM;
        return Continue()
    def visitReturn_statement(self,ctx:MCParser.Return_statementContext):
        # return_statement: RETURN (exp|) SM;
        return Return(self.visit(ctx.exp())) if ctx.exp() else Return()
    def visitExp_statement(self,ctx:MCParser.Exp_statementContext):
        # exp_statement: exp SM;
        return self.visit(ctx.exp())
    def visitExp(self,ctx:MCParser.ExpContext):
        # exp: exp1 ASSIGN exp | exp1;    
        return BinaryOp(ctx.ASSIGN().getText(),self.visit(ctx.exp1()),self.visit(ctx.exp())) if ctx.ASSIGN() else self.visit(ctx.exp1())
    def visitExp1(self,ctx:MCParser.Exp1Context):
        #exp1: exp1 OR exp2 | exp2;
        return BinaryOp(ctx.OR().getText(),self.visit(ctx.exp1()),self.visit(ctx.exp2())) if ctx.OR() else self.visit(ctx.exp2())
    def visitExp2(self,ctx:MCParser.Exp2Context):
        # exp2: exp2 AND exp3 | exp3;
        return BinaryOp(ctx.AND().getText(),self.visit(ctx.exp2()),self.visit(ctx.exp3())) if ctx.AND() else self.visit(ctx.exp3())
    def visitExp3(self,ctx:MCParser.Exp3Context):
        # exp3: exp4 (EQ|NOTEQ) exp4 | exp4;
        if (ctx.EQ()):
            return BinaryOp(ctx.EQ().getText(),self.visit(ctx.exp4(0)),self.visit(ctx.exp4(1)))
        elif (ctx.NOTEQ()):
            return BinaryOp(ctx.NOTEQ().getText(),self.visit(ctx.exp4(0)),self.visit(ctx.exp4(1)))
        else:
            return self.visit(ctx.exp4(0))
    def visitExp4(self,ctx:MCParser.Exp4Context):
        # exp4: exp5 (LESS|LESSEQ|GREA|GREAEQ) exp5 | exp5;
        if (ctx.LESS()):
            return BinaryOp(ctx.LESS().getText(),self.visit(ctx.exp5(0)),self.visit(ctx.exp5(1)))
        elif (ctx.LESSEQ()):
            return BinaryOp(ctx.LESSEQ().getText(),self.visit(ctx.exp5(0)),self.visit(ctx.exp5(1)))
        elif (ctx.GREA()):
            return BinaryOp(ctx.GREA().getText(),self.visit(ctx.exp5(0)),self.visit(ctx.exp5(1)))
        elif (ctx.GREAEQ()):
            return BinaryOp(ctx.GREAEQ().getText(),self.visit(ctx.exp5(0)),self.visit(ctx.exp5(1)))
        else:
            return self.visit(ctx.exp5(0)) 
    def visitExp5(self,ctx:MCParser.Exp5Context):
        # exp5: exp5 (ADD|SUB) exp6 | exp6;
        if (ctx.ADD()):
            return BinaryOp(ctx.ADD().getText(),self.visit(ctx.exp5()),self.visit(ctx.exp6()))
        elif (ctx.SUB()):
            return BinaryOp(ctx.SUB().getText(),self.visit(ctx.exp5()),self.visit(ctx.exp6()))
        else:
            return self.visit(ctx.exp6())
    def visitExp6(self,ctx:MCParser.Exp6Context):
        # exp6: exp6 (DIV|MUL|MOD) exp7 | exp7;
        if (ctx.DIV()):
            return BinaryOp(ctx.DIV().getText(),self.visit(ctx.exp6()),self.visit(ctx.exp7()))
        elif (ctx.MUL()):
            return BinaryOp(ctx.MUL().getText(),self.visit(ctx.exp6()),self.visit(ctx.exp7()))
        elif (ctx.MOD()):
            return BinaryOp(ctx.MOD().getText(),self.visit(ctx.exp6()),self.visit(ctx.exp7()))
        else:
            return self.visit(ctx.exp7())
    def visitExp7(self,ctx:MCParser.Exp7Context):
        # exp7: (SUB|NOT) exp7 | exp8;
        if (ctx.SUB()):
            return UnaryOp(ctx.SUB().getText(),self.visit(ctx.exp7()))
        elif (ctx.NOT()):
            return UnaryOp(ctx.NOT().getText(),self.visit(ctx.exp7()))
        else:
            return self.visit(ctx.exp8())
    def visitExp8(self,ctx:MCParser.Exp8Context):
        # exp8: exp9 LSB exp RSB | exp9;
        return ArrayCell(self.visit(ctx.exp9()),self.visit(ctx.exp())) if ctx.exp() else self.visit(ctx.exp9())
    def visitExp9(self,ctx:MCParser.Exp9Context):
        # exp9: LB exp RB | operand;
        return self.visit(ctx.exp()) if ctx.getChildCount()==3 else self.visit(ctx.operand())
    def visitOperand(self,ctx:MCParser.OperandContext):
        # operand: literal | ID | funcall;
        return self.visit(ctx.literal()) if ctx.literal() else Id(ctx.ID().getText()) if ctx.ID() else self.visit(ctx.funcall())
    def visitLiteral(self,ctx:MCParser.LiteralContext):
        # literal: INTLIT|FLOATLIT|BOOLLIT|STRINGLIT;
        if (ctx.INTLIT()):
            return IntLiteral(int(ctx.INTLIT().getText()))
        elif (ctx.FLOATLIT()):
            return FloatLiteral(float(ctx.FLOATLIT().getText()))
        elif (ctx.BOOLLIT()):
            text=ctx.BOOLLIT().getText().lower()
            if (text =='true'):
                return BooleanLiteral(True)
            elif (text=='false'):
                return BooleanLiteral(False)
        else: 
            return StringLiteral(ctx.STRINGLIT().getText())
    def visitFuncall(self,ctx:MCParser.FuncallContext):
        # funcall: ID LB (exp (CM exp)*)? RB;
        lstExp=[]
        lst=ctx.exp()
        for item in lst:
            lstExp+=[self.visit(item)]
        return CallExpr(Id(ctx.ID().getText()),lstExp)
    


        









    
        
