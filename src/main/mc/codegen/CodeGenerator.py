'''
 *   @author Nguyen Hua Phung
 *   @version 1.0
 *   23/10/2015
 *   This file provides a simple version of code generator
 *
'''
from Utils import *
from StaticCheck import *
from StaticError import *
from Emitter import Emitter
from Frame import Frame
from abc import ABC, abstractmethod
from functools import reduce

class CodeGenerator(Utils):
    def __init__(self):
        self.libName = "io"
        self.currentFunc=Symbol("null",MType([],VoidType()),CName("MCClass"))
    def init(self):
        return [Symbol("getInt", MType(list(), IntType()), CName(self.libName)),
                    Symbol("putInt", MType([IntType()], VoidType()), CName(self.libName)),
                    Symbol("putIntLn", MType([IntType()], VoidType()), CName(self.libName)),
                    Symbol("putFloatLn", MType([FloatType()], VoidType()), CName(self.libName))
                    ]

    def gen(self, ast, dir_):
        #ast: AST
        #dir_: String

        gl = self.init()
        gc = CodeGenVisitor(ast, gl, dir_)
        gc.visit(ast, None)

class ClassType(Type):
    def __init__(self, cname):
        #cname: String
        self.cname = cname

    def __str__(self):
        return "ClassType"

    def accept(self, v, param):
        return v.visitClassType(self, param)

class SubBody():
    def __init__(self, frame, sym):
        #frame: Frame
        #sym: List[Symbol]

        self.frame = frame
        self.sym = sym

class Access():
    def __init__(self, frame, sym, isLeft, isFirst,isDup = False):
        #frame: Frame
        #sym: List[Symbol]
        #isLeft: Boolean
        #isFirst: Boolean

        self.frame = frame
        self.sym = sym
        self.isLeft = isLeft
        self.isFirst = isFirst
        self.isDup = isDup
class Val(ABC):
    pass

class Index(Val):
    def __init__(self, value):
        #value: Int

        self.value = value

class CName(Val):
    def __init__(self, value):
        #value: String

        self.value = value

