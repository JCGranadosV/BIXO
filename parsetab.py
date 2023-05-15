
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'leftLTLTEGTGTEleftPLUSMINUSleftMULTDIVleftEQUALDIFFleftLPARENRPARENleftLBRACERBRACEleftLBRACKETRBRACKETAND ARRAY ASSIGN CHAR COLON COMMA COMPILE CTF CTI DIFF DIV DOT ELSE EPOCHS EQUAL FALSE FIT FLOAT FOR FUNCESP FUNCTION GETWEIGHTS GT GTE ID IF INT LAYERS LBRACE LBRACKET LPAREN LT LTE MATRIX MEAN MINUS MULT NUMPY OR PLUS PREDICT PRINT PROGRAM QUOTE RBRACE RBRACKET READ RPAREN SEMICOLON SEQUENTIAL STRING TRUE UNITS VAR VERBOSE VOID WHILEprogram : PROGRAM ID SEMICOLON decvardecvar : VAR type decvarp SEMICOLONdecvarp : ID COMMA decvarp\n               | IDtype : INT\n            | FLOATfunction : FUNCTION type ID LPAREN param RPAREN bodyvoidfunction : FUNCTION VOID ID LPAREN param RPAREN bodybody : LBRACE bodyp RBRACEbodyp : decvar statements bodyp\n             | statements bodyp\n             | decvar\n             | param : \n             | type paramp paramp : ID\n               | ID COMMA paramexp : texp \n           | texp OR exptexp : gexp \n            | gexp AND texpgexp : mexp \n            | mexp gexpp mexpgexpp : LT\n             | GT\n             | EQUAL\n             | DIFFmexp : t\n            | t PLUS mexp\n            | t MINUS mexpt : f \n         | f MULT t\n         | f DIV tf : LPAREN exp RPAREN\n         | INT\n         | FLOAT\n         | var\n         | callstatements : assign\n                 |  function\n                 |  voidfunction\n                 |  call\n                 |  read\n                 |  print\n                 |  if\n                 |  while\n                 |  for\n                 |  funcespassign : var EQUAL expread : READ varprint : PRINT LPAREN printpprintp : exp RPAREN\n              | exp COMMA printpvar : ID \n           | ID LBRACKET exp RBRACKET\n           | ID LBRACKET exp RBRACKET LBRACKET exp RBRACKETcall : ID LPAREN callp RPARENcallp : exp SEMICOLON callp\n             | expif : IF LPAREN CTI GT CTI RPAREN quadsIf ifp jumpsIf ifp : \n            | ELSE quadsElse statementsquadsIf : jumpsIf : quadsElse :  while : WHILE LPAREN exp RPAREN statements whilep whilep : SEMICOLON\n               | statements whilepfor : FOR LPAREN var SEMICOLON exp SEMICOLON exp RPAREN LBRACKET statements forp forp : RBRACKET\n             | statements forp funcesp : array\n                | matrix\n                | mean\n                | layers\n                | sequential\n                | compile\n                | fit\n                | predict\n                | getweights array : ID EQUAL ARRAY LPAREN var arrayp arrayp : RPAREN\n               | COMMA var RPAREN matrix : ID EQUAL MATRIX LPAREN array matrixp matrixp : RPAREN\n                | COMMA array RPARENmean : MEAN LPAREN array RPARENlayers : ID EQUAL LAYERS LPAREN UNITS EQUAL INT RPAREN sequential : ID EQUAL SEQUENTIAL LPAREN LBRACKET layers sequentialp sequentialp : RBRACKET RPAREN\n                    | COMMA layers sequentialp compile : sequential DOT COMPILE LPAREN RPAREN fit : ID EQUAL sequential DOT FIT LPAREN array COMMA array COMMA EPOCHS EQUAL INT COMMA VERBOSE EQUAL fitp fitp : TRUE RPAREN\n             | FALSE RPAREN predict : ID EQUAL sequential DOT PREDICT LPAREN LBRACKET predictp predictp : INT RBRACKET RPAREN\n                 | FLOAT RBRACKET RPAREN getweights : layers DOT GETWEIGHTS LPAREN RPARENempty :'
    
