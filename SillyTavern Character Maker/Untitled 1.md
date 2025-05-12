/ife (( {{var::variableName}} == '') or ({{var::variableName}} == 'None')) {:
	/buttons labels=["Yes", "No"] Do you want to set {{var::variableName}} (it's currently empty)?|
	/var key=do {{pipe}}|
	/ife (do == '') {:
		/echo Aborting |
		/abort
	:}|
:}|
/elseif (skip == 'Update') {:
	/getvar key={{var::variableName}}|
    /buttons labels=["Yes", "No"] Do you want to redo {{var::variableName}} (current value: {{pipe}})?|
    /var key=do {{pipe}}|
    /ife (do == '') {:
        /echo Aborting |
        /abort
    :}|
:}|
/ife ( do == 'Yes' ) {:

:}|