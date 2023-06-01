
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'leftLTLTEGTGTEleftPLUSMINUSleftMULTDIVleftEQUALDIFFleftLPARENRPARENleftLBRACERBRACEleftLBRACKETRBRACKETAND ARRAY ASSIGN CHAR COLON COMMA COMPILE CTF CTI DIFF DIV DOT ELSE END EPOCHS EQUAL FALSE FIT FLOAT FOR FUNCESP FUNCTION GETWEIGHTS GT GTE ID IF IFEQUAL INT LAYERS LBRACE LBRACKET LPAREN LT LTE MAIN MATRIX MEAN MINUS MULT NUMPY OR PLUS PREDICT PRINT PROGRAM QUOTE RBRACE RBRACKET READ RETURN RPAREN SEMICOLON SEQUENTIAL STRING TRUE UNITS VAR VERBOSE VOID WHILEprogram : PROGRAM gotomain ID SEMICOLON decvar modules mainfunctiongotomain : decvar : VAR decvarp\n              | VAR decvarp decvar\n              |decvarp : type decvarpp SEMICOLONdecvarpp : ID COMMA decvarpp\n                | IDtype : INT\n            | FLOATfunction : FUNCTION decfunctype decfunc LPAREN param RPAREN LBRACE body RETURN exp SEMICOLON RBRACEdecfunctype : typedecfunc : IDvoidfunction : FUNCTION VOID decfunc LPAREN param RPAREN LBRACE body RBRACEdecfuncmain : mainfunction : MAIN decfuncmain LPAREN RPAREN LBRACE body RBRACEmodules : function modules\n               | voidfunction modules\n               | function\n               | voidfunctionbody : decvar statements body\n            | statements body\n            | decvar\n            | param : type ID\n             | type ID COMMA param\n             |exp : texp \n           | texp OR exptexp : gexp \n            | gexp AND texpgexp : mexp \n            | mexp gexpp mexpgexpp : LT\n             | GT\n             | IFEQUAL\n             | DIFFmexp : t\n            | mexp PLUS t\n            | mexp MINUS tt : f \n         | t MULT f\n         | t DIV ff : LPAREN exp RPAREN\n         | CTI\n         | CTF\n         | var\n         | callstatements : assign\n                 |  function\n                 |  voidfunction\n                 |  call\n                 |  read\n                 |  print\n                 |  if\n                 |  while\n                 |  for\n                 |  array\n                 |  matrix\n                 |  mean\n                 |  layers\n                 |  sequential\n                 |  compileassign : var EQUAL exp SEMICOLONread : READ LPAREN var RPAREN SEMICOLONprint : PRINT LPAREN printp SEMICOLONprintp : exp RPAREN\n              | exp COMMA printpvar : ID call : ID LPAREN callp RPARENcallp : exp COMMA callp\n             | exp\n             | if : IF LPAREN ifexp RPAREN quadsIf LBRACE body RBRACE ifelse jumpsIf SEMICOLONifexp : exp  ifelse : \n               | ELSE quadsElse LBRACE body RBRACEquadsIf : jumpsIf : quadsElse :  while : WHILE saveJumps LPAREN whilexp RPAREN quadsWhile LBRACE body RBRACE jumpsWhile SEMICOLONwhilexp : exp  saveJumps : quadsWhile : jumpsWhile :for : FOR LPAREN var SEMICOLON exp SEMICOLON exp RPAREN LBRACKET statements forp forp : RBRACKET\n             | statements forp funcesp : array\n                | mean\n                | layers\n                | sequential\n                | compile\n                | fit\n                | predict\n                | getweights array : ARRAY ID LBRACKET exp RBRACKET EQUAL LBRACKET arrvalues RBRACKET SEMICOLONarrvalues : exp\n                 | exp COMMA arrvaluesmatrix : MATRIX ID LBRACKET exp RBRACKET LBRACKET exp RBRACKET EQUAL LBRACKET matvalues RBRACKET SEMICOLONmatvalues : exp\n                 | exp COMMA matvaluesmean : MEAN LPAREN ID RPAREN SEMICOLONlayers : LAYERS LPAREN UNITS EQUAL CTI RPAREN SEMICOLON sequential : SEQUENTIAL LPAREN RPAREN SEMICOLON compile : COMPILE LPAREN CTF RPAREN SEMICOLON fit : FIT LPAREN ID COMMA ID COMMA EPOCHS EQUAL CTI COMMA VERBOSE EQUAL CTI  predict : ID EQUAL sequential DOT PREDICT LPAREN LBRACKET predictp predictp : INT RBRACKET RPAREN\n                 | FLOAT RBRACKET RPAREN getweights : layers DOT GETWEIGHTS LPAREN RPARENempty :'
    
