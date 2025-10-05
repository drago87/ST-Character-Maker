/let key=anatomyPrompt {{noop}}|
	/var key=find "Anatomy: {{getvar::characterArchetype}}: {{getvar::characterType}}: {{getvar::parsedAnimalType}}"|
	/findentry field=comment file="CMC Anatomy" "{{var::find}}"|
	/var key=wi_uid {{pipe}}|
	/getentryfield field=comment file="CMC Anatomy" {{var::wi_uid}}|
	/let key=testComment {{pipe}}|
	/ife ( find == testComment) {:
		/getentryfield field=content file="CMC Anatomy" {{var::wi_uid}}|
		/var key=anatomyPrompt {{pipe}}|
		/ife (anatomyPrompt == '') {: 
		:}|
		/else {:
			/var key=anatomyPrompt "{{getvar::characterArchetype}} Anatomy: {{getvar::characterType}}{{newline}}{{var::anatomyPrompt}}"
		:}|
		
	:}|