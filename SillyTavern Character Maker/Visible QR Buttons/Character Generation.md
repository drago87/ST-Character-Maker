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
/ife ( stepVar == 'Step3') {:
	/ife (stepDone == 'Yes') {:
		//Load Step4|
		/:"CMC Generate.Generate Character Personality"|
	:}|
	/else {:
		//Load Step3|
		/:"CMC Generate.Generate Character Information"|
	:}|
:}|
/ife ( stepVar == 'Step4') {:
	/ife (stepDone == 'Yes') {:
		//Load Step5|
		//:"CMC Generate.Generate Character Personality"|
	:}|
	/else {:
		//Load Step4|
		/:"CMC Generate.Generate Character Personality"|
	:}|
:}|