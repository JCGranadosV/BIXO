
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'leftLTLTEGTGTEleftPLUSMINUSleftMULTDIVleftEQUALDIFFleftLPARENRPARENleftLBRACERBRACEleftLBRACKETRBRACKETAND ARRAY ASSIGN CHAR COLON COMMA COMPILE CTF CTI DIFF DIV DOT ELSE END EPOCHS EQUAL FALSE FIT FLOAT FOR FUNCESP FUNCTION GETWEIGHTS GT GTE ID IF INT LAYERS LBRACE LBRACKET LPAREN LT LTE MAIN MATRIX MEAN MINUS MULT NUMPY OR PLUS PREDICT PRINT PROGRAM QUOTE RBRACE RBRACKET READ RPAREN SEMICOLON SEQUENTIAL STRING TRUE UNITS VAR VERBOSE VOID WHILEprogram : PROGRAM ID SEMICOLON decvar assigndecvar : VAR decvarp\n              | VAR decvarp decvardecvarp : type decvarpp SEMICOLONdecvarpp : ID COMMA decvarpp\n                | IDtype : INT\n            | FLOATfunction : FUNCTION type ID LPAREN param RPAREN bodyvoidfunction : FUNCTION VOID ID LPAREN param RPAREN bodybody : LBRACE bodyp RBRACEbodyp : decvar statements bodyp\n             | statements bodyp\n             | decvar\n             | param : \n             | type paramp paramp : ID\n               | ID COMMA paramexp : texp \n           | texp OR exptexp : gexp \n            | gexp AND texpgexp : mexp \n            | mexp gexpp mexpgexpp : LT\n             | GT\n             | EQUAL\n             | DIFFmexp : t\n            | t PLUS mexp\n            | t MINUS mexpt : f \n         | f MULT t\n         | f DIV tf : LPAREN exp RPAREN\n         | CTI\n         | CTF\n         | var\n         | callstatements : assign\n                 |  function\n                 |  voidfunction\n                 |  call\n                 |  read\n                 |  print\n                 |  if\n                 |  while\n                 |  for\n                 |  funcespassign : var EQUAL expread : READ varprint : PRINT LPAREN printpprintp : exp RPAREN\n              | exp COMMA printpvar : ID call : ID LPAREN callp RPARENcallp : exp SEMICOLON callp\n             | expif : IF LPAREN CTI GT CTI RPAREN quadsIf ifp jumpsIf ifp : \n            | ELSE quadsElse statementsquadsIf : jumpsIf : quadsElse :  while : WHILE LPAREN exp RPAREN statements whilep whilep : SEMICOLON\n               | statements whilepfor : FOR LPAREN var SEMICOLON exp SEMICOLON exp RPAREN LBRACKET statements forp forp : RBRACKET\n             | statements forp funcesp : array\n                | matrix\n                | mean\n                | layers\n                | sequential\n                | compile\n                | fit\n                | predict\n                | getweights array : ID EQUAL ARRAY LPAREN var arrayp arrayp : RPAREN\n               | COMMA var RPAREN matrix : ID EQUAL MATRIX LPAREN array matrixp matrixp : RPAREN\n                | COMMA array RPARENmean : MEAN LPAREN array RPARENlayers : ID EQUAL LAYERS LPAREN UNITS EQUAL INT RPAREN sequential : ID EQUAL SEQUENTIAL LPAREN LBRACKET layers sequentialp sequentialp : RBRACKET RPAREN\n                    | COMMA layers sequentialp compile : sequential DOT COMPILE LPAREN RPAREN fit : ID EQUAL sequential DOT FIT LPAREN array COMMA array COMMA EPOCHS EQUAL INT COMMA VERBOSE EQUAL fitp fitp : TRUE RPAREN\n             | FALSE RPAREN predict : ID EQUAL sequential DOT PREDICT LPAREN LBRACKET predictp predictp : INT RBRACKET RPAREN\n                 | FLOAT RBRACKET RPAREN getweights : layers DOT GETWEIGHTS LPAREN RPARENempty :'
    
