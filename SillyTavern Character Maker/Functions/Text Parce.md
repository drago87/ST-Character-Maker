/let textParse {: input=
	/let x {{var::input}}|
	/ife ( (firstName != '') and (firstName in x)) {:
		/re-replace find="/{{getvar::firstName}}/g" replace="{\{getvar::firstName}}" {{var::x}}|
		/var x {{pipe}}|
	:}|
	/elseif ( (firstName != '') and ('--name--' in x)) {:
		/ife (lastName != '') {:
			/re-replace find="/--name--/g" replace="{\{getvar::firstName}} {\{getvar::lastName}}" {{var::x}}|
			/var x {{pipe}}|
		:}|
		/else {:
			/re-replace find="/--name--/g" replace="{\{getvar::firstName}}" {{var::x}}|
			/var x {{pipe}}|
		:}|
	:}|
	/ife ((lastName != '') and (lastName in x)) {:
		/re-replace find="/{{getvar::lastName}}/g" replace="{\{getvar::lastName}}" {{var::x}}|
		/var x {{pipe}}|
	:}|
	/ife ((parcedSpecies != '') and (parcedSpecies in x)) {:
		/re-replace find="/{{getvar::parcedSpecies}}/g" replace="{\{getvar::parcedSpecies}}" {{var::x}}|
		/var x {{pipe}}|
	:}|
	/elseif ( (parcedSpecies != '') and ('--species--' in x)) {:
		/re-replace find="/--species--/g" replace="{\{getvar::parcedSpecies}}" {{var::x}}|
		/var x {{pipe}}|
	:}|
	/ife ((parcedAge != '') and (parcedAge in x)) {:
		/re-replace find="/{{getvar::parcedAge}}/g" replace="{\{getvar::parcedAge}}" {{var::x}}|
		/var x {{pipe}}|
	:}|
	/elseif ((parcedAge != '') and ('--age--' in x)) {:
		/re-replace find="/--age--/g" replace="{\{getvar::parcedAge}}" {{var::x}}|
		/var x {{pipe}}|
	:}|
	/ife ((realParced != '') and (realParced in x)) {:
		/re-replace find="/{{getvar::realParced}}/g" replace="{\{getvar::realParced}}" {{var::x}}|
		/var x {{pipe}}|
	:}|
	/re-replace find="/{{char}}/g" replace="{\{getvar::firstName}}" {{var::x}}|
	/re-replace find="/{{user}}/g" replace="{\{user}}" {{var::x}}|
	/var x {{pipe}}|
	
:}||