/ife ( (stepVar == 'Step1') or (stepVar == '')) {:
	/ife (stepDone == 'Yes') {:
		//Load Step2|
		/:"CMC Main.Generate Basic World Info"|
	:}|
	/else {:
		//Load Step1|
		/:"CMC Main.New Char"|
	:}|
:}|
/ife ( stepVar == 'Step2') {:
	/ife (stepDone == 'Yes') {:
		//Load Step3|
	:}|
	/else {:
		//Load Step2|
		/:"CMC Main.Generate Basic World Info"|
	:}|
:}|