_lr_action_items = {'PROGRAM':([0,],[2,]),'$end':([1,16,78,],[0,-1,-16,]),'ID':([2,3,12,13,14,15,20,21,22,23,30,31,38,40,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,69,70,75,77,79,81,82,83,84,85,87,90,105,118,120,121,126,127,128,129,130,131,132,133,134,135,136,137,138,139,141,142,144,146,150,155,167,174,176,178,180,182,184,186,188,190,200,201,207,209,210,211,212,213,214,215,216,220,221,225,],[-2,4,-3,25,-9,-10,28,28,-12,-4,-6,25,42,63,63,63,-49,-50,-51,-52,-53,-54,-55,-56,-57,-58,-59,-60,-61,-62,-63,88,89,63,63,63,109,109,113,109,109,113,122,109,109,109,109,109,-14,-64,109,109,109,109,109,-34,-35,-36,-37,109,109,-70,109,-66,109,109,-105,-65,-103,-106,63,109,109,-11,63,109,-104,63,109,63,-97,109,-74,63,-81,63,-86,-87,-88,109,-100,]),'SEMICOLON':([4,24,25,35,98,99,100,101,102,103,104,106,107,108,109,113,114,119,124,141,143,145,153,156,157,158,159,160,161,162,163,164,165,168,171,183,191,197,199,202,204,206,222,223,],[5,30,-8,-7,-47,128,-28,-30,-32,-38,-41,-45,-46,-48,-69,-69,144,150,155,-70,167,-67,174,176,177,-29,-31,-33,-39,-40,-42,-43,-44,-68,180,190,-76,-79,-85,209,211,213,225,-77,]),'VAR':([5,12,30,40,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,75,77,79,127,128,141,144,155,167,174,176,178,184,186,190,209,211,212,213,215,216,220,225,],[7,7,-6,7,7,-49,-50,-51,-52,-53,-54,-55,-56,-57,-58,-59,-60,-61,-62,-63,7,7,7,-14,-64,-70,-66,-105,-65,-103,-106,7,-11,7,-104,-97,-74,7,-81,-86,-87,-88,-100,]),'FUNCTION':([5,6,9,10,12,23,30,40,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,75,77,79,127,128,141,144,155,167,174,176,178,184,186,190,200,207,209,211,212,213,214,215,216,220,225,],[-5,11,11,11,-3,-4,-6,11,11,11,-49,-50,-51,-52,-53,-54,-55,-56,-57,-58,-59,-60,-61,-62,-63,11,11,11,-14,-64,-70,-66,-105,-65,-103,-106,11,-11,11,-104,11,11,-97,-74,11,-81,11,-86,-87,-88,-100,]),'INT':([7,11,33,34,76,],[14,14,14,14,14,]),'FLOAT':([7,11,33,34,76,],[15,15,15,15,15,]),'MAIN':([8,9,10,18,19,127,184,],[17,-19,-20,-17,-18,-14,-11,]),'VOID':([11,],[21,]),'READ':([12,23,30,40,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,75,77,79,127,128,141,144,155,167,174,176,178,184,186,190,200,207,209,211,212,213,214,215,216,220,225,],[-3,-4,-6,64,64,64,-49,-50,-51,-52,-53,-54,-55,-56,-57,-58,-59,-60,-61,-62,-63,64,64,64,-14,-64,-70,-66,-105,-65,-103,-106,64,-11,64,-104,64,64,-97,-74,64,-81,64,-86,-87,-88,-100,]),'PRINT':([12,23,30,40,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,75,77,79,127,128,141,144,155,167,174,176,178,184,186,190,200,207,209,211,212,213,214,215,216,220,225,],[-3,-4,-6,65,65,65,-49,-50,-51,-52,-53,-54,-55,-56,-57,-58,-59,-60,-61,-62,-63,65,65,65,-14,-64,-70,-66,-105,-65,-103,-106,65,-11,65,-104,65,65,-97,-74,65,-81,65,-86,-87,-88,-100,]),'IF':([12,23,30,40,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,75,77,79,127,128,141,144,155,167,174,176,178,184,186,190,200,207,209,211,212,213,214,215,216,220,225,],[-3,-4,-6,66,66,66,-49,-50,-51,-52,-53,-54,-55,-56,-57,-58,-59,-60,-61,-62,-63,66,66,66,-14,-64,-70,-66,-105,-65,-103,-106,66,-11,66,-104,66,66,-97,-74,66,-81,66,-86,-87,-88,-100,]),'WHILE':([12,23,30,40,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,75,77,79,127,128,141,144,155,167,174,176,178,184,186,190,200,207,209,211,212,213,214,215,216,220,225,],[-3,-4,-6,67,67,67,-49,-50,-51,-52,-53,-54,-55,-56,-57,-58,-59,-60,-61,-62,-63,67,67,67,-14,-64,-70,-66,-105,-65,-103,-106,67,-11,67,-104,67,67,-97,-74,67,-81,67,-86,-87,-88,-100,]),'FOR':([12,23,30,40,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,75,77,79,127,128,141,144,155,167,174,176,178,184,186,190,200,207,209,211,212,213,214,215,216,220,225,],[-3,-4,-6,68,68,68,-49,-50,-51,-52,-53,-54,-55,-56,-57,-58,-59,-60,-61,-62,-63,68,68,68,-14,-64,-70,-66,-105,-65,-103,-106,68,-11,68,-104,68,68,-97,-74,68,-81,68,-86,-87,-88,-100,]),'ARRAY':([12,23,30,40,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,75,77,79,127,128,141,144,155,167,174,176,178,184,186,190,200,207,209,211,212,213,214,215,216,220,225,],[-3,-4,-6,69,69,69,-49,-50,-51,-52,-53,-54,-55,-56,-57,-58,-59,-60,-61,-62,-63,69,69,69,-14,-64,-70,-66,-105,-65,-103,-106,69,-11,69,-104,69,69,-97,-74,69,-81,69,-86,-87,-88,-100,]),'MATRIX':([12,23,30,40,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,75,77,79,127,128,141,144,155,167,174,176,178,184,186,190,200,207,209,211,212,213,214,215,216,220,225,],[-3,-4,-6,70,70,70,-49,-50,-51,-52,-53,-54,-55,-56,-57,-58,-59,-60,-61,-62,-63,70,70,70,-14,-64,-70,-66,-105,-65,-103,-106,70,-11,70,-104,70,70,-97,-74,70,-81,70,-86,-87,-88,-100,]),'MEAN':([12,23,30,40,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,75,77,79,127,128,141,144,155,167,174,176,178,184,186,190,200,207,209,211,212,213,214,215,216,220,225,],[-3,-4,-6,71,71,71,-49,-50,-51,-52,-53,-54,-55,-56,-57,-58,-59,-60,-61,-62,-63,71,71,71,-14,-64,-70,-66,-105,-65,-103,-106,71,-11,71,-104,71,71,-97,-74,71,-81,71,-86,-87,-88,-100,]),'LAYERS':([12,23,30,40,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,75,77,79,127,128,141,144,155,167,174,176,178,184,186,190,200,207,209,211,212,213,214,215,216,220,225,],[-3,-4,-6,72,72,72,-49,-50,-51,-52,-53,-54,-55,-56,-57,-58,-59,-60,-61,-62,-63,72,72,72,-14,-64,-70,-66,-105,-65,-103,-106,72,-11,72,-104,72,72,-97,-74,72,-81,72,-86,-87,-88,-100,]),'SEQUENTIAL':([12,23,30,40,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,75,77,79,127,128,141,144,155,167,174,176,178,184,186,190,200,207,209,211,212,213,214,215,216,220,225,],[-3,-4,-6,73,73,73,-49,-50,-51,-52,-53,-54,-55,-56,-57,-58,-59,-60,-61,-62,-63,73,73,73,-14,-64,-70,-66,-105,-65,-103,-106,73,-11,73,-104,73,73,-97,-74,73,-81,73,-86,-87,-88,-100,]),'COMPILE':([12,23,30,40,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,75,77,79,127,128,141,144,155,167,174,176,178,184,186,190,200,207,209,211,212,213,214,215,216,220,225,],[-3,-4,-6,74,74,74,-49,-50,-51,-52,-53,-54,-55,-56,-57,-58,-59,-60,-61,-62,-63,74,74,74,-14,-64,-70,-66,-105,-65,-103,-106,74,-11,74,-104,74,74,-97,-74,74,-81,74,-86,-87,-88,-100,]),'RBRACE':([12,23,30,40,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,77,79,80,96,97,127,128,141,144,155,167,174,176,177,178,184,185,186,190,192,209,211,212,213,215,216,219,220,225,],[-3,-4,-6,-5,78,-23,-5,-49,-50,-51,-52,-53,-54,-55,-56,-57,-58,-59,-60,-61,-62,-63,-5,-5,-22,127,-21,-14,-64,-70,-66,-105,-65,-103,-106,184,-5,-11,191,-5,-104,199,-97,-74,-5,-81,-86,-87,223,-88,-100,]),'RETURN':([12,23,30,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,75,79,80,94,97,127,128,141,144,155,167,174,176,184,190,209,211,213,215,216,220,225,],[-3,-4,-6,-23,-5,-49,-50,-51,-52,-53,-54,-55,-56,-57,-58,-59,-60,-61,-62,-63,-5,-5,-22,126,-21,-14,-64,-70,-66,-105,-65,-103,-106,-11,-104,-97,-74,-81,-86,-87,-88,-100,]),'LPAREN':([17,26,27,28,29,63,64,65,66,67,68,71,72,73,74,81,82,84,85,86,105,109,118,120,121,126,129,130,131,132,133,134,135,136,137,138,139,142,146,150,180,182,188,201,210,221,],[-15,32,33,-13,34,82,83,84,85,-83,87,90,91,92,93,105,105,105,105,118,105,82,105,105,105,105,105,105,105,105,105,-34,-35,-36,-37,105,105,105,105,105,105,105,105,105,105,105,]),'COMMA':([25,42,98,100,101,102,103,104,106,107,108,109,111,115,141,158,159,160,161,162,163,164,165,194,217,],[31,76,-47,-28,-30,-32,-38,-41,-45,-46,-48,-69,142,146,-70,-29,-31,-33,-39,-40,-42,-43,-44,201,221,]),'RPAREN':([32,33,34,37,39,42,76,82,92,95,98,100,101,102,103,104,106,107,108,109,110,111,112,113,115,116,117,122,125,140,141,142,148,149,158,159,160,161,162,163,164,165,166,175,187,],[36,-27,-27,41,43,-25,-27,-73,124,-26,-47,-28,-30,-32,-38,-41,-45,-46,-48,-69,141,-72,143,-69,145,147,-75,153,156,165,-70,-73,170,-82,-29,-31,-33,-39,-40,-42,-43,-44,-71,183,193,]),'LBRACE':([36,41,43,147,169,170,179,198,205,],[40,75,77,-78,178,-84,186,-80,212,]),'RBRACKET':([47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,98,100,101,102,103,104,106,107,108,109,127,128,141,144,151,152,155,158,159,160,161,162,163,164,165,167,174,176,184,189,190,194,195,207,208,209,211,213,214,215,216,217,218,220,224,225,],[-49,-50,-51,-52,-53,-54,-55,-56,-57,-58,-59,-60,-61,-62,-63,-47,-28,-30,-32,-38,-41,-45,-46,-48,-69,-14,-64,-70,-66,172,173,-105,-29,-31,-33,-39,-40,-42,-43,-44,-65,-103,-106,-11,196,-104,-98,202,216,-99,-97,-74,-81,216,-86,-87,-101,222,-88,-102,-100,]),'EQUAL':([62,63,123,172,196,],[81,-69,154,181,203,]),'CTI':([81,82,84,85,105,118,120,121,126,129,130,131,132,133,134,135,136,137,138,139,142,146,150,154,180,182,188,201,210,221,],[106,106,106,106,106,106,106,106,106,106,106,106,106,106,-34,-35,-36,-37,106,106,106,106,106,175,106,106,106,106,106,106,]),'CTF':([81,82,84,85,93,105,118,120,121,126,129,130,131,132,133,134,135,136,137,138,139,142,146,150,180,182,188,201,210,221,],[107,107,107,107,125,107,107,107,107,107,107,107,107,107,107,-34,-35,-36,-37,107,107,107,107,107,107,107,107,107,107,107,]),'LBRACKET':([88,89,173,181,193,203,],[120,121,182,188,200,210,]),'UNITS':([91,],[123,]),'MULT':([98,103,104,106,107,108,109,141,161,162,163,164,165,],[-47,138,-41,-45,-46,-48,-69,-70,138,138,-42,-43,-44,]),'DIV':([98,103,104,106,107,108,109,141,161,162,163,164,165,],[-47,139,-41,-45,-46,-48,-69,-70,139,139,-42,-43,-44,]),'PLUS':([98,102,103,104,106,107,108,109,141,160,161,162,163,164,165,],[-47,132,-38,-41,-45,-46,-48,-69,-70,132,-39,-40,-42,-43,-44,]),'MINUS':([98,102,103,104,106,107,108,109,141,160,161,162,163,164,165,],[-47,133,-38,-41,-45,-46,-48,-69,-70,133,-39,-40,-42,-43,-44,]),'LT':([98,102,103,104,106,107,108,109,141,161,162,163,164,165,],[-47,134,-38,-41,-45,-46,-48,-69,-70,-39,-40,-42,-43,-44,]),'GT':([98,102,103,104,106,107,108,109,141,161,162,163,164,165,],[-47,135,-38,-41,-45,-46,-48,-69,-70,-39,-40,-42,-43,-44,]),'IFEQUAL':([98,102,103,104,106,107,108,109,141,161,162,163,164,165,],[-47,136,-38,-41,-45,-46,-48,-69,-70,-39,-40,-42,-43,-44,]),'DIFF':([98,102,103,104,106,107,108,109,141,161,162,163,164,165,],[-47,137,-38,-41,-45,-46,-48,-69,-70,-39,-40,-42,-43,-44,]),'AND':([98,101,102,103,104,106,107,108,109,141,160,161,162,163,164,165,],[-47,130,-32,-38,-41,-45,-46,-48,-69,-70,-33,-39,-40,-42,-43,-44,]),'OR':([98,100,101,102,103,104,106,107,108,109,141,159,160,161,162,163,164,165,],[-47,129,-30,-32,-38,-41,-45,-46,-48,-69,-70,-31,-33,-39,-40,-42,-43,-44,]),'ELSE':([191,],[198,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'program':([0,],[1,]),'gotomain':([2,],[3,]),'decvar':([5,12,40,46,75,77,79,178,186,212,],[6,23,45,45,45,45,45,45,45,45,]),'modules':([6,9,10,],[8,18,19,]),'function':([6,9,10,40,45,46,75,77,79,178,186,200,207,212,214,],[9,9,9,48,48,48,48,48,48,48,48,48,48,48,48,]),'voidfunction':([6,9,10,40,45,46,75,77,79,178,186,200,207,212,214,],[10,10,10,49,49,49,49,49,49,49,49,49,49,49,49,]),'decvarp':([7,],[12,]),'type':([7,11,33,34,76,],[13,22,38,38,38,]),'mainfunction':([8,],[16,]),'decfunctype':([11,],[20,]),'decvarpp':([13,31,],[24,35,]),'decfuncmain':([17,],[26,]),'decfunc':([20,21,],[27,29,]),'param':([33,34,76,],[37,39,95,]),'body':([40,46,75,77,79,178,186,212,],[44,80,94,96,97,185,192,219,]),'statements':([40,45,46,75,77,79,178,186,200,207,212,214,],[46,79,46,46,46,46,46,46,207,214,46,214,]),'assign':([40,45,46,75,77,79,178,186,200,207,212,214,],[47,47,47,47,47,47,47,47,47,47,47,47,]),'call':([40,45,46,75,77,79,81,82,84,85,105,118,120,121,126,129,130,131,132,133,138,139,142,146,150,178,180,182,186,188,200,201,207,210,212,214,221,],[50,50,50,50,50,50,108,108,108,108,108,108,108,108,108,108,108,108,108,108,108,108,108,108,108,50,108,108,50,108,50,108,50,108,50,50,108,]),'read':([40,45,46,75,77,79,178,186,200,207,212,214,],[51,51,51,51,51,51,51,51,51,51,51,51,]),'print':([40,45,46,75,77,79,178,186,200,207,212,214,],[52,52,52,52,52,52,52,52,52,52,52,52,]),'if':([40,45,46,75,77,79,178,186,200,207,212,214,],[53,53,53,53,53,53,53,53,53,53,53,53,]),'while':([40,45,46,75,77,79,178,186,200,207,212,214,],[54,54,54,54,54,54,54,54,54,54,54,54,]),'for':([40,45,46,75,77,79,178,186,200,207,212,214,],[55,55,55,55,55,55,55,55,55,55,55,55,]),'array':([40,45,46,75,77,79,178,186,200,207,212,214,],[56,56,56,56,56,56,56,56,56,56,56,56,]),'matrix':([40,45,46,75,77,79,178,186,200,207,212,214,],[57,57,57,57,57,57,57,57,57,57,57,57,]),'mean':([40,45,46,75,77,79,178,186,200,207,212,214,],[58,58,58,58,58,58,58,58,58,58,58,58,]),'layers':([40,45,46,75,77,79,178,186,200,207,212,214,],[59,59,59,59,59,59,59,59,59,59,59,59,]),'sequential':([40,45,46,75,77,79,178,186,200,207,212,214,],[60,60,60,60,60,60,60,60,60,60,60,60,]),'compile':([40,45,46,75,77,79,178,186,200,207,212,214,],[61,61,61,61,61,61,61,61,61,61,61,61,]),'var':([40,45,46,75,77,79,81,82,83,84,85,87,105,118,120,121,126,129,130,131,132,133,138,139,142,146,150,178,180,182,186,188,200,201,207,210,212,214,221,],[62,62,62,62,62,62,98,98,112,98,98,119,98,98,98,98,98,98,98,98,98,98,98,98,98,98,98,62,98,98,62,98,62,98,62,98,62,62,98,]),'saveJumps':([67,],[86,]),'exp':([81,82,84,85,105,118,120,121,126,129,142,146,150,180,182,188,201,210,221,],[99,111,115,117,140,149,151,152,157,158,111,115,171,187,189,194,194,217,217,]),'texp':([81,82,84,85,105,118,120,121,126,129,130,142,146,150,180,182,188,201,210,221,],[100,100,100,100,100,100,100,100,100,100,159,100,100,100,100,100,100,100,100,100,]),'gexp':([81,82,84,85,105,118,120,121,126,129,130,142,146,150,180,182,188,201,210,221,],[101,101,101,101,101,101,101,101,101,101,101,101,101,101,101,101,101,101,101,101,]),'mexp':([81,82,84,85,105,118,120,121,126,129,130,131,142,146,150,180,182,188,201,210,221,],[102,102,102,102,102,102,102,102,102,102,102,160,102,102,102,102,102,102,102,102,102,]),'t':([81,82,84,85,105,118,120,121,126,129,130,131,132,133,142,146,150,180,182,188,201,210,221,],[103,103,103,103,103,103,103,103,103,103,103,103,161,162,103,103,103,103,103,103,103,103,103,]),'f':([81,82,84,85,105,118,120,121,126,129,130,131,132,133,138,139,142,146,150,180,182,188,201,210,221,],[104,104,104,104,104,104,104,104,104,104,104,104,104,104,163,164,104,104,104,104,104,104,104,104,104,]),'callp':([82,142,],[110,166,]),'printp':([84,146,],[114,168,]),'ifexp':([85,],[116,]),'gexpp':([102,],[131,]),'whilexp':([118,],[148,]),'quadsIf':([147,],[169,]),'quadsWhile':([170,],[179,]),'arrvalues':([188,201,],[195,208,]),'ifelse':([191,],[197,]),'jumpsIf':([197,],[204,]),'quadsElse':([198,],[205,]),'jumpsWhile':([199,],[206,]),'forp':([207,214,],[215,220,]),'matvalues':([210,221,],[218,224,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> program","S'",1,None,None,None),
  ('program -> PROGRAM gotomain ID SEMICOLON decvar modules mainfunction','program',7,'p_program','bixoParser.py',270),
  ('gotomain -> <empty>','gotomain',0,'p_gotomain','bixoParser.py',278),
  ('decvar -> VAR decvarp','decvar',2,'p_decvar','bixoParser.py',286),
  ('decvar -> VAR decvarp decvar','decvar',3,'p_decvar','bixoParser.py',287),
  ('decvar -> <empty>','decvar',0,'p_decvar','bixoParser.py',288),
  ('decvarp -> type decvarpp SEMICOLON','decvarp',3,'p_decvarp','bixoParser.py',294),
  ('decvarpp -> ID COMMA decvarpp','decvarpp',3,'p_decvarpp','bixoParser.py',331),
  ('decvarpp -> ID','decvarpp',1,'p_decvarpp','bixoParser.py',332),
  ('type -> INT','type',1,'p_type','bixoParser.py',341),
  ('type -> FLOAT','type',1,'p_type','bixoParser.py',342),
  ('function -> FUNCTION decfunctype decfunc LPAREN param RPAREN LBRACE body RETURN exp SEMICOLON RBRACE','function',12,'p_function','bixoParser.py',346),
  ('decfunctype -> type','decfunctype',1,'p_decfunctype','bixoParser.py',370),
  ('decfunc -> ID','decfunc',1,'p_decfunc','bixoParser.py',376),
  ('voidfunction -> FUNCTION VOID decfunc LPAREN param RPAREN LBRACE body RBRACE','voidfunction',9,'p_voidfunction','bixoParser.py',393),
  ('decfuncmain -> <empty>','decfuncmain',0,'p_decfuncmain','bixoParser.py',416),
  ('mainfunction -> MAIN decfuncmain LPAREN RPAREN LBRACE body RBRACE','mainfunction',7,'p_mainfunction','bixoParser.py',434),
  ('modules -> function modules','modules',2,'p_modules','bixoParser.py',456),
  ('modules -> voidfunction modules','modules',2,'p_modules','bixoParser.py',457),
  ('modules -> function','modules',1,'p_modules','bixoParser.py',458),
  ('modules -> voidfunction','modules',1,'p_modules','bixoParser.py',459),
  ('body -> decvar statements body','body',3,'p_body','bixoParser.py',467),
  ('body -> statements body','body',2,'p_body','bixoParser.py',468),
  ('body -> decvar','body',1,'p_body','bixoParser.py',469),
  ('body -> <empty>','body',0,'p_body','bixoParser.py',470),
  ('param -> type ID','param',2,'p_param','bixoParser.py',474),
  ('param -> type ID COMMA param','param',4,'p_param','bixoParser.py',475),
  ('param -> <empty>','param',0,'p_param','bixoParser.py',476),
  ('exp -> texp','exp',1,'p_exp','bixoParser.py',488),
  ('exp -> texp OR exp','exp',3,'p_exp','bixoParser.py',489),
  ('texp -> gexp','texp',1,'p_texp','bixoParser.py',518),
  ('texp -> gexp AND texp','texp',3,'p_texp','bixoParser.py',519),
  ('gexp -> mexp','gexp',1,'p_gexp','bixoParser.py',547),
  ('gexp -> mexp gexpp mexp','gexp',3,'p_gexp','bixoParser.py',548),
  ('gexpp -> LT','gexpp',1,'p_gexpp','bixoParser.py',669),
  ('gexpp -> GT','gexpp',1,'p_gexpp','bixoParser.py',670),
  ('gexpp -> IFEQUAL','gexpp',1,'p_gexpp','bixoParser.py',671),
  ('gexpp -> DIFF','gexpp',1,'p_gexpp','bixoParser.py',672),
  ('mexp -> t','mexp',1,'p_mexp','bixoParser.py',676),
  ('mexp -> mexp PLUS t','mexp',3,'p_mexp','bixoParser.py',677),
  ('mexp -> mexp MINUS t','mexp',3,'p_mexp','bixoParser.py',678),
  ('t -> f','t',1,'p_t','bixoParser.py',782),
  ('t -> t MULT f','t',3,'p_t','bixoParser.py',783),
  ('t -> t DIV f','t',3,'p_t','bixoParser.py',784),
  ('f -> LPAREN exp RPAREN','f',3,'p_f','bixoParser.py',881),
  ('f -> CTI','f',1,'p_f','bixoParser.py',882),
  ('f -> CTF','f',1,'p_f','bixoParser.py',883),
  ('f -> var','f',1,'p_f','bixoParser.py',884),
  ('f -> call','f',1,'p_f','bixoParser.py',885),
  ('statements -> assign','statements',1,'p_statements','bixoParser.py',897),
  ('statements -> function','statements',1,'p_statements','bixoParser.py',898),
  ('statements -> voidfunction','statements',1,'p_statements','bixoParser.py',899),
  ('statements -> call','statements',1,'p_statements','bixoParser.py',900),
  ('statements -> read','statements',1,'p_statements','bixoParser.py',901),
  ('statements -> print','statements',1,'p_statements','bixoParser.py',902),
  ('statements -> if','statements',1,'p_statements','bixoParser.py',903),
  ('statements -> while','statements',1,'p_statements','bixoParser.py',904),
  ('statements -> for','statements',1,'p_statements','bixoParser.py',905),
  ('statements -> array','statements',1,'p_statements','bixoParser.py',906),
  ('statements -> matrix','statements',1,'p_statements','bixoParser.py',907),
  ('statements -> mean','statements',1,'p_statements','bixoParser.py',908),
  ('statements -> layers','statements',1,'p_statements','bixoParser.py',909),
  ('statements -> sequential','statements',1,'p_statements','bixoParser.py',910),
  ('statements -> compile','statements',1,'p_statements','bixoParser.py',911),
  ('assign -> var EQUAL exp SEMICOLON','assign',4,'p_assign','bixoParser.py',915),
  ('read -> READ LPAREN var RPAREN SEMICOLON','read',5,'p_read','bixoParser.py',980),
  ('print -> PRINT LPAREN printp SEMICOLON','print',4,'p_print','bixoParser.py',1003),
  ('printp -> exp RPAREN','printp',2,'p_printp','bixoParser.py',1011),
  ('printp -> exp COMMA printp','printp',3,'p_printp','bixoParser.py',1012),
  ('var -> ID','var',1,'p_var','bixoParser.py',1025),
  ('call -> ID LPAREN callp RPAREN','call',4,'p_call','bixoParser.py',1029),
  ('callp -> exp COMMA callp','callp',3,'p_callp','bixoParser.py',1082),
  ('callp -> exp','callp',1,'p_callp','bixoParser.py',1083),
  ('callp -> <empty>','callp',0,'p_callp','bixoParser.py',1084),
  ('if -> IF LPAREN ifexp RPAREN quadsIf LBRACE body RBRACE ifelse jumpsIf SEMICOLON','if',11,'p_if','bixoParser.py',1095),
  ('ifexp -> exp','ifexp',1,'p_ifexp','bixoParser.py',1098),
  ('ifelse -> <empty>','ifelse',0,'p_ifelse','bixoParser.py',1103),
  ('ifelse -> ELSE quadsElse LBRACE body RBRACE','ifelse',5,'p_ifelse','bixoParser.py',1104),
  ('quadsIf -> <empty>','quadsIf',0,'p_quadsIf','bixoParser.py',1112),
  ('jumpsIf -> <empty>','jumpsIf',0,'p_jumpsIf','bixoParser.py',1121),
  ('quadsElse -> <empty>','quadsElse',0,'p_quadsElse','bixoParser.py',1136),
  ('while -> WHILE saveJumps LPAREN whilexp RPAREN quadsWhile LBRACE body RBRACE jumpsWhile SEMICOLON','while',11,'p_while','bixoParser.py',1147),
  ('whilexp -> exp','whilexp',1,'p_whilexp','bixoParser.py',1150),
  ('saveJumps -> <empty>','saveJumps',0,'p_saveJumps','bixoParser.py',1155),
  ('quadsWhile -> <empty>','quadsWhile',0,'p_quadsWhile','bixoParser.py',1160),
  ('jumpsWhile -> <empty>','jumpsWhile',0,'p_jumpsWhile','bixoParser.py',1168),
  ('for -> FOR LPAREN var SEMICOLON exp SEMICOLON exp RPAREN LBRACKET statements forp','for',11,'p_for','bixoParser.py',1181),
  ('forp -> RBRACKET','forp',1,'p_forp','bixoParser.py',1184),
  ('forp -> statements forp','forp',2,'p_forp','bixoParser.py',1185),
  ('funcesp -> array','funcesp',1,'p_funcesp','bixoParser.py',1190),
  ('funcesp -> mean','funcesp',1,'p_funcesp','bixoParser.py',1191),
  ('funcesp -> layers','funcesp',1,'p_funcesp','bixoParser.py',1192),
  ('funcesp -> sequential','funcesp',1,'p_funcesp','bixoParser.py',1193),
  ('funcesp -> compile','funcesp',1,'p_funcesp','bixoParser.py',1194),
  ('funcesp -> fit','funcesp',1,'p_funcesp','bixoParser.py',1195),
  ('funcesp -> predict','funcesp',1,'p_funcesp','bixoParser.py',1196),
  ('funcesp -> getweights','funcesp',1,'p_funcesp','bixoParser.py',1197),
  ('array -> ARRAY ID LBRACKET exp RBRACKET EQUAL LBRACKET arrvalues RBRACKET SEMICOLON','array',10,'p_array','bixoParser.py',1200),
  ('arrvalues -> exp','arrvalues',1,'p_arrvalues','bixoParser.py',1245),
  ('arrvalues -> exp COMMA arrvalues','arrvalues',3,'p_arrvalues','bixoParser.py',1246),
  ('matrix -> MATRIX ID LBRACKET exp RBRACKET LBRACKET exp RBRACKET EQUAL LBRACKET matvalues RBRACKET SEMICOLON','matrix',13,'p_matrix','bixoParser.py',1257),
  ('matvalues -> exp','matvalues',1,'p_mat_values','bixoParser.py',1323),
  ('matvalues -> exp COMMA matvalues','matvalues',3,'p_mat_values','bixoParser.py',1324),
  ('mean -> MEAN LPAREN ID RPAREN SEMICOLON','mean',5,'p_mean','bixoParser.py',1335),
  ('layers -> LAYERS LPAREN UNITS EQUAL CTI RPAREN SEMICOLON','layers',7,'p_layers','bixoParser.py',1343),
  ('sequential -> SEQUENTIAL LPAREN RPAREN SEMICOLON','sequential',4,'p_sequential','bixoParser.py',1351),
  ('compile -> COMPILE LPAREN CTF RPAREN SEMICOLON','compile',5,'p_compile','bixoParser.py',1363),
  ('fit -> FIT LPAREN ID COMMA ID COMMA EPOCHS EQUAL CTI COMMA VERBOSE EQUAL CTI','fit',13,'p_fit','bixoParser.py',1374),
  ('predict -> ID EQUAL sequential DOT PREDICT LPAREN LBRACKET predictp','predict',8,'p_predict','bixoParser.py',1379),
  ('predictp -> INT RBRACKET RPAREN','predictp',3,'p_predictp','bixoParser.py',1382),
  ('predictp -> FLOAT RBRACKET RPAREN','predictp',3,'p_predictp','bixoParser.py',1383),
  ('getweights -> layers DOT GETWEIGHTS LPAREN RPAREN','getweights',5,'p_getweights','bixoParser.py',1386),
  ('empty -> <empty>','empty',0,'p_empty','bixoParser.py',1390),
]
