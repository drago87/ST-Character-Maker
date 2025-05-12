/getvar key=genSettings index=question|
/let key=question_f {{pipe}}|
/ife ( question_f == '') {:
	/abort quiet=false Missing question setting in input.|
:}|

/getvar key=genSettings index=needOutput|
/let key=needOutput_f {{pipe}}|
/ife ( needOutput_f == '') {:
	/var key=needOutput_f Yes|
:}|
/getvar key=genSettings index=useContext|
/let key=useContext_f {{pipe}}|
/ife ( useContext_f == '') {:
	/abort quiet=false Missing useContext setting in input.|
:}|
/getvar key=genSettings index=contextKey|
/let as=array key=contextKey_f {{pipe}}|

/let key=wi_uid {{noop}}|
/let key=find "{{var::question_f}}: Q"|
/findentry field=comment file="CMC Questions" "{{var::find}}"|
/getentryfield field=content file="CMC Questions" {{pipe}}|
/setvar key=questions {{pipe}}|
/split find="/\n/" {{getvar::questions}}|
/setvar key=questions {{pipe}}|
/ife ( user != 'Yes') {:
	/setvar key=remIndex []|
	/foreach {{getvar::questions}} {:
		/ife ( '--User--' in item) {:
			/addvar key=remIndex {{var::index}}|
		:}|
	:}|
	/reverse {{getvar::remIndex}}|
	/setvar key=remIndex {{pipe}}|
	/foreach {{getvar::remIndex}} {:
		/splice start={{var::item}} delete=1 {{getvar::questions}}|
		/setvar key=questions {{pipe}}|
	:}|
	/flsuhvar remIndex|
:}|

/ife ( useContext_f == 'Yes') {:
	/findentry field=comment file="CMC Information" "Base Information"|
	/var key=wi_uid {{pipe}}|
	/getentryfield field=content file="CMC Information" {{var::wi_uid}}|
	/var key=context {{pipe}}|
	/ife ( real == 'Yes') {:
		/var key=context {{var::context}}{{var::realParced}}|
	:}|
	/ife ( contextKey_f != '') {:
		/foreach {{var::contextKey_f}} {:
			/var key=find "{{var::item}}: Context"|
			/findentry field=comment file="CMC Information" "{{var::find}}"|
			/var key=wi_uid {{pipe}}|
			/ife ( wi_uid != '') {:
				/getentryfield field=content file="CMC Information" {{var::wi_uid}}|
				/var key=context "{{var::context}}{{newline}}{{newline}}{{pipe}}"|
			:}|
		:}|
	:}|
	/var key=context "{{var::context}}{{newline}}{{newline}}"|
:}|



/flushvar questions|