# Generated from main/mc/parser/MC.g4 by ANTLR 4.7.2
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


from lexererr import *



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\62")
        buf.write("\u017e\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\3\2\3\2\3\2\3\2\3\3\3\3\3\3\3\3\3\3\3\3\3\4\3\4")
        buf.write("\3\4\3\4\3\4\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\6\3\6\3")
        buf.write("\6\3\6\3\6\3\6\3\6\3\7\3\7\3\7\3\7\3\7\3\7\3\b\3\b\3\b")
        buf.write("\3\b\3\b\3\b\3\b\3\b\3\b\3\t\3\t\3\t\3\t\3\t\3\n\3\n\3")
        buf.write("\n\3\n\3\13\3\13\3\13\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\r")
        buf.write("\3\r\3\r\3\16\3\16\3\16\3\16\3\16\3\16\3\17\3\17\3\20")
        buf.write("\3\20\3\21\3\21\3\22\3\22\3\22\3\23\3\23\3\23\3\24\3\24")
        buf.write("\3\25\3\25\3\25\3\26\3\26\3\27\3\27\3\30\3\30\3\31\3\31")
        buf.write("\3\32\3\32\3\32\3\33\3\33\3\33\3\34\3\34\3\35\3\35\3\35")
        buf.write("\3\36\6\36\u00d8\n\36\r\36\16\36\u00d9\3\37\7\37\u00dd")
        buf.write("\n\37\f\37\16\37\u00e0\13\37\3\37\5\37\u00e3\n\37\3\37")
        buf.write("\6\37\u00e6\n\37\r\37\16\37\u00e7\3\37\5\37\u00eb\n\37")
        buf.write("\3\37\6\37\u00ee\n\37\r\37\16\37\u00ef\3\37\5\37\u00f3")
        buf.write("\n\37\3\37\7\37\u00f6\n\37\f\37\16\37\u00f9\13\37\3\37")
        buf.write("\5\37\u00fc\n\37\5\37\u00fe\n\37\5\37\u0100\n\37\3 \3")
        buf.write(" \5 \u0104\n \3 \6 \u0107\n \r \16 \u0108\3!\3!\3\"\3")
        buf.write("\"\3#\3#\5#\u0111\n#\3$\3$\3$\3$\3$\3%\3%\3%\3%\3%\3%")
        buf.write("\3&\3&\3&\3&\7&\u0122\n&\f&\16&\u0125\13&\3&\3&\3&\3&")
        buf.write("\3&\3&\7&\u012d\n&\f&\16&\u0130\13&\5&\u0132\n&\3&\3&")
        buf.write("\3\'\3\'\3(\3(\3)\3)\3*\3*\3+\3+\3,\3,\3-\3-\3.\3.\3/")
        buf.write("\6/\u0147\n/\r/\16/\u0148\3/\3/\3\60\3\60\7\60\u014f\n")
        buf.write("\60\f\60\16\60\u0152\13\60\3\61\3\61\3\61\3\61\7\61\u0158")
        buf.write("\n\61\f\61\16\61\u015b\13\61\3\61\3\61\3\61\3\62\3\62")
        buf.write("\3\62\3\62\7\62\u0164\n\62\f\62\16\62\u0167\13\62\3\62")
        buf.write("\3\62\3\62\3\62\3\62\3\63\3\63\3\63\3\63\7\63\u0172\n")
        buf.write("\63\f\63\16\63\u0175\13\63\3\63\5\63\u0178\n\63\3\63\3")
        buf.write("\63\3\64\3\64\3\64\3\u0123\2\65\3\3\5\4\7\5\t\6\13\7\r")
        buf.write("\b\17\t\21\n\23\13\25\f\27\r\31\16\33\17\35\20\37\21!")
        buf.write("\22#\23%\24\'\25)\26+\27-\30/\31\61\32\63\33\65\34\67")
        buf.write("\359\36;\37= ?\2A\2C\2E!G\"I#K$M%O&Q\'S(U)W*Y+[,]-_.a")
        buf.write("/c\60e\61g\62\3\2\f\3\2\62;\4\2GGgg\4\2\f\f\17\17\5\2")
        buf.write("\13\f\17\17\"\"\5\2C\\aac|\6\2\62;C\\aac|\t\2$$^^ddhh")
        buf.write("ppttvv\6\2\f\f\17\17$$^^\b\2^^ddhhppttvv\5\2\17\17$$^")
        buf.write("^\2\u0194\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2")
        buf.write("\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2")
        buf.write("\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2")
        buf.write("\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#")
        buf.write("\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2")
        buf.write("\2-\3\2\2\2\2/\3\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2\2\65")
        buf.write("\3\2\2\2\2\67\3\2\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2")
        buf.write("\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2\2\2\2M\3\2\2")
        buf.write("\2\2O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2\2\2U\3\2\2\2\2W\3\2")
        buf.write("\2\2\2Y\3\2\2\2\2[\3\2\2\2\2]\3\2\2\2\2_\3\2\2\2\2a\3")
        buf.write("\2\2\2\2c\3\2\2\2\2e\3\2\2\2\2g\3\2\2\2\3i\3\2\2\2\5m")
        buf.write("\3\2\2\2\7s\3\2\2\2\tx\3\2\2\2\13\u0080\3\2\2\2\r\u0087")
        buf.write("\3\2\2\2\17\u008d\3\2\2\2\21\u0096\3\2\2\2\23\u009b\3")
        buf.write("\2\2\2\25\u009f\3\2\2\2\27\u00a2\3\2\2\2\31\u00a9\3\2")
        buf.write("\2\2\33\u00ac\3\2\2\2\35\u00b2\3\2\2\2\37\u00b4\3\2\2")
        buf.write("\2!\u00b6\3\2\2\2#\u00b8\3\2\2\2%\u00bb\3\2\2\2\'\u00be")
        buf.write("\3\2\2\2)\u00c0\3\2\2\2+\u00c3\3\2\2\2-\u00c5\3\2\2\2")
        buf.write("/\u00c7\3\2\2\2\61\u00c9\3\2\2\2\63\u00cb\3\2\2\2\65\u00ce")
        buf.write("\3\2\2\2\67\u00d1\3\2\2\29\u00d3\3\2\2\2;\u00d7\3\2\2")
        buf.write("\2=\u00ff\3\2\2\2?\u0101\3\2\2\2A\u010a\3\2\2\2C\u010c")
        buf.write("\3\2\2\2E\u0110\3\2\2\2G\u0112\3\2\2\2I\u0117\3\2\2\2")
        buf.write("K\u0131\3\2\2\2M\u0135\3\2\2\2O\u0137\3\2\2\2Q\u0139\3")
        buf.write("\2\2\2S\u013b\3\2\2\2U\u013d\3\2\2\2W\u013f\3\2\2\2Y\u0141")
        buf.write("\3\2\2\2[\u0143\3\2\2\2]\u0146\3\2\2\2_\u014c\3\2\2\2")
        buf.write("a\u0153\3\2\2\2c\u015f\3\2\2\2e\u016d\3\2\2\2g\u017b\3")
        buf.write("\2\2\2ij\7k\2\2jk\7p\2\2kl\7v\2\2l\4\3\2\2\2mn\7h\2\2")
        buf.write("no\7n\2\2op\7q\2\2pq\7c\2\2qr\7v\2\2r\6\3\2\2\2st\7x\2")
        buf.write("\2tu\7q\2\2uv\7k\2\2vw\7f\2\2w\b\3\2\2\2xy\7d\2\2yz\7")
        buf.write("q\2\2z{\7q\2\2{|\7n\2\2|}\7g\2\2}~\7c\2\2~\177\7p\2\2")
        buf.write("\177\n\3\2\2\2\u0080\u0081\7u\2\2\u0081\u0082\7v\2\2\u0082")
        buf.write("\u0083\7t\2\2\u0083\u0084\7k\2\2\u0084\u0085\7p\2\2\u0085")
        buf.write("\u0086\7i\2\2\u0086\f\3\2\2\2\u0087\u0088\7d\2\2\u0088")
        buf.write("\u0089\7t\2\2\u0089\u008a\7g\2\2\u008a\u008b\7c\2\2\u008b")
        buf.write("\u008c\7m\2\2\u008c\16\3\2\2\2\u008d\u008e\7e\2\2\u008e")
        buf.write("\u008f\7q\2\2\u008f\u0090\7p\2\2\u0090\u0091\7v\2\2\u0091")
        buf.write("\u0092\7k\2\2\u0092\u0093\7p\2\2\u0093\u0094\7w\2\2\u0094")
        buf.write("\u0095\7g\2\2\u0095\20\3\2\2\2\u0096\u0097\7g\2\2\u0097")
        buf.write("\u0098\7n\2\2\u0098\u0099\7u\2\2\u0099\u009a\7g\2\2\u009a")
        buf.write("\22\3\2\2\2\u009b\u009c\7h\2\2\u009c\u009d\7q\2\2\u009d")
        buf.write("\u009e\7t\2\2\u009e\24\3\2\2\2\u009f\u00a0\7k\2\2\u00a0")
        buf.write("\u00a1\7h\2\2\u00a1\26\3\2\2\2\u00a2\u00a3\7t\2\2\u00a3")
        buf.write("\u00a4\7g\2\2\u00a4\u00a5\7v\2\2\u00a5\u00a6\7w\2\2\u00a6")
        buf.write("\u00a7\7t\2\2\u00a7\u00a8\7p\2\2\u00a8\30\3\2\2\2\u00a9")
        buf.write("\u00aa\7f\2\2\u00aa\u00ab\7q\2\2\u00ab\32\3\2\2\2\u00ac")
        buf.write("\u00ad\7y\2\2\u00ad\u00ae\7j\2\2\u00ae\u00af\7k\2\2\u00af")
        buf.write("\u00b0\7n\2\2\u00b0\u00b1\7g\2\2\u00b1\34\3\2\2\2\u00b2")
        buf.write("\u00b3\7-\2\2\u00b3\36\3\2\2\2\u00b4\u00b5\7,\2\2\u00b5")
        buf.write(" \3\2\2\2\u00b6\u00b7\7#\2\2\u00b7\"\3\2\2\2\u00b8\u00b9")
        buf.write("\7~\2\2\u00b9\u00ba\7~\2\2\u00ba$\3\2\2\2\u00bb\u00bc")
        buf.write("\7#\2\2\u00bc\u00bd\7?\2\2\u00bd&\3\2\2\2\u00be\u00bf")
        buf.write("\7>\2\2\u00bf(\3\2\2\2\u00c0\u00c1\7>\2\2\u00c1\u00c2")
        buf.write("\7?\2\2\u00c2*\3\2\2\2\u00c3\u00c4\7?\2\2\u00c4,\3\2\2")
        buf.write("\2\u00c5\u00c6\7/\2\2\u00c6.\3\2\2\2\u00c7\u00c8\7\61")
        buf.write("\2\2\u00c8\60\3\2\2\2\u00c9\u00ca\7\'\2\2\u00ca\62\3\2")
        buf.write("\2\2\u00cb\u00cc\7(\2\2\u00cc\u00cd\7(\2\2\u00cd\64\3")
        buf.write("\2\2\2\u00ce\u00cf\7?\2\2\u00cf\u00d0\7?\2\2\u00d0\66")
        buf.write("\3\2\2\2\u00d1\u00d2\7@\2\2\u00d28\3\2\2\2\u00d3\u00d4")
        buf.write("\7@\2\2\u00d4\u00d5\7?\2\2\u00d5:\3\2\2\2\u00d6\u00d8")
        buf.write("\t\2\2\2\u00d7\u00d6\3\2\2\2\u00d8\u00d9\3\2\2\2\u00d9")
        buf.write("\u00d7\3\2\2\2\u00d9\u00da\3\2\2\2\u00da<\3\2\2\2\u00db")
        buf.write("\u00dd\5C\"\2\u00dc\u00db\3\2\2\2\u00dd\u00e0\3\2\2\2")
        buf.write("\u00de\u00dc\3\2\2\2\u00de\u00df\3\2\2\2\u00df\u00e2\3")
        buf.write("\2\2\2\u00e0\u00de\3\2\2\2\u00e1\u00e3\5A!\2\u00e2\u00e1")
        buf.write("\3\2\2\2\u00e2\u00e3\3\2\2\2\u00e3\u00e5\3\2\2\2\u00e4")
        buf.write("\u00e6\5C\"\2\u00e5\u00e4\3\2\2\2\u00e6\u00e7\3\2\2\2")
        buf.write("\u00e7\u00e5\3\2\2\2\u00e7\u00e8\3\2\2\2\u00e8\u00ea\3")
        buf.write("\2\2\2\u00e9\u00eb\5? \2\u00ea\u00e9\3\2\2\2\u00ea\u00eb")
        buf.write("\3\2\2\2\u00eb\u0100\3\2\2\2\u00ec\u00ee\5C\"\2\u00ed")
        buf.write("\u00ec\3\2\2\2\u00ee\u00ef\3\2\2\2\u00ef\u00ed\3\2\2\2")
        buf.write("\u00ef\u00f0\3\2\2\2\u00f0\u00f2\3\2\2\2\u00f1\u00f3\5")
        buf.write("A!\2\u00f2\u00f1\3\2\2\2\u00f2\u00f3\3\2\2\2\u00f3\u00fd")
        buf.write("\3\2\2\2\u00f4\u00f6\5C\"\2\u00f5\u00f4\3\2\2\2\u00f6")
        buf.write("\u00f9\3\2\2\2\u00f7\u00f5\3\2\2\2\u00f7\u00f8\3\2\2\2")
        buf.write("\u00f8\u00fb\3\2\2\2\u00f9\u00f7\3\2\2\2\u00fa\u00fc\5")
        buf.write("? \2\u00fb\u00fa\3\2\2\2\u00fb\u00fc\3\2\2\2\u00fc\u00fe")
        buf.write("\3\2\2\2\u00fd\u00f7\3\2\2\2\u00fd\u00fe\3\2\2\2\u00fe")
        buf.write("\u0100\3\2\2\2\u00ff\u00de\3\2\2\2\u00ff\u00ed\3\2\2\2")
        buf.write("\u0100>\3\2\2\2\u0101\u0103\t\3\2\2\u0102\u0104\7/\2\2")
        buf.write("\u0103\u0102\3\2\2\2\u0103\u0104\3\2\2\2\u0104\u0106\3")
        buf.write("\2\2\2\u0105\u0107\5C\"\2\u0106\u0105\3\2\2\2\u0107\u0108")
        buf.write("\3\2\2\2\u0108\u0106\3\2\2\2\u0108\u0109\3\2\2\2\u0109")
        buf.write("@\3\2\2\2\u010a\u010b\7\60\2\2\u010bB\3\2\2\2\u010c\u010d")
        buf.write("\t\2\2\2\u010dD\3\2\2\2\u010e\u0111\5G$\2\u010f\u0111")
        buf.write("\5I%\2\u0110\u010e\3\2\2\2\u0110\u010f\3\2\2\2\u0111F")
        buf.write("\3\2\2\2\u0112\u0113\7v\2\2\u0113\u0114\7t\2\2\u0114\u0115")
        buf.write("\7w\2\2\u0115\u0116\7g\2\2\u0116H\3\2\2\2\u0117\u0118")
        buf.write("\7h\2\2\u0118\u0119\7c\2\2\u0119\u011a\7n\2\2\u011a\u011b")
        buf.write("\7u\2\2\u011b\u011c\7g\2\2\u011cJ\3\2\2\2\u011d\u011e")
        buf.write("\7\61\2\2\u011e\u011f\7,\2\2\u011f\u0123\3\2\2\2\u0120")
        buf.write("\u0122\13\2\2\2\u0121\u0120\3\2\2\2\u0122\u0125\3\2\2")
        buf.write("\2\u0123\u0124\3\2\2\2\u0123\u0121\3\2\2\2\u0124\u0126")
        buf.write("\3\2\2\2\u0125\u0123\3\2\2\2\u0126\u0127\7,\2\2\u0127")
        buf.write("\u0132\7\61\2\2\u0128\u0129\7\61\2\2\u0129\u012a\7\61")
        buf.write("\2\2\u012a\u012e\3\2\2\2\u012b\u012d\n\4\2\2\u012c\u012b")
        buf.write("\3\2\2\2\u012d\u0130\3\2\2\2\u012e\u012c\3\2\2\2\u012e")
        buf.write("\u012f\3\2\2\2\u012f\u0132\3\2\2\2\u0130\u012e\3\2\2\2")
        buf.write("\u0131\u011d\3\2\2\2\u0131\u0128\3\2\2\2\u0132\u0133\3")
        buf.write("\2\2\2\u0133\u0134\b&\2\2\u0134L\3\2\2\2\u0135\u0136\7")
        buf.write("*\2\2\u0136N\3\2\2\2\u0137\u0138\7+\2\2\u0138P\3\2\2\2")
        buf.write("\u0139\u013a\7}\2\2\u013aR\3\2\2\2\u013b\u013c\7\177\2")
        buf.write("\2\u013cT\3\2\2\2\u013d\u013e\7]\2\2\u013eV\3\2\2\2\u013f")
        buf.write("\u0140\7_\2\2\u0140X\3\2\2\2\u0141\u0142\7=\2\2\u0142")
        buf.write("Z\3\2\2\2\u0143\u0144\7.\2\2\u0144\\\3\2\2\2\u0145\u0147")
        buf.write("\t\5\2\2\u0146\u0145\3\2\2\2\u0147\u0148\3\2\2\2\u0148")
        buf.write("\u0146\3\2\2\2\u0148\u0149\3\2\2\2\u0149\u014a\3\2\2\2")
        buf.write("\u014a\u014b\b/\2\2\u014b^\3\2\2\2\u014c\u0150\t\6\2\2")
        buf.write("\u014d\u014f\t\7\2\2\u014e\u014d\3\2\2\2\u014f\u0152\3")
        buf.write("\2\2\2\u0150\u014e\3\2\2\2\u0150\u0151\3\2\2\2\u0151`")
        buf.write("\3\2\2\2\u0152\u0150\3\2\2\2\u0153\u0159\7$\2\2\u0154")
        buf.write("\u0155\7^\2\2\u0155\u0158\t\b\2\2\u0156\u0158\n\t\2\2")
        buf.write("\u0157\u0154\3\2\2\2\u0157\u0156\3\2\2\2\u0158\u015b\3")
        buf.write("\2\2\2\u0159\u0157\3\2\2\2\u0159\u015a\3\2\2\2\u015a\u015c")
        buf.write("\3\2\2\2\u015b\u0159\3\2\2\2\u015c\u015d\7$\2\2\u015d")
        buf.write("\u015e\b\61\3\2\u015eb\3\2\2\2\u015f\u0165\7$\2\2\u0160")
        buf.write("\u0161\7^\2\2\u0161\u0164\t\n\2\2\u0162\u0164\n\13\2\2")
        buf.write("\u0163\u0160\3\2\2\2\u0163\u0162\3\2\2\2\u0164\u0167\3")
        buf.write("\2\2\2\u0165\u0163\3\2\2\2\u0165\u0166\3\2\2\2\u0166\u0168")
        buf.write("\3\2\2\2\u0167\u0165\3\2\2\2\u0168\u0169\7^\2\2\u0169")
        buf.write("\u016a\n\b\2\2\u016a\u016b\3\2\2\2\u016b\u016c\b\62\4")
        buf.write("\2\u016cd\3\2\2\2\u016d\u0173\7$\2\2\u016e\u016f\7^\2")
        buf.write("\2\u016f\u0172\t\b\2\2\u0170\u0172\n\t\2\2\u0171\u016e")
        buf.write("\3\2\2\2\u0171\u0170\3\2\2\2\u0172\u0175\3\2\2\2\u0173")
        buf.write("\u0171\3\2\2\2\u0173\u0174\3\2\2\2\u0174\u0177\3\2\2\2")
        buf.write("\u0175\u0173\3\2\2\2\u0176\u0178\7^\2\2\u0177\u0176\3")
        buf.write("\2\2\2\u0177\u0178\3\2\2\2\u0178\u0179\3\2\2\2\u0179\u017a")
        buf.write("\b\63\5\2\u017af\3\2\2\2\u017b\u017c\13\2\2\2\u017c\u017d")
        buf.write("\b\64\6\2\u017dh\3\2\2\2\35\2\u00d9\u00de\u00e2\u00e7")
        buf.write("\u00ea\u00ef\u00f2\u00f7\u00fb\u00fd\u00ff\u0103\u0108")
        buf.write("\u0110\u0123\u012e\u0131\u0148\u0150\u0157\u0159\u0163")
        buf.write("\u0165\u0171\u0173\u0177\7\b\2\2\3\61\2\3\62\3\3\63\4")
        buf.write("\3\64\5")
        return buf.getvalue()


class MCLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    INT = 1
    FLOAT = 2
    VOID = 3
    BOOLEAN = 4
    STRING = 5
    BREAK = 6
    CONTINUE = 7
    ELSE = 8
    FOR = 9
    IF = 10
    RETURN = 11
    DO = 12
    WHILE = 13
    ADD = 14
    MUL = 15
    NOT = 16
    OR = 17
    NOTEQ = 18
    LESS = 19
    LESSEQ = 20
    ASSIGN = 21
    SUB = 22
    DIV = 23
    MOD = 24
    AND = 25
    EQ = 26
    GREA = 27
    GREAEQ = 28
    INTLIT = 29
    FLOATLIT = 30
    BOOLLIT = 31
    TRUE = 32
    FALSE = 33
    COMMENT = 34
    LB = 35
    RB = 36
    LP = 37
    RP = 38
    LSB = 39
    RSB = 40
    SM = 41
    CM = 42
    WS = 43
    ID = 44
    STRINGLIT = 45
    ILLEGAL_ESCAPE = 46
    UNCLOSE_STRING = 47
    ERROR_CHAR = 48

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'int'", "'float'", "'void'", "'boolean'", "'string'", "'break'", 
            "'continue'", "'else'", "'for'", "'if'", "'return'", "'do'", 
            "'while'", "'+'", "'*'", "'!'", "'||'", "'!='", "'<'", "'<='", 
            "'='", "'-'", "'/'", "'%'", "'&&'", "'=='", "'>'", "'>='", "'true'", 
            "'false'", "'('", "')'", "'{'", "'}'", "'['", "']'", "';'", 
            "','" ]

    symbolicNames = [ "<INVALID>",
            "INT", "FLOAT", "VOID", "BOOLEAN", "STRING", "BREAK", "CONTINUE", 
            "ELSE", "FOR", "IF", "RETURN", "DO", "WHILE", "ADD", "MUL", 
            "NOT", "OR", "NOTEQ", "LESS", "LESSEQ", "ASSIGN", "SUB", "DIV", 
            "MOD", "AND", "EQ", "GREA", "GREAEQ", "INTLIT", "FLOATLIT", 
            "BOOLLIT", "TRUE", "FALSE", "COMMENT", "LB", "RB", "LP", "RP", 
            "LSB", "RSB", "SM", "CM", "WS", "ID", "STRINGLIT", "ILLEGAL_ESCAPE", 
            "UNCLOSE_STRING", "ERROR_CHAR" ]

    ruleNames = [ "INT", "FLOAT", "VOID", "BOOLEAN", "STRING", "BREAK", 
                  "CONTINUE", "ELSE", "FOR", "IF", "RETURN", "DO", "WHILE", 
                  "ADD", "MUL", "NOT", "OR", "NOTEQ", "LESS", "LESSEQ", 
                  "ASSIGN", "SUB", "DIV", "MOD", "AND", "EQ", "GREA", "GREAEQ", 
                  "INTLIT", "FLOATLIT", "Exponent", "Dot", "DIGIT", "BOOLLIT", 
                  "TRUE", "FALSE", "COMMENT", "LB", "RB", "LP", "RP", "LSB", 
                  "RSB", "SM", "CM", "WS", "ID", "STRINGLIT", "ILLEGAL_ESCAPE", 
                  "UNCLOSE_STRING", "ERROR_CHAR" ]

    grammarFileName = "MC.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    def emit(self):
        tk = self.type
        if tk == self.UNCLOSE_STRING:
            result = super().emit();
            raise UncloseString(result.text);
        elif tk == self.ILLEGAL_ESCAPE:
            result = super().emit();
            raise IllegalEscape(result.text);
        elif tk == self.ERROR_CHAR:
            result = super().emit();
            raise ErrorToken(result.text);
        else:
            return super().emit();


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[47] = self.STRINGLIT_action 
            actions[48] = self.ILLEGAL_ESCAPE_action 
            actions[49] = self.UNCLOSE_STRING_action 
            actions[50] = self.ERROR_CHAR_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def STRINGLIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:

               self.text=self.text[1:-1]

     

    def ILLEGAL_ESCAPE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 1:

                raise IllegalEscape(self.text[1:])

     

    def UNCLOSE_STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 2:

               raise UncloseString(self.text[1:])

     

    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 3:

                raise ErrorToken(self.text);

     


