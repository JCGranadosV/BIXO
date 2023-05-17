
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'leftLTLTEGTGTEleftPLUSMINUSleftMULTDIVleftEQUALDIFFleftLPARENRPARENleftLBRACERBRACEleftLBRACKETRBRACKETAND ARRAY ASSIGN CHAR COLON COMMA COMPILE CTF CTI DIFF DIV DOT ELSE EPOCHS EQUAL FALSE FIT FLOAT FOR FUNCESP FUNCTION GETWEIGHTS GT GTE ID IF IFEQUAL INT LAYERS LBRACE LBRACKET LPAREN LT LTE MATRIX MEAN MINUS MULT NUMPY OR PLUS PREDICT PRINT PROGRAM QUOTE RBRACE RBRACKET READ RPAREN SEMICOLON SEQUENTIAL STRING TRUE UNITS VAR VERBOSE VOID WHILEprogram : PROGRAM ID SEMICOLON ifdecvar : VAR decvarp\n              | VAR decvarp decvardecvarp : type decvarpp SEMICOLONdecvarpp : ID COMMA decvarpp\n                | IDtype : INT\n            | FLOATfunction : FUNCTION type ID LPAREN param RPAREN bodyvoidfunction : FUNCTION VOID ID LPAREN param RPAREN bodybody : LBRACE bodyp RBRACEbodyp : decvar statements bodyp\n             | statements bodyp\n             | decvar\n             | param : \n             | type paramp paramp : ID\n               | ID COMMA paramexp : texp \n           | texp OR exptexp : gexp \n            | gexp AND texpgexp : mexp \n            | mexp gexpp mexpgexpp : LT\n             | GT\n             | IFEQUAL\n             | DIFFmexp : t\n            | t PLUS mexp\n            | t MINUS mexpt : f \n         | f MULT t\n         | f DIV tf : LPAREN exp RPAREN\n         | CTI\n         | CTF\n         | var\n         | callstatements : assign\n                 |  function\n                 |  voidfunction\n                 |  call\n                 |  read\n                 |  print\n                 |  if\n                 |  while\n                 |  for\n                 |  funcespassign : var EQUAL expread : READ varprint : PRINT LPAREN printpprintp : exp RPAREN\n              | exp COMMA printpvar : ID call : ID LPAREN callp RPARENcallp : exp SEMICOLON callp\n             | expif : IF LPAREN exp RPAREN quadsIf ifp jumpsIf ifp : \n            | ELSE quadsElse statementsquadsIf : jumpsIf : quadsElse :  while : WHILE LPAREN exp RPAREN statements whilep whilep : SEMICOLON\n               | statements whilepfor : FOR LPAREN var SEMICOLON exp SEMICOLON exp RPAREN LBRACKET statements forp forp : RBRACKET\n             | statements forp funcesp : array\n                | matrix\n                | mean\n                | layers\n                | sequential\n                | compile\n                | fit\n                | predict\n                | getweights array : ID EQUAL ARRAY LPAREN var arrayp arrayp : RPAREN\n               | COMMA var RPAREN matrix : ID EQUAL MATRIX LPAREN array matrixp matrixp : RPAREN\n                | COMMA array RPARENmean : MEAN LPAREN array RPARENlayers : ID EQUAL LAYERS LPAREN UNITS EQUAL INT RPAREN sequential : ID EQUAL SEQUENTIAL LPAREN LBRACKET layers sequentialp sequentialp : RBRACKET RPAREN\n                    | COMMA layers sequentialp compile : sequential DOT COMPILE LPAREN RPAREN fit : ID EQUAL sequential DOT FIT LPAREN array COMMA array COMMA EPOCHS EQUAL INT COMMA VERBOSE EQUAL fitp fitp : TRUE RPAREN\n             | FALSE RPAREN predict : ID EQUAL sequential DOT PREDICT LPAREN LBRACKET predictp predictp : INT RBRACKET RPAREN\n                 | FLOAT RBRACKET RPAREN getweights : layers DOT GETWEIGHTS LPAREN RPARENempty :'
    
