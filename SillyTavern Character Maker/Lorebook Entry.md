/ife (lorebookName == '') {:
	/popup <div>Create a lorebook and copy it's name. Make sure to remember it's name.</div><div>Recommended Name: {{getvar::firstName}} {{getvar::lastName}}</div><div>Press the blue box at the top with the text "Done" when done.</div>|
	/echo timeout=0 awaitDismissal=true Done|
	/let key=fileN {{noop}}|
	/ife ((lastName != '') and (lastName != 'None')) {:
		/var key=fileN {{getvar::firstName}} {{getvar::lastName}}|
	:}|
	/else {:
		/var key=fileN {{getvar::firstName}}|
	:}|
	/input rows=1 default={{var::fileN}} Paste or write the name of the lorebook.|
	/setvar key=lorebookName {{pipe}}|
	/ife (lorebookName == '') {:
		/echo Aborting|
		/abort|
	:}|
:}|

/wi-list-books all=true|
/let key=gLore {{pipe}}|

/let key=done No|

/ife (lorebookName in gLore) {:
	
	/let key=lorebookEntryName {{noop}}|
	/let key=lorebookTriggers {{noop}}|
	/let key=lorebookContent {{noop}}|
	/whilee (done != 'Yes') {:
		
		/input What do you want to lorebook entry to be called?|
		/var key=lorebookEntryName {{pipe}}|
		/ife (lorebookEntryName == '') {:
			/echo Aborting|
			/abort|
		:}|
		
		/input </div>What trigger words do you want the lorebook entry to have?</div><div>Supply a comma-seperated list.</div>|
		/var key=lorebookTriggers {{pipe}}|
		/ife (lorebookTriggers == '') {:
			/echo Aborting|
			/abort|
		:}|
		
		/input Write the content of the lorebook entry.|
		/var key=lorebookContent {{pipe}}|
		/ife (lorebookContent == '') {:
			/echo Aborting|
			/abort|
		:}|
		
		/createlore file={{getvar::lorebookName}} key={{var::lorebookEntryName}} {{var::lorebookContent}}|
		/setwifield field=key file={{getvar::lorebookName}} uid={{pipe}} {{var::lorebookTriggers}}|
		
		/buttons labels=["Yes", "No"] Have you added all Lorebook entries you want?|
		/var key=done {{pipe}}|
		/ife (done == '') {:
			/echo Aborting|
			/abort|
		:}|
	:}|
:}|
/else {:
	/popup The name of the lorebook is wrong. Try again.|
	/setvar key=lorebookName {{noop}}|
:}|