class CodeGenVisitor(BaseVisitor, Utils):
    def __init__(self, astTree, env, dir_):
        #astTree: AST
        #env: List[Symbol]
        #dir_: File

        self.astTree = astTree
        self.env = env
        self.className = "MCClass"
        self.path = dir_
        self.emit = Emitter(self.path + "/" + self.className + ".j")
        self.currentFunc=Symbol("null",MType([],VoidType()),CName(self.className))
    def visitVarGlobal(self,ast,c):
        _ctxt = c
        _name=ast.variable
        _type=ast.varType
        self.emit.printout(self.emit.emitATTRIBUTE(_name,_type,False,""))
        _sym = Symbol(_name,_type,CName(self.className))
        _ctxt.append(_sym)
        return _ctxt
    def visitFunGlobal(self,ast,c):
        _ctxt=c
        _name = ast.name.name
        _type = MType([x.varType for x in ast.param],ast.returnType)
        _sym =Symbol(_name,_type,CName(self.className))
        _ctxt.append(_sym)
        return _ctxt
    def visitProgram(self,ast,c):
        self.emit.printout(self.emit.emitPROLOG(self.className,'java.lang.Object'))
        lstVarDecl=[]
        lstFuncDecl=[]
        
        for x in ast.decl:
            if type(x) is VarDecl:
                lstVarDecl+=[x]
            elif type(x) is FuncDecl:
                lstFuncDecl +=[x]
        for x in ast.decl:
            self.env+= self.visitVarGlobal(x,self.env) if type (x) is VarDecl else self.visitFunGlobal(x,self.env)
        for funDecl in lstFuncDecl:
            self.visit(funDecl,SubBody(None,self.env))
        self.genMETHOD(FuncDecl(Id("<init>"),[],None,[]),c,Frame("<init>",VoidType))
        lstArrayType =[]
        for item in lstVarDecl:
            if type(item.varType) is ArrayType:
                lstArrayType+=[item]
        
        if lstArrayType:
            self.emit.printout(self.emit.emitCLINIT(self.className,lstArrayType,Frame("<clinit>",VoidType())))
        self.emit.emitEPILOG()
        return c
    def genMETHOD(self,decl,c,frame): 
        IsInit = True if decl.returnType is None else False
        IsMain = True if decl.name.name == "main" else False
        nameMethod =  "<init>" if IsInit else decl.name.name
        typePara = [ArrayPointerType(StringType())] if IsMain else [x.varType for x in decl.param]
        returntype = VoidType() if IsInit else decl.returnType
        mtype =MType(typePara,returntype)
        self.emit.printout(self.emit.emitMETHOD(nameMethod,mtype,not IsInit,frame))
        
        frame.enterScope(True);
        

        if IsInit:
            self.emit.printout(self.emit.emitVAR(frame.getNewIndex(),'this',ClassType(self.className),frame.getStartLabel(),frame.getEndLabel(),frame))
        if IsMain:
            self.emit.printout(self.emit.emitVAR(frame.getNewIndex(),'args',ArrayPointerType(StringType()),frame.getStartLabel(),frame.getEndLabel(),frame))
        subBody = SubBody(frame,c)
        if not IsMain and len (decl.param)!=0:
            for param in decl.param:
                subBody=self.visit(param,subBody)
        body=decl.body
        if not IsInit:
            for member in body.member:
                if type(member) is VarDecl:
                    subBody=self.visit(member,subBody)

        self.emit.printout(self.emit.emitLABEL(frame.getStartLabel(),frame))

        if IsInit:
            self.emit.printout(self.emit.emitREADVAR('this',ClassType(self.className),0,frame))
            self.emit.printout(self.emit.emitINVOKESPECIAL(frame))

        lstReturnStmt=[]
        lstVarArrayType=[]
        if not IsInit:
            for member in decl.body.member:
                if type(member) is VarDecl:
                    if type(member.varType) is ArrayType:
                        lstVarArrayType+=[member]
        [self.ArrayTypeDecl(x,subBody) for x in lstVarArrayType]
        if not IsInit:
            for member in decl.body.member:
                if not type(member) is VarDecl:
                    if type(member) is Return:
                        lstReturnStmt+=[member]    
                    self.visit(member,subBody)
        
        for i in range(0,frame.getStackSize(),1):
            self.emit.printout(self.emit.emitPOP(frame))
        self.emit.printout(self.emit.emitLABEL(frame.getEndLabel(),frame))
        
        if (type(returntype) is VoidType or len(lstReturnStmt)==0):
            self.emit.printout(self.emit.emitRETURN(VoidType(),frame))
        
        
        self.emit.printout(self.emit.emitENDMETHOD(frame))


        frame.exitScope()


    def visitVarDecl (self,ast,c):
        frame = c.frame
        lstSym = c.sym if type(c) is SubBody else []
        varIndex = frame.getNewIndex()
        varName = ast.variable
        varType = ast.varType
        self.emit.printout(self.emit.emitVAR(varIndex,varName,varType,frame.getStartLabel(),frame.getEndLabel(),frame))
        lstSym=[Symbol(varName,varType,Index(varIndex))]+lstSym
        return SubBody(frame,lstSym)
    def visitFuncDecl(self,ast,c):
        frame = Frame(ast.name.name,ast.returnType)
        lstSym =  c.sym
        self.currentFunc=self.lookup(ast.name.name,lstSym,lambda x:x.name)
        self.genMETHOD(ast,lstSym,frame)
        return c

   
    def genBinString(self,frame,retLeft,typeLeft,retRight,typeRight):
        if type(typeLeft) is IntType and type(typeRight) is FloatType:
            return retLeft + self.emit.emitI2F(frame)+retRight , FloatType()
        if type(typeLeft) is FloatType and type(typeRight) is IntType:
            return retLeft + retRight + self.emit.emitI2F(frame),FloatType()
        if type(typeLeft) is FloatType and type(typeRight) is FloatType():
            return retLeft+self.emit.emitI2F(frame)+retRight+self.emit.emitI2F(frame),FloatType()
        stringReturn = retLeft+retRight,typeLeft
        # print(stringReturn)
        return stringReturn
    
            
    
            
    def visitUnaryOp(self,ast,c):
        op = ast.op 
        frame = c.frame 
        lstSym = c.sym 
        (retExpr , typeExpr)=self.visit(ast.body,Access(frame,lstSym,False,True))
        if op == '-':
            return retExpr + self.emit.emitNEGOP(typeExpr,frame),typeExpr
        elif op == '!':
            return retExpr + self.emit.emitNOT(BoolType(),frame),BoolType()
    def ArrayTypeDecl(self,ast,c):
        lstSym =c.sym
        frame = c.frame
        sym = self.lookup(ast.variable,lstSym,lambda x:x.name)
        index=sym.value.value
        self.emit.printout(self.emit.emitNEWARRAY(ast.varType,frame))
        self.emit.printout(self.emit.emitWRITEVAR(ast.variable,ast.varType,index,frame))
        return SubBody(frame,sym)


    def visitBlock(self,ast,c):
        frame = c.frame
        oldEnv = c.sym
        frame.enterScope(False)
        varDeclInBlock = SubBody(frame,oldEnv)
        arrayDecl = []
        lstStmt =[]
        for item in ast.member:
            if type(item) is VarDecl:
                varDeclInBlock = self.visit(item,c)
            else:
                lstStmt+=[item]
            if type(item.varType) is ArrayType:
                arrayDecl+=[item]
        
        self.emit.printout(self.emit.emitLABEL(frame.getStartLabel(),frame))
        [self.ArrayTypeDecl(x,varDeclInBlock) for x in arrayDecl]
        [self.visit(x,varDeclInBlock) for x in lstStmt]  
        self.emit.printout(self.emit.emitLABEL(frame.getEndLabel(),frame))
        frame.exitScope()
        return None
        
    

    
    def visitIf(self,ast,c):
        frame = c.frame
        lstSym = c.sym

        stringReturn,typeReturn=self.visit(ast.expr,Access(frame,lstSym,False,True))
        falseLabel = frame.getNewLabel()
        self.emit.printout(stringReturn+self.emit.emitIFFALSE(falseLabel,frame))
        if not type(ast.thenStmt) is Block:
            [self.visit(ast.thenStmt,c)]
        else:
            [self.visit(x,c) for x in ast.thenStmt.member]
        if not ast.elseStmt:
            self.emit.printout(self.emit.emitLABEL(falseLabel,frame))
        else:
            trueLabel=frame.getNewLabel()
            self.emit.printout(self.emit.emitGOTO(trueLabel,frame))
            self.emit.printout(self.emit.emitLABEL(falseLabel,frame))
            if not type(ast.elseStmt) is Block:
                [self.visit(ast.elseStmt,c)]
            else:
                [self.visit(x,c) for x in ast.elseStmt.member]
            self.emit.printout(self.emit.emitLABEL(trueLabel,frame))
        return None
    def visitDowhile(self,ast,c):
        frame=c.frame
        lstSym=c.sym
        loopLabel = frame.getNewLabel()
        frame.enterLoop()
        self.emit.printout(self.emit.emitLABEL(loopLabel,frame))
        [self.visit(x,c) for x in ast.sl]
        self.emit.printout(self.emit.emitLABEL(frame.getContinueLabel(),frame))
        stringReturn,typeReturn = self.visit(ast.exp,Access(frame,lstSym,False,True))
        self.emit.printout(stringReturn)
        self.emit.printout(self.emit.emitIFFALSE(frame.getBreakLabel(),frame))
        self.emit.printout(self.emit.emitGOTO(loopLabel,frame))
        self.emit.printout(self.emit.emitLABEL(frame.getBreakLabel(),frame))
        frame.exitLoop()
        return None
    def visitFor(self,ast,c):
        frame =c.frame
        lstSym=c.sym
        loopLabel = frame.getNewLabel()
        frame.enterLoop()
        self.visit(ast.expr1,Access(frame,lstSym,False,True))
        self.emit.printout(self.emit.emitLABEL(loopLabel,frame))
        stringReturn,typeReturn = self.visit(ast.expr2,Access(frame,lstSym,False,True))
        self.emit.printout(stringReturn)
        self.emit.printout(self.emit.emitIFFALSE(frame.getBreakLabel(),frame))
        if (type(ast.loop) is Block):
            [self.visit(x,c) for x in ast.loop.member]
        else:
            [self.visit(ast.loop,c)]
        self.emit.printout(self.emit.emitLABEL(frame.getContinueLabel(),frame))
        self.visit(ast.expr3,Access(frame,lstSym,False,True))
        self.emit.printout(self.emit.emitGOTO(loopLabel,frame))
        self.emit.printout(self.emit.emitLABEL(frame.getBreakLabel(),frame))
        frame.exitLoop()
        return None
    def visitCallExpr(self,ast,c):
        lstSym = c.sym
        frame=c.frame
        sym = self.lookup(ast.method.name,lstSym,lambda x: x.name)
        cname = sym.value.value
        ctype = sym.mtype
        lstParaType = ctype.partype

        if type(c) is Access: 
            if c.isLeft and not c.isFirst:
                return self.emit.emitWRITEVAR2(ast.method.name, ctype.rettype, frame), ctype.rettype
        _in = ("",[])
        lstCheck = []
        for item in range(len(lstParaType)):
            lstCheck.append((ast.param[item],lstParaType[item]))
        for x in lstCheck:
            (stringReturn,typeReturn)=self.visit(x[0],Access(frame,lstSym,False,True))
            if type(x[1]) is FloatType and type(typeReturn) is IntType:
                _in=(_in[0]+stringReturn+self.emit.emitI2F(frame),_in[1]+[typeReturn])
            else:
                _in=(_in[0]+stringReturn,_in[1]+[typeReturn])
        
        self.emit.printout(_in[0])
        self.emit.printout(self.emit.emitINVOKESTATIC(cname + "/" + sym.name, ctype, frame))
        return "", ctype.rettype
    def visitArrayCell(self,ast,c):
       
        frame=c.frame
        lstSym=c.sym
        if type(c) !=SubBody:
            if c.isLeft == True and c.isFirst == True:
                arrStringReturn,arrTypeReturn=self.visit(ast.arr,Access(frame,lstSym,False,True))
                idxStringReturn,idxTypeReturn = self.visit(ast.idx,Access(frame,lstSym,False,True))
                return arrStringReturn+idxStringReturn,arrTypeReturn.eleType
            elif c.isLeft == True and c.isFirst==False:
                arrStringReturn,arrTypeReturn=self.visit(ast.arr,Access(frame,lstSym,True,False))
                return arrStringReturn,arrTypeReturn
            elif c.isLeft == False:
                arrStringReturn,arrTypeReturn=self.visit(ast.arr,Access(frame,lstSym,False,True))
                idxStringReturn,idxTypeReturn = self.visit(ast.idx,Access(frame,lstSym,False,True))
                if type(arrTypeReturn) is ArrayType:
                    arrayType=arrTypeReturn.eleType
                    aload=self.emit.emitALOAD(arrayType,frame)
                    return arrStringReturn+idxStringReturn+aload,arrayType
                elif type (arrTypeReturn) is ArrayPointerType:
                    arrayPointerType = arrTypeReturn.eleType
                    aload = self.emit.emitALOAD(arrayPointerType,frame)
                    return arrStringReturn+idxStringReturn+aload,arrayPointerType
        else:
            arrStringReturn,arrTypeReturn=self.visit(ast.arr,Access(frame,lstSym,False,True))
            arrType = arrTypeReturn.eleType
            return "",arrTypeReturn
        return None
    def visitBinaryOp(self,ast,c):
        frame = c.frame
        lstSym=c.sym
        op=ast.op
        if op != '=':
            (retLeft,typeLeft)=self.visit(ast.left,Access(frame,lstSym,False,True))
            (retRight,typeRight)=self.visit(ast.right,Access(frame,lstSym,False,True))
            stringExp,typeExp = self.genBinString(frame,retLeft,typeLeft,retRight,typeRight)
            if (op in ['+','-']):
                stringOp=self.emit.emitADDOP(op,typeExp,frame)
            elif op in ['*','/']:
                stringOp = self.emit.emitMULOP(op,typeExp,frame)
            elif op in ['>','>=','<','<=','!=','==']:
                stringOp = self.emit.emitREOP(op,typeExp,frame)
                typeExp = BoolType()
            elif op == '%':
                stringOp = self.emit.emitMOD(frame)
            elif op == '||':
                stringOp = self.emit.emitOROP(frame)
                typeExp = BoolType()
            elif op == '&&':
                stringOp = self.emit.emitANDOP(frame)
                typeExp = BoolType()
            return stringExp + stringOp,typeExp
        elif op == '=':
            # print(ast)
            strDup =""
            strForI2F=""
            stringReturn =""
            (retFirstLeft,typeFirstLeft) = self.visit(ast.left,Access(frame,lstSym,True,True))
            (retRight,typeRight)=self.visit(ast.right,Access(frame,lstSym,False,True,True))
            
            if type(typeFirstLeft) is FloatType and type(typeRight) is IntType:
                strForI2F=self.emit.emitI2F(frame)
            if (type(c) is Access) and (c.isDup == True):
                strDup=self.emit.emitDUP(frame)
                self.emit.printout(retRight)
            stringReturn=retFirstLeft+strForI2F
            self.emit.printout(stringReturn+strDup)

            (retSecondLeft,typeSecondLeft)  = self.visit(ast.left,Access(frame,lstSym,True,False))
        
            
            self.emit.printout(retSecondLeft)
            return (stringReturn,typeSecondLeft)
    def visitId(self,ast,c):
        if not type(c) is SubBody:
            frame=c.frame
            lstSym = c.sym
            sym = self.lookup(ast.name,lstSym,lambda x:x.name)
            stringReturn=""
            if c.isLeft == True and c.isFirst == True:
                pass
            elif c.isLeft == True and c.isFirst ==False: 
                if type(sym.mtype) is ArrayType or type(sym.mtype) is ArrayPointerType:
                    stringReturn =self.emit.emitWRITEVAR2(sym.name,sym.mtype,frame)
                else:
                    if type(sym.value) is CName:
                        stringReturn = self.emit.emitPUTSTATIC(sym.value.value+"."+sym.name,sym.mtype,frame)
                    elif type(sym.value) is Index:
                        stringReturn = self.emit.emitWRITEVAR(sym.name,sym.mtype,sym.value.value,frame)
            elif c.isLeft==False:
                if type(sym.value) is CName:
                    stringReturn = self.emit.emitGETSTATIC(sym.value.value+"."+sym.name,sym.mtype,frame)
                elif type(sym.value) is Index:
                    stringReturn = self.emit.emitREADVAR(sym.name,sym.mtype,sym.value.value,frame)
            return stringReturn,sym.mtype
        else:
            
            sym = self.lookup(ast.name,lstSym,lambda x:x.name)
            return ("",sym.mtype)

    def visitReturn(self,ast,c):
        frame=c.frame
        lstSym = c.sym
        if ast.expr:
            stringReturn,typeReturn = self.visit(ast.expr,Access(frame,lstSym,False,True))
            typeFuncReturn = self.currentFunc.mtype.rettype
            if (type(typeFuncReturn) is FloatType and type(typeReturn) is IntType):
                self.emit.printout(stringReturn + self.emit.emitI2F(frame)+self.emit.emitRETURN(FloatType(),frame))  
            else:
                self.emit.printout(stringReturn + self.emit.emitRETURN(typeReturn,frame))
        else:
            self.emit.printout(self.emit.emitRETURN(VoidType(),frame))
    def visitContinue(self,ast,c):
        self.emit.printout(self.emit.emitGOTO(c.frame.getContinueLabel(),c.frame))
        return None
    def visitBreak(self,ast,c):
        self.emit.printout(self.emit.emitGOTO(c.frame.getBreakLabel(),c.frame))
        return None
    def visitIntLiteral(self,ast,c):
        ctxt=c
        frame = ctxt.frame
        return self.emit.emitPUSHICONST(ast.value,frame),IntType()
    def visitFloatLiteral(self,ast,c):
        ctxt=c
        frame = ctxt.frame
        return self.emit.emitPUSHFCONST(str(ast.value),frame),FloatType()
    def visitStringLiteral(self,ast,c):
        ctxt=c
        frame = ctxt.frame
        return self.emit.emitPUSHCONST(ast.value,StringType(),frame),StringType()
    def visitBooleanLiteral(self,ast,c):
        ctxt=c
        frame = ctxt.frame
        return self.emit.emitPUSHICONST(str(ast.value).lower(),frame),BoolType()







    
