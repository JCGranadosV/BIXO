
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'leftLTLTEGTGTEleftPLUSMINUSleftMULTDIVleftEQUALDIFFleftLPARENRPARENleftLBRACERBRACEleftLBRACKETRBRACKETAND ARRAY ASSIGN CHAR COLON COMMA COMPILE CTF CTI DIFF DIV DOT ELSE EPOCHS EQUAL FALSE FIT FLOAT FOR FUNCESP FUNCTION GETWEIGHTS GT GTE ID IF INT LAYERS LBRACE LBRACKET LPAREN LT LTE MATRIX MEAN MINUS MULT NUMPY OR PLUS PREDICT PRINT PROGRAM QUOTE RBRACE RBRACKET READ RPAREN SEMICOLON SEQUENTIAL STRING TRUE UNITS VAR VERBOSE VOID WHILEprogram : PROGRAM ID SEMICOLON ifdecvar : VAR decvarp\n              | VAR decvarp decvardecvarp : type decvarpp SEMICOLONdecvarpp : ID COMMA decvarpp\n                | IDtype : INT\n            | FLOATfunction : FUNCTION type ID LPAREN param RPAREN bodyvoidfunction : FUNCTION VOID ID LPAREN param RPAREN bodybody : LBRACE bodyp RBRACEbodyp : decvar statements bodyp\n             | statements bodyp\n             | decvar\n             | param : \n             | parampparamp : type parampp parampp : ID\n                | ID COMMA parampexp : texp \n           | texp OR exptexp : gexp \n            | gexp AND texpgexp : mexp \n            | mexp gexpp mexpgexpp : LT\n             | GT\n             | EQUAL\n             | DIFFmexp : t\n            | t PLUS mexp\n            | t MINUS mexpt : f \n         | f MULT t\n         | f DIV tf : LPAREN exp RPAREN\n         | INT\n         | FLOAT\n         | var\n         | callstatements : assign\n                 |  function\n                 |  voidfunction\n                 |  call\n                 |  read\n                 |  print\n                 |  if\n                 |  while\n                 |  for\n                 |  funcespassign : var EQUAL expread : READ varprint : PRINT LPAREN printpprintp : exp RPAREN\n              | exp COMMA printpvar : ID \n           | ID LBRACKET exp RBRACKET\n           | ID LBRACKET exp RBRACKET LBRACKET exp RBRACKETcall : ID LPAREN callp RPARENcallp : exp SEMICOLON callp\n             | expif : IF LPAREN INT EQUAL EQUAL CTI RPAREN quadsIf ifp jumpsIf ifp : \n            | ELSE quadsElse statementsquadsIf : jumpsIf : quadsElse :  while : WHILE LPAREN exp RPAREN statements whilep whilep : SEMICOLON\n               | statements whilepfor : FOR LPAREN var SEMICOLON exp SEMICOLON exp RPAREN LBRACKET statements forp forp : RBRACKET\n             | statements forp funcesp : array\n                | matrix\n                | mean\n                | layers\n                | sequential\n                | compile\n                | fit\n                | predict\n                | getweights array : ID EQUAL ARRAY LPAREN var arrayp arrayp : RPAREN\n               | COMMA var RPAREN matrix : ID EQUAL MATRIX LPAREN array matrixp matrixp : RPAREN\n                | COMMA array RPARENmean : MEAN LPAREN array RPARENlayers : ID EQUAL LAYERS LPAREN UNITS EQUAL INT RPAREN sequential : ID EQUAL SEQUENTIAL LPAREN LBRACKET layers sequentialp sequentialp : RBRACKET RPAREN\n                    | COMMA layers sequentialp compile : sequential DOT COMPILE LPAREN RPAREN fit : ID EQUAL sequential DOT FIT LPAREN array COMMA array COMMA EPOCHS EQUAL INT COMMA VERBOSE EQUAL fitp fitp : TRUE RPAREN\n             | FALSE RPAREN predict : ID EQUAL sequential DOT PREDICT LPAREN LBRACKET predictp predictp : INT RBRACKET RPAREN\n                 | FLOAT RBRACKET RPAREN getweights : layers DOT GETWEIGHTS LPAREN RPARENempty :'
    
