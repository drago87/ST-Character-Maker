/ife ( save == ''){:
	/echo Aborting SaveGen|
	/abort
:}|
/let x {{getvar::save}}|
/getvar key=genSettings index=isGeneration|
/let key=isGeneration_f {{pipe}}|
/getvar key=genSettings index=outputIsList|
/let key=outputIsList_f {{pipe}}|
/getvar key=genSettings index=inputIsList|
/let key=inputIsList_f {{pipe}}|
/ife ( save == 'Done') {:
	/ife (tempList != '' ) {:
		/setvar key=output {{getvar::tempList}}|
	:}|
	/else {:
		/setvar key=output None|
	:}|
:}|
/elseif ( isGeneration_f == 'Yes') {:
	/ife (( outputIsList_f == 'Yes') {:
		/ife ( inputIsList_f == 'Yes') {:
			/addvar key=tempList {{getvar::item}}: {{getvar::save}}|
		:}|
		/else {:
			/addvar key=tempList {{getvar::save}}|
		:}|
	:}|
	/else {:
		/ife ( inputIsList_f == 'Yes') {:
			/setvar key=output {{getvar::item}}: {{getvar::save}}|
		:}|
		/else {:
			/setvar key=output {{getvar::save}}|
		:}|
	:}|
:}|
/else {:
	/ife (outputIsList_f == 'Yes') {:
		/addvar key=tempList {{getvar::save}}|
	:}|
	/else {:
		/setvar key=output {{getvar::save}}|
	:}|
:}|
/flushvar guidence|