_lr_action_items = {'PROGRAM':([0,],[2,]),'$end':([1,8,18,19,20,21,22,23,24,26,27,28,29,46,47,48,49,50,51,52,53,56,],[0,-1,-39,-51,-20,-22,-24,-30,-33,-37,-38,-40,-56,-21,-23,-25,-31,-32,-34,-35,-36,-57,]),'ID':([2,5,10,11,12,13,14,15,25,30,31,32,33,34,35,36,37,38,39,40,41,42,44,57,],[3,7,-2,17,-7,-8,29,-3,29,-4,17,29,29,29,-26,-27,-28,-29,29,29,29,29,29,29,]),'SEMICOLON':([3,16,17,18,20,21,22,23,24,26,27,28,29,45,46,47,48,49,50,51,52,53,55,56,],[4,30,-6,-39,-20,-22,-24,-30,-33,-37,-38,-40,-56,-5,-21,-23,-25,-31,-32,-34,-35,-36,57,-57,]),'VAR':([4,10,30,],[6,6,-4,]),'INT':([6,],[12,]),'FLOAT':([6,],[13,]),'EQUAL':([7,9,18,22,23,24,26,27,28,29,49,50,51,52,53,56,],[-56,14,-39,37,-30,-33,-37,-38,-40,-56,-31,-32,-34,-35,-36,-57,]),'LPAREN':([14,25,29,32,33,34,35,36,37,38,39,40,41,42,44,57,],[25,25,44,25,25,25,-26,-27,-28,-29,25,25,25,25,25,25,]),'CTI':([14,25,32,33,34,35,36,37,38,39,40,41,42,44,57,],[26,26,26,26,26,-26,-27,-28,-29,26,26,26,26,26,26,]),'CTF':([14,25,32,33,34,35,36,37,38,39,40,41,42,44,57,],[27,27,27,27,27,-26,-27,-28,-29,27,27,27,27,27,27,]),'COMMA':([17,],[31,]),'MULT':([18,24,26,27,28,29,53,56,],[-39,41,-37,-38,-40,-56,-36,-57,]),'DIV':([18,24,26,27,28,29,53,56,],[-39,42,-37,-38,-40,-56,-36,-57,]),'PLUS':([18,23,24,26,27,28,29,51,52,53,56,],[-39,39,-33,-37,-38,-40,-56,-34,-35,-36,-57,]),'MINUS':([18,23,24,26,27,28,29,51,52,53,56,],[-39,40,-33,-37,-38,-40,-56,-34,-35,-36,-57,]),'LT':([18,22,23,24,26,27,28,29,49,50,51,52,53,56,],[-39,35,-30,-33,-37,-38,-40,-56,-31,-32,-34,-35,-36,-57,]),'GT':([18,22,23,24,26,27,28,29,49,50,51,52,53,56,],[-39,36,-30,-33,-37,-38,-40,-56,-31,-32,-34,-35,-36,-57,]),'DIFF':([18,22,23,24,26,27,28,29,49,50,51,52,53,56,],[-39,38,-30,-33,-37,-38,-40,-56,-31,-32,-34,-35,-36,-57,]),'AND':([18,21,22,23,24,26,27,28,29,48,49,50,51,52,53,56,],[-39,33,-24,-30,-33,-37,-38,-40,-56,-25,-31,-32,-34,-35,-36,-57,]),'OR':([18,20,21,22,23,24,26,27,28,29,47,48,49,50,51,52,53,56,],[-39,32,-22,-24,-30,-33,-37,-38,-40,-56,-23,-25,-31,-32,-34,-35,-36,-57,]),'RPAREN':([18,20,21,22,23,24,26,27,28,29,43,46,47,48,49,50,51,52,53,54,55,56,58,],[-39,-20,-22,-24,-30,-33,-37,-38,-40,-56,53,-21,-23,-25,-31,-32,-34,-35,-36,56,-59,-57,-58,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'program':([0,],[1,]),'decvar':([4,10,],[5,15,]),'assign':([5,],[8,]),'var':([5,14,25,32,33,34,39,40,41,42,44,57,],[9,18,18,18,18,18,18,18,18,18,18,18,]),'decvarp':([6,],[10,]),'type':([6,],[11,]),'decvarpp':([11,31,],[16,45,]),'exp':([14,25,32,44,57,],[19,43,46,55,55,]),'texp':([14,25,32,33,44,57,],[20,20,20,47,20,20,]),'gexp':([14,25,32,33,44,57,],[21,21,21,21,21,21,]),'mexp':([14,25,32,33,34,39,40,44,57,],[22,22,22,22,48,49,50,22,22,]),'t':([14,25,32,33,34,39,40,41,42,44,57,],[23,23,23,23,23,23,23,51,52,23,23,]),'f':([14,25,32,33,34,39,40,41,42,44,57,],[24,24,24,24,24,24,24,24,24,24,24,]),'call':([14,25,32,33,34,39,40,41,42,44,57,],[28,28,28,28,28,28,28,28,28,28,28,]),'gexpp':([22,],[34,]),'callp':([44,57,],[54,58,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> program","S'",1,None,None,None),
  ('program -> PROGRAM ID SEMICOLON decvar assign','program',5,'p_program','bixoParser.py',156),
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
  ('paramp -> ID','paramp',1,'p_paramp','bixoParser.py',242),
  ('paramp -> ID COMMA param','paramp',3,'p_paramp','bixoParser.py',243),
  ('exp -> texp','exp',1,'p_exp','bixoParser.py',246),
  ('exp -> texp OR exp','exp',3,'p_exp','bixoParser.py',247),
  ('texp -> gexp','texp',1,'p_texp','bixoParser.py',250),
  ('texp -> gexp AND texp','texp',3,'p_texp','bixoParser.py',251),
  ('gexp -> mexp','gexp',1,'p_gexp','bixoParser.py',254),
  ('gexp -> mexp gexpp mexp','gexp',3,'p_gexp','bixoParser.py',255),
  ('gexpp -> LT','gexpp',1,'p_gexpp','bixoParser.py',258),
  ('gexpp -> GT','gexpp',1,'p_gexpp','bixoParser.py',259),
  ('gexpp -> EQUAL','gexpp',1,'p_gexpp','bixoParser.py',260),
  ('gexpp -> DIFF','gexpp',1,'p_gexpp','bixoParser.py',261),
  ('mexp -> t','mexp',1,'p_mexp','bixoParser.py',264),
  ('mexp -> t PLUS mexp','mexp',3,'p_mexp','bixoParser.py',265),
  ('mexp -> t MINUS mexp','mexp',3,'p_mexp','bixoParser.py',266),
  ('t -> f','t',1,'p_t','bixoParser.py',274),
  ('t -> f MULT t','t',3,'p_t','bixoParser.py',275),
  ('t -> f DIV t','t',3,'p_t','bixoParser.py',276),
  ('f -> LPAREN exp RPAREN','f',3,'p_f','bixoParser.py',281),
  ('f -> CTI','f',1,'p_f','bixoParser.py',282),
  ('f -> CTF','f',1,'p_f','bixoParser.py',283),
  ('f -> var','f',1,'p_f','bixoParser.py',284),
  ('f -> call','f',1,'p_f','bixoParser.py',285),
  ('statements -> assign','statements',1,'p_statements','bixoParser.py',291),
  ('statements -> function','statements',1,'p_statements','bixoParser.py',292),
  ('statements -> voidfunction','statements',1,'p_statements','bixoParser.py',293),
  ('statements -> call','statements',1,'p_statements','bixoParser.py',294),
  ('statements -> read','statements',1,'p_statements','bixoParser.py',295),
  ('statements -> print','statements',1,'p_statements','bixoParser.py',296),
  ('statements -> if','statements',1,'p_statements','bixoParser.py',297),
  ('statements -> while','statements',1,'p_statements','bixoParser.py',298),
  ('statements -> for','statements',1,'p_statements','bixoParser.py',299),
  ('statements -> funcesp','statements',1,'p_statements','bixoParser.py',300),
  ('assign -> var EQUAL exp','assign',3,'p_assign','bixoParser.py',304),
  ('read -> READ var','read',2,'p_read','bixoParser.py',336),
  ('print -> PRINT LPAREN printp','print',3,'p_print','bixoParser.py',339),
  ('printp -> exp RPAREN','printp',2,'p_printp','bixoParser.py',342),
  ('printp -> exp COMMA printp','printp',3,'p_printp','bixoParser.py',343),
  ('var -> ID','var',1,'p_var','bixoParser.py',346),
  ('call -> ID LPAREN callp RPAREN','call',4,'p_call','bixoParser.py',350),
  ('callp -> exp SEMICOLON callp','callp',3,'p_callp','bixoParser.py',353),
  ('callp -> exp','callp',1,'p_callp','bixoParser.py',354),
  ('if -> IF LPAREN CTI GT CTI RPAREN quadsIf ifp jumpsIf','if',9,'p_if','bixoParser.py',360),
  ('ifp -> <empty>','ifp',0,'p_ifp','bixoParser.py',363),
  ('ifp -> ELSE quadsElse statements','ifp',3,'p_ifp','bixoParser.py',364),
  ('quadsIf -> <empty>','quadsIf',0,'p_quadsIf','bixoParser.py',367),
  ('jumpsIf -> <empty>','jumpsIf',0,'p_jumpsIf','bixoParser.py',384),
  ('quadsElse -> <empty>','quadsElse',0,'p_quadsElse','bixoParser.py',390),
  ('while -> WHILE LPAREN exp RPAREN statements whilep','while',6,'p_while','bixoParser.py',400),
  ('whilep -> SEMICOLON','whilep',1,'p_whilep','bixoParser.py',403),
  ('whilep -> statements whilep','whilep',2,'p_whilep','bixoParser.py',404),
  ('for -> FOR LPAREN var SEMICOLON exp SEMICOLON exp RPAREN LBRACKET statements forp','for',11,'p_for','bixoParser.py',423),
  ('forp -> RBRACKET','forp',1,'p_forp','bixoParser.py',426),
  ('forp -> statements forp','forp',2,'p_forp','bixoParser.py',427),
  ('funcesp -> array','funcesp',1,'p_funcesp','bixoParser.py',432),
  ('funcesp -> matrix','funcesp',1,'p_funcesp','bixoParser.py',433),
  ('funcesp -> mean','funcesp',1,'p_funcesp','bixoParser.py',434),
  ('funcesp -> layers','funcesp',1,'p_funcesp','bixoParser.py',435),
  ('funcesp -> sequential','funcesp',1,'p_funcesp','bixoParser.py',436),
  ('funcesp -> compile','funcesp',1,'p_funcesp','bixoParser.py',437),
  ('funcesp -> fit','funcesp',1,'p_funcesp','bixoParser.py',438),
  ('funcesp -> predict','funcesp',1,'p_funcesp','bixoParser.py',439),
  ('funcesp -> getweights','funcesp',1,'p_funcesp','bixoParser.py',440),
  ('array -> ID EQUAL ARRAY LPAREN var arrayp','array',6,'p_array','bixoParser.py',443),
  ('arrayp -> RPAREN','arrayp',1,'p_arrayp','bixoParser.py',446),
  ('arrayp -> COMMA var RPAREN','arrayp',3,'p_arrayp','bixoParser.py',447),
  ('matrix -> ID EQUAL MATRIX LPAREN array matrixp','matrix',6,'p_matrix','bixoParser.py',450),
  ('matrixp -> RPAREN','matrixp',1,'p_matrixp','bixoParser.py',453),
  ('matrixp -> COMMA array RPAREN','matrixp',3,'p_matrixp','bixoParser.py',454),
  ('mean -> MEAN LPAREN array RPAREN','mean',4,'p_mean','bixoParser.py',457),
  ('layers -> ID EQUAL LAYERS LPAREN UNITS EQUAL INT RPAREN','layers',8,'p_layers','bixoParser.py',460),
  ('sequential -> ID EQUAL SEQUENTIAL LPAREN LBRACKET layers sequentialp','sequential',7,'p_sequential','bixoParser.py',463),
  ('sequentialp -> RBRACKET RPAREN','sequentialp',2,'p_sequentialp','bixoParser.py',466),
  ('sequentialp -> COMMA layers sequentialp','sequentialp',3,'p_sequentialp','bixoParser.py',467),
  ('compile -> sequential DOT COMPILE LPAREN RPAREN','compile',5,'p_compile','bixoParser.py',470),
  ('fit -> ID EQUAL sequential DOT FIT LPAREN array COMMA array COMMA EPOCHS EQUAL INT COMMA VERBOSE EQUAL fitp','fit',17,'p_fit','bixoParser.py',473),
  ('fitp -> TRUE RPAREN','fitp',2,'p_fitp','bixoParser.py',476),
  ('fitp -> FALSE RPAREN','fitp',2,'p_fitp','bixoParser.py',477),
  ('predict -> ID EQUAL sequential DOT PREDICT LPAREN LBRACKET predictp','predict',8,'p_predict','bixoParser.py',480),
  ('predictp -> INT RBRACKET RPAREN','predictp',3,'p_predictp','bixoParser.py',483),
  ('predictp -> FLOAT RBRACKET RPAREN','predictp',3,'p_predictp','bixoParser.py',484),
  ('getweights -> layers DOT GETWEIGHTS LPAREN RPAREN','getweights',5,'p_getweights','bixoParser.py',487),
  ('empty -> <empty>','empty',0,'p_empty','bixoParser.py',491),
]