_lr_action_items = {'PROGRAM':([0,],[2,]),'$end':([1,5,12,13,14,16,18,19,20,21,22,23,24,25,26,27,28,36,37,38,39,40,41,42,43,44,54,55,62,63,64,65,66,67,68,70,71,72,73,85,107,109,116,122,124,125,126,127,128,129,130,131,144,147,148,154,155,157,158,166,167,170,172,173,178,183,190,191,192,193,196,200,205,215,216,222,223,226,231,234,235,],[0,-1,-66,-64,-67,-63,-65,-42,-43,-44,-45,-46,-47,-48,-49,-50,-51,-75,-76,-77,-78,-79,-80,-81,-82,-83,-53,-57,-40,-52,-21,-23,-25,-31,-34,-38,-39,-41,-57,-54,-60,-58,-55,-90,-22,-24,-26,-32,-33,-35,-36,-37,-56,-102,-95,-84,-85,-87,-88,-69,-70,-9,-10,-59,-92,-71,-86,-89,-91,-93,-99,-11,-94,-100,-101,-72,-73,-74,-96,-97,-98,]),'ID':([2,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,32,36,37,38,39,40,41,42,43,44,46,47,48,49,50,51,52,53,54,55,56,57,58,61,62,63,64,65,66,67,68,69,70,71,72,73,85,93,94,95,96,97,98,99,100,101,102,103,107,108,109,111,112,116,117,118,119,122,124,125,126,127,128,129,130,131,132,137,141,144,145,147,148,154,155,156,157,158,159,163,165,166,167,168,170,171,172,173,178,180,183,187,188,190,191,192,193,195,196,200,201,203,204,205,209,211,215,216,217,218,219,221,222,223,226,231,234,235,],[3,-66,-64,-67,-68,-63,31,-65,-42,-43,-44,-45,-46,-47,-48,-49,-50,-51,55,-75,-76,-77,-78,-79,-80,-81,-82,-83,73,74,75,-7,-8,73,73,79,-53,-57,73,73,55,92,-40,-52,-21,-23,-25,-31,-34,73,-38,-39,-41,-57,-54,73,73,73,-27,-28,-29,-30,73,73,73,73,-60,73,-58,55,92,-55,73,31,73,-90,-22,-24,-26,-32,-33,-35,-36,-37,150,73,161,-56,31,-102,-95,-84,-85,55,-87,-88,92,92,31,-69,-70,73,-9,31,-10,-59,-92,161,-71,31,31,-86,-89,-91,-93,92,-99,-11,31,-2,213,-94,31,-3,-100,-101,31,-4,213,31,-72,-73,-74,-96,-97,-98,]),'SEMICOLON':([3,12,13,14,16,18,19,20,21,22,23,24,25,26,27,28,36,37,38,39,40,41,42,43,44,54,55,62,63,64,65,66,67,68,70,71,72,73,77,85,88,107,109,116,122,124,125,126,127,128,129,130,131,144,145,146,147,148,154,155,157,158,165,166,167,170,172,173,178,183,190,191,192,193,196,200,205,212,213,215,216,222,223,224,226,231,234,235,],[4,-66,-64,-67,-63,-65,-42,-43,-44,-45,-46,-47,-48,-49,-50,-51,-75,-76,-77,-78,-79,-80,-81,-82,-83,-53,-57,-40,-52,-21,-23,-25,-31,-34,-38,-39,-41,-57,108,-54,119,-60,-58,-55,-90,-22,-24,-26,-32,-33,-35,-36,-37,-56,167,168,-102,-95,-84,-85,-87,-88,167,-69,-70,-9,-10,-59,-92,-71,-86,-89,-91,-93,-99,-11,-94,218,-6,-100,-101,-72,-73,-5,-74,-96,-97,-98,]),'IF':([4,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,36,37,38,39,40,41,42,43,44,54,55,62,63,64,65,66,67,68,70,71,72,73,85,107,109,116,118,122,124,125,126,127,128,129,130,131,144,145,147,148,154,155,157,158,165,166,167,170,171,172,173,178,183,187,188,190,191,192,193,196,200,201,203,205,209,211,215,216,217,218,221,222,223,226,231,234,235,],[6,-66,-64,-67,-68,-63,6,-65,-42,-43,-44,-45,-46,-47,-48,-49,-50,-51,-75,-76,-77,-78,-79,-80,-81,-82,-83,-53,-57,-40,-52,-21,-23,-25,-31,-34,-38,-39,-41,-57,-54,-60,-58,-55,6,-90,-22,-24,-26,-32,-33,-35,-36,-37,-56,6,-102,-95,-84,-85,-87,-88,6,-69,-70,-9,6,-10,-59,-92,-71,6,6,-86,-89,-91,-93,-99,-11,6,-2,-94,6,-3,-100,-101,6,-4,6,-72,-73,-74,-96,-97,-98,]),'LPAREN':([6,31,33,34,35,45,46,51,52,56,57,69,73,74,75,80,81,82,83,89,90,93,94,95,96,97,98,99,100,101,102,103,108,117,119,137,142,143,168,],[7,51,56,57,58,61,69,69,69,69,69,69,51,105,106,111,112,113,114,120,121,69,69,69,-27,-28,-29,-30,69,69,69,69,69,69,69,69,163,164,69,]),'INT':([7,30,46,51,52,56,57,69,93,94,95,96,97,98,99,100,101,102,103,105,106,108,117,119,137,160,168,169,182,189,225,],[8,49,70,70,70,70,70,70,70,70,70,-27,-28,-29,-30,70,70,70,70,49,49,70,70,70,70,176,70,49,197,49,227,]),'EQUAL':([8,9,29,31,62,66,67,68,70,71,72,73,79,92,107,109,127,128,129,130,131,140,161,173,220,229,],[9,10,46,53,-40,98,-31,-34,-38,-39,-41,-57,110,123,-60,-58,-32,-33,-35,-36,-37,160,177,-59,225,230,]),'CTI':([10,],[11,]),'RPAREN':([11,55,62,64,65,66,67,68,70,71,72,73,76,77,86,87,91,104,105,106,107,109,120,121,124,125,126,127,128,129,130,131,133,134,135,136,138,139,149,150,154,155,173,174,175,176,179,184,185,190,207,208,232,233,],[12,-57,-40,-21,-23,-25,-31,-34,-38,-39,-41,-57,107,-62,116,118,122,131,-16,-16,-60,-58,147,148,-22,-24,-26,-32,-33,-35,-36,-37,151,-17,152,-61,155,158,-18,-19,-84,-85,-59,190,191,192,193,199,-20,-86,215,216,234,235,]),'ELSE':([12,13,],[-66,15,]),'FUNCTION':([12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,36,37,38,39,40,41,42,43,44,54,55,62,63,64,65,66,67,68,70,71,72,73,85,107,109,116,118,122,124,125,126,127,128,129,130,131,144,145,147,148,154,155,157,158,165,166,167,170,171,172,173,178,183,187,188,190,191,192,193,196,200,201,203,205,209,211,215,216,217,218,221,222,223,226,231,234,235,],[-66,-64,-67,-68,-63,30,-65,-42,-43,-44,-45,-46,-47,-48,-49,-50,-51,-75,-76,-77,-78,-79,-80,-81,-82,-83,-53,-57,-40,-52,-21,-23,-25,-31,-34,-38,-39,-41,-57,-54,-60,-58,-55,30,-90,-22,-24,-26,-32,-33,-35,-36,-37,-56,30,-102,-95,-84,-85,-87,-88,30,-69,-70,-9,30,-10,-59,-92,-71,30,30,-86,-89,-91,-93,-99,-11,30,-2,-94,30,-3,-100,-101,30,-4,30,-72,-73,-74,-96,-97,-98,]),'READ':([12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,36,37,38,39,40,41,42,43,44,54,55,62,63,64,65,66,67,68,70,71,72,73,85,107,109,116,118,122,124,125,126,127,128,129,130,131,144,145,147,148,154,155,157,158,165,166,167,170,171,172,173,178,183,187,188,190,191,192,193,196,200,201,203,205,209,211,215,216,217,218,221,222,223,226,231,234,235,],[-66,-64,-67,-68,-63,32,-65,-42,-43,-44,-45,-46,-47,-48,-49,-50,-51,-75,-76,-77,-78,-79,-80,-81,-82,-83,-53,-57,-40,-52,-21,-23,-25,-31,-34,-38,-39,-41,-57,-54,-60,-58,-55,32,-90,-22,-24,-26,-32,-33,-35,-36,-37,-56,32,-102,-95,-84,-85,-87,-88,32,-69,-70,-9,32,-10,-59,-92,-71,32,32,-86,-89,-91,-93,-99,-11,32,-2,-94,32,-3,-100,-101,32,-4,32,-72,-73,-74,-96,-97,-98,]),'PRINT':([12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,36,37,38,39,40,41,42,43,44,54,55,62,63,64,65,66,67,68,70,71,72,73,85,107,109,116,118,122,124,125,126,127,128,129,130,131,144,145,147,148,154,155,157,158,165,166,167,170,171,172,173,178,183,187,188,190,191,192,193,196,200,201,203,205,209,211,215,216,217,218,221,222,223,226,231,234,235,],[-66,-64,-67,-68,-63,33,-65,-42,-43,-44,-45,-46,-47,-48,-49,-50,-51,-75,-76,-77,-78,-79,-80,-81,-82,-83,-53,-57,-40,-52,-21,-23,-25,-31,-34,-38,-39,-41,-57,-54,-60,-58,-55,33,-90,-22,-24,-26,-32,-33,-35,-36,-37,-56,33,-102,-95,-84,-85,-87,-88,33,-69,-70,-9,33,-10,-59,-92,-71,33,33,-86,-89,-91,-93,-99,-11,33,-2,-94,33,-3,-100,-101,33,-4,33,-72,-73,-74,-96,-97,-98,]),'WHILE':([12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,36,37,38,39,40,41,42,43,44,54,55,62,63,64,65,66,67,68,70,71,72,73,85,107,109,116,118,122,124,125,126,127,128,129,130,131,144,145,147,148,154,155,157,158,165,166,167,170,171,172,173,178,183,187,188,190,191,192,193,196,200,201,203,205,209,211,215,216,217,218,221,222,223,226,231,234,235,],[-66,-64,-67,-68,-63,34,-65,-42,-43,-44,-45,-46,-47,-48,-49,-50,-51,-75,-76,-77,-78,-79,-80,-81,-82,-83,-53,-57,-40,-52,-21,-23,-25,-31,-34,-38,-39,-41,-57,-54,-60,-58,-55,34,-90,-22,-24,-26,-32,-33,-35,-36,-37,-56,34,-102,-95,-84,-85,-87,-88,34,-69,-70,-9,34,-10,-59,-92,-71,34,34,-86,-89,-91,-93,-99,-11,34,-2,-94,34,-3,-100,-101,34,-4,34,-72,-73,-74,-96,-97,-98,]),'FOR':([12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,36,37,38,39,40,41,42,43,44,54,55,62,63,64,65,66,67,68,70,71,72,73,85,107,109,116,118,122,124,125,126,127,128,129,130,131,144,145,147,148,154,155,157,158,165,166,167,170,171,172,173,178,183,187,188,190,191,192,193,196,200,201,203,205,209,211,215,216,217,218,221,222,223,226,231,234,235,],[-66,-64,-67,-68,-63,35,-65,-42,-43,-44,-45,-46,-47,-48,-49,-50,-51,-75,-76,-77,-78,-79,-80,-81,-82,-83,-53,-57,-40,-52,-21,-23,-25,-31,-34,-38,-39,-41,-57,-54,-60,-58,-55,35,-90,-22,-24,-26,-32,-33,-35,-36,-37,-56,35,-102,-95,-84,-85,-87,-88,35,-69,-70,-9,35,-10,-59,-92,-71,35,35,-86,-89,-91,-93,-99,-11,35,-2,-94,35,-3,-100,-101,35,-4,35,-72,-73,-74,-96,-97,-98,]),'MEAN':([12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,36,37,38,39,40,41,42,43,44,54,55,62,63,64,65,66,67,68,70,71,72,73,85,107,109,116,118,122,124,125,126,127,128,129,130,131,144,145,147,148,154,155,157,158,165,166,167,170,171,172,173,178,183,187,188,190,191,192,193,196,200,201,203,205,209,211,215,216,217,218,221,222,223,226,231,234,235,],[-66,-64,-67,-68,-63,45,-65,-42,-43,-44,-45,-46,-47,-48,-49,-50,-51,-75,-76,-77,-78,-79,-80,-81,-82,-83,-53,-57,-40,-52,-21,-23,-25,-31,-34,-38,-39,-41,-57,-54,-60,-58,-55,45,-90,-22,-24,-26,-32,-33,-35,-36,-37,-56,45,-102,-95,-84,-85,-87,-88,45,-69,-70,-9,45,-10,-59,-92,-71,45,45,-86,-89,-91,-93,-99,-11,45,-2,-94,45,-3,-100,-101,45,-4,45,-72,-73,-74,-96,-97,-98,]),'VAR':([12,13,14,16,18,19,20,21,22,23,24,25,26,27,28,36,37,38,39,40,41,42,43,44,54,55,62,63,64,65,66,67,68,70,71,72,73,85,107,109,116,122,124,125,126,127,128,129,130,131,144,147,148,154,155,157,158,166,167,170,171,172,173,178,183,188,190,191,192,193,196,200,201,203,205,215,216,218,222,223,226,231,234,235,],[-66,-64,-67,-63,-65,-42,-43,-44,-45,-46,-47,-48,-49,-50,-51,-75,-76,-77,-78,-79,-80,-81,-82,-83,-53,-57,-40,-52,-21,-23,-25,-31,-34,-38,-39,-41,-57,-54,-60,-58,-55,-90,-22,-24,-26,-32,-33,-35,-36,-37,-56,-102,-95,-84,-85,-87,-88,-69,-70,-9,189,-10,-59,-92,-71,189,-86,-89,-91,-93,-99,-11,189,189,-94,-100,-101,-4,-72,-73,-74,-96,-97,-98,]),'RBRACE':([12,13,14,16,18,19,20,21,22,23,24,25,26,27,28,36,37,38,39,40,41,42,43,44,54,55,62,63,64,65,66,67,68,70,71,72,73,85,107,109,116,122,124,125,126,127,128,129,130,131,144,147,148,154,155,157,158,166,167,170,171,172,173,178,183,186,187,188,190,191,192,193,196,200,201,202,203,205,210,211,215,216,218,222,223,226,231,234,235,],[-66,-64,-67,-63,-65,-42,-43,-44,-45,-46,-47,-48,-49,-50,-51,-75,-76,-77,-78,-79,-80,-81,-82,-83,-53,-57,-40,-52,-21,-23,-25,-31,-34,-38,-39,-41,-57,-54,-60,-58,-55,-90,-22,-24,-26,-32,-33,-35,-36,-37,-56,-102,-95,-84,-85,-87,-88,-69,-70,-9,-15,-10,-59,-92,-71,200,-14,-15,-86,-89,-91,-93,-99,-11,-15,-13,-2,-94,-12,-3,-100,-101,-4,-72,-73,-74,-96,-97,-98,]),'RBRACKET':([12,13,14,16,18,19,20,21,22,23,24,25,26,27,28,36,37,38,39,40,41,42,43,44,54,55,62,63,64,65,66,67,68,70,71,72,73,78,85,107,109,116,122,124,125,126,127,128,129,130,131,144,147,148,153,154,155,157,158,162,166,167,170,172,173,178,183,190,191,192,193,194,196,197,198,200,205,215,216,217,221,222,223,226,231,234,235,],[-66,-64,-67,-63,-65,-42,-43,-44,-45,-46,-47,-48,-49,-50,-51,-75,-76,-77,-78,-79,-80,-81,-82,-83,-53,-57,-40,-52,-21,-23,-25,-31,-34,-38,-39,-41,-57,109,-54,-60,-58,-55,-90,-22,-24,-26,-32,-33,-35,-36,-37,-56,-102,-95,173,-84,-85,-87,-88,179,-69,-70,-9,-10,-59,-92,-71,-86,-89,-91,-93,179,-99,207,208,-11,-94,-100,-101,223,223,-72,-73,-74,-96,-97,-98,]),'VOID':([30,],[48,]),'FLOAT':([30,46,51,52,56,57,69,93,94,95,96,97,98,99,100,101,102,103,105,106,108,117,119,137,168,169,182,189,],[50,71,71,71,71,71,71,71,71,71,-27,-28,-29,-30,71,71,71,71,50,50,71,71,71,71,71,50,198,50,]),'LBRACKET':([31,55,73,109,114,164,199,],[52,52,52,137,141,182,209,]),'DOT':([39,40,84,178,192,193,205,],[59,60,115,-92,-91,-93,-94,]),'ARRAY':([53,123,],[80,80,]),'MATRIX':([53,],[81,]),'LAYERS':([53,177,],[82,82,]),'SEQUENTIAL':([53,110,],[83,83,]),'COMMA':([55,62,64,65,66,67,68,70,71,72,73,86,107,109,124,125,126,127,128,129,130,131,138,139,150,154,155,162,173,181,190,192,194,206,213,227,],[-57,-40,-21,-23,-25,-31,-34,-38,-39,-41,-57,117,-60,-58,-22,-24,-26,-32,-33,-35,-36,-37,156,159,169,-84,-85,180,-59,195,-86,-91,180,214,219,228,]),'GETWEIGHTS':([59,],[89,]),'COMPILE':([60,],[90,]),'MULT':([62,68,70,71,72,73,107,109,131,173,],[-40,102,-38,-39,-41,-57,-60,-58,-37,-59,]),'DIV':([62,68,70,71,72,73,107,109,131,173,],[-40,103,-38,-39,-41,-57,-60,-58,-37,-59,]),'PLUS':([62,67,68,70,71,72,73,107,109,129,130,131,173,],[-40,100,-34,-38,-39,-41,-57,-60,-58,-35,-36,-37,-59,]),'MINUS':([62,67,68,70,71,72,73,107,109,129,130,131,173,],[-40,101,-34,-38,-39,-41,-57,-60,-58,-35,-36,-37,-59,]),'LT':([62,66,67,68,70,71,72,73,107,109,127,128,129,130,131,173,],[-40,96,-31,-34,-38,-39,-41,-57,-60,-58,-32,-33,-35,-36,-37,-59,]),'GT':([62,66,67,68,70,71,72,73,107,109,127,128,129,130,131,173,],[-40,97,-31,-34,-38,-39,-41,-57,-60,-58,-32,-33,-35,-36,-37,-59,]),'DIFF':([62,66,67,68,70,71,72,73,107,109,127,128,129,130,131,173,],[-40,99,-31,-34,-38,-39,-41,-57,-60,-58,-32,-33,-35,-36,-37,-59,]),'AND':([62,65,66,67,68,70,71,72,73,107,109,126,127,128,129,130,131,173,],[-40,94,-25,-31,-34,-38,-39,-41,-57,-60,-58,-26,-32,-33,-35,-36,-37,-59,]),'OR':([62,64,65,66,67,68,70,71,72,73,107,109,125,126,127,128,129,130,131,173,],[-40,93,-23,-25,-31,-34,-38,-39,-41,-57,-60,-58,-24,-26,-32,-33,-35,-36,-37,-59,]),'UNITS':([113,],[140,]),'FIT':([115,],[142,]),'PREDICT':([115,],[143,]),'LBRACE':([151,152,],[171,171,]),'EPOCHS':([214,],[220,]),'VERBOSE':([228,],[229,]),'TRUE':([230,],[232,]),'FALSE':([230,],[233,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'program':([0,],[1,]),'if':([4,17,118,145,165,171,187,188,201,209,217,221,],[5,25,25,25,25,25,25,25,25,25,25,25,]),'quadsIf':([12,],[13,]),'ifp':([13,],[14,]),'jumpsIf':([14,],[16,]),'quadsElse':([15,],[17,]),'statements':([17,118,145,165,171,187,188,201,209,217,221,],[18,145,165,165,188,201,188,188,217,221,221,]),'assign':([17,118,145,165,171,187,188,201,209,217,221,],[19,19,19,19,19,19,19,19,19,19,19,]),'function':([17,118,145,165,171,187,188,201,209,217,221,],[20,20,20,20,20,20,20,20,20,20,20,]),'voidfunction':([17,118,145,165,171,187,188,201,209,217,221,],[21,21,21,21,21,21,21,21,21,21,21,]),'call':([17,46,51,52,56,57,69,93,94,95,100,101,102,103,108,117,118,119,137,145,165,168,171,187,188,201,209,217,221,],[22,72,72,72,72,72,72,72,72,72,72,72,72,72,72,72,22,72,72,22,22,72,22,22,22,22,22,22,22,]),'read':([17,118,145,165,171,187,188,201,209,217,221,],[23,23,23,23,23,23,23,23,23,23,23,]),'print':([17,118,145,165,171,187,188,201,209,217,221,],[24,24,24,24,24,24,24,24,24,24,24,]),'while':([17,118,145,165,171,187,188,201,209,217,221,],[26,26,26,26,26,26,26,26,26,26,26,]),'for':([17,118,145,165,171,187,188,201,209,217,221,],[27,27,27,27,27,27,27,27,27,27,27,]),'funcesp':([17,118,145,165,171,187,188,201,209,217,221,],[28,28,28,28,28,28,28,28,28,28,28,]),'var':([17,32,46,51,52,56,57,58,69,93,94,95,100,101,102,103,108,111,117,118,119,137,145,156,165,168,171,187,188,201,209,217,221,],[29,54,62,62,62,62,62,88,62,62,62,62,62,62,62,62,62,138,62,29,62,62,29,174,29,62,29,29,29,29,29,29,29,]),'array':([17,61,112,118,145,159,163,165,171,187,188,195,201,209,217,221,],[36,91,139,36,36,175,181,36,36,36,36,206,36,36,36,36,]),'matrix':([17,118,145,165,171,187,188,201,209,217,221,],[37,37,37,37,37,37,37,37,37,37,37,]),'mean':([17,118,145,165,171,187,188,201,209,217,221,],[38,38,38,38,38,38,38,38,38,38,38,]),'layers':([17,118,141,145,165,171,180,187,188,201,209,217,221,],[39,39,162,39,39,39,194,39,39,39,39,39,39,]),'sequential':([17,53,118,145,165,171,187,188,201,209,217,221,],[40,84,40,40,40,40,40,40,40,40,40,40,]),'compile':([17,118,145,165,171,187,188,201,209,217,221,],[41,41,41,41,41,41,41,41,41,41,41,]),'fit':([17,118,145,165,171,187,188,201,209,217,221,],[42,42,42,42,42,42,42,42,42,42,42,]),'predict':([17,118,145,165,171,187,188,201,209,217,221,],[43,43,43,43,43,43,43,43,43,43,43,]),'getweights':([17,118,145,165,171,187,188,201,209,217,221,],[44,44,44,44,44,44,44,44,44,44,44,]),'type':([30,105,106,169,189,],[47,132,132,132,204,]),'exp':([46,51,52,56,57,69,93,108,117,119,137,168,],[63,77,78,86,87,104,124,77,86,146,153,184,]),'texp':([46,51,52,56,57,69,93,94,108,117,119,137,168,],[64,64,64,64,64,64,64,125,64,64,64,64,64,]),'gexp':([46,51,52,56,57,69,93,94,108,117,119,137,168,],[65,65,65,65,65,65,65,65,65,65,65,65,65,]),'mexp':([46,51,52,56,57,69,93,94,95,100,101,108,117,119,137,168,],[66,66,66,66,66,66,66,66,126,127,128,66,66,66,66,66,]),'t':([46,51,52,56,57,69,93,94,95,100,101,102,103,108,117,119,137,168,],[67,67,67,67,67,67,67,67,67,67,67,129,130,67,67,67,67,67,]),'f':([46,51,52,56,57,69,93,94,95,100,101,102,103,108,117,119,137,168,],[68,68,68,68,68,68,68,68,68,68,68,68,68,68,68,68,68,68,]),'callp':([51,108,],[76,136,]),'printp':([56,117,],[85,144,]),'gexpp':([66,],[95,]),'param':([105,106,],[133,135,]),'paramp':([105,106,169,],[134,134,185,]),'parampp':([132,],[149,]),'arrayp':([138,],[154,]),'matrixp':([139,],[157,]),'whilep':([145,165,],[166,183,]),'body':([151,152,],[170,172,]),'sequentialp':([162,194,],[178,205,]),'bodyp':([171,188,201,],[186,202,210,]),'decvar':([171,188,201,203,],[187,187,187,211,]),'predictp':([182,],[196,]),'decvarp':([189,],[203,]),'decvarpp':([204,219,],[212,224,]),'forp':([217,221,],[222,226,]),'fitp':([230,],[231,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> program","S'",1,None,None,None),
  ('program -> PROGRAM ID SEMICOLON if','program',4,'p_program','bixoParser.py',156),
  ('decvar -> VAR decvarp','decvar',2,'p_decvar','bixoParser.py',162),
  ('decvar -> VAR decvarp decvar','decvar',3,'p_decvar','bixoParser.py',163),
  ('decvarp -> type decvarpp SEMICOLON','decvarp',3,'p_decvarp','bixoParser.py',167),
  ('decvarpp -> ID COMMA decvarpp','decvarpp',3,'p_decvarpp','bixoParser.py',206),
  ('decvarpp -> ID','decvarpp',1,'p_decvarpp','bixoParser.py',207),
  ('type -> INT','type',1,'p_type','bixoParser.py',218),
  ('type -> FLOAT','type',1,'p_type','bixoParser.py',219),
  ('function -> FUNCTION type ID LPAREN param RPAREN body','function',7,'p_function','bixoParser.py',223),
  ('voidfunction -> FUNCTION VOID ID LPAREN param RPAREN body','voidfunction',7,'p_voidfunction','bixoParser.py',226),
  ('body -> LBRACE bodyp RBRACE','body',3,'p_body','bixoParser.py',229),
  ('bodyp -> decvar statements bodyp','bodyp',3,'p_bodyp','bixoParser.py',232),
  ('bodyp -> statements bodyp','bodyp',2,'p_bodyp','bixoParser.py',233),
  ('bodyp -> decvar','bodyp',1,'p_bodyp','bixoParser.py',234),
  ('bodyp -> <empty>','bodyp',0,'p_bodyp','bixoParser.py',235),
  ('param -> <empty>','param',0,'p_param','bixoParser.py',238),
  ('param -> paramp','param',1,'p_param','bixoParser.py',239),
  ('paramp -> type parampp','paramp',2,'p_paramp','bixoParser.py',242),
  ('parampp -> ID','parampp',1,'p_parampp','bixoParser.py',245),
  ('parampp -> ID COMMA paramp','parampp',3,'p_parampp','bixoParser.py',246),
  ('exp -> texp','exp',1,'p_exp','bixoParser.py',249),
  ('exp -> texp OR exp','exp',3,'p_exp','bixoParser.py',250),
  ('texp -> gexp','texp',1,'p_texp','bixoParser.py',253),
  ('texp -> gexp AND texp','texp',3,'p_texp','bixoParser.py',254),
  ('gexp -> mexp','gexp',1,'p_gexp','bixoParser.py',257),
  ('gexp -> mexp gexpp mexp','gexp',3,'p_gexp','bixoParser.py',258),
  ('gexpp -> LT','gexpp',1,'p_gexpp','bixoParser.py',261),
  ('gexpp -> GT','gexpp',1,'p_gexpp','bixoParser.py',262),
  ('gexpp -> EQUAL','gexpp',1,'p_gexpp','bixoParser.py',263),
  ('gexpp -> DIFF','gexpp',1,'p_gexpp','bixoParser.py',264),
  ('mexp -> t','mexp',1,'p_mexp','bixoParser.py',267),
  ('mexp -> t PLUS mexp','mexp',3,'p_mexp','bixoParser.py',268),
  ('mexp -> t MINUS mexp','mexp',3,'p_mexp','bixoParser.py',269),
  ('t -> f','t',1,'p_t','bixoParser.py',277),
  ('t -> f MULT t','t',3,'p_t','bixoParser.py',278),
  ('t -> f DIV t','t',3,'p_t','bixoParser.py',279),
  ('f -> LPAREN exp RPAREN','f',3,'p_f','bixoParser.py',284),
  ('f -> INT','f',1,'p_f','bixoParser.py',285),
  ('f -> FLOAT','f',1,'p_f','bixoParser.py',286),
  ('f -> var','f',1,'p_f','bixoParser.py',287),
  ('f -> call','f',1,'p_f','bixoParser.py',288),
  ('statements -> assign','statements',1,'p_statements','bixoParser.py',294),
  ('statements -> function','statements',1,'p_statements','bixoParser.py',295),
  ('statements -> voidfunction','statements',1,'p_statements','bixoParser.py',296),
  ('statements -> call','statements',1,'p_statements','bixoParser.py',297),
  ('statements -> read','statements',1,'p_statements','bixoParser.py',298),
  ('statements -> print','statements',1,'p_statements','bixoParser.py',299),
  ('statements -> if','statements',1,'p_statements','bixoParser.py',300),
  ('statements -> while','statements',1,'p_statements','bixoParser.py',301),
  ('statements -> for','statements',1,'p_statements','bixoParser.py',302),
  ('statements -> funcesp','statements',1,'p_statements','bixoParser.py',303),
  ('assign -> var EQUAL exp','assign',3,'p_assign','bixoParser.py',307),
  ('read -> READ var','read',2,'p_read','bixoParser.py',310),
  ('print -> PRINT LPAREN printp','print',3,'p_print','bixoParser.py',313),
  ('printp -> exp RPAREN','printp',2,'p_printp','bixoParser.py',316),
  ('printp -> exp COMMA printp','printp',3,'p_printp','bixoParser.py',317),
  ('var -> ID','var',1,'p_var','bixoParser.py',320),
  ('var -> ID LBRACKET exp RBRACKET','var',4,'p_var','bixoParser.py',321),
  ('var -> ID LBRACKET exp RBRACKET LBRACKET exp RBRACKET','var',7,'p_var','bixoParser.py',322),
  ('call -> ID LPAREN callp RPAREN','call',4,'p_call','bixoParser.py',328),
  ('callp -> exp SEMICOLON callp','callp',3,'p_callp','bixoParser.py',331),
  ('callp -> exp','callp',1,'p_callp','bixoParser.py',332),
  ('if -> IF LPAREN INT EQUAL EQUAL CTI RPAREN quadsIf ifp jumpsIf','if',10,'p_if','bixoParser.py',338),
  ('ifp -> <empty>','ifp',0,'p_ifp','bixoParser.py',341),
  ('ifp -> ELSE quadsElse statements','ifp',3,'p_ifp','bixoParser.py',342),
  ('quadsIf -> <empty>','quadsIf',0,'p_quadsIf','bixoParser.py',345),
  ('jumpsIf -> <empty>','jumpsIf',0,'p_jumpsIf','bixoParser.py',361),
  ('quadsElse -> <empty>','quadsElse',0,'p_quadsElse','bixoParser.py',367),
  ('while -> WHILE LPAREN exp RPAREN statements whilep','while',6,'p_while','bixoParser.py',377),
  ('whilep -> SEMICOLON','whilep',1,'p_whilep','bixoParser.py',380),
  ('whilep -> statements whilep','whilep',2,'p_whilep','bixoParser.py',381),
  ('for -> FOR LPAREN var SEMICOLON exp SEMICOLON exp RPAREN LBRACKET statements forp','for',11,'p_for','bixoParser.py',400),
  ('forp -> RBRACKET','forp',1,'p_forp','bixoParser.py',403),
  ('forp -> statements forp','forp',2,'p_forp','bixoParser.py',404),
  ('funcesp -> array','funcesp',1,'p_funcesp','bixoParser.py',409),
  ('funcesp -> matrix','funcesp',1,'p_funcesp','bixoParser.py',410),
  ('funcesp -> mean','funcesp',1,'p_funcesp','bixoParser.py',411),
  ('funcesp -> layers','funcesp',1,'p_funcesp','bixoParser.py',412),
  ('funcesp -> sequential','funcesp',1,'p_funcesp','bixoParser.py',413),
  ('funcesp -> compile','funcesp',1,'p_funcesp','bixoParser.py',414),
  ('funcesp -> fit','funcesp',1,'p_funcesp','bixoParser.py',415),
  ('funcesp -> predict','funcesp',1,'p_funcesp','bixoParser.py',416),
  ('funcesp -> getweights','funcesp',1,'p_funcesp','bixoParser.py',417),
  ('array -> ID EQUAL ARRAY LPAREN var arrayp','array',6,'p_array','bixoParser.py',420),
  ('arrayp -> RPAREN','arrayp',1,'p_arrayp','bixoParser.py',423),
  ('arrayp -> COMMA var RPAREN','arrayp',3,'p_arrayp','bixoParser.py',424),
  ('matrix -> ID EQUAL MATRIX LPAREN array matrixp','matrix',6,'p_matrix','bixoParser.py',427),
  ('matrixp -> RPAREN','matrixp',1,'p_matrixp','bixoParser.py',430),
  ('matrixp -> COMMA array RPAREN','matrixp',3,'p_matrixp','bixoParser.py',431),
  ('mean -> MEAN LPAREN array RPAREN','mean',4,'p_mean','bixoParser.py',434),
  ('layers -> ID EQUAL LAYERS LPAREN UNITS EQUAL INT RPAREN','layers',8,'p_layers','bixoParser.py',437),
  ('sequential -> ID EQUAL SEQUENTIAL LPAREN LBRACKET layers sequentialp','sequential',7,'p_sequential','bixoParser.py',440),
  ('sequentialp -> RBRACKET RPAREN','sequentialp',2,'p_sequentialp','bixoParser.py',443),
  ('sequentialp -> COMMA layers sequentialp','sequentialp',3,'p_sequentialp','bixoParser.py',444),
  ('compile -> sequential DOT COMPILE LPAREN RPAREN','compile',5,'p_compile','bixoParser.py',447),
  ('fit -> ID EQUAL sequential DOT FIT LPAREN array COMMA array COMMA EPOCHS EQUAL INT COMMA VERBOSE EQUAL fitp','fit',17,'p_fit','bixoParser.py',450),
  ('fitp -> TRUE RPAREN','fitp',2,'p_fitp','bixoParser.py',453),
  ('fitp -> FALSE RPAREN','fitp',2,'p_fitp','bixoParser.py',454),
  ('predict -> ID EQUAL sequential DOT PREDICT LPAREN LBRACKET predictp','predict',8,'p_predict','bixoParser.py',457),
  ('predictp -> INT RBRACKET RPAREN','predictp',3,'p_predictp','bixoParser.py',460),
  ('predictp -> FLOAT RBRACKET RPAREN','predictp',3,'p_predictp','bixoParser.py',461),
  ('getweights -> layers DOT GETWEIGHTS LPAREN RPAREN','getweights',5,'p_getweights','bixoParser.py',464),
  ('empty -> <empty>','empty',0,'p_empty','bixoParser.py',468),
]