_lr_action_items = {'PROGRAM':([0,],[2,]),'$end':([1,5,12,],[0,-1,-2,]),'ID':([2,7,8,9,13,],[3,11,-5,-6,11,]),'SEMICOLON':([3,10,11,14,],[4,12,-4,-3,]),'VAR':([4,],[6,]),'INT':([6,],[8,]),'FLOAT':([6,],[9,]),'COMMA':([11,],[13,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'program':([0,],[1,]),'decvar':([4,],[5,]),'type':([6,],[7,]),'decvarp':([7,13,],[10,14,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> program","S'",1,None,None,None),
  ('program -> PROGRAM ID SEMICOLON decvar','program',4,'p_program','bixoParser.py',123),
  ('decvar -> VAR type decvarp SEMICOLON','decvar',4,'p_decvar','bixoParser.py',129),
  ('decvarp -> ID COMMA decvarp','decvarp',3,'p_decvarp','bixoParser.py',178),
  ('decvarp -> ID','decvarp',1,'p_decvarp','bixoParser.py',179),
  ('type -> INT','type',1,'p_type','bixoParser.py',188),
  ('type -> FLOAT','type',1,'p_type','bixoParser.py',189),
  ('function -> FUNCTION type ID LPAREN param RPAREN body','function',7,'p_function','bixoParser.py',193),
  ('voidfunction -> FUNCTION VOID ID LPAREN param RPAREN body','voidfunction',7,'p_voidfunction','bixoParser.py',196),
  ('body -> LBRACE bodyp RBRACE','body',3,'p_body','bixoParser.py',199),
  ('bodyp -> decvar statements bodyp','bodyp',3,'p_bodyp','bixoParser.py',202),
  ('bodyp -> statements bodyp','bodyp',2,'p_bodyp','bixoParser.py',203),
  ('bodyp -> decvar','bodyp',1,'p_bodyp','bixoParser.py',204),
  ('bodyp -> <empty>','bodyp',0,'p_bodyp','bixoParser.py',205),
  ('param -> <empty>','param',0,'p_param','bixoParser.py',208),
  ('param -> type paramp','param',2,'p_param','bixoParser.py',209),
  ('paramp -> ID','paramp',1,'p_paramp','bixoParser.py',212),
  ('paramp -> ID COMMA param','paramp',3,'p_paramp','bixoParser.py',213),
  ('exp -> texp','exp',1,'p_exp','bixoParser.py',216),
  ('exp -> texp OR exp','exp',3,'p_exp','bixoParser.py',217),
  ('texp -> gexp','texp',1,'p_texp','bixoParser.py',220),
  ('texp -> gexp AND texp','texp',3,'p_texp','bixoParser.py',221),
  ('gexp -> mexp','gexp',1,'p_gexp','bixoParser.py',224),
  ('gexp -> mexp gexpp mexp','gexp',3,'p_gexp','bixoParser.py',225),
  ('gexpp -> LT','gexpp',1,'p_gexpp','bixoParser.py',228),
  ('gexpp -> GT','gexpp',1,'p_gexpp','bixoParser.py',229),
  ('gexpp -> EQUAL','gexpp',1,'p_gexpp','bixoParser.py',230),
  ('gexpp -> DIFF','gexpp',1,'p_gexpp','bixoParser.py',231),
  ('mexp -> t','mexp',1,'p_mexp','bixoParser.py',234),
  ('mexp -> t PLUS mexp','mexp',3,'p_mexp','bixoParser.py',235),
  ('mexp -> t MINUS mexp','mexp',3,'p_mexp','bixoParser.py',236),
  ('t -> f','t',1,'p_t','bixoParser.py',244),
  ('t -> f MULT t','t',3,'p_t','bixoParser.py',245),
  ('t -> f DIV t','t',3,'p_t','bixoParser.py',246),
  ('f -> LPAREN exp RPAREN','f',3,'p_f','bixoParser.py',251),
  ('f -> INT','f',1,'p_f','bixoParser.py',252),
  ('f -> FLOAT','f',1,'p_f','bixoParser.py',253),
  ('f -> var','f',1,'p_f','bixoParser.py',254),
  ('f -> call','f',1,'p_f','bixoParser.py',255),
  ('statements -> assign','statements',1,'p_statements','bixoParser.py',261),
  ('statements -> function','statements',1,'p_statements','bixoParser.py',262),
  ('statements -> voidfunction','statements',1,'p_statements','bixoParser.py',263),
  ('statements -> call','statements',1,'p_statements','bixoParser.py',264),
  ('statements -> read','statements',1,'p_statements','bixoParser.py',265),
  ('statements -> print','statements',1,'p_statements','bixoParser.py',266),
  ('statements -> if','statements',1,'p_statements','bixoParser.py',267),
  ('statements -> while','statements',1,'p_statements','bixoParser.py',268),
  ('statements -> for','statements',1,'p_statements','bixoParser.py',269),
  ('statements -> funcesp','statements',1,'p_statements','bixoParser.py',270),
  ('assign -> var EQUAL exp','assign',3,'p_assign','bixoParser.py',274),
  ('read -> READ var','read',2,'p_read','bixoParser.py',277),
  ('print -> PRINT LPAREN printp','print',3,'p_print','bixoParser.py',280),
  ('printp -> exp RPAREN','printp',2,'p_printp','bixoParser.py',283),
  ('printp -> exp COMMA printp','printp',3,'p_printp','bixoParser.py',284),
  ('var -> ID','var',1,'p_var','bixoParser.py',287),
  ('var -> ID LBRACKET exp RBRACKET','var',4,'p_var','bixoParser.py',288),
  ('var -> ID LBRACKET exp RBRACKET LBRACKET exp RBRACKET','var',7,'p_var','bixoParser.py',289),
  ('call -> ID LPAREN callp RPAREN','call',4,'p_call','bixoParser.py',295),
  ('callp -> exp SEMICOLON callp','callp',3,'p_callp','bixoParser.py',298),
  ('callp -> exp','callp',1,'p_callp','bixoParser.py',299),
  ('if -> IF LPAREN CTI GT CTI RPAREN quadsIf ifp jumpsIf','if',9,'p_if','bixoParser.py',305),
  ('ifp -> <empty>','ifp',0,'p_ifp','bixoParser.py',308),
  ('ifp -> ELSE quadsElse statements','ifp',3,'p_ifp','bixoParser.py',309),
  ('quadsIf -> <empty>','quadsIf',0,'p_quadsIf','bixoParser.py',312),
  ('jumpsIf -> <empty>','jumpsIf',0,'p_jumpsIf','bixoParser.py',326),
  ('quadsElse -> <empty>','quadsElse',0,'p_quadsElse','bixoParser.py',332),
  ('while -> WHILE LPAREN exp RPAREN statements whilep','while',6,'p_while','bixoParser.py',342),
  ('whilep -> SEMICOLON','whilep',1,'p_whilep','bixoParser.py',345),
  ('whilep -> statements whilep','whilep',2,'p_whilep','bixoParser.py',346),
  ('for -> FOR LPAREN var SEMICOLON exp SEMICOLON exp RPAREN LBRACKET statements forp','for',11,'p_for','bixoParser.py',365),
  ('forp -> RBRACKET','forp',1,'p_forp','bixoParser.py',368),
  ('forp -> statements forp','forp',2,'p_forp','bixoParser.py',369),
  ('funcesp -> array','funcesp',1,'p_funcesp','bixoParser.py',374),
  ('funcesp -> matrix','funcesp',1,'p_funcesp','bixoParser.py',375),
  ('funcesp -> mean','funcesp',1,'p_funcesp','bixoParser.py',376),
  ('funcesp -> layers','funcesp',1,'p_funcesp','bixoParser.py',377),
  ('funcesp -> sequential','funcesp',1,'p_funcesp','bixoParser.py',378),
  ('funcesp -> compile','funcesp',1,'p_funcesp','bixoParser.py',379),
  ('funcesp -> fit','funcesp',1,'p_funcesp','bixoParser.py',380),
  ('funcesp -> predict','funcesp',1,'p_funcesp','bixoParser.py',381),
  ('funcesp -> getweights','funcesp',1,'p_funcesp','bixoParser.py',382),
  ('array -> ID EQUAL ARRAY LPAREN var arrayp','array',6,'p_array','bixoParser.py',385),
  ('arrayp -> RPAREN','arrayp',1,'p_arrayp','bixoParser.py',388),
  ('arrayp -> COMMA var RPAREN','arrayp',3,'p_arrayp','bixoParser.py',389),
  ('matrix -> ID EQUAL MATRIX LPAREN array matrixp','matrix',6,'p_matrix','bixoParser.py',392),
  ('matrixp -> RPAREN','matrixp',1,'p_matrixp','bixoParser.py',395),
  ('matrixp -> COMMA array RPAREN','matrixp',3,'p_matrixp','bixoParser.py',396),
  ('mean -> MEAN LPAREN array RPAREN','mean',4,'p_mean','bixoParser.py',399),
  ('layers -> ID EQUAL LAYERS LPAREN UNITS EQUAL INT RPAREN','layers',8,'p_layers','bixoParser.py',402),
  ('sequential -> ID EQUAL SEQUENTIAL LPAREN LBRACKET layers sequentialp','sequential',7,'p_sequential','bixoParser.py',405),
  ('sequentialp -> RBRACKET RPAREN','sequentialp',2,'p_sequentialp','bixoParser.py',408),
  ('sequentialp -> COMMA layers sequentialp','sequentialp',3,'p_sequentialp','bixoParser.py',409),
  ('compile -> sequential DOT COMPILE LPAREN RPAREN','compile',5,'p_compile','bixoParser.py',412),
  ('fit -> ID EQUAL sequential DOT FIT LPAREN array COMMA array COMMA EPOCHS EQUAL INT COMMA VERBOSE EQUAL fitp','fit',17,'p_fit','bixoParser.py',415),
  ('fitp -> TRUE RPAREN','fitp',2,'p_fitp','bixoParser.py',418),
  ('fitp -> FALSE RPAREN','fitp',2,'p_fitp','bixoParser.py',419),
  ('predict -> ID EQUAL sequential DOT PREDICT LPAREN LBRACKET predictp','predict',8,'p_predict','bixoParser.py',422),
  ('predictp -> INT RBRACKET RPAREN','predictp',3,'p_predictp','bixoParser.py',425),
  ('predictp -> FLOAT RBRACKET RPAREN','predictp',3,'p_predictp','bixoParser.py',426),
  ('getweights -> layers DOT GETWEIGHTS LPAREN RPAREN','getweights',5,'p_getweights','bixoParser.py',429),
  ('empty -> <empty>','empty',0,'p_empty','bixoParser.py',433),
]
