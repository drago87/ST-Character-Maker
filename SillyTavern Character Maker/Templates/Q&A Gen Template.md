/var key=do Yes|
/var key=variableName ""|
/ife ( {{var::variableName}} != '') {:
	/buttons labels=["Yes", "No"] Do you want to redo the Q&A {{var::variableName}}|
	/var key=do {{pipe}}|
	/ife ( do == ''){:
		/echo Aborting |
		/abort
	:}|
:}|
/ife ( do == 'Yes' ) {:
	
	/setvar key=genSettings index=question Personality|
	/setvar key=genSettings index=needOutput No|
	/setvar key=genSettings index=useContext Yes|
	/setvar as=array key=list []|
	/ife ( normal_form == 'Anthropomorphic') {:
		/addvar key=list Anthropomorphic|
	:}|
	/elseif ( normal_form == 'Demi-Human') {:
		/addvar key=list Demi-Human|
	:}|
	/elseif ( normal_form == 'Kemonomimi') {:
		/addvar key=list Kemonomimi|
	:}|
	/elseif ( normal_form == 'Animalistic') {:
		/addvar key=list Animalistic|
	:}|
	/elseif ( normal_form == 'Pokémon') {:
		/addvar key=list Pokémon|
	:}|
	/elseif ( normal_form == 'Digimon') {:
		/addvar key=list Digimon|
	:}|
	/elseif ( normal_form == 'Android') {:
		/addvar key=list Android|
	:}|
	/setvar key=genSettings index=contextKey {{getvar::list}}|
	
	
	
:}|
/else {:
	/addvar key=dataBaseNames {{var::variableName}}|
:}|