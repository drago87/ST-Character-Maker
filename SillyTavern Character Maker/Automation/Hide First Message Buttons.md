/ife (('{{char}}' == 'Character Maker QR') and (((stepDone == 'Yes') and (stepVar == 'Step11' )) or ((stepDone == 'No') and (stepVar == 'Step12' )))) {:
	/qr-update hidden=false set="CMC Main" label="Redo current Greeting"|
	/qr-update hidden=false set="CMC Main" label="Make a Alt. Greeting"|
:}|
/else {:
	/qr-update hidden=true set="CMC Main" label="Redo current Greeting"|
	/qr-update hidden=true set="CMC Main" label="Make a Alt. Greeting"|
:}|