#    **************************************
#    * Student name: Dang Van Dung        *
#    * Student ID: 1710853                *
#    **************************************
from AST import * 
from Visitor import *
from Utils import Utils
from StaticError import *
from functools import reduce

class MType:
    def __init__(self,partype,rettype):
        self.partype = partype
        self.rettype = rettype

class Symbol:
    def __init__(self,name,mtype,value = None):
        self.name = name
        self.mtype = mtype
        self.value = value
def checkValidReturn(left,right):
    if (type(left),type(right)) in [(StringType,StringType),(BoolType,BoolType),(IntType,IntType),(FloatType,IntType),(FloatType,FloatType)]:
        return True
    if type(left) is VoidType:
        if not type(right) is list:
            return False
        else:
            return True
    if type(left) is ArrayPointerType:
        if not type(right) in [ArrayPointerType,ArrayType]:
            return False
        else:
            if (type(left.eleType),type(right.eleType)) in [(StringType,StringType),(BoolType,BoolType),(IntType,IntType),(FloatType,FloatType)]:
                return True
    return False
def checkParseType(listParaDecl,listParaCall):
    validType=[(ArrayPointerType,ArrayPointerType),(ArrayPointerType,ArrayType),(StringType,StringType),(BoolType,BoolType),(IntType,IntType),(FloatType,FloatType),(FloatType,IntType)]
    validTypePointer=[(StringType,StringType),(BoolType,BoolType),(IntType,IntType),(FloatType,FloatType)]
    listTypeParaDecl=[]
    listTypeParaCall=[]
    listTypeParaDeclPointer=[]
    listTypeParaCallPointer=[]
    for item in listParaDecl:
        if type(item) is ArrayPointerType:
            listTypeParaDeclPointer.append(type(item.eleType))
        listTypeParaDecl.append(type(item))
    for item in listParaCall:
        if type(item) in [ArrayPointerType,ArrayType]:
            listTypeParaCallPointer.append(type(item.eleType))
        listTypeParaCall.append(type(item))
    zipPara=list(zip(listTypeParaDecl,listTypeParaCall))
    zipParaPointer=list(zip(listTypeParaDeclPointer,listTypeParaCallPointer))
    for item in zipPara:
        if (not item in validType):
                return False
    for item in zipParaPointer:
        if (not item in validTypePointer):
                return False
    return True
def checkValidOperation(left,right):
    if (type(left),type(right))==(IntType,IntType):
        return IntType()
    if (type(left),type(right)) in [(IntType,FloatType),(FloatType,IntType),(FloatType,FloatType)]:
        return FloatType()
    return None
def checkTypeAssignment(left,right):
    leftType=type(left)
    rightType=type(right)
    if ( (leftType or rightType) is VoidType) or ((leftType or rightType) is ArrayType) or ((leftType or rightType) is ArrayPointerType):
        return False
    return True  

