
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'leftLTLTEGTGTEleftPLUSMINUSleftMULTDIVleftEQUALDIFFleftLPARENRPARENleftLBRACERBRACEleftLBRACKETRBRACKETAND ARRAY ASSIGN CHAR COLON COMMA COMPILE CTF CTI DIFF DIV DOT ELSE END EPOCHS EQUAL FALSE FIT FLOAT FOR FUNCESP FUNCTION GETWEIGHTS GT GTE ID IF IFEQUAL INT LAYERS LBRACE LBRACKET LPAREN LT LTE MAIN MATRIX MEAN MINUS MULT NUMPY OR PLUS PREDICT PRINT PROGRAM QUOTE RBRACE RBRACKET READ RPAREN SEMICOLON SEQUENTIAL STRING TRUE UNITS VAR VERBOSE VOID WHILEprogram : PROGRAM ID SEMICOLON decvar modules mainfunctiondecvar : VAR decvarp\n              | VAR decvarp decvardecvarp : type decvarpp SEMICOLONdecvarpp : ID COMMA decvarpp\n                | IDtype : INT\n            | FLOATfunction : FUNCTION type decfunc LPAREN param RPAREN LBRACE body RBRACEdecfunc : IDvoidfunction : FUNCTION VOID decfunc LPAREN param RPAREN LBRACE body RBRACEmainfunction : MAINmodules : function modules\n               | voidfunction modules\n               | function\n               | voidfunctionbody : decvar statements body\n            | statements body\n            | decvar\n            | param : type ID\n             | type ID COMMA paramexp : texp \n           | texp OR exptexp : gexp \n            | gexp AND texpgexp : mexp \n            | mexp gexpp mexpgexpp : LT\n             | GT\n             | EQUAL\n             | DIFFmexp : t\n            | t PLUS mexp\n            | t MINUS mexpt : f \n         | f MULT t\n         | f DIV tf : LPAREN exp RPAREN\n         | CTI\n         | CTF\n         | var\n         | callstatements : assign\n                 |  function\n                 |  voidfunction\n                 |  call\n                 |  read\n                 |  print\n                 |  if\n                 |  while\n                 |  for\n                 |  funcespassign : var EQUAL exp SEMICOLONread : READ varprint : PRINT LPAREN printpprintp : exp RPAREN\n              | exp COMMA printpvar : ID call : ID LPAREN callp RPARENcallp : exp SEMICOLON callp\n             | expif : IF LPAREN CTI GT CTI RPAREN quadsIf ifp jumpsIf ifp : \n            | ELSE quadsElse statementsquadsIf : jumpsIf : quadsElse :  while : WHILE LPAREN exp RPAREN statements whilep whilep : SEMICOLON\n               | statements whilepfor : FOR LPAREN var SEMICOLON exp SEMICOLON exp RPAREN LBRACKET statements forp forp : RBRACKET\n             | statements forp funcesp : array\n                | matrix\n                | mean\n                | layers\n                | sequential\n                | compile\n                | fit\n                | predict\n                | getweights array : ID EQUAL ARRAY LPAREN var arrayp arrayp : RPAREN\n               | COMMA var RPAREN matrix : ID EQUAL MATRIX LPAREN array matrixp matrixp : RPAREN\n                | COMMA array RPARENmean : MEAN LPAREN array RPARENlayers : ID EQUAL LAYERS LPAREN UNITS EQUAL INT RPAREN sequential : ID EQUAL SEQUENTIAL LPAREN LBRACKET layers sequentialp sequentialp : RBRACKET RPAREN\n                    | COMMA layers sequentialp compile : sequential DOT COMPILE LPAREN RPAREN fit : ID EQUAL sequential DOT FIT LPAREN array COMMA array COMMA EPOCHS EQUAL INT COMMA VERBOSE EQUAL fitp fitp : TRUE RPAREN\n             | FALSE RPAREN predict : ID EQUAL sequential DOT PREDICT LPAREN LBRACKET predictp predictp : INT RBRACKET RPAREN\n                 | FLOAT RBRACKET RPAREN getweights : layers DOT GETWEIGHTS LPAREN RPARENempty :'
    
_lr_action_items = {'PROGRAM':([0,],[2,]),'$end':([1,15,16,],[0,-1,-12,]),'ID':([2,11,12,13,14,19,20,21,27,28,32,39,40,43,44,45,46,47,48,49,50,51,52,53,54,57,62,63,64,65,66,67,68,69,70,73,74,76,77,78,79,80,81,83,84,87,88,97,110,119,120,121,122,123,124,125,126,127,128,129,130,132,133,135,136,140,141,143,144,147,161,164,166,168,169,170,171,172,173,174,175,179,181,182,183,184,185,190,192,195,196,198,199,200,201,203,204,207,208,210,214,215,216,218,219,220,221,223,224,225,227,232,235,236,],[3,-2,23,-7,-8,25,25,-3,-4,23,35,56,56,56,56,-44,-45,-46,-47,-48,-49,-50,-51,-52,-53,80,-75,-76,-77,-78,-79,-80,-81,-82,-83,-9,56,101,101,104,-55,-59,101,101,80,118,-11,101,-56,-54,101,101,101,-29,-30,-31,-32,101,101,101,101,-60,101,80,118,-57,101,56,101,-90,177,-58,56,-102,-95,-84,-85,80,-87,-88,118,118,-66,56,-69,-70,101,-92,177,-64,-71,-86,-89,-91,-93,118,-99,-67,-68,-94,-63,56,56,-100,-101,-65,56,56,-72,-73,-74,-96,-97,-98,]),'SEMICOLON':([3,22,23,31,45,46,47,48,49,50,51,52,53,54,62,63,64,65,66,67,68,69,70,73,79,80,88,90,91,92,93,94,95,96,98,99,100,101,103,110,114,119,132,140,147,149,150,151,152,153,154,155,156,164,166,167,168,169,170,171,173,174,181,182,183,184,190,195,196,198,199,200,201,204,207,210,214,218,219,220,224,225,227,232,235,236,],[4,27,-6,-5,-44,-45,-46,-47,-48,-49,-50,-51,-52,-53,-75,-76,-77,-78,-79,-80,-81,-82,-83,-9,-55,-59,-11,-42,119,-23,-25,-27,-33,-36,-40,-41,-43,-59,133,-56,144,-54,-60,-57,-90,-24,-26,-28,-34,-35,-37,-38,-39,-58,184,185,-102,-95,-84,-85,-87,-88,-66,184,-69,-70,-92,-64,-71,-86,-89,-91,-93,-99,-67,-94,-63,-100,-101,-65,-72,-73,-74,-96,-97,-98,]),'VAR':([4,11,27,39,40,44,45,46,47,48,49,50,51,52,53,54,62,63,64,65,66,67,68,69,70,73,74,79,80,88,110,119,132,140,147,164,168,169,170,171,173,174,181,183,184,190,195,196,198,199,200,201,204,207,210,214,218,219,220,224,225,227,232,235,236,],[6,6,-4,6,6,6,-44,-45,-46,-47,-48,-49,-50,-51,-52,-53,-75,-76,-77,-78,-79,-80,-81,-82,-83,-9,6,-55,-59,-11,-56,-54,-60,-57,-90,-58,-102,-95,-84,-85,-87,-88,-66,-69,-70,-92,-64,-71,-86,-89,-91,-93,-99,-67,-94,-63,-100,-101,-65,-72,-73,-74,-96,-97,-98,]),'FUNCTION':([5,8,9,11,21,27,39,40,43,44,45,46,47,48,49,50,51,52,53,54,62,63,64,65,66,67,68,69,70,73,74,79,80,88,110,119,132,140,143,147,164,166,168,169,170,171,173,174,181,182,183,184,190,195,196,198,199,200,201,204,207,208,210,214,215,216,218,219,220,221,223,224,225,227,232,235,236,],[10,10,10,-2,-3,-4,10,10,10,10,-44,-45,-46,-47,-48,-49,-50,-51,-52,-53,-75,-76,-77,-78,-79,-80,-81,-82,-83,-9,10,-55,-59,-11,-56,-54,-60,-57,10,-90,-58,10,-102,-95,-84,-85,-87,-88,-66,10,-69,-70,-92,-64,-71,-86,-89,-91,-93,-99,-67,-68,-94,-63,10,10,-100,-101,-65,10,10,-72,-73,-74,-96,-97,-98,]),'INT':([6,10,29,30,38,176,194,226,],[13,13,13,13,13,188,205,228,]),'FLOAT':([6,10,29,30,38,194,],[14,14,14,14,14,206,]),'MAIN':([7,8,9,17,18,73,88,],[16,-15,-16,-13,-14,-9,-11,]),'VOID':([10,],[20,]),'READ':([11,21,27,39,40,43,44,45,46,47,48,49,50,51,52,53,54,62,63,64,65,66,67,68,69,70,73,74,79,80,88,110,119,132,140,143,147,164,166,168,169,170,171,173,174,181,182,183,184,190,195,196,198,199,200,201,204,207,208,210,214,215,216,218,219,220,221,223,224,225,227,232,235,236,],[-2,-3,-4,57,57,57,57,-44,-45,-46,-47,-48,-49,-50,-51,-52,-53,-75,-76,-77,-78,-79,-80,-81,-82,-83,-9,57,-55,-59,-11,-56,-54,-60,-57,57,-90,-58,57,-102,-95,-84,-85,-87,-88,-66,57,-69,-70,-92,-64,-71,-86,-89,-91,-93,-99,-67,-68,-94,-63,57,57,-100,-101,-65,57,57,-72,-73,-74,-96,-97,-98,]),'PRINT':([11,21,27,39,40,43,44,45,46,47,48,49,50,51,52,53,54,62,63,64,65,66,67,68,69,70,73,74,79,80,88,110,119,132,140,143,147,164,166,168,169,170,171,173,174,181,182,183,184,190,195,196,198,199,200,201,204,207,208,210,214,215,216,218,219,220,221,223,224,225,227,232,235,236,],[-2,-3,-4,58,58,58,58,-44,-45,-46,-47,-48,-49,-50,-51,-52,-53,-75,-76,-77,-78,-79,-80,-81,-82,-83,-9,58,-55,-59,-11,-56,-54,-60,-57,58,-90,-58,58,-102,-95,-84,-85,-87,-88,-66,58,-69,-70,-92,-64,-71,-86,-89,-91,-93,-99,-67,-68,-94,-63,58,58,-100,-101,-65,58,58,-72,-73,-74,-96,-97,-98,]),'IF':([11,21,27,39,40,43,44,45,46,47,48,49,50,51,52,53,54,62,63,64,65,66,67,68,69,70,73,74,79,80,88,110,119,132,140,143,147,164,166,168,169,170,171,173,174,181,182,183,184,190,195,196,198,199,200,201,204,207,208,210,214,215,216,218,219,220,221,223,224,225,227,232,235,236,],[-2,-3,-4,59,59,59,59,-44,-45,-46,-47,-48,-49,-50,-51,-52,-53,-75,-76,-77,-78,-79,-80,-81,-82,-83,-9,59,-55,-59,-11,-56,-54,-60,-57,59,-90,-58,59,-102,-95,-84,-85,-87,-88,-66,59,-69,-70,-92,-64,-71,-86,-89,-91,-93,-99,-67,-68,-94,-63,59,59,-100,-101,-65,59,59,-72,-73,-74,-96,-97,-98,]),'WHILE':([11,21,27,39,40,43,44,45,46,47,48,49,50,51,52,53,54,62,63,64,65,66,67,68,69,70,73,74,79,80,88,110,119,132,140,143,147,164,166,168,169,170,171,173,174,181,182,183,184,190,195,196,198,199,200,201,204,207,208,210,214,215,216,218,219,220,221,223,224,225,227,232,235,236,],[-2,-3,-4,60,60,60,60,-44,-45,-46,-47,-48,-49,-50,-51,-52,-53,-75,-76,-77,-78,-79,-80,-81,-82,-83,-9,60,-55,-59,-11,-56,-54,-60,-57,60,-90,-58,60,-102,-95,-84,-85,-87,-88,-66,60,-69,-70,-92,-64,-71,-86,-89,-91,-93,-99,-67,-68,-94,-63,60,60,-100,-101,-65,60,60,-72,-73,-74,-96,-97,-98,]),'FOR':([11,21,27,39,40,43,44,45,46,47,48,49,50,51,52,53,54,62,63,64,65,66,67,68,69,70,73,74,79,80,88,110,119,132,140,143,147,164,166,168,169,170,171,173,174,181,182,183,184,190,195,196,198,199,200,201,204,207,208,210,214,215,216,218,219,220,221,223,224,225,227,232,235,236,],[-2,-3,-4,61,61,61,61,-44,-45,-46,-47,-48,-49,-50,-51,-52,-53,-75,-76,-77,-78,-79,-80,-81,-82,-83,-9,61,-55,-59,-11,-56,-54,-60,-57,61,-90,-58,61,-102,-95,-84,-85,-87,-88,-66,61,-69,-70,-92,-64,-71,-86,-89,-91,-93,-99,-67,-68,-94,-63,61,61,-100,-101,-65,61,61,-72,-73,-74,-96,-97,-98,]),'MEAN':([11,21,27,39,40,43,44,45,46,47,48,49,50,51,52,53,54,62,63,64,65,66,67,68,69,70,73,74,79,80,88,110,119,132,140,143,147,164,166,168,169,170,171,173,174,181,182,183,184,190,195,196,198,199,200,201,204,207,208,210,214,215,216,218,219,220,221,223,224,225,227,232,235,236,],[-2,-3,-4,71,71,71,71,-44,-45,-46,-47,-48,-49,-50,-51,-52,-53,-75,-76,-77,-78,-79,-80,-81,-82,-83,-9,71,-55,-59,-11,-56,-54,-60,-57,71,-90,-58,71,-102,-95,-84,-85,-87,-88,-66,71,-69,-70,-92,-64,-71,-86,-89,-91,-93,-99,-67,-68,-94,-63,71,71,-100,-101,-65,71,71,-72,-73,-74,-96,-97,-98,]),'RBRACE':([11,21,27,39,40,42,43,44,45,46,47,48,49,50,51,52,53,54,62,63,64,65,66,67,68,69,70,72,73,74,75,79,80,88,89,110,119,132,140,147,164,168,169,170,171,173,174,181,183,184,190,195,196,198,199,200,201,204,207,210,214,218,219,220,224,225,227,232,235,236,],[-2,-3,-4,-20,-20,73,-19,-20,-44,-45,-46,-47,-48,-49,-50,-51,-52,-53,-75,-76,-77,-78,-79,-80,-81,-82,-83,88,-9,-20,-18,-55,-59,-11,-17,-56,-54,-60,-57,-90,-58,-102,-95,-84,-85,-87,-88,-66,-69,-70,-92,-64,-71,-86,-89,-91,-93,-99,-67,-94,-63,-100,-101,-65,-72,-73,-74,-96,-97,-98,]),'COMMA':([23,35,80,90,92,93,94,95,96,98,99,100,101,111,132,149,150,151,152,153,154,155,156,158,159,170,171,178,193,198,200,202,211,228,],[28,38,-59,-42,-23,-25,-27,-33,-36,-40,-41,-43,-59,141,-60,-24,-26,-28,-34,-35,-37,-38,-39,172,175,-84,-85,192,203,-86,-91,192,217,229,]),'LPAREN':([24,25,26,56,58,59,60,61,71,76,77,81,83,97,101,105,106,107,108,115,116,120,121,122,123,124,125,126,127,128,129,130,133,141,144,162,163,185,],[29,-10,30,77,81,82,83,84,87,97,97,97,97,97,77,135,136,137,138,145,146,97,97,97,-29,-30,-31,-32,97,97,97,97,97,97,97,179,180,97,]),'RPAREN':([33,34,35,41,80,90,92,93,94,95,96,98,99,100,101,102,103,111,113,117,131,132,145,146,149,150,151,152,153,154,155,156,157,158,159,165,170,171,186,187,188,191,197,198,212,213,233,234,],[36,37,-21,-22,-59,-42,-23,-25,-27,-33,-36,-40,-41,-43,-59,132,-62,140,143,147,156,-60,168,169,-24,-26,-28,-34,-35,-37,-38,-39,-61,171,174,181,-84,-85,198,199,200,201,209,-86,218,219,235,236,]),'LBRACE':([36,37,],[39,40,]),'RBRACKET':([45,46,47,48,49,50,51,52,53,54,62,63,64,65,66,67,68,69,70,73,79,80,88,110,119,132,140,147,164,168,169,170,171,173,174,178,181,183,184,190,195,196,198,199,200,201,202,204,205,206,207,210,214,218,219,220,221,223,224,225,227,232,235,236,],[-44,-45,-46,-47,-48,-49,-50,-51,-52,-53,-75,-76,-77,-78,-79,-80,-81,-82,-83,-9,-55,-59,-11,-56,-54,-60,-57,-90,-58,-102,-95,-84,-85,-87,-88,191,-66,-69,-70,-92,-64,-71,-86,-89,-91,-93,191,-99,212,213,-67,-94,-63,-100,-101,-65,225,225,-72,-73,-74,-96,-97,-98,]),'EQUAL':([55,56,90,94,95,96,98,99,100,101,104,118,132,152,153,154,155,156,160,177,222,230,],[76,78,-42,125,-33,-36,-40,-41,-43,-59,134,148,-60,-34,-35,-37,-38,-39,176,189,226,231,]),'DOT':([65,66,109,190,200,201,210,],[85,86,139,-92,-91,-93,-94,]),'CTI':([76,77,81,82,83,97,120,121,122,123,124,125,126,127,128,129,130,133,141,142,144,185,],[98,98,98,112,98,98,98,98,98,-29,-30,-31,-32,98,98,98,98,98,98,165,98,98,]),'CTF':([76,77,81,83,97,120,121,122,123,124,125,126,127,128,129,130,133,141,144,185,],[99,99,99,99,99,99,99,99,-29,-30,-31,-32,99,99,99,99,99,99,99,99,]),'ARRAY':([78,148,],[105,105,]),'MATRIX':([78,],[106,]),'LAYERS':([78,189,],[107,107,]),'SEQUENTIAL':([78,134,],[108,108,]),'GETWEIGHTS':([85,],[115,]),'COMPILE':([86,],[116,]),'MULT':([90,96,98,99,100,101,132,156,],[-42,129,-40,-41,-43,-59,-60,-39,]),'DIV':([90,96,98,99,100,101,132,156,],[-42,130,-40,-41,-43,-59,-60,-39,]),'PLUS':([90,95,96,98,99,100,101,132,154,155,156,],[-42,127,-36,-40,-41,-43,-59,-60,-37,-38,-39,]),'MINUS':([90,95,96,98,99,100,101,132,154,155,156,],[-42,128,-36,-40,-41,-43,-59,-60,-37,-38,-39,]),'LT':([90,94,95,96,98,99,100,101,132,152,153,154,155,156,],[-42,123,-33,-36,-40,-41,-43,-59,-60,-34,-35,-37,-38,-39,]),'GT':([90,94,95,96,98,99,100,101,112,132,152,153,154,155,156,],[-42,124,-33,-36,-40,-41,-43,-59,142,-60,-34,-35,-37,-38,-39,]),'DIFF':([90,94,95,96,98,99,100,101,132,152,153,154,155,156,],[-42,126,-33,-36,-40,-41,-43,-59,-60,-34,-35,-37,-38,-39,]),'AND':([90,93,94,95,96,98,99,100,101,132,151,152,153,154,155,156,],[-42,121,-27,-33,-36,-40,-41,-43,-59,-60,-28,-34,-35,-37,-38,-39,]),'OR':([90,92,93,94,95,96,98,99,100,101,132,150,151,152,153,154,155,156,],[-42,120,-25,-27,-33,-36,-40,-41,-43,-59,-60,-26,-28,-34,-35,-37,-38,-39,]),'UNITS':([137,],[160,]),'LBRACKET':([138,180,209,],[161,194,216,]),'FIT':([139,],[162,]),'PREDICT':([139,],[163,]),'ELSE':([181,195,],[-66,208,]),'EPOCHS':([217,],[222,]),'VERBOSE':([229,],[230,]),'TRUE':([231,],[233,]),'FALSE':([231,],[234,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'program':([0,],[1,]),'decvar':([4,11,39,40,44,74,],[5,21,43,43,43,43,]),'modules':([5,8,9,],[7,17,18,]),'function':([5,8,9,39,40,43,44,74,143,166,182,215,216,221,223,],[8,8,8,46,46,46,46,46,46,46,46,46,46,46,46,]),'voidfunction':([5,8,9,39,40,43,44,74,143,166,182,215,216,221,223,],[9,9,9,47,47,47,47,47,47,47,47,47,47,47,47,]),'decvarp':([6,],[11,]),'type':([6,10,29,30,38,],[12,19,32,32,32,]),'mainfunction':([7,],[15,]),'decvarpp':([12,28,],[22,31,]),'decfunc':([19,20,],[24,26,]),'param':([29,30,38,],[33,34,41,]),'body':([39,40,44,74,],[42,72,75,89,]),'statements':([39,40,43,44,74,143,166,182,215,216,221,223,],[44,44,74,44,44,166,182,182,220,221,223,223,]),'assign':([39,40,43,44,74,143,166,182,215,216,221,223,],[45,45,45,45,45,45,45,45,45,45,45,45,]),'call':([39,40,43,44,74,76,77,81,83,97,120,121,122,127,128,129,130,133,141,143,144,166,182,185,215,216,221,223,],[48,48,48,48,48,100,100,100,100,100,100,100,100,100,100,100,100,100,100,48,100,48,48,100,48,48,48,48,]),'read':([39,40,43,44,74,143,166,182,215,216,221,223,],[49,49,49,49,49,49,49,49,49,49,49,49,]),'print':([39,40,43,44,74,143,166,182,215,216,221,223,],[50,50,50,50,50,50,50,50,50,50,50,50,]),'if':([39,40,43,44,74,143,166,182,215,216,221,223,],[51,51,51,51,51,51,51,51,51,51,51,51,]),'while':([39,40,43,44,74,143,166,182,215,216,221,223,],[52,52,52,52,52,52,52,52,52,52,52,52,]),'for':([39,40,43,44,74,143,166,182,215,216,221,223,],[53,53,53,53,53,53,53,53,53,53,53,53,]),'funcesp':([39,40,43,44,74,143,166,182,215,216,221,223,],[54,54,54,54,54,54,54,54,54,54,54,54,]),'var':([39,40,43,44,57,74,76,77,81,83,84,97,120,121,122,127,128,129,130,133,135,141,143,144,166,172,182,185,215,216,221,223,],[55,55,55,55,79,55,90,90,90,90,114,90,90,90,90,90,90,90,90,90,158,90,55,90,55,186,55,90,55,55,55,55,]),'array':([39,40,43,44,74,87,136,143,166,175,179,182,203,215,216,221,223,],[62,62,62,62,62,117,159,62,62,187,193,62,211,62,62,62,62,]),'matrix':([39,40,43,44,74,143,166,182,215,216,221,223,],[63,63,63,63,63,63,63,63,63,63,63,63,]),'mean':([39,40,43,44,74,143,166,182,215,216,221,223,],[64,64,64,64,64,64,64,64,64,64,64,64,]),'layers':([39,40,43,44,74,143,161,166,182,192,215,216,221,223,],[65,65,65,65,65,65,178,65,65,202,65,65,65,65,]),'sequential':([39,40,43,44,74,78,143,166,182,215,216,221,223,],[66,66,66,66,66,109,66,66,66,66,66,66,66,]),'compile':([39,40,43,44,74,143,166,182,215,216,221,223,],[67,67,67,67,67,67,67,67,67,67,67,67,]),'fit':([39,40,43,44,74,143,166,182,215,216,221,223,],[68,68,68,68,68,68,68,68,68,68,68,68,]),'predict':([39,40,43,44,74,143,166,182,215,216,221,223,],[69,69,69,69,69,69,69,69,69,69,69,69,]),'getweights':([39,40,43,44,74,143,166,182,215,216,221,223,],[70,70,70,70,70,70,70,70,70,70,70,70,]),'exp':([76,77,81,83,97,120,133,141,144,185,],[91,103,111,113,131,149,103,111,167,197,]),'texp':([76,77,81,83,97,120,121,133,141,144,185,],[92,92,92,92,92,92,150,92,92,92,92,]),'gexp':([76,77,81,83,97,120,121,133,141,144,185,],[93,93,93,93,93,93,93,93,93,93,93,]),'mexp':([76,77,81,83,97,120,121,122,127,128,133,141,144,185,],[94,94,94,94,94,94,94,151,152,153,94,94,94,94,]),'t':([76,77,81,83,97,120,121,122,127,128,129,130,133,141,144,185,],[95,95,95,95,95,95,95,95,95,95,154,155,95,95,95,95,]),'f':([76,77,81,83,97,120,121,122,127,128,129,130,133,141,144,185,],[96,96,96,96,96,96,96,96,96,96,96,96,96,96,96,96,]),'callp':([77,133,],[102,157,]),'printp':([81,141,],[110,164,]),'gexpp':([94,],[122,]),'arrayp':([158,],[170,]),'matrixp':([159,],[173,]),'whilep':([166,182,],[183,196,]),'sequentialp':([178,202,],[190,210,]),'quadsIf':([181,],[195,]),'predictp':([194,],[204,]),'ifp':([195,],[207,]),'jumpsIf':([207,],[214,]),'quadsElse':([208,],[215,]),'forp':([221,223,],[224,227,]),'fitp':([231,],[232,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> program","S'",1,None,None,None),
  ('program -> PROGRAM ID SEMICOLON decvar modules mainfunction','program',6,'p_program','bixoParser.py',161),
  ('decvar -> VAR decvarp','decvar',2,'p_decvar','bixoParser.py',166),
  ('decvar -> VAR decvarp decvar','decvar',3,'p_decvar','bixoParser.py',167),
  ('decvarp -> type decvarpp SEMICOLON','decvarp',3,'p_decvarp','bixoParser.py',173),
  ('decvarpp -> ID COMMA decvarpp','decvarpp',3,'p_decvarpp','bixoParser.py',218),
  ('decvarpp -> ID','decvarpp',1,'p_decvarpp','bixoParser.py',219),
  ('type -> INT','type',1,'p_type','bixoParser.py',228),
  ('type -> FLOAT','type',1,'p_type','bixoParser.py',229),
  ('function -> FUNCTION type decfunc LPAREN param RPAREN LBRACE body RBRACE','function',9,'p_function','bixoParser.py',233),
  ('decfunc -> ID','decfunc',1,'p_decfunc','bixoParser.py',245),
  ('voidfunction -> FUNCTION VOID decfunc LPAREN param RPAREN LBRACE body RBRACE','voidfunction',9,'p_voidfunction','bixoParser.py',252),
  ('mainfunction -> MAIN','mainfunction',1,'p_mainfunction','bixoParser.py',264),
  ('modules -> function modules','modules',2,'p_modules','bixoParser.py',269),
  ('modules -> voidfunction modules','modules',2,'p_modules','bixoParser.py',270),
  ('modules -> function','modules',1,'p_modules','bixoParser.py',271),
  ('modules -> voidfunction','modules',1,'p_modules','bixoParser.py',272),
  ('body -> decvar statements body','body',3,'p_body','bixoParser.py',278),
  ('body -> statements body','body',2,'p_body','bixoParser.py',279),
  ('body -> decvar','body',1,'p_body','bixoParser.py',280),
  ('body -> <empty>','body',0,'p_body','bixoParser.py',281),
  ('param -> type ID','param',2,'p_param','bixoParser.py',285),
  ('param -> type ID COMMA param','param',4,'p_param','bixoParser.py',286),
  ('exp -> texp','exp',1,'p_exp','bixoParser.py',293),
  ('exp -> texp OR exp','exp',3,'p_exp','bixoParser.py',294),
  ('texp -> gexp','texp',1,'p_texp','bixoParser.py',300),
  ('texp -> gexp AND texp','texp',3,'p_texp','bixoParser.py',301),
  ('gexp -> mexp','gexp',1,'p_gexp','bixoParser.py',306),
  ('gexp -> mexp gexpp mexp','gexp',3,'p_gexp','bixoParser.py',307),
  ('gexpp -> LT','gexpp',1,'p_gexpp','bixoParser.py',316),
  ('gexpp -> GT','gexpp',1,'p_gexpp','bixoParser.py',317),
  ('gexpp -> EQUAL','gexpp',1,'p_gexpp','bixoParser.py',318),
  ('gexpp -> DIFF','gexpp',1,'p_gexpp','bixoParser.py',319),
  ('mexp -> t','mexp',1,'p_mexp','bixoParser.py',323),
  ('mexp -> t PLUS mexp','mexp',3,'p_mexp','bixoParser.py',324),
  ('mexp -> t MINUS mexp','mexp',3,'p_mexp','bixoParser.py',325),
  ('t -> f','t',1,'p_t','bixoParser.py',336),
  ('t -> f MULT t','t',3,'p_t','bixoParser.py',337),
  ('t -> f DIV t','t',3,'p_t','bixoParser.py',338),
  ('f -> LPAREN exp RPAREN','f',3,'p_f','bixoParser.py',348),
  ('f -> CTI','f',1,'p_f','bixoParser.py',349),
  ('f -> CTF','f',1,'p_f','bixoParser.py',350),
  ('f -> var','f',1,'p_f','bixoParser.py',351),
  ('f -> call','f',1,'p_f','bixoParser.py',352),
  ('statements -> assign','statements',1,'p_statements','bixoParser.py',357),
  ('statements -> function','statements',1,'p_statements','bixoParser.py',358),
  ('statements -> voidfunction','statements',1,'p_statements','bixoParser.py',359),
  ('statements -> call','statements',1,'p_statements','bixoParser.py',360),
  ('statements -> read','statements',1,'p_statements','bixoParser.py',361),
  ('statements -> print','statements',1,'p_statements','bixoParser.py',362),
  ('statements -> if','statements',1,'p_statements','bixoParser.py',363),
  ('statements -> while','statements',1,'p_statements','bixoParser.py',364),
  ('statements -> for','statements',1,'p_statements','bixoParser.py',365),
  ('statements -> funcesp','statements',1,'p_statements','bixoParser.py',366),
  ('assign -> var EQUAL exp SEMICOLON','assign',4,'p_assign','bixoParser.py',370),
  ('read -> READ var','read',2,'p_read','bixoParser.py',399),
  ('print -> PRINT LPAREN printp','print',3,'p_print','bixoParser.py',402),
  ('printp -> exp RPAREN','printp',2,'p_printp','bixoParser.py',405),
  ('printp -> exp COMMA printp','printp',3,'p_printp','bixoParser.py',406),
  ('var -> ID','var',1,'p_var','bixoParser.py',409),
  ('call -> ID LPAREN callp RPAREN','call',4,'p_call','bixoParser.py',413),
  ('callp -> exp SEMICOLON callp','callp',3,'p_callp','bixoParser.py',416),
  ('callp -> exp','callp',1,'p_callp','bixoParser.py',417),
  ('if -> IF LPAREN CTI GT CTI RPAREN quadsIf ifp jumpsIf','if',9,'p_if','bixoParser.py',423),
  ('ifp -> <empty>','ifp',0,'p_ifp','bixoParser.py',426),
  ('ifp -> ELSE quadsElse statements','ifp',3,'p_ifp','bixoParser.py',427),
  ('quadsIf -> <empty>','quadsIf',0,'p_quadsIf','bixoParser.py',430),
  ('jumpsIf -> <empty>','jumpsIf',0,'p_jumpsIf','bixoParser.py',447),
  ('quadsElse -> <empty>','quadsElse',0,'p_quadsElse','bixoParser.py',453),
  ('while -> WHILE LPAREN exp RPAREN statements whilep','while',6,'p_while','bixoParser.py',463),
  ('whilep -> SEMICOLON','whilep',1,'p_whilep','bixoParser.py',466),
  ('whilep -> statements whilep','whilep',2,'p_whilep','bixoParser.py',467),
  ('for -> FOR LPAREN var SEMICOLON exp SEMICOLON exp RPAREN LBRACKET statements forp','for',11,'p_for','bixoParser.py',486),
  ('forp -> RBRACKET','forp',1,'p_forp','bixoParser.py',489),
  ('forp -> statements forp','forp',2,'p_forp','bixoParser.py',490),
  ('funcesp -> array','funcesp',1,'p_funcesp','bixoParser.py',495),
  ('funcesp -> matrix','funcesp',1,'p_funcesp','bixoParser.py',496),
  ('funcesp -> mean','funcesp',1,'p_funcesp','bixoParser.py',497),
  ('funcesp -> layers','funcesp',1,'p_funcesp','bixoParser.py',498),
  ('funcesp -> sequential','funcesp',1,'p_funcesp','bixoParser.py',499),
  ('funcesp -> compile','funcesp',1,'p_funcesp','bixoParser.py',500),
  ('funcesp -> fit','funcesp',1,'p_funcesp','bixoParser.py',501),
  ('funcesp -> predict','funcesp',1,'p_funcesp','bixoParser.py',502),
  ('funcesp -> getweights','funcesp',1,'p_funcesp','bixoParser.py',503),
  ('array -> ID EQUAL ARRAY LPAREN var arrayp','array',6,'p_array','bixoParser.py',506),
  ('arrayp -> RPAREN','arrayp',1,'p_arrayp','bixoParser.py',509),
  ('arrayp -> COMMA var RPAREN','arrayp',3,'p_arrayp','bixoParser.py',510),
  ('matrix -> ID EQUAL MATRIX LPAREN array matrixp','matrix',6,'p_matrix','bixoParser.py',513),
  ('matrixp -> RPAREN','matrixp',1,'p_matrixp','bixoParser.py',516),
  ('matrixp -> COMMA array RPAREN','matrixp',3,'p_matrixp','bixoParser.py',517),
  ('mean -> MEAN LPAREN array RPAREN','mean',4,'p_mean','bixoParser.py',520),
  ('layers -> ID EQUAL LAYERS LPAREN UNITS EQUAL INT RPAREN','layers',8,'p_layers','bixoParser.py',523),
  ('sequential -> ID EQUAL SEQUENTIAL LPAREN LBRACKET layers sequentialp','sequential',7,'p_sequential','bixoParser.py',526),
  ('sequentialp -> RBRACKET RPAREN','sequentialp',2,'p_sequentialp','bixoParser.py',529),
  ('sequentialp -> COMMA layers sequentialp','sequentialp',3,'p_sequentialp','bixoParser.py',530),
  ('compile -> sequential DOT COMPILE LPAREN RPAREN','compile',5,'p_compile','bixoParser.py',533),
  ('fit -> ID EQUAL sequential DOT FIT LPAREN array COMMA array COMMA EPOCHS EQUAL INT COMMA VERBOSE EQUAL fitp','fit',17,'p_fit','bixoParser.py',536),
  ('fitp -> TRUE RPAREN','fitp',2,'p_fitp','bixoParser.py',539),
  ('fitp -> FALSE RPAREN','fitp',2,'p_fitp','bixoParser.py',540),
  ('predict -> ID EQUAL sequential DOT PREDICT LPAREN LBRACKET predictp','predict',8,'p_predict','bixoParser.py',543),
  ('predictp -> INT RBRACKET RPAREN','predictp',3,'p_predictp','bixoParser.py',546),
  ('predictp -> FLOAT RBRACKET RPAREN','predictp',3,'p_predictp','bixoParser.py',547),
  ('getweights -> layers DOT GETWEIGHTS LPAREN RPAREN','getweights',5,'p_getweights','bixoParser.py',550),
  ('empty -> <empty>','empty',0,'p_empty','bixoParser.py',554),
]
