/ife (qestions == '') {: 
	/findentry field=comment file="CMC Questions" "Personality: Q"|
	/let key=wi_uid {{pipe}}|
	/getentryfield field=content file="CMC Information {{getglobalvar::model}}" {{var::wi_uid}}|
	/let key=unfilteredQuestions {{pipe}}|
	/split find="\n" {{var::unfilteredQuestions}}|
	/var key=unfilteredQuestions {{pipe}}|


	/setvar key=qestions []|
	/foreach {{var::unfilteredQuestions}} {:
		/ife (( user != 'Yes') and ('--User--' not in item)) or ( user == 'Yes') {:
			/buttons labels=["Yes", "No"] <div>Do you want to have this question?</div><div>{{var::item}}</div>|
			/let key=exp {{pipe}}|
			/ife ( exp == ''){:
				/echo Aborting |
				/abort
			:}|
			/elseif ( exp == 'Yes') {:
				/addvar key=qestions {{var::item}}|
			:}|
		:}| 
	:}|
:}|
/let key=stop Yes|
/whilee (stop == 'Yes') {:
	/buttons labels=["Yes", "No"] Do you want to add another question?|
	/var key=stop {{pipe}}|
	/ife ( stop == '') {:
		/echo Aborting |
		/abort
	:}|
	/ife ( stop == 'Yes') {:
		/input What is the question you want {{getvar::firstName}} to answer?|
		/let key=q {{pipe}}|
		/ife ( q == '') {:
			/echo Aborting |
			/abort
		:}|
		/addvar key=qestions {{var::q}}|
	:}|
:}|