class StaticChecker(BaseVisitor,Utils):

    global_envi = [
        Symbol("getInt", MType([], IntType())),
        Symbol("putInt", MType([IntType()], VoidType())),
        Symbol("putIntLn", MType([IntType()], VoidType())),
        Symbol("getFloat", MType([], FloatType())),
        Symbol("putFloat", MType([FloatType()], VoidType())),
        Symbol("putFloatLn", MType([FloatType()], VoidType())),
        Symbol("putBool", MType([BoolType()], VoidType())),
        Symbol("putBoolLn", MType([BoolType()], VoidType())),
        Symbol("putString", MType([StringType()], VoidType())),
        Symbol("putStringLn", MType([StringType()], VoidType())),
        Symbol("putLn", MType([], VoidType()))
    ]
            
    
    def __init__(self,ast):
        #print(ast)
        #print(ast)
        #print()
        self.ast = ast

 
    
    def check(self):
        return self.visit(self.ast,StaticChecker.global_envi)

    def visitProgram(self,ast, c):
        checkEntryPoint=False
        lstGlobal=[]
        UnreachableFunc=[]
        Flag=True
        for decl in ast.decl:
            if (type(decl) is FuncDecl):
                lstGlobal.append(Symbol(decl.name.name,MType([x.varType for x in decl.param],decl.returnType)))
                if decl.name.name == "main":
                    checkEntryPoint=True
                else:
                    UnreachableFunc.append(decl.name.name)   
            else:
                lstGlobal.append(Symbol(decl.variable,decl.varType)) 
        if (checkEntryPoint==False):
            raise NoEntryPoint()
        
        lstGlobal+=c
        lst=reduce(lambda x,y: [x[0]+self.visit(y,x),UnreachableFunc,lstGlobal,[Flag]],ast.decl,[[],UnreachableFunc,lstGlobal,[Flag]])  
        if len(UnreachableFunc)!=0:
            raise UnreachableFunction(UnreachableFunc[0])
        return lst
    def visitFuncDecl(self,ast, c):
        
        checkInLoop=0
        checkReturn=False
        nameFunc=[ast.name.name]
        if (len(ast.param)!=0): 
            local_var=reduce(lambda x,y: [x[0]+self.visit(y,x),c[0],['parameter']],ast.param,[[],c[0],['parameter']])
            local_var[2][0]='variable'
            local_var.extend([[checkInLoop]]) 
            local_var.extend([[checkReturn]])
            local_var.extend([c[1]]) 
            local_var.extend([c[2]])
            local_var.extend([nameFunc])
            
            for member in ast.body.member:
                temp=self.visit(member,local_var)
                if isinstance(temp,list):
                    local_var[0]+=temp
            checkReturn=local_var[4][0]
            if isinstance(ast.returnType,VoidType):
                checkReturn=True
            if checkReturn==False:
                raise FunctionNotReturn(ast.name.name)
            if not self.lookup(ast.name.name,c[0],lambda x: x.name) is None:
                raise Redeclared(Function(),ast.name.name)
            else:
                return [Symbol(ast.name.name,MType([x.varType for x in ast.param],ast.returnType))]
        else:
            
            local_var=[[],c[0],['variable'],[checkInLoop],[checkReturn],c[1],c[2],nameFunc]
            for member in ast.body.member:
                temp=self.visit(member,local_var)
                if isinstance(temp,list):
                    local_var[0]+=temp
            checkReturn=local_var[4][0]
            if isinstance(ast.returnType,VoidType):
                checkReturn=True
            if checkReturn==False:
                raise FunctionNotReturn(ast.name.name)
            if not self.lookup(ast.name.name,c[0],lambda x: x.name) is None:
                raise Redeclared(Function(),ast.name.name)
            else:
                return [Symbol(ast.name.name,MType([x.varType for x in ast.param],ast.returnType))]
        

    def visitVarDecl(self,ast,c):
        if (len(c)!=4):
            check=c[2][0]
            if (check=='parameter'):
                if not self.lookup(ast.variable,c[0],lambda x:x.name) is None:
                    raise Redeclared(Parameter(),ast.variable)
                else:
                    return [Symbol(ast.variable,ast.varType)]
        if not self.lookup(ast.variable,c[0],lambda x: x.name) is None:
            raise Redeclared(Variable(),ast.variable)
        else:
            return [Symbol(ast.variable,ast.varType)]
    def visitReturn(self,ast,c):
        c[4][0]=True  # IsReturn
        nameFunc=c[7][0]
        lstGlobal=c[6]
        if not ast.expr is None:
            returnType=self.visit(ast.expr,c)
            count=0;
            for item in lstGlobal:
                if (nameFunc==item.name):
                    count+=1
            if count>1:
                res=self.lookup(nameFunc,lstGlobal[::-1],lambda x:x.name)
                if type(res.mtype) is MType:
                    raise Redeclared(Function(),nameFunc)
            res=self.lookup(nameFunc,lstGlobal,lambda x:x.name)             
            if not res is None and type(res.mtype) is MType:
                typeFunc=res.mtype.rettype
                if not checkValidReturn(typeFunc,returnType):
                    raise TypeMismatchInStatement(ast)
            return returnType
        else:
            count=0;
            for item in lstGlobal:
                if (nameFunc==item.name and type(item.mtype) is MType):
                    count+=1
            if count>1:
                res=self.lookup(nameFunc,lstGlobal[::-1],lambda x:x.name)
                if type(res.mtype) is MType:
                    raise Redeclared(Function(),nameFunc)
            res=self.lookup(nameFunc,lstGlobal,lambda x:x.name) 
            if not res is None and type(res.mtype) is MType:
                typeFunc=res.mtype.rettype
                if (not type(typeFunc) is VoidType):
                    raise TypeMismatchInStatement(ast)
            return []
    def visitFor(self,ast,c):
          # CheckInLoop
        c[3][0]=c[3][0]+1
        expr1=self.visit(ast.expr1,c)
        expr2=self.visit(ast.expr2,c)
        expr3=self.visit(ast.expr3,c)
        if not (type(expr1) is IntType and type(expr3) is IntType and type(expr2) is BoolType):
            raise TypeMismatchInStatement(ast)
        self.visit(ast.loop,c)
    
       
                    
        c[3][0]=c[3][0]-1 # CheckInLoop
        c[4][0]=False # IsReturn
        return []
    def visitBlock(self,ast,c):
        lstVarDecl=[]
        for member in ast.member:
            if type(member) is VarDecl:
                lstVarDecl.append(member.variable)
        declOutBlock=c[0].copy()
        for localvar in c[0]:
            if localvar.name in lstVarDecl:
                c[0].remove(localvar)
        
        for member in ast.member:
            temp=self.visit(member,c)
            if isinstance(temp,list):
                c[0]+=temp
        c[0]=declOutBlock.copy()
        return []
    def visitDowhile(self,ast,c):
        
        c[3][0]=c[3][0]+1
        expr=self.visit(ast.exp,c)
        if not type(expr) is BoolType:
            raise TypeMismatchInStatement(ast) 
        for stmt in ast.sl:
            self.visit(stmt,c)
        
        c[3][0]=c[3][0]-1
        return []
    def visitContinue(self,ast,c):
        checkInLoop=c[3][0]
        if  checkInLoop==0:
            raise ContinueNotInLoop()
        return []
    def visitBreak(self,ast,c):
        checkInLoop=c[3][0]
        if checkInLoop==0:
            raise BreakNotInLoop()
        return []
    def visitIf(self,ast,c):
        expr=ast.expr
        thenStmt=ast.thenStmt
        elseStmt=ast.elseStmt
        if not type(self.visit(expr,c)) is BoolType:
            raise TypeMismatchInStatement(ast)
        if not elseStmt is None:
            isReturnThen=self.visit(thenStmt,c)
            checkReturnInThen=c[4][0]
            c[4][0]=False
            isReturnElse=self.visit(elseStmt,c)
            checkReturnInElse=c[4][0]
            if not (checkReturnInThen and checkReturnInElse) == True:
                c[4][0]=False
        else:
            self.visit(thenStmt,c)
            c[4][0]=False
        return []
    def visitBinaryOp(self,ast,c):
        left=self.visit(ast.left,c)
        right=self.visit(ast.right,c)
        op=ast.op
        if op in ['+','-','*']:
            returnType=checkValidOperation(left,right)
            if returnType is None:
                raise TypeMismatchInExpression(ast)
            return returnType
        elif op == '/':
            returnType=checkValidOperation(left,right)
            if returnType is None:
                raise TypeMismatchInExpression(ast)
            return returnType
        elif op in ['<','<=','>=','>']:
            returnType = checkValidOperation(left,right)
            if not returnType is None:
                return BoolType()
            else:
                raise TypeMismatchInExpression(ast)
        elif op in ['&&','||']:
            if (type(left),type(right))==(BoolType,BoolType):
                return BoolType()
            else:
                raise TypeMismatchInExpression(ast)
        elif op in ['==','!=','%']:
            if (type(left),type(right)) in [(IntType,IntType),(BoolType,BoolType)]:
                if op in ['==','!=']:
                    return BoolType()
                else:
                    return IntType()
            else: 
                raise TypeMismatchInExpression(ast)
        elif op == '=':
            if not type(ast.left) in [ArrayCell,Id]:
                raise NotLeftValue(ast.left)
            if checkTypeAssignment(left,right) == True:
                
                typeLeft=type(left)
                typeRight=type(right)
                
                if (typeLeft,typeRight) == (IntType,IntType):
                    return IntType()
                elif (typeLeft,typeRight) in [(FloatType,IntType),(FloatType,FloatType)]:
                    return FloatType()
                elif (typeLeft,typeRight) == (StringType,StringType):
                    return StringType()
                elif (typeLeft,typeRight) == (BoolType,BoolType):
                    return BoolType()
                raise TypeMismatchInExpression(ast)
            else:
                raise TypeMismatchInExpression(ast)
        raise TypeMismatchInExpression(ast)
    def visitUnaryOp(self,ast,c):
        op=ast.op
        body=self.visit(ast.body,c)
        if op == '-':
            if type(body) is FloatType:
                return FloatType()
            elif type(body) is IntType:
                return IntType()
            else:
                raise TypeMismatchInExpression(ast)
        elif op =='!':
            if type(body) is BoolType:
                return BoolType()
            else:
                raise TypeMismatchInExpression(ast)
    def visitCallExpr(self, ast, c): 
        lstTypeParaCall = [self.visit(x,c) for x in ast.param]
        nameFunc=c[7][0]
        IsFuncCall='funccall'
        c.extend([[IsFuncCall]])
        typeFuncCall=self.visit(ast.method,c)
        c.remove(['funccall'])
        res= self.lookup(ast.method.name,c[0]+c[6],lambda x: x.name)
        UnreachableFunction=c[5]
        if (type(res.mtype) is MType):
            if (ast.method.name in UnreachableFunction) and nameFunc != ast.method.name:
                UnreachableFunction.remove(ast.method.name)
            if not res is None:
                lstTypeParaDecl=res.mtype.partype
            if res is None:
                raise Undeclared(Function(),ast.method.name)
            elif len(lstTypeParaDecl) != len(lstTypeParaCall):
                raise TypeMismatchInExpression(ast)
            else:
                if not checkParseType(lstTypeParaDecl,lstTypeParaCall):
                    raise TypeMismatchInExpression(ast)
                return res.mtype.rettype
        else:
            raise TypeMismatchInExpression(ast)
    def visitId(self,ast,c):
        
        localEnvi=c[0]
        globalEnvi=c[6]
        
        if (len(c)==9):
            IsFuncCall=c[8][0]
        else:
            IsFuncCall='no-funccall'
        checkLocal=self.lookup(ast.name,localEnvi,lambda x:x.name)
        if (not checkLocal is None):
            return checkLocal.mtype
        checkGlobal=self.lookup(ast.name,globalEnvi,lambda x:x.name)
        if (not checkGlobal is None):
            return checkGlobal.mtype
        if IsFuncCall=='funccall':
            raise Undeclared(Function(),ast.name)
        raise Undeclared(Identifier(),ast.name)
    def visitArrayCell(self,ast,c):
        name=self.visit(ast.arr,c)
        index=self.visit(ast.idx,c)
        if not type(name) in [ArrayType,ArrayPointerType]:
            raise TypeMismatchInExpression(ast)
        if not type(index) is IntType:
            raise TypeMismatchInExpression(ast)
        return name.eleType
    
    def visitIntLiteral(self,ast, c): 
        return IntType()
    def visitFloatLiteral(self,ast,c):
        return FloatType()
    def visitStringLiteral(self,ast,c):
        return StringType()
    def visitBooleanLiteral(self,ast,c):
        return BoolType()
    

