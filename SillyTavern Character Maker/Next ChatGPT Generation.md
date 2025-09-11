I change part of the task  to this
```
Body/Silhouette: {{getvar::appearanceBody}}
{{getvar::bodyProportions}}

{{getvar::genitalia}}

Distinct features:
```

and i'm using this logic
```
/setvar key=bodyProportions {{noop}}|
/ife ((buttSize != '') or (thighsSize != '') or (hipsSize != '') or (breastSize != '')) {:
	/setvar key=bodyAdd {{noop}}|
	/addvar key=bodyProportions "Body proportions (read as silhouettes only):"|
	/ife (buttSize != '') {:
		/ife (bodyAdd != '') {:
			/addvar key=bodyAdd ", "|
		:}|
		/addvar key=bodyAdd {{getvar::buttSize}}|
	:}|
	/ife (thighsSize != '') {:
		/ife (bodyAdd != '') {:
			/addvar key=bodyAdd ", "|
		:}|
		/addvar key=bodyAdd {{getvar::thighsSize}}|
	:}|
	/ife (hipsSize != '') {:
		/ife (bodyAdd != '') {:
			/addvar key=bodyAdd ", "|
		:}|
		/addvar key=bodyAdd {{getvar::hipsSize}}|
	:}|
	/ife (breastSize != '') {:
		/ife (bodyAdd != '') {:
			/addvar key=bodyAdd ", "|
		:}|
		/addvar key=bodyAdd {{getvar::breastSize}}|
	:}|
	/addvar key=bodyProportions " {{getvar::bodyAdd}}"|
	/flushvar bodyAdd|
:}|

/setvar key=genitalia "Genitalia:"|
/ife ((appearancePussy != 'None') and (appearancePussy != '')) {:
	/addvar key=genitalia {{newline}}- Pussy: {{getvar::appearancePussy}}|
:}|
/ife ((clitVisability != 'None') and (clitVisability != '')) {:
	/addvar key=genitalia {{newline}}- Clit visibility: {{getvar::clitVisability}}|
:}|
/ife ((labiaMinoraVisability != 'None') and (labiaMinoraVisability != '')) {:
	/addvar key=genitalia {{newline}}- Labia minora visibility: {{getvar::labiaMinoraVisability}}|
:}|
/ife ((appearanceCock != 'None') and (appearanceCock != '')) {:
	/addvar key=genitalia {{newline}}- Cock: {{getvar::appearanceCock}}|
:}|
/ife ((appearanceGenitals != 'None') and (appearanceGenitals != '')) {:
	/addvar key=genitalia {{newline}}- Combined genitals (futanari): {{getvar::appearanceGenitals}}|
:}|
```