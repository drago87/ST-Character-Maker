/let textParse {: input=
	/let x {{var::input}}|
	/ife (notes != '') {:
		/re-replace find="/{{getvar::firstName}}\|{\{char}}\|--FirstName--/g" replace="{\{getvar::FirstName}}" {{var::x}}|
		/var x {{pipe}}|
	:}|
	/return {{var::x}}|
:}||