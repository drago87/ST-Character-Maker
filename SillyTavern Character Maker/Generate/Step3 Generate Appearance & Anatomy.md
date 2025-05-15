/qr-list CMC Main|
/getat index=1 {{pipe}}|
/let qrlabel {{pipe}}|
/qr-get set="CMC Main" label={{var::qrlabel}}|
/getat index="message" {{pipe}}|
/qr-update set="CMC Main" label={{var::qrlabel}} newlabel="Continue Generating Appearance & Anatomy" {{pipe}}|

/:"CMC Logic.Get Char info"|

/setvar key=dataBaseNames []|
/flushvar genSettings|

/setvar key=stepVar Step3|

/setvar key=skip Update|
/ife ( stepDone == 'No') {:
	/buttons labels=["Skip", "Update"] Do you want to skip or update already generated content? You will get a question for each already done if you select Update.|
	/setvar key=skip {{pipe}}|
	/ife ( skip == ''){:
		/echo Aborting |
		/abort
	:}|
:}|

/setvar key=stepDone No|

/let key=do {{noop}}|
/let key=variableName {{noop}}|
/let selected_btn {{noop}}|

//**Length**|

//-----------|

//**Height**|

//-----------|

//**Face**|

//-----------|

//**Hair**|

//-----------|

//**Eyes**|

//-----------|

//**Body**|

//-----------|

//**Features**|

//-----------|

//**Nipples**|

//-----------|

//**Breasts**|

//-----------|

//**Privates**|

//-----------|

//**Anus**|

//-----------|

//**Appearance Traits**|

//-----------|


/:"CMC Logic.JEDParse"|

/:"CMC Logic.Save DataBase"|

/setvar key=stepDone Yes|
/qr-list CMC Main|
/getat index=1 {{pipe}}|
/var qrlabel {{pipe}}|
/qr-get set="CMC Main" label={{var::qrlabel}}|
/getat index="message" {{pipe}}|
/qr-update set="CMC Main" label={{var::qrlabel}} newlabel="Start Generating Outfit" {{pipe}}|