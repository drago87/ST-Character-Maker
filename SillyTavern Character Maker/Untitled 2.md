/getvar key=genSettings index=wi_book|
/let key=wi_book_f {{pipe}}|
/ife ( wi_book_f == '') {:
	/var key=wi_book_f "CMC Generation Prompts"|
:}|
/getvar key=genSettings index=wi_book_key|
/let key=wi_book_key_f {{pipe}}|
/ife ( wi_book_key_f == '') {:
	/abort quiet=false Missing wi_book_key name in input.|
:}|
/getvar key=genSettings index=genIsList|
/let key=genIsList_f {{pipe}}|
/ife ( genIsList_f == '') {:
	/abort quiet=false Missing genIsList setting in input.|
:}|
/getvar key=genSettings index=genIsSentence|
/let key=genIsSentence_f {{pipe}}|
/ife ( genIsSentence_f == '') {:
	/abort quiet=false Missing genIsSentence setting in input.|
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
/getvar key=genSettings index=inputIsTaskList|
/let key=inputIsTaskList_f {{pipe}}|
/ife ( inputIsTaskList_f == '') {:
	/abort quiet=false Missing inputIsTaskList setting in input.|
:}|

/getvar key=genSettings index=contextKey|
/let key=contextKey_f {{pipe}}|

/let key=wi_uid {{noop}}|
/let key=actionType {{noop}}|
/let key=context {{noop}}|
/let key=find {{noop}}|
/let key=examples {{noop}}|
/let key=taskList {{noop}}|

/echo wi_book_key_f: {{var::wi_book_key_f}}|
/var key=find "{{var::wi_book_key_f}}: Task"|
/echo find: {{var::find}}|
/echo wi_book_f: {{var::wi_book_f}}|
/findentry field=comment file="{{var::wi_book_f}}" "{{var::find}}"|
/var key=wi_uid {{pipe}}|
/echo wi_uid: {{var::wi_uid}}|
/getentryfield field=content file={{var::wi_book_f}} {{var::wi_uid}}|
/let key=task {{pipe}}|
/ife (debug == 'Yes') {:
	/setvar key=a3 {{var::task}}|
:}|
/else {:
	/flushvar a3|
:}|