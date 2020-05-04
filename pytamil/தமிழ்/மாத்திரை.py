import regex
from pytamil.தமிழ் import எழுத்து
# -*- coding: utf-8 -*-

import sys
import antlr4
from antlr4 import *
from antlr4.tree.Trees import Trees
import os

# from codegen import codegen
from pytamil.தமிழ்.codegen.மாத்திரைLexer import மாத்திரைLexer
from pytamil.தமிழ்.codegen.மாத்திரைParser import மாத்திரைParser
from pytamil.தமிழ்.codegen.மாத்திரைListener import மாத்திரைListener
from pytamil.தமிழ்.codegen.மாத்திரைVisitor import மாத்திரைVisitor


from codecs import open
from nltk import Tree as nltkTree
from nltk.treeprettyprinter import TreePrettyPrinter

#                      மாத்திரை                                           
#       __________________|_________________________________________       
#      |         |                   மொழியிடை                    |     
#      |         |                      |                           |      
#  மொழிமுதல்  மொழியிடை          உயிர்மெய்க்குறில்               மொழியிறுதி
#      |         |         _____________|_______________            |      
# உயிர்நெடில்   மெய்     மெய்                     உயிர்க்குறில்    மெய்   
#      |         |        |                             |           |      
#      ஊ         க்       க்                            அ           ம்    

# calculate மாத்திரை for rules at second level. 

class நம்மாத்திரைListener(மாத்திரைListener):
    def __init__(self):
        self.seq = []

    def enterஉயிர்க்குறில்(self, ctx:மாத்திரைParser.உயிர்க்குறில்Context):
        if ctx.parentCtx.parentCtx.getRuleIndex() == ctx.parser.RULE_மாத்திரை:
            self.seq.append([ctx.getText(), ctx.parser.ruleNames[ctx.getRuleIndex()] , 1])
    
    def enterஉயிர்நெடில்(self, ctx:மாத்திரைParser.உயிர்நெடில்Context):
        if ctx.parentCtx.parentCtx.getRuleIndex() == ctx.parser.RULE_மாத்திரை:
            self.seq.append([ctx.getText(),  ctx.parser.ruleNames[ctx.getRuleIndex()] ,2])

    def enterமெய்(self, ctx:மாத்திரைParser.மெய்Context):
        if ctx.parentCtx.parentCtx.getRuleIndex() == ctx.parser.RULE_மாத்திரை:
            self.seq.append([ctx.getText(), ctx.parser.ruleNames[ctx.getRuleIndex()] , 0.5])

    def enterஆய்தம்(self, ctx:மாத்திரைParser.ஆய்தம்Context):
        if ctx.parentCtx.parentCtx.getRuleIndex() == ctx.parser.RULE_மாத்திரை:
            self.seq.append([ctx.getText(), ctx.parser.ruleNames[ctx.getRuleIndex()] , 0.5])

    def enterஉயிர்மெய்க்குறில்(self, ctx:மாத்திரைParser.உயிர்மெய்க்குறில்Context):
        if ctx.parentCtx.parentCtx.getRuleIndex() == ctx.parser.RULE_மாத்திரை:
            எழுத்துவரிசை = எழுத்து.எழுத்தாக்கு(ctx.getText())
            உயிர்மெய் = எழுத்து.உயிர்மெய்தொகை(எழுத்துவரிசை)
            self.seq.append([உயிர்மெய், ctx.parser.ruleNames[ctx.getRuleIndex()] , 1])

    def enterஉயிர்மெய்நெடில்(self, ctx:மாத்திரைParser.உயிர்மெய்நெடில்Context):
        if ctx.parentCtx.parentCtx.getRuleIndex() == ctx.parser.RULE_மாத்திரை:
            எழுத்துவரிசை = எழுத்து.எழுத்தாக்கு(ctx.getText())
            உயிர்மெய் = எழுத்து.உயிர்மெய்தொகை(எழுத்துவரிசை)
            self.seq.append([உயிர்மெய், ctx.parser.ruleNames[ctx.getRuleIndex()] , 2])

    def enterஉயிரளபெடை(self, ctx:மாத்திரைParser.உயிரளபெடைContext):
        if ctx.parentCtx.parentCtx.getRuleIndex() == ctx.parser.RULE_மாத்திரை:
            எழுத்துவரிசை = எழுத்து.எழுத்தாக்கு(ctx.getText())
            உயிர்மெய் = எழுத்து.உயிர்மெய்தொகை(எழுத்துவரிசை)
            self.seq.append([உயிர்மெய், ctx.parser.ruleNames[ctx.getRuleIndex()] , 3])

    
    # def enterமொழியிடை(self, ctx:மாத்திரைParser.மொழியிடைContext):
    #     self.seq.append([ctx.getText(), 1])
    #     a= ctx.getParent().getText()s

# class நம்மாத்திரைVisitor(மாத்திரைVisitor):
#     def __init__(self):
#         self.seq = []

#     def visitமொழியிடை(self, ctx:மாத்திரைParser.மொழியிடைContext):
#         self.seq.append([ctx.getText(), 1])
#         return self.visitChildren(ctx)
 
def printtree(தொடர்):
    # infilename = os.path.join(os.path.dirname(__file__),'யாப்பு/வெண்பாinput.txt')
    # outfilename = os.path.join(os.path.dirname(__file__),'யாப்பு/வெண்பாoutput.txt')
    # data = open(infilename).read()   
    
    விரிதொடர் = எழுத்து.உயிர்மெய்விரி(தொடர்)
    input_stream = antlr4.InputStream(விரிதொடர்)
    
    lexer = மாத்திரைLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = மாத்திரைParser(stream)
    tree = parser.மாத்திரை()

    # print(tree.toStringTree())
    strtree = Trees.toStringTree(tree, None, parser)
    print(strtree)
    t = nltkTree.fromstring(strtree)
    # t.pretty_print()
    treestr = TreePrettyPrinter(t).text()
    # print (treestr)
    # t.pprint(margin=70, indent=0, nodesep=u'', parens=u'()', quotes=False)
    # pprint(Trees.toStringTree(tree, None, parser), width=20, indent=4)
 
    return treestr

def printtree_tofile(தொடர், outfilename):
    treestr = printtree(தொடர்)
    with open(outfilename, 'w', encoding='utf8') as f:
        f.write( treestr)


def மாத்திரைவரிசை_கொடு(தொடர்):
    விரிதொடர் = எழுத்து.உயிர்மெய்விரி(தொடர்)
    input_stream = antlr4.InputStream(விரிதொடர்)

    lexer = மாத்திரைLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = மாத்திரைParser(stream)
    tree = parser.மாத்திரை()

    நம்listener = நம்மாத்திரைListener()
    walker = ParseTreeWalker()
    walker.walk(நம்listener, tree)

    # நம்visitor = நம்மாத்திரைVisitor()
    # நம்visitor.visit(tree)

    return நம்listener.seq





def மொத்தமாத்திரை(தொடர்):
    மாத்திரைவரிசை = மாத்திரை_கொடு(தொடர்)
    மாத்திரை=0
    for மா in மாத்திரைவரிசை:
        மாத்திரை = மாத்திரை + மா
    
    return மாத்திரை



    