_lr_action_items = {'PROGRAM':([0,],[2,]),'$end':([1,5,10,11,12,13,14,15,16,17,18,19,21,34,35,36,37,38,39,40,41,42,45,47,49,52,53,54,55,56,57,58,59,60,61,62,70,71,72,73,74,75,76,77,78,86,87,94,103,119,125,136,139,140,145,146,148,149,157,158,161,163,168,173,180,181,182,183,186,190,195,205,206,212,213,216,221,224,225,],[0,-1,-20,-22,-24,-30,-33,-37,-38,-39,-40,-56,-63,-36,-61,-21,-23,-25,-31,-32,-34,-35,-64,-57,-60,-62,-41,-42,-43,-44,-45,-46,-47,-48,-49,-50,-72,-73,-74,-75,-76,-77,-78,-79,-80,-52,-56,-51,-53,-54,-87,-55,-99,-92,-81,-82,-84,-85,-66,-67,-9,-10,-89,-68,-83,-86,-88,-90,-96,-11,-91,-97,-98,-69,-70,-71,-93,-94,-95,]),'ID':([2,7,8,10,11,12,13,14,15,16,17,18,19,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,45,46,47,48,49,50,52,53,54,55,56,57,58,59,60,61,62,66,70,71,72,73,74,75,76,77,78,80,81,82,83,84,85,86,87,88,89,90,93,94,103,114,115,119,120,121,122,125,127,133,136,137,139,140,145,146,147,148,149,150,154,156,157,158,159,161,162,163,168,170,173,177,178,180,181,182,183,185,186,190,191,193,194,195,199,201,205,206,207,208,209,211,212,213,216,221,224,225,],[3,19,19,-20,-22,-24,-30,-33,-37,-38,-39,-40,-56,-63,19,19,19,-26,-27,-28,-29,19,19,19,19,19,-36,-61,-21,-23,-25,-31,-32,-34,-35,-64,-65,-57,19,-60,65,-62,-41,-42,-43,-44,-45,-46,-47,-48,-49,-50,87,-72,-73,-74,-75,-76,-77,-78,-79,-80,19,95,96,-7,-8,97,-52,-56,19,19,87,110,-51,-53,87,110,-54,19,65,19,-87,142,152,-55,65,-99,-92,-81,-82,87,-84,-85,110,110,65,-66,-67,19,-9,65,-10,-89,152,-68,65,65,-83,-86,-88,-90,110,-96,-11,65,-2,203,-91,65,-3,-97,-98,65,-4,203,65,-69,-70,-71,-93,-94,-95,]),'SEMICOLON':([3,10,11,12,13,14,15,16,17,18,19,21,34,35,36,37,38,39,40,41,42,44,45,47,49,52,53,54,55,56,57,58,59,60,61,62,70,71,72,73,74,75,76,77,78,86,87,94,103,106,119,125,136,137,138,139,140,145,146,148,149,156,157,158,161,163,168,173,180,181,182,183,186,190,195,202,203,205,206,212,213,214,216,221,224,225,],[4,-20,-22,-24,-30,-33,-37,-38,-39,-40,-56,-63,-36,-61,-21,-23,-25,-31,-32,-34,-35,48,-64,-57,-60,-62,-41,-42,-43,-44,-45,-46,-47,-48,-49,-50,-72,-73,-74,-75,-76,-77,-78,-79,-80,-52,-56,-51,-53,122,-54,-87,-55,158,159,-99,-92,-81,-82,-84,-85,158,-66,-67,-9,-10,-89,-68,-83,-86,-88,-90,-96,-11,-91,208,-6,-97,-98,-69,-70,-5,-71,-93,-94,-95,]),'IF':([4,10,11,12,13,14,15,16,17,18,19,21,34,35,36,37,38,39,40,41,42,45,46,47,49,50,52,53,54,55,56,57,58,59,60,61,62,70,71,72,73,74,75,76,77,78,86,87,94,103,119,121,125,136,137,139,140,145,146,148,149,156,157,158,161,162,163,168,173,177,178,180,181,182,183,186,190,191,193,195,199,201,205,206,207,208,211,212,213,216,221,224,225,],[6,-20,-22,-24,-30,-33,-37,-38,-39,-40,-56,-63,-36,-61,-21,-23,-25,-31,-32,-34,-35,-64,-65,-57,-60,6,-62,-41,-42,-43,-44,-45,-46,-47,-48,-49,-50,-72,-73,-74,-75,-76,-77,-78,-79,-80,-52,-56,-51,-53,-54,6,-87,-55,6,-99,-92,-81,-82,-84,-85,6,-66,-67,-9,6,-10,-89,-68,6,6,-83,-86,-88,-90,-96,-11,6,-2,-91,6,-3,-97,-98,6,-4,6,-69,-70,-71,-93,-94,-95,]),'LPAREN':([6,7,8,19,22,23,24,25,26,27,28,29,30,31,32,33,48,65,67,68,69,79,80,88,89,95,96,98,99,100,101,107,108,120,122,134,135,159,],[7,8,8,33,8,8,8,-26,-27,-28,-29,8,8,8,8,8,8,33,88,89,90,93,8,8,8,111,112,114,115,116,117,123,124,8,8,154,155,8,]),'CTI':([7,8,22,23,24,25,26,27,28,29,30,31,32,33,48,80,88,89,120,122,159,],[15,15,15,15,15,-26,-27,-28,-29,15,15,15,15,15,15,15,15,15,15,15,15,]),'CTF':([7,8,22,23,24,25,26,27,28,29,30,31,32,33,48,80,88,89,120,122,159,],[16,16,16,16,16,-26,-27,-28,-29,16,16,16,16,16,16,16,16,16,16,16,16,]),'RPAREN':([9,10,11,12,13,14,15,16,17,18,19,20,34,36,37,38,39,40,41,42,43,44,47,51,87,104,105,109,111,112,123,124,128,129,130,131,141,142,145,146,160,164,165,166,169,174,175,180,197,198,222,223,],[21,-20,-22,-24,-30,-33,-37,-38,-39,-40,-56,34,-36,-21,-23,-25,-31,-32,-34,-35,47,-59,-57,-58,-56,119,121,125,-16,-16,139,140,143,144,146,149,-17,-18,-81,-82,-16,180,181,182,183,189,-19,-83,205,206,224,225,]),'FUNCTION':([10,11,12,13,14,15,16,17,18,19,21,34,35,36,37,38,39,40,41,42,45,46,47,49,50,52,53,54,55,56,57,58,59,60,61,62,70,71,72,73,74,75,76,77,78,86,87,94,103,119,121,125,136,137,139,140,145,146,148,149,156,157,158,161,162,163,168,173,177,178,180,181,182,183,186,190,191,193,195,199,201,205,206,207,208,211,212,213,216,221,224,225,],[-20,-22,-24,-30,-33,-37,-38,-39,-40,-56,-63,-36,-61,-21,-23,-25,-31,-32,-34,-35,-64,-65,-57,-60,64,-62,-41,-42,-43,-44,-45,-46,-47,-48,-49,-50,-72,-73,-74,-75,-76,-77,-78,-79,-80,-52,-56,-51,-53,-54,64,-87,-55,64,-99,-92,-81,-82,-84,-85,64,-66,-67,-9,64,-10,-89,-68,64,64,-83,-86,-88,-90,-96,-11,64,-2,-91,64,-3,-97,-98,64,-4,64,-69,-70,-71,-93,-94,-95,]),'READ':([10,11,12,13,14,15,16,17,18,19,21,34,35,36,37,38,39,40,41,42,45,46,47,49,50,52,53,54,55,56,57,58,59,60,61,62,70,71,72,73,74,75,76,77,78,86,87,94,103,119,121,125,136,137,139,140,145,146,148,149,156,157,158,161,162,163,168,173,177,178,180,181,182,183,186,190,191,193,195,199,201,205,206,207,208,211,212,213,216,221,224,225,],[-20,-22,-24,-30,-33,-37,-38,-39,-40,-56,-63,-36,-61,-21,-23,-25,-31,-32,-34,-35,-64,-65,-57,-60,66,-62,-41,-42,-43,-44,-45,-46,-47,-48,-49,-50,-72,-73,-74,-75,-76,-77,-78,-79,-80,-52,-56,-51,-53,-54,66,-87,-55,66,-99,-92,-81,-82,-84,-85,66,-66,-67,-9,66,-10,-89,-68,66,66,-83,-86,-88,-90,-96,-11,66,-2,-91,66,-3,-97,-98,66,-4,66,-69,-70,-71,-93,-94,-95,]),'PRINT':([10,11,12,13,14,15,16,17,18,19,21,34,35,36,37,38,39,40,41,42,45,46,47,49,50,52,53,54,55,56,57,58,59,60,61,62,70,71,72,73,74,75,76,77,78,86,87,94,103,119,121,125,136,137,139,140,145,146,148,149,156,157,158,161,162,163,168,173,177,178,180,181,182,183,186,190,191,193,195,199,201,205,206,207,208,211,212,213,216,221,224,225,],[-20,-22,-24,-30,-33,-37,-38,-39,-40,-56,-63,-36,-61,-21,-23,-25,-31,-32,-34,-35,-64,-65,-57,-60,67,-62,-41,-42,-43,-44,-45,-46,-47,-48,-49,-50,-72,-73,-74,-75,-76,-77,-78,-79,-80,-52,-56,-51,-53,-54,67,-87,-55,67,-99,-92,-81,-82,-84,-85,67,-66,-67,-9,67,-10,-89,-68,67,67,-83,-86,-88,-90,-96,-11,67,-2,-91,67,-3,-97,-98,67,-4,67,-69,-70,-71,-93,-94,-95,]),'WHILE':([10,11,12,13,14,15,16,17,18,19,21,34,35,36,37,38,39,40,41,42,45,46,47,49,50,52,53,54,55,56,57,58,59,60,61,62,70,71,72,73,74,75,76,77,78,86,87,94,103,119,121,125,136,137,139,140,145,146,148,149,156,157,158,161,162,163,168,173,177,178,180,181,182,183,186,190,191,193,195,199,201,205,206,207,208,211,212,213,216,221,224,225,],[-20,-22,-24,-30,-33,-37,-38,-39,-40,-56,-63,-36,-61,-21,-23,-25,-31,-32,-34,-35,-64,-65,-57,-60,68,-62,-41,-42,-43,-44,-45,-46,-47,-48,-49,-50,-72,-73,-74,-75,-76,-77,-78,-79,-80,-52,-56,-51,-53,-54,68,-87,-55,68,-99,-92,-81,-82,-84,-85,68,-66,-67,-9,68,-10,-89,-68,68,68,-83,-86,-88,-90,-96,-11,68,-2,-91,68,-3,-97,-98,68,-4,68,-69,-70,-71,-93,-94,-95,]),'FOR':([10,11,12,13,14,15,16,17,18,19,21,34,35,36,37,38,39,40,41,42,45,46,47,49,50,52,53,54,55,56,57,58,59,60,61,62,70,71,72,73,74,75,76,77,78,86,87,94,103,119,121,125,136,137,139,140,145,146,148,149,156,157,158,161,162,163,168,173,177,178,180,181,182,183,186,190,191,193,195,199,201,205,206,207,208,211,212,213,216,221,224,225,],[-20,-22,-24,-30,-33,-37,-38,-39,-40,-56,-63,-36,-61,-21,-23,-25,-31,-32,-34,-35,-64,-65,-57,-60,69,-62,-41,-42,-43,-44,-45,-46,-47,-48,-49,-50,-72,-73,-74,-75,-76,-77,-78,-79,-80,-52,-56,-51,-53,-54,69,-87,-55,69,-99,-92,-81,-82,-84,-85,69,-66,-67,-9,69,-10,-89,-68,69,69,-83,-86,-88,-90,-96,-11,69,-2,-91,69,-3,-97,-98,69,-4,69,-69,-70,-71,-93,-94,-95,]),'MEAN':([10,11,12,13,14,15,16,17,18,19,21,34,35,36,37,38,39,40,41,42,45,46,47,49,50,52,53,54,55,56,57,58,59,60,61,62,70,71,72,73,74,75,76,77,78,86,87,94,103,119,121,125,136,137,139,140,145,146,148,149,156,157,158,161,162,163,168,173,177,178,180,181,182,183,186,190,191,193,195,199,201,205,206,207,208,211,212,213,216,221,224,225,],[-20,-22,-24,-30,-33,-37,-38,-39,-40,-56,-63,-36,-61,-21,-23,-25,-31,-32,-34,-35,-64,-65,-57,-60,79,-62,-41,-42,-43,-44,-45,-46,-47,-48,-49,-50,-72,-73,-74,-75,-76,-77,-78,-79,-80,-52,-56,-51,-53,-54,79,-87,-55,79,-99,-92,-81,-82,-84,-85,79,-66,-67,-9,79,-10,-89,-68,79,79,-83,-86,-88,-90,-96,-11,79,-2,-91,79,-3,-97,-98,79,-4,79,-69,-70,-71,-93,-94,-95,]),'VAR':([10,11,12,13,14,15,16,17,18,19,21,34,35,36,37,38,39,40,41,42,45,47,49,52,53,54,55,56,57,58,59,60,61,62,70,71,72,73,74,75,76,77,78,86,87,94,103,119,125,136,139,140,145,146,148,149,157,158,161,162,163,168,173,178,180,181,182,183,186,190,191,193,195,205,206,208,212,213,216,221,224,225,],[-20,-22,-24,-30,-33,-37,-38,-39,-40,-56,-63,-36,-61,-21,-23,-25,-31,-32,-34,-35,-64,-57,-60,-62,-41,-42,-43,-44,-45,-46,-47,-48,-49,-50,-72,-73,-74,-75,-76,-77,-78,-79,-80,-52,-56,-51,-53,-54,-87,-55,-99,-92,-81,-82,-84,-85,-66,-67,-9,179,-10,-89,-68,179,-83,-86,-88,-90,-96,-11,179,179,-91,-97,-98,-4,-69,-70,-71,-93,-94,-95,]),'RBRACE':([10,11,12,13,14,15,16,17,18,19,21,34,35,36,37,38,39,40,41,42,45,47,49,52,53,54,55,56,57,58,59,60,61,62,70,71,72,73,74,75,76,77,78,86,87,94,103,119,125,136,139,140,145,146,148,149,157,158,161,162,163,168,173,176,177,178,180,181,182,183,186,190,191,192,193,195,200,201,205,206,208,212,213,216,221,224,225,],[-20,-22,-24,-30,-33,-37,-38,-39,-40,-56,-63,-36,-61,-21,-23,-25,-31,-32,-34,-35,-64,-57,-60,-62,-41,-42,-43,-44,-45,-46,-47,-48,-49,-50,-72,-73,-74,-75,-76,-77,-78,-79,-80,-52,-56,-51,-53,-54,-87,-55,-99,-92,-81,-82,-84,-85,-66,-67,-9,-15,-10,-89,-68,190,-14,-15,-83,-86,-88,-90,-96,-11,-15,-13,-2,-91,-12,-3,-97,-98,-4,-69,-70,-71,-93,-94,-95,]),'RBRACKET':([10,11,12,13,14,15,16,17,18,19,21,34,35,36,37,38,39,40,41,42,45,47,49,52,53,54,55,56,57,58,59,60,61,62,70,71,72,73,74,75,76,77,78,86,87,94,103,119,125,136,139,140,145,146,148,149,153,157,158,161,163,168,173,180,181,182,183,184,186,187,188,190,195,205,206,207,211,212,213,216,221,224,225,],[-20,-22,-24,-30,-33,-37,-38,-39,-40,-56,-63,-36,-61,-21,-23,-25,-31,-32,-34,-35,-64,-57,-60,-62,-41,-42,-43,-44,-45,-46,-47,-48,-49,-50,-72,-73,-74,-75,-76,-77,-78,-79,-80,-52,-56,-51,-53,-54,-87,-55,-99,-92,-81,-82,-84,-85,169,-66,-67,-9,-10,-89,-68,-83,-86,-88,-90,169,-96,197,198,-11,-91,-97,-98,213,213,-69,-70,-71,-93,-94,-95,]),'COMMA':([10,11,12,13,14,15,16,17,18,19,34,36,37,38,39,40,41,42,47,87,104,130,131,142,145,146,153,171,180,182,184,196,203,217,],[-20,-22,-24,-30,-33,-37,-38,-39,-40,-56,-36,-21,-23,-25,-31,-32,-34,-35,-57,-56,120,147,150,160,-81,-82,170,185,-83,-88,170,204,209,218,]),'OR':([10,11,12,13,14,15,16,17,18,19,34,37,38,39,40,41,42,47,],[22,-22,-24,-30,-33,-37,-38,-39,-40,-56,-36,-23,-25,-31,-32,-34,-35,-57,]),'AND':([11,12,13,14,15,16,17,18,19,34,38,39,40,41,42,47,],[23,-24,-30,-33,-37,-38,-39,-40,-56,-36,-25,-31,-32,-34,-35,-57,]),'LT':([12,13,14,15,16,17,18,19,34,39,40,41,42,47,],[25,-30,-33,-37,-38,-39,-40,-56,-36,-31,-32,-34,-35,-57,]),'GT':([12,13,14,15,16,17,18,19,34,39,40,41,42,47,],[26,-30,-33,-37,-38,-39,-40,-56,-36,-31,-32,-34,-35,-57,]),'IFEQUAL':([12,13,14,15,16,17,18,19,34,39,40,41,42,47,],[27,-30,-33,-37,-38,-39,-40,-56,-36,-31,-32,-34,-35,-57,]),'DIFF':([12,13,14,15,16,17,18,19,34,39,40,41,42,47,],[28,-30,-33,-37,-38,-39,-40,-56,-36,-31,-32,-34,-35,-57,]),'PLUS':([13,14,15,16,17,18,19,34,41,42,47,],[29,-33,-37,-38,-39,-40,-56,-36,-34,-35,-57,]),'MINUS':([13,14,15,16,17,18,19,34,41,42,47,],[30,-33,-37,-38,-39,-40,-56,-36,-34,-35,-57,]),'MULT':([14,15,16,17,18,19,34,47,],[31,-37,-38,-39,-40,-56,-36,-57,]),'DIV':([14,15,16,17,18,19,34,47,],[32,-37,-38,-39,-40,-56,-36,-57,]),'ELSE':([21,35,],[-63,46,]),'EQUAL':([63,65,97,110,132,152,210,219,],[80,85,113,126,151,167,215,220,]),'VOID':([64,],[82,]),'INT':([64,111,112,151,160,172,179,215,],[83,83,83,166,83,187,83,217,]),'FLOAT':([64,111,112,160,172,179,],[84,84,84,84,188,84,]),'DOT':([73,74,102,168,182,183,195,],[91,92,118,-89,-88,-90,-91,]),'ARRAY':([85,126,],[98,98,]),'MATRIX':([85,],[99,]),'LAYERS':([85,167,],[100,100,]),'SEQUENTIAL':([85,113,],[101,101,]),'GETWEIGHTS':([91,],[107,]),'COMPILE':([92,],[108,]),'UNITS':([116,],[132,]),'LBRACKET':([117,155,189,],[133,172,199,]),'FIT':([118,],[134,]),'PREDICT':([118,],[135,]),'LBRACE':([143,144,],[162,162,]),'EPOCHS':([204,],[210,]),'VERBOSE':([218,],[219,]),'TRUE':([220,],[222,]),'FALSE':([220,],[223,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'program':([0,],[1,]),'if':([4,50,121,137,156,162,177,178,191,199,207,211,],[5,59,59,59,59,59,59,59,59,59,59,59,]),'exp':([7,8,22,33,48,80,88,89,120,122,159,],[9,20,36,44,44,94,104,105,104,138,174,]),'texp':([7,8,22,23,33,48,80,88,89,120,122,159,],[10,10,10,37,10,10,10,10,10,10,10,10,]),'gexp':([7,8,22,23,33,48,80,88,89,120,122,159,],[11,11,11,11,11,11,11,11,11,11,11,11,]),'mexp':([7,8,22,23,24,29,30,33,48,80,88,89,120,122,159,],[12,12,12,12,38,39,40,12,12,12,12,12,12,12,12,]),'t':([7,8,22,23,24,29,30,31,32,33,48,80,88,89,120,122,159,],[13,13,13,13,13,13,13,41,42,13,13,13,13,13,13,13,13,]),'f':([7,8,22,23,24,29,30,31,32,33,48,80,88,89,120,122,159,],[14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,]),'var':([7,8,22,23,24,29,30,31,32,33,48,50,66,80,88,89,90,114,120,121,122,137,147,156,159,162,177,178,191,199,207,211,],[17,17,17,17,17,17,17,17,17,17,17,63,86,17,17,17,106,130,17,63,17,63,164,63,17,63,63,63,63,63,63,63,]),'call':([7,8,22,23,24,29,30,31,32,33,48,50,80,88,89,120,121,122,137,156,159,162,177,178,191,199,207,211,],[18,18,18,18,18,18,18,18,18,18,18,56,18,18,18,18,56,18,56,56,18,56,56,56,56,56,56,56,]),'gexpp':([12,],[24,]),'quadsIf':([21,],[35,]),'callp':([33,48,],[43,51,]),'ifp':([35,],[45,]),'jumpsIf':([45,],[49,]),'quadsElse':([46,],[50,]),'statements':([50,121,137,156,162,177,178,191,199,207,211,],[52,137,156,156,178,191,178,178,207,211,211,]),'assign':([50,121,137,156,162,177,178,191,199,207,211,],[53,53,53,53,53,53,53,53,53,53,53,]),'function':([50,121,137,156,162,177,178,191,199,207,211,],[54,54,54,54,54,54,54,54,54,54,54,]),'voidfunction':([50,121,137,156,162,177,178,191,199,207,211,],[55,55,55,55,55,55,55,55,55,55,55,]),'read':([50,121,137,156,162,177,178,191,199,207,211,],[57,57,57,57,57,57,57,57,57,57,57,]),'print':([50,121,137,156,162,177,178,191,199,207,211,],[58,58,58,58,58,58,58,58,58,58,58,]),'while':([50,121,137,156,162,177,178,191,199,207,211,],[60,60,60,60,60,60,60,60,60,60,60,]),'for':([50,121,137,156,162,177,178,191,199,207,211,],[61,61,61,61,61,61,61,61,61,61,61,]),'funcesp':([50,121,137,156,162,177,178,191,199,207,211,],[62,62,62,62,62,62,62,62,62,62,62,]),'array':([50,93,115,121,137,150,154,156,162,177,178,185,191,199,207,211,],[70,109,131,70,70,165,171,70,70,70,70,196,70,70,70,70,]),'matrix':([50,121,137,156,162,177,178,191,199,207,211,],[71,71,71,71,71,71,71,71,71,71,71,]),'mean':([50,121,137,156,162,177,178,191,199,207,211,],[72,72,72,72,72,72,72,72,72,72,72,]),'layers':([50,121,133,137,156,162,170,177,178,191,199,207,211,],[73,73,153,73,73,73,184,73,73,73,73,73,73,]),'sequential':([50,85,121,137,156,162,177,178,191,199,207,211,],[74,102,74,74,74,74,74,74,74,74,74,74,]),'compile':([50,121,137,156,162,177,178,191,199,207,211,],[75,75,75,75,75,75,75,75,75,75,75,]),'fit':([50,121,137,156,162,177,178,191,199,207,211,],[76,76,76,76,76,76,76,76,76,76,76,]),'predict':([50,121,137,156,162,177,178,191,199,207,211,],[77,77,77,77,77,77,77,77,77,77,77,]),'getweights':([50,121,137,156,162,177,178,191,199,207,211,],[78,78,78,78,78,78,78,78,78,78,78,]),'type':([64,111,112,160,179,],[81,127,127,127,194,]),'printp':([88,120,],[103,136,]),'param':([111,112,160,],[128,129,175,]),'paramp':([127,],[141,]),'arrayp':([130,],[145,]),'matrixp':([131,],[148,]),'whilep':([137,156,],[157,173,]),'body':([143,144,],[161,163,]),'sequentialp':([153,184,],[168,195,]),'bodyp':([162,178,191,],[176,192,200,]),'decvar':([162,178,191,193,],[177,177,177,201,]),'predictp':([172,],[186,]),'decvarp':([179,],[193,]),'decvarpp':([194,209,],[202,214,]),'forp':([207,211,],[212,216,]),'fitp':([220,],[221,]),}

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
  ('decvarpp -> ID COMMA decvarpp','decvarpp',3,'p_decvarpp','bixoParser.py',205),
  ('decvarpp -> ID','decvarpp',1,'p_decvarpp','bixoParser.py',206),
  ('type -> INT','type',1,'p_type','bixoParser.py',217),
  ('type -> FLOAT','type',1,'p_type','bixoParser.py',218),
  ('function -> FUNCTION type ID LPAREN param RPAREN body','function',7,'p_function','bixoParser.py',222),
  ('voidfunction -> FUNCTION VOID ID LPAREN param RPAREN body','voidfunction',7,'p_voidfunction','bixoParser.py',225),
  ('body -> LBRACE bodyp RBRACE','body',3,'p_body','bixoParser.py',228),
  ('bodyp -> decvar statements bodyp','bodyp',3,'p_bodyp','bixoParser.py',232),
  ('bodyp -> statements bodyp','bodyp',2,'p_bodyp','bixoParser.py',233),
  ('bodyp -> decvar','bodyp',1,'p_bodyp','bixoParser.py',234),
  ('bodyp -> <empty>','bodyp',0,'p_bodyp','bixoParser.py',235),
  ('param -> <empty>','param',0,'p_param','bixoParser.py',238),
  ('param -> type paramp','param',2,'p_param','bixoParser.py',239),
  ('paramp -> ID','paramp',1,'p_paramp','bixoParser.py',243),
  ('paramp -> ID COMMA param','paramp',3,'p_paramp','bixoParser.py',244),
  ('exp -> texp','exp',1,'p_exp','bixoParser.py',250),
  ('exp -> texp OR exp','exp',3,'p_exp','bixoParser.py',251),
  ('texp -> gexp','texp',1,'p_texp','bixoParser.py',257),
  ('texp -> gexp AND texp','texp',3,'p_texp','bixoParser.py',258),
  ('gexp -> mexp','gexp',1,'p_gexp','bixoParser.py',264),
  ('gexp -> mexp gexpp mexp','gexp',3,'p_gexp','bixoParser.py',265),
  ('gexpp -> LT','gexpp',1,'p_gexpp','bixoParser.py',271),
  ('gexpp -> GT','gexpp',1,'p_gexpp','bixoParser.py',272),
  ('gexpp -> IFEQUAL','gexpp',1,'p_gexpp','bixoParser.py',273),
  ('gexpp -> DIFF','gexpp',1,'p_gexpp','bixoParser.py',274),
  ('mexp -> t','mexp',1,'p_mexp','bixoParser.py',278),
  ('mexp -> t PLUS mexp','mexp',3,'p_mexp','bixoParser.py',279),
  ('mexp -> t MINUS mexp','mexp',3,'p_mexp','bixoParser.py',280),
  ('t -> f','t',1,'p_t','bixoParser.py',291),
  ('t -> f MULT t','t',3,'p_t','bixoParser.py',292),
  ('t -> f DIV t','t',3,'p_t','bixoParser.py',293),
  ('f -> LPAREN exp RPAREN','f',3,'p_f','bixoParser.py',303),
  ('f -> CTI','f',1,'p_f','bixoParser.py',304),
  ('f -> CTF','f',1,'p_f','bixoParser.py',305),
  ('f -> var','f',1,'p_f','bixoParser.py',306),
  ('f -> call','f',1,'p_f','bixoParser.py',307),
  ('statements -> assign','statements',1,'p_statements','bixoParser.py',312),
  ('statements -> function','statements',1,'p_statements','bixoParser.py',313),
  ('statements -> voidfunction','statements',1,'p_statements','bixoParser.py',314),
  ('statements -> call','statements',1,'p_statements','bixoParser.py',315),
  ('statements -> read','statements',1,'p_statements','bixoParser.py',316),
  ('statements -> print','statements',1,'p_statements','bixoParser.py',317),
  ('statements -> if','statements',1,'p_statements','bixoParser.py',318),
  ('statements -> while','statements',1,'p_statements','bixoParser.py',319),
  ('statements -> for','statements',1,'p_statements','bixoParser.py',320),
  ('statements -> funcesp','statements',1,'p_statements','bixoParser.py',321),
  ('assign -> var EQUAL exp','assign',3,'p_assign','bixoParser.py',325),
  ('read -> READ var','read',2,'p_read','bixoParser.py',354),
  ('print -> PRINT LPAREN printp','print',3,'p_print','bixoParser.py',357),
  ('printp -> exp RPAREN','printp',2,'p_printp','bixoParser.py',360),
  ('printp -> exp COMMA printp','printp',3,'p_printp','bixoParser.py',361),
  ('var -> ID','var',1,'p_var','bixoParser.py',364),
  ('call -> ID LPAREN callp RPAREN','call',4,'p_call','bixoParser.py',368),
  ('callp -> exp SEMICOLON callp','callp',3,'p_callp','bixoParser.py',371),
  ('callp -> exp','callp',1,'p_callp','bixoParser.py',372),
  ('if -> IF LPAREN exp RPAREN quadsIf ifp jumpsIf','if',7,'p_if','bixoParser.py',378),
  ('ifp -> <empty>','ifp',0,'p_ifp','bixoParser.py',381),
  ('ifp -> ELSE quadsElse statements','ifp',3,'p_ifp','bixoParser.py',382),
  ('quadsIf -> <empty>','quadsIf',0,'p_quadsIf','bixoParser.py',385),
  ('jumpsIf -> <empty>','jumpsIf',0,'p_jumpsIf','bixoParser.py',403),
  ('quadsElse -> <empty>','quadsElse',0,'p_quadsElse','bixoParser.py',409),
  ('while -> WHILE LPAREN exp RPAREN statements whilep','while',6,'p_while','bixoParser.py',419),
  ('whilep -> SEMICOLON','whilep',1,'p_whilep','bixoParser.py',422),
  ('whilep -> statements whilep','whilep',2,'p_whilep','bixoParser.py',423),
  ('for -> FOR LPAREN var SEMICOLON exp SEMICOLON exp RPAREN LBRACKET statements forp','for',11,'p_for','bixoParser.py',442),
  ('forp -> RBRACKET','forp',1,'p_forp','bixoParser.py',445),
  ('forp -> statements forp','forp',2,'p_forp','bixoParser.py',446),
  ('funcesp -> array','funcesp',1,'p_funcesp','bixoParser.py',451),
  ('funcesp -> matrix','funcesp',1,'p_funcesp','bixoParser.py',452),
  ('funcesp -> mean','funcesp',1,'p_funcesp','bixoParser.py',453),
  ('funcesp -> layers','funcesp',1,'p_funcesp','bixoParser.py',454),
  ('funcesp -> sequential','funcesp',1,'p_funcesp','bixoParser.py',455),
  ('funcesp -> compile','funcesp',1,'p_funcesp','bixoParser.py',456),
  ('funcesp -> fit','funcesp',1,'p_funcesp','bixoParser.py',457),
  ('funcesp -> predict','funcesp',1,'p_funcesp','bixoParser.py',458),
  ('funcesp -> getweights','funcesp',1,'p_funcesp','bixoParser.py',459),
  ('array -> ID EQUAL ARRAY LPAREN var arrayp','array',6,'p_array','bixoParser.py',462),
  ('arrayp -> RPAREN','arrayp',1,'p_arrayp','bixoParser.py',465),
  ('arrayp -> COMMA var RPAREN','arrayp',3,'p_arrayp','bixoParser.py',466),
  ('matrix -> ID EQUAL MATRIX LPAREN array matrixp','matrix',6,'p_matrix','bixoParser.py',469),
  ('matrixp -> RPAREN','matrixp',1,'p_matrixp','bixoParser.py',472),
  ('matrixp -> COMMA array RPAREN','matrixp',3,'p_matrixp','bixoParser.py',473),
  ('mean -> MEAN LPAREN array RPAREN','mean',4,'p_mean','bixoParser.py',476),
  ('layers -> ID EQUAL LAYERS LPAREN UNITS EQUAL INT RPAREN','layers',8,'p_layers','bixoParser.py',479),
  ('sequential -> ID EQUAL SEQUENTIAL LPAREN LBRACKET layers sequentialp','sequential',7,'p_sequential','bixoParser.py',482),
  ('sequentialp -> RBRACKET RPAREN','sequentialp',2,'p_sequentialp','bixoParser.py',485),
  ('sequentialp -> COMMA layers sequentialp','sequentialp',3,'p_sequentialp','bixoParser.py',486),
  ('compile -> sequential DOT COMPILE LPAREN RPAREN','compile',5,'p_compile','bixoParser.py',489),
  ('fit -> ID EQUAL sequential DOT FIT LPAREN array COMMA array COMMA EPOCHS EQUAL INT COMMA VERBOSE EQUAL fitp','fit',17,'p_fit','bixoParser.py',492),
  ('fitp -> TRUE RPAREN','fitp',2,'p_fitp','bixoParser.py',495),
  ('fitp -> FALSE RPAREN','fitp',2,'p_fitp','bixoParser.py',496),
  ('predict -> ID EQUAL sequential DOT PREDICT LPAREN LBRACKET predictp','predict',8,'p_predict','bixoParser.py',499),
  ('predictp -> INT RBRACKET RPAREN','predictp',3,'p_predictp','bixoParser.py',502),
  ('predictp -> FLOAT RBRACKET RPAREN','predictp',3,'p_predictp','bixoParser.py',503),
  ('getweights -> layers DOT GETWEIGHTS LPAREN RPAREN','getweights',5,'p_getweights','bixoParser.py',506),
  ('empty -> <empty>','empty',0,'p_empty','bixoParser.py',510),
]
