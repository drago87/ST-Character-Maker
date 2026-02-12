/setvar key=baseContext {{noop}}|
/ife (parsedName != '') {:
	/addvar key=baseContext "{{newline}}- Name: {{getvar::parsedName}}"|
:}|
/ife (realParcedContext != '') {:
	/addvar key=baseContext "{{newline}}{{getvar::realParcedContext}}"|
:}|
/ife ((parsedOrigin != '') and (parsedOrigin != 'None')) {:
	/addvar key=baseContext "{{newline}}- Origin: {{getvar::parsedOrigin}}"
:}|
/ife (lifeStage != '') {:
	/addvar key=baseContext "{{newline}}- Life Stage: {{getvar::lifeStage}}"
:}|
/ife (parcedAge != '') {:
	/addvar key=baseContext "{{newline}}- Age: {{getvar::parcedAge}}"
:}|
/ife (gender != '') {:
	/addvar key=baseContext "{{newline}}- Gender: {{getvar::gender}}"
:}|
/ife (parsedSpecies != '') {:
	/addvar key=baseContext "{{newline}}- Species: {{getvar::parsedSpecies}}"
:}|




/ife (baseContext != '') {:
	
	/let key=tempContext {{noop}}|
	/let key=find {{noop}}|
	/let key=wi_uid {{noop}}|
	/let key=wi_book_f {{noop}}|
	/let key=wi_book_key_f {{noop}}|
	
	/getvar key=genSettings index=wi_book|
	/var key=wi_book_f {{pipe}}|
	/ife ( wi_book_f == '') {:
		/var key=wi_book_f "CMC Generation Prompts"|
	:}|
	
	/ife ((wi_book_f == 'CMC Generation Prompts') or (wi_book_f == 'CMC Information')) {:
		/var key=wi_book_f "{{var::wi_book_f}} {{getglobalvar::model}}"|
	:}|
	
	/getvar key=genSettings index=wi_book_key|
	/var key=wi_book_key_f {{pipe}}|
	/ife ( wi_book_key_f == '') {:
		/abort quiet=false Missing wi_book_key name in input.|
	:}|
	
	
	/var key=find "{{var::wi_book_key_f}}: Context"|
	/findentry field=comment file="CMC Generation Prompts {{getglobalvar::model}}" "{{var::find}}"|
	/var key=wi_uid {{pipe}}|
	/getentryfield field=comment file="CMC Generation Prompts {{getglobalvar::model}}" {{var::wi_uid}}|
	/let key=testPrompt {{pipe}}|
	/ife ( find == testPrompt) {:
		/getentryfield field=content file="CMC Generation Prompts {{getglobalvar::model}}" {{var::wi_uid}}|
		/var key=tempContext {{pipe}}|
		/ife (tempContext == '') {:
			/var key=find "Context"|
			/findentry field=comment file="CMC Generation Prompts {{getglobalvar::model}}" "{{var::find}}"|
			/var key=wi_uid {{pipe}}|
			/getentryfield field=content file="CMC Generation Prompts {{getglobalvar::model}}" {{var::wi_uid}}|
			/var key=tempContext {{pipe}}|
		:}|
	:}|
	/else {:
		/var key=find "Context"|
		/findentry field=comment file="CMC Generation Prompts {{getglobalvar::model}}" "{{var::find}}"|
		/var key=wi_uid {{pipe}}|
		/getentryfield field=content file="CMC Generation Prompts {{getglobalvar::model}}" {{var::wi_uid}}|
		/var key=tempContext {{pipe}}|
	:}|
	/setvar key=baseContext {{var::tempContext}}|
:}|