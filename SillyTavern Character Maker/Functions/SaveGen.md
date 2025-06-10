/getvar key=genSettings index=isGeneration|
/let key=isGeneration_f {{pipe}}|
/getvar key=genSettings index=outputIsList|
/let key=outputIsList_f {{pipe}}|
/getvar key=genSettings index=inputIsList|
/let key=inputIsList_f {{pipe}}|
/getvar key=genSettings index=wi_book|
/let key=wi_book_f {{pipe}}|
/ife (( save == '') and (wi_book_f != 'CMC Rules')) {:
	/echo Aborting SaveGen|
	/abort
:}|
/elseif (wi_book_f == 'CMC Rules')) {:
	/setvar key=output Remove|
:}|
/let x {{getvar::save}}|
/elseif ( save == 'Done') {:
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