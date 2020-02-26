import unittest
from TestUtils import TestCodeGen
from AST import *


class CheckCodeGenSuite(unittest.TestCase):
    def test_int(self):
        """Simple program: int main() {} """
        input = """
        
        
        void main(){
           
           int a,b,c;
           a=b=c=10;
           putInt(1000);
           
          
             
        }
        
        """
        expect = "100"
        self.assertTrue(TestCodeGen.test(input,expect,510))
    # def test_int_ast(self):
    # 	input = Program([
    # 		FuncDecl(Id("main"),[],VoidType(),Block([
    # 			CallExpr(Id("putInt"),[IntLiteral(5)])]))])
    # 	expect = "5"
    # 	self.assertTrue(TestCodeGen.test(input,expect,501))
