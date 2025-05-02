/let SaveGen {: input=
	/ife ( input == ''){:
		/echo Aborting |
		/abort
	:}|
	/let x {{var::input}}|
	/ife ( input == 'Done') {:
		/setvar key=output {{getvar::tempList}}|
	:}|
	/elseif ( isGeneration == 'Yes') {:
		/ife ( outputIsList == 'Yes') {:
			/ife ( inputIsList == 'Yes') {:
				/addvar key=tempList {{getvar::item}}: {{var::input}}|
			:}|
			/else {:
				/addvar key=tempList {{var::input}}|
			:}|
		:}|
		/else {:
			/ife ( inputIsList == 'Yes') {:
				/setvar key=output {{getvar::item}}: {{var::input}}|
			:}|
			/else {:
				/setvar key=output {{var::input}}|
			:}|
		:}|
	:}|
	/else {:
		/ife (outputIsList == 'Yes') {:
			/addvar key=tempList {{var::input}}|
		:}|
		/else {:
			/setvar key=output {{var::input}}|
		:}|
	:}|
:}||