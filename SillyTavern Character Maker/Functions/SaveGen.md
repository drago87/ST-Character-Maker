/ife ( save == ''){:
	/echo Aborting |
	/abort
:}|
/let x {{getvar::save}}|
/ife ( save == 'Done') {:
	/setvar key=output {{getvar::tempList}}|
:}|
/elseif ( isGeneration == 'Yes') {:
	/ife ( outputIsList == 'Yes') {:
		/ife ( inputIsList == 'Yes') {:
			/addvar key=tempList {{getvar::item}}: {{getvar::save}}|
		:}|
		/else {:
			/addvar key=tempList {{getvar::save}}|
		:}|
	:}|
	/else {:
		/ife ( inputIsList == 'Yes') {:
			/setvar key=output {{getvar::item}}: {{getvar::save}}|
		:}|
		/else {:
			/setvar key=output {{getvar::save}}|
		:}|
	:}|
:}|
/else {:
	/ife (outputIsList == 'Yes') {:
		/addvar key=tempList {{getvar::save}}|
	:}|
	/else {:
		/setvar key=output {{getvar::save}}|
	:}|
:}|