/ife ( (stepVar == 'Step1') or (stepVar == '')) {:
	/ife (stepDone == 'Yes') {:
		//Load Step2|
		/:"CMC Generate.Generate World Info"|
	:}|
	/else {:
		//Load Step1|
		/:"CMC Main.New Character"|
	:}|
:}|
/ife ( stepVar == 'Step2') {:
	/ife (stepDone == 'Yes') {:
		//Load Step3|
		/:"CMC Generate.Generate Character Information"|
	:}|
	/else {:
		//Load Step2|
		/:"CMC Generate.Generate World Info"|
	:}|
:}|