/ife ( (stepVar == 'Step1') or (stepVar == '')) {:
	/ife (stepDone == 'Yes') {:
		//Load Step2|
		/qr-update set="CMC Main" id=1 newlabel="Start Generating World Info"|
		/:"CMC Main.Generate Basic World Info"
	:}|
	/else {:
		//Load Step1|
		/qr-update set="CMC Main" id=1 newlabel="Restart/Continue with a New Character"|
		/:"CMC Main.New Char"|
	:}|
:}|
/ife ( stepVar == 'Step2') {:
	/ife (stepDone == 'Yes') {:
		//Load Step3|
		/qr-update set="CMC Main" id=1 newlabel="Start Generating Basic Character Information"|
	:}|
	/else {:
		//Load Step2|
		/qr-update set="CMC Main" id=1 newlabel="Restart/Continue with World Info"|
	:}|
:}|