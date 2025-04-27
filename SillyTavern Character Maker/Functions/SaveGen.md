/let SaveGen {: input=
	/ife ( input == ''){:
		//[[FlushVar]]|
		/echo Aborting | /ife ( quickRoll == 'Yes' ) {: /setvar key=debug {{getvar::tempDebug}}| :}| /:"CMC Logic.Flushvar"|
	:}|
	/let x {{var::input}}|
	/ife ( input == 'Done') {:
		/setvar key=output {{getvar::tempList}}|
	:}|
	/elseif ( isGeneration == 'Yes') {:
		/ife ( outputIsList == 'Yes) {:
			/ife ( inputIsList == 'Yes') {:
				/addvar key=tempList {{getvar::item}}: {{getvar::input}}|
			:}|
			/else {:
				/addvar key=tempList {{getvar::input}}|
			:}|
		:}|
		/else {:
			/ife ( inputIsList == 'Yes') {:
				/setvar key=output {{getvar::item}}: {{getvar::input}}|
			:}|
			/eslse {:
				/setvar key=output {{getvar::input}}|
			:}|
		:}|
	:}|
	/else {:
		/ife (outputIsList == 'Yes') {:
			/addvar key=tempList {{getvar::input}}|
		:}|
		/else {:
			/setvar key=output {{getvar::input}}|
		:}|
	:}|
:}||