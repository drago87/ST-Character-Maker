/qr-list CMC Main|
/getat index=1 {{pipe}}|
/let qrlabel {{pipe}}|
/qr-get set="CMC Main" label={{var::qrlabel}}|
/getat index="message" {{pipe}}|
/qr-update set="CMC Main" label={{var::qrlabel}} newlabel="Continue Generating Outfit" {{pipe}}|

/:"CMC Logic.Get Char info"|

/setvar key=dataBaseNames []|
/flushvar genSettings|

/setvar key=stepVar Step4|

/setvar key=skip Add|
/*
/ife ( stepDone == 'No') {:
	/buttons labels=["Restart", "Add"] Do you want to add a new outfit or start from the beginning?|
	/setvar key=skip {{pipe}}|
	/ife ( skip == ''){:
		/echo Aborting |
		/abort
	:}|
:}|
/ife ( skip == 'Add') {:
	/flushvar outfitHead|
	/flushvar outfitAccessories|
	/flushvar outfitMakeup|
	/flushvar outfitNeck|
	/flushvar outfitOnePiece|
	/flushvar outfitTop|
	/flushvar outfitBottom|
	/flushvar outfitLegs|
	/flushvar outfitShoes|
	/flushvar outfitUnderwearTop|
	/flushvar outfitUnderwearBottom|
	/flushvar outfitHeadDescription|
	/flushvar outfitAccessoriesDescription|
	/flushvar outfitMakeupDescription|
	/flushvar outfitNeckDescription|
	/flushvar outfitOnePieceDescription|
	/flushvar outfitTopDescription|
	/flushvar outfitBottomDescription|
	/flushvar outfitLegsDescription|
	/flushvar outfitShoesDescription|
	/flushvar outfitUnderwearTopDescription|
	/flushvar outfitUnderwearBottomDescription|
:}|
/else {:
	/flushvar outfits|
	/flushvar outfitHead|
	/flushvar outfitAccessories|
	/flushvar outfitMakeup|
	/flushvar outfitNeck|
	/flushvar outfitOnePiece|
	/flushvar outfitTop|
	/flushvar outfitBottom|
	/flushvar outfitLegs|
	/flushvar outfitShoes|
	/flushvar outfitUnderwearTop|
	/flushvar outfitUnderwearBottom|
	/flushvar outfitHeadDescription|
	/flushvar outfitAccessoriesDescription|
	/flushvar outfitMakeupDescription|
	/flushvar outfitNeckDescription|
	/flushvar outfitOnePieceDescription|
	/flushvar outfitTopDescription|
	/flushvar outfitBottomDescription|
	/flushvar outfitLegsDescription|
	/flushvar outfitShoesDescription|
	/flushvar outfitUnderwearTopDescription|
	/flushvar outfitUnderwearBottomDescription|
:}|
*|
/setvar key=stepDone No|
/setvar key=outfitsDone Yes|
/let key=do {{noop}}|
/let key=variableName {{noop}}|
/let key=selected_btn {{noop}}|
/let key=overallOutfit {{noop}}|


/flushvar outfits|
/flushvar outfitHead|
/flushvar outfitAccessories|
/flushvar outfitMakeup|
/flushvar outfitNeck|
/flushvar outfitOnePiece|
/flushvar outfitTop|
/flushvar outfitBottom|
/flushvar outfitLegs|
/flushvar outfitShoes|
/flushvar outfitUnderwearTop|
/flushvar outfitUnderwearBottom|
/flushvar outfitHeadDescription|
/flushvar outfitAccessoriesDescription|
/flushvar outfitMakeupDescription|
/flushvar outfitNeckDescription|
/flushvar outfitOnePieceDescription|
/flushvar outfitTopDescription|
/flushvar outfitBottomDescription|
/flushvar outfitLegsDescription|
/flushvar outfitShoesDescription|
/flushvar outfitUnderwearTopDescription|
/flushvar outfitUnderwearBottomDescription|


/getvar key=outfits index="Main Outfit"|
/let key=outfitsCheck {{pipe}}|

/ife (outfitsCheck == '') {:
	/setvar key=outfits {}|
:}|
/*
/else {:
	/buttons labels=["Yes", "No"] Do you want to add more outfits?|
	/setvar key=outfitsDone {{pipe}}|
:}|
*|

/whilee (outfitsDone != 'No') {:
	/var key=overallOutfit {{noop}}|
	/buttons labels=["Yes", "No"] <div>Do you want to set a overall outfit look? This can be changed for each outfit part</div><div>Example1: School Uniform</div><div>Example2: School Swimsuit</div><div>Example3: Office Outfit</div>|
	/var selected_btn {{pipe}}|
	/ife ( selected_btn == ''){:
		/echo Aborting |
		/abort
	:}|
	/elseif ( selected_btn == 'Yes') {:
		/input <div>Example1: School Uniform</div><div>Example2: School Swimsuit</div><div>Example3: Office Outfit</div>|
		/var key=overallOutfit {{pipe}}|
		/ife ( overallOutfit == ''){:
			/echo Aborting |
			/abort
		:}|
	:}|
	//Outfit Head|
	/var key=do No|
	/var key=variableName "outfitHead"|
	/ife ({{var::variableName}} == '') {:
	    /var key=do Yes|
	:}|
	/elseif (skip == 'Update') {:
	    /getvar key={{var::variableName}}|
	    /buttons labels=["Yes", "No"] Do you want to set or redo {{var::variableName}} (current value: {{pipe}})?|
	    /var key=do {{pipe}}|
	    /ife (do == '') {:
	        /echo Aborting |
	        /abort
	    :}|
	:}|
	/ife ( do == 'Yes' ) {:
		/setvar key=genSettings index=wi_book_key "Outfit Head"|
		/setvar key=genSettings index=genIsList Yes|
		/setvar key=genSettings index=inputIsTaskList No|
		/setvar key=genSettings index=genIsSentence No|
		/setvar key=genSettings index=needOutput Yes|
		/setvar key=genSettings index=outputIsList No|
		/setvar key=genSettings index=useContext Yes|
		/setvar key=extra []|
		/:"CMC Logic.Get Basic Type Context"|
		/ife (extra != '') {:
			/setvar key=genSettings index=contextKey {{getvar::extra}}|
		:}|
		/flushvar extra|
		/wait {{getvar::wait}}|
		
		/getvar key=genSettings index=inputIsList|
		/let key=inputIsList {{pipe}}|
		/getvar key=genSettings index=inputIsList|
		/let key=outputIsList {{pipe}}|
		
		/setvar key=guidance "The response should be guided toward: {{var::overallOutfit}}"|
		
		/ife ((outputIsList == 'Yes') or (outputIsList == 'Yes')) {:
			/setvar as=array key={{var::variableName}} []|
		:}|
		/else {:
			/setvar as=string key={{var::variableName}} {{noop}}|
		:}|
		//[[Generate with Prompt]]|
		/:"CMC Logic.GenerateWithPrompt"|
		/setvar key={{var::variableName}} {{getvar::output}}|
		
		/addvar key=dataBaseNames {{var::variableName}}|
		/flushvar output|
		/flushvar guidance|
		/flushvar genOrder|
		/flushvar genContent|
		/flushvar genSettings|
	:}|
	/else {:
		/addvar key=dataBaseNames {{var::variableName}}|
	:}|
	//--------|
	
	//Outfit Head Description|
	/ife (outfitHead != 'None') {:
		/var key=do No|
		/var key=variableName "outfitHeadDescription"|
		/ife ({{var::variableName}} == '') {:
		    /var key=do Yes|
		:}|
		/elseif (skip == 'Update') {:
		    /getvar key={{var::variableName}}|
		    /buttons labels=["Yes", "No"] Do you want to set or redo {{var::variableName}} (current value: {{pipe}})?|
		    /var key=do {{pipe}}|
		    /ife (do == '') {:
		        /echo Aborting |
		        /abort
		    :}|
		:}|
		/ife ( do == 'Yes' ) {:
			/setvar key=genSettings index=wi_book_key "Outfit Head Description"|
			/setvar key=genSettings index=genIsList No|
			/setvar key=genSettings index=inputIsTaskList No|
			/setvar key=genSettings index=genIsSentence Yes|
			/setvar key=genSettings index=needOutput Yes|
			/setvar key=genSettings index=outputIsList No|
			/setvar key=genSettings index=useContext Yes|
			/setvar key=extra []|
			/addvar key=extra "- Hair: {{getvar::appearanceHair}}"|
			/ife ( appearanceFeatures != 'None') {:
				/addvar key=extra "- Features: {{getvar::appearanceFeatures}}"|
			:}|
			/setvar key=genSettings index=extraContext {{getvar::extra}}|
			/setvar key=extra []|
			/:"CMC Logic.Get Basic Type Context"|
			/ife (extra != '') {:
				/setvar key=genSettings index=contextKey {{getvar::extra}}|
			:}|
			/flushvar extra|
			/wait {{getvar::wait}}|
			
			/ife (( characterArchetype != 'Human') and ( characterArchetype != 'Android')) {:
				/setvar key=logicBasedInstruction "6. If {{getvar::parsedSpecies}} includes visible head features (ears, horns, fins, wings, etc), consider how they affect fit or placement of the headwear."|
			:}|
			/elseif (( characterArchetype == 'Human') or ( characterArchetype == 'Android')) {:
				/setvar key=logicBasedInstruction "6. If {{getvar::appearanceFeatures}} includes scars, prosthetics, cybernetics, piercings, or other physical modifications, consider how they visually contrast with or influence the item’s appearance or placement."|
			:}|
			
			/getvar key=genSettings index=inputIsList|
			/let key=inputIsList {{pipe}}|
			/getvar key=genSettings index=inputIsList|
			/let key=outputIsList {{pipe}}|
			
			/ife ((outputIsList == 'Yes') or (outputIsList == 'Yes')) {:
				/setvar as=array key={{var::variableName}} []|
			:}|
			/else {:
				/setvar as=string key={{var::variableName}} {{noop}}|
			:}|
			//[[Generate with Prompt]]|
			/:"CMC Logic.GenerateWithPrompt"|
			/setvar key={{var::variableName}} {{getvar::output}}|
			
			/addvar key=dataBaseNames {{var::variableName}}|
			/flushvar output|
			/flushvar logicBasedInstruction|
			/flushvar guidance|
			/flushvar genOrder|
			/flushvar genContent|
			/flushvar genSettings|
		:}|
		/else {:
			/addvar key=dataBaseNames {{var::variableName}}|
		:}|
	:}|
	/else {:
		/setvar key=outfitHeadDescription None|
		/addvar key=dataBaseNames outfitHeadDescription|
	:}|
	//--------|
	
	//Outfit Accessories|
	/var key=do No|
	/var key=variableName "outfitAccessories"|
	/ife ({{var::variableName}} == '') {:
	    /var key=do Yes|
	:}|
	/elseif (skip == 'Update') {:
	    /getvar key={{var::variableName}}|
	    /buttons labels=["Yes", "No"] Do you want to set or redo {{var::variableName}} (current value: {{pipe}})?|
	    /var key=do {{pipe}}|
	    /ife (do == '') {:
	        /echo Aborting |
	        /abort
	    :}|
	:}|
	/ife ( do == 'Yes' ) {:
		/setvar key=genSettings index=wi_book_key "Outfit Accessories"|
		/setvar key=genSettings index=genIsList Yes|
		/setvar key=genSettings index=inputIsTaskList No|
		/setvar key=genSettings index=genIsSentence No|
		/setvar key=genSettings index=needOutput Yes|
		/setvar key=genSettings index=outputIsList No|
		/setvar key=genSettings index=useContext Yes|
		/setvar key=extra []|
		/:"CMC Logic.Get Basic Type Context"|
		/ife (extra != '') {:
			/setvar key=genSettings index=contextKey {{getvar::extra}}|
		:}|
		/flushvar extra|
		/wait {{getvar::wait}}|
		
		/getvar key=genSettings index=inputIsList|
		/let key=inputIsList {{pipe}}|
		/getvar key=genSettings index=inputIsList|
		/let key=outputIsList {{pipe}}|
		
		/setvar key=guidance "The response should be guided toward: {{var::overallOutfit}}"|
		
		/ife ((outputIsList == 'Yes') or (outputIsList == 'Yes')) {:
			/setvar as=array key={{var::variableName}} []|
		:}|
		/else {:
			/setvar as=string key={{var::variableName}} {{noop}}|
		:}|
		//[[Generate with Prompt]]|
		/:"CMC Logic.GenerateWithPrompt"|
		/setvar key={{var::variableName}} {{getvar::output}}|
		
		/addvar key=dataBaseNames {{var::variableName}}|
		/flushvar output|
		/flushvar guidance|
		/flushvar genOrder|
		/flushvar genContent|
		/flushvar genSettings|
	:}|
	/else {:
		/addvar key=dataBaseNames {{var::variableName}}|
	:}|
	//--------|
	
	//Outfit Accessories Description|
	/ife (outfitAccessories != 'None') {:
		/var key=do No|
		/var key=variableName "outfitAccessoriesDescription"|
		/ife ({{var::variableName}} == '') {:
		    /var key=do Yes|
		:}|
		/elseif (skip == 'Update') {:
		    /getvar key={{var::variableName}}|
		    /buttons labels=["Yes", "No"] Do you want to set or redo {{var::variableName}} (current value: {{pipe}})?|
		    /var key=do {{pipe}}|
		    /ife (do == '') {:
		        /echo Aborting |
		        /abort
		    :}|
		:}|
		/ife ( do == 'Yes' ) {:
			/setvar key=genSettings index=wi_book_key "Outfit Accessories Description"|
			/setvar key=genSettings index=genIsList No|
			/setvar key=genSettings index=inputIsList Yes|
			/setvar key=genSettings index=inputIsTaskList No|
			/setvar key=genSettings index=genIsSentence Yes|
			/setvar key=genSettings index=needOutput Yes|
			/setvar key=genSettings index=outputIsList No|
			/setvar key=genSettings index=useContext Yes|
			/setvar key=extra []|
			/ife ( appearanceFeatures != 'None') {:
				/addvar key=extra "- Features: {{getvar::appearanceFeatures}}"|
			:}|
			/setvar key=genSettings index=extraContext {{getvar::extra}}|
			/setvar key=extra []|
			/:"CMC Logic.Get Basic Type Context"|
			/ife (extra != '') {:
				/setvar key=genSettings index=contextKey {{getvar::extra}}|
			:}|
			/flushvar extra|
			/wait {{getvar::wait}}|
			
			/ife (( characterArchetype != 'Human') and ( characterArchetype != 'Android')) {:
				/setvar key=logicBasedInstruction "7. If {{getvar::parsedSpecies}} includes tails, horns, paws, wings, or other non-human limbs, consider how this affects where or how the accessory is worn."|
			:}|
			/elseif (( characterArchetype == 'Human') or ( characterArchetype == 'Android')) {:
				/setvar key=logicBasedInstruction "7. If {{getvar::appearanceFeatures}} includes prosthetics, piercings, cybernetics, or scars, consider how the accessory interacts with or highlights these features."|
			:}|
			
			/getvar key=genSettings index=inputIsList|
			/let key=inputIsList {{pipe}}|
			/getvar key=genSettings index=inputIsList|
			/let key=outputIsList {{pipe}}|
			
			/ife ((inputIsList == 'Yes') or (outputIsList == 'Yes')) {:
				/setvar as=array key={{var::variableName}} []|
			:}|
			/else {:
				/setvar as=string key={{var::variableName}} {{noop}}|
			:}|
			//[[Generate with Prompt]]|
			/ife (inputIsList == 'Yes') {:
				/foreach {{getvar::outfitAccessories}} {:
					/setvar key={{var::variableName}}Item {{var::item}}|
					/:"CMC Logic.GenerateWithPrompt"|
					/addvar key={{var::variableName}} {{getvar::output}}|
					/flushvar output|
					/flushvar guidance|
				:}|
				/flushvar {{var::variableName}}Item|
			:}|
			/else {:
				/:"CMC Logic.GenerateWithPrompt"|
				/setvar key={{var::variableName}} {{getvar::output}}|
			:}|
			
			/addvar key=dataBaseNames {{var::variableName}}|
			/flushvar output|
			/flushvar logicBasedInstruction|
			/flushvar guidance|
			/flushvar genOrder|
			/flushvar genContent|
			/flushvar genSettings|
		:}|
		/else {:
			/addvar key=dataBaseNames {{var::variableName}}|
		:}|
	:}|
	/else {:
		/setvar key=outfitAccessoriesDescription None|
		/addvar key=dataBaseNames outfitAccessoriesDescription|
	:}|
	//--------|
	/wait {{getvar::wait}}|
	/setvar key=parsedAccessories {{noop}}|
	/ife (outfitAccessoriesDescription == 'None') {:
		/addvar key=parsedAccessories " {{getvar::outfitAccessoriesDescription}}"|
	:}|
	/elseif (outfitAccessoriesDescription is list) {:
		/foreach {{getvar::outfitAccessoriesDescription}} {:
			/addvar key=parsedAccessories "{{newline}}  - {{var::item}}"|
		:}|
	:}|
	/addvar key=dataBaseNames parsedAccessories|
	
	//Outfit Makeup|
	/var key=do No|
	/var key=variableName "outfitMakeup"|
	/ife ({{var::variableName}} == '') {:
	    /var key=do Yes|
	:}|
	/elseif (skip == 'Update') {:
	    /getvar key={{var::variableName}}|
	    /buttons labels=["Yes", "No"] Do you want to set or redo {{var::variableName}} (current value: {{pipe}})?|
	    /var key=do {{pipe}}|
	    /ife (do == '') {:
	        /echo Aborting |
	        /abort
	    :}|
	:}|
	/ife ( do == 'Yes' ) {:
		/setvar key=genSettings index=wi_book_key "Outfit Makeup"|
		/setvar key=genSettings index=genIsList Yes|
		/setvar key=genSettings index=inputIsTaskList No|
		/setvar key=genSettings index=genIsSentence No|
		/setvar key=genSettings index=needOutput Yes|
		/setvar key=genSettings index=outputIsList No|
		/setvar key=genSettings index=useContext Yes|
		/setvar key=extra []|
		/:"CMC Logic.Get Basic Type Context"|
		/ife (extra != '') {:
			/setvar key=genSettings index=contextKey {{getvar::extra}}|
		:}|
		/flushvar extra|
		/wait {{getvar::wait}}|
		
		/getvar key=genSettings index=inputIsList|
		/let key=inputIsList {{pipe}}|
		/getvar key=genSettings index=inputIsList|
		/let key=outputIsList {{pipe}}|
		
		/setvar key=guidance "The response should be guided toward: {{var::overallOutfit}}"|
		
		/ife ((outputIsList == 'Yes') or (outputIsList == 'Yes')) {:
			/setvar as=array key={{var::variableName}} []|
		:}|
		/else {:
			/setvar as=string key={{var::variableName}} {{noop}}|
		:}|
		//[[Generate with Prompt]]|
		/:"CMC Logic.GenerateWithPrompt"|
		/setvar key={{var::variableName}} {{getvar::output}}|
		
		/addvar key=dataBaseNames {{var::variableName}}|
		/flushvar output|
		/flushvar guidance|
		/flushvar genOrder|
		/flushvar genContent|
		/flushvar genSettings|
	:}|
	/else {:
		/addvar key=dataBaseNames {{var::variableName}}|
	:}|
	//--------|
	
	//Outfit Makeup Description|
	/ife (outfitMakeup != 'None') {:
		/var key=do No|
		/var key=variableName "outfitMakeupDescription"|
		/ife ({{var::variableName}} == '') {:
		    /var key=do Yes|
		:}|
		/elseif (skip == 'Update') {:
		    /getvar key={{var::variableName}}|
		    /buttons labels=["Yes", "No"] Do you want to set or redo {{var::variableName}} (current value: {{pipe}})?|
		    /var key=do {{pipe}}|
		    /ife (do == '') {:
		        /echo Aborting |
		        /abort
		    :}|
		:}|
		/ife ( do == 'Yes' ) {:
			/setvar key=genSettings index=wi_book_key "Outfit Makeup Description"|
			/setvar key=genSettings index=genIsList No|
			/setvar key=genSettings index=inputIsList Yes|
			/setvar key=genSettings index=inputIsTaskList No|
			/setvar key=genSettings index=genIsSentence Yes|
			/setvar key=genSettings index=needOutput Yes|
			/setvar key=genSettings index=outputIsList No|
			/setvar key=genSettings index=useContext Yes|
			/setvar key=extra []|
			/ife ( appearanceFeatures != 'None') {:
				/addvar key=extra "- Features: {{getvar::appearanceFeatures}}"|
			:}|
			/setvar key=genSettings index=extraContext {{getvar::extra}}|
			/setvar key=extra []|
			/:"CMC Logic.Get Basic Type Context"|
			/ife (extra != '') {:
				/setvar key=genSettings index=contextKey {{getvar::extra}}|
			:}|
			/flushvar extra|
			/wait {{getvar::wait}}|
			
			/ife (( characterArchetype != 'Human') and ( characterArchetype != 'Android')) {:
				/setvar key=logicBasedInstruction "7. If {{getvar::appearanceFeatures}} includes fur, scales, feathers, or non-human markings, ensure the makeup is applied in visible or exposed areas — such as facial skin patches, ridges, horns, or ceremonial markings — and accounts for species texture."|
			:}|
			/elseif (( characterArchetype == 'Human') or ( characterArchetype == 'Android')) {:
				/setvar key=logicBasedInstruction "7. If {{getvar::appearanceFeatures}} includes prosthetics, cybernetics, scars, piercings, or skin conditions, consider how the makeup highlights or contrasts with these features visually."|
			:}|
			
			/getvar key=genSettings index=inputIsList|
			/let key=inputIsList {{pipe}}|
			/getvar key=genSettings index=inputIsList|
			/let key=outputIsList {{pipe}}|
			
			/ife ((inputIsList == 'Yes') or (outputIsList == 'Yes')) {:
				/setvar as=array key={{var::variableName}} []|
			:}|
			/else {:
				/setvar as=string key={{var::variableName}} {{noop}}|
			:}|
			//[[Generate with Prompt]]|
			/ife (inputIsList == 'Yes') {:
				/foreach {{getvar::outfitMakeup}} {:
					/setvar key={{var::variableName}}Item {{var::item}}|
					/:"CMC Logic.GenerateWithPrompt"|
					/addvar key={{var::variableName}} {{getvar::output}}|
					/flushvar output|
					/flushvar guidance|
				:}|
				/flushvar {{var::variableName}}Item|
			:}|
			/else {:
				/:"CMC Logic.GenerateWithPrompt"|
				/setvar key={{var::variableName}} {{getvar::output}}|
			:}|
			
			/addvar key=dataBaseNames {{var::variableName}}|
			/flushvar output|
			/flushvar logicBasedInstruction|
			/flushvar guidance|
			/flushvar genOrder|
			/flushvar genContent|
			/flushvar genSettings|
		:}|
		/else {:
			/addvar key=dataBaseNames {{var::variableName}}|
		:}|
	:}|
	/else {:
		/setvar key=outfitMakeupDescription None|
		/addvar key=dataBaseNames outfitMakeupDescription|
	:}|
	//--------|
	/wait {{getvar::wait}}|
	/setvar key=parsedMakeup {{noop}}|
	/ife (outfitMakeupDescription == 'None') {:
		/addvar key=parsedMakeup " {{getvar::outfitMakeupDescription}}"|
	:}|
	/elseif (outfitMakeupDescription is list) {:
		/foreach {{getvar::outfitMakeupDescription}} {:
			/addvar key=parsedMakeup "{{newline}}  - {{var::item}}"|
		:}|
	:}|
	/addvar key=dataBaseNames parsedMakeup|
	
	//Outfit Neck|
	/var key=do No|
	/var key=variableName "outfitNeck"|
	/ife ({{var::variableName}} == '') {:
	    /var key=do Yes|
	:}|
	/elseif (skip == 'Update') {:
	    /getvar key={{var::variableName}}|
	    /buttons labels=["Yes", "No"] Do you want to set or redo {{var::variableName}} (current value: {{pipe}})?|
	    /var key=do {{pipe}}|
	    /ife (do == '') {:
	        /echo Aborting |
	        /abort
	    :}|
	:}|
	/ife ( do == 'Yes' ) {:
		/setvar key=genSettings index=wi_book_key "Outfit Neck"|
		/setvar key=genSettings index=genIsList Yes|
		/setvar key=genSettings index=inputIsTaskList No|
		/setvar key=genSettings index=genIsSentence No|
		/setvar key=genSettings index=needOutput Yes|
		/setvar key=genSettings index=outputIsList No|
		/setvar key=genSettings index=useContext Yes|
		/setvar key=extra []|
		/:"CMC Logic.Get Basic Type Context"|
		/ife (extra != '') {:
			/setvar key=genSettings index=contextKey {{getvar::extra}}|
		:}|
		/flushvar extra|
		/wait {{getvar::wait}}|
		
		/getvar key=genSettings index=inputIsList|
		/let key=inputIsList {{pipe}}|
		/getvar key=genSettings index=inputIsList|
		/let key=outputIsList {{pipe}}|
		
		/setvar key=guidance "The response should be guided toward: {{var::overallOutfit}}"|
		
		/ife ((outputIsList == 'Yes') or (outputIsList == 'Yes')) {:
			/setvar as=array key={{var::variableName}} []|
		:}|
		/else {:
			/setvar as=string key={{var::variableName}} {{noop}}|
		:}|
		//[[Generate with Prompt]]|
		/:"CMC Logic.GenerateWithPrompt"|
		/setvar key={{var::variableName}} {{getvar::output}}|
		
		/addvar key=dataBaseNames {{var::variableName}}|
		/flushvar output|
		/flushvar guidance|
		/flushvar genOrder|
		/flushvar genContent|
		/flushvar genSettings|
	:}|
	/else {:
		/addvar key=dataBaseNames {{var::variableName}}|
	:}|
	//--------|
	
	//Outfit Neck Description|
	/ife (outfitNeck != 'None') {:
		/var key=do No|
		/var key=variableName "outfitNeckDescription"|
		/ife ({{var::variableName}} == '') {:
		    /var key=do Yes|
		:}|
		/elseif (skip == 'Update') {:
		    /getvar key={{var::variableName}}|
		    /buttons labels=["Yes", "No"] Do you want to set or redo {{var::variableName}} (current value: {{pipe}})?|
		    /var key=do {{pipe}}|
		    /ife (do == '') {:
		        /echo Aborting |
		        /abort
		    :}|
		:}|
		/ife ( do == 'Yes' ) {:
			/setvar key=genSettings index=wi_book_key "Outfit Neck Description"|
			/setvar key=genSettings index=genIsList No|
			/setvar key=genSettings index=inputIsList No|
			/setvar key=genSettings index=inputIsTaskList No|
			/setvar key=genSettings index=genIsSentence Yes|
			/setvar key=genSettings index=needOutput Yes|
			/setvar key=genSettings index=outputIsList No|
			/setvar key=genSettings index=useContext Yes|
			/setvar key=extra []|
			/ife ( appearanceFeatures != 'None') {:
				/addvar key=extra "- Features: {{getvar::appearanceFeatures}}"|
			:}|
			/setvar key=genSettings index=extraContext {{getvar::extra}}|
			/setvar key=extra []|
			/:"CMC Logic.Get Basic Type Context"|
			/ife (extra != '') {:
				/setvar key=genSettings index=contextKey {{getvar::extra}}|
			:}|
			/flushvar extra|
			/wait {{getvar::wait}}|
			
			/ife (( characterArchetype != 'Human') and ( characterArchetype != 'Android')) {:
				/setvar key=logicBasedInstruction "7. If {{getvar::appearanceFeatures}} includes fur, scales, manes, ruffs, or neck-based traits (e.g., gills, fins, feathers), describe how the neckwear fits, wraps around, or contrasts with those features."|
			:}|
			/elseif (( characterArchetype == 'Human') or ( characterArchetype == 'Android')) {:
				/setvar key=logicBasedInstruction "7. If {{getvar::appearanceFeatures}} includes scars, prosthetics, piercings, or visible augmentations around the neck or upper torso, reflect how the neckwear interacts with or complements these features."|
			:}|
			
			/getvar key=genSettings index=inputIsList|
			/let key=inputIsList {{pipe}}|
			/getvar key=genSettings index=inputIsList|
			/let key=outputIsList {{pipe}}|
			
			/ife ((inputIsList == 'Yes') or (outputIsList == 'Yes')) {:
				/setvar as=array key={{var::variableName}} []|
			:}|
			/else {:
				/setvar as=string key={{var::variableName}} {{noop}}|
			:}|
			//[[Generate with Prompt]]|
			
			/:"CMC Logic.GenerateWithPrompt"|
			/setvar key={{var::variableName}} {{getvar::output}}|
			
			
			/addvar key=dataBaseNames {{var::variableName}}|
			/flushvar output|
			/flushvar logicBasedInstruction|
			/flushvar guidance|
			/flushvar genOrder|
			/flushvar genContent|
			/flushvar genSettings|
		:}|
		/else {:
			/addvar key=dataBaseNames {{var::variableName}}|
		:}|
	:}|
	/else {:
		/setvar key=outfitNeckDescription None|
		/addvar key=dataBaseNames outfitNeckDescription|
	:}|
	//--------|
	
	//Outfit One-Piece|
	/var key=do No|
	/var key=variableName "outfitOnePiece"|
	/ife ({{var::variableName}} == '') {:
	    /var key=do Yes|
	:}|
	/elseif (skip == 'Update') {:
	    /getvar key={{var::variableName}}|
	    /buttons labels=["Yes", "No"] Do you want to set or redo {{var::variableName}} (current value: {{pipe}})?|
	    /var key=do {{pipe}}|
	    /ife (do == '') {:
	        /echo Aborting |
	        /abort
	    :}|
	:}|
	/ife ( do == 'Yes' ) {:
		/setvar key=genSettings index=wi_book_key "Outfit One-Piece"|
		/setvar key=genSettings index=genIsList Yes|
		/setvar key=genSettings index=inputIsTaskList No|
		/setvar key=genSettings index=genIsSentence No|
		/setvar key=genSettings index=needOutput Yes|
		/setvar key=genSettings index=outputIsList No|
		/setvar key=genSettings index=useContext Yes|
		/setvar key=extra []|
		/:"CMC Logic.Get Basic Type Context"|
		/ife (extra != '') {:
			/setvar key=genSettings index=contextKey {{getvar::extra}}|
		:}|
		/flushvar extra|
		/wait {{getvar::wait}}|
		
		/getvar key=genSettings index=inputIsList|
		/let key=inputIsList {{pipe}}|
		/getvar key=genSettings index=inputIsList|
		/let key=outputIsList {{pipe}}|
		
		/setvar key=guidance "The response should be guided toward: {{var::overallOutfit}}"|
		
		/ife ((outputIsList == 'Yes') or (outputIsList == 'Yes')) {:
			/setvar as=array key={{var::variableName}} []|
		:}|
		/else {:
			/setvar as=string key={{var::variableName}} {{noop}}|
		:}|
		//[[Generate with Prompt]]|
		/:"CMC Logic.GenerateWithPrompt"|
		/setvar key={{var::variableName}} {{getvar::output}}|
		
		/addvar key=dataBaseNames {{var::variableName}}|
		/flushvar output|
		/flushvar guidance|
		/flushvar genOrder|
		/flushvar genContent|
		/flushvar genSettings|
	:}|
	/else {:
		/addvar key=dataBaseNames {{var::variableName}}|
	:}|
	//--------|
	
	//Outfit One-Piece Description|
	/ife (outfitOnePiece != 'None') {:
		/var key=do No|
		/var key=variableName "outfitOnePieceDescription"|
		/ife ({{var::variableName}} == '') {:
		    /var key=do Yes|
		:}|
		/elseif (skip == 'Update') {:
		    /getvar key={{var::variableName}}|
		    /buttons labels=["Yes", "No"] Do you want to set or redo {{var::variableName}} (current value: {{pipe}})?|
		    /var key=do {{pipe}}|
		    /ife (do == '') {:
		        /echo Aborting |
		        /abort
		    :}|
		:}|
		/ife ( do == 'Yes' ) {:
			/setvar key=genSettings index=wi_book_key "Outfit One-Piece Description"|
			/setvar key=genSettings index=genIsList No|
			/setvar key=genSettings index=inputIsList No|
			/setvar key=genSettings index=inputIsTaskList No|
			/setvar key=genSettings index=genIsSentence Yes|
			/setvar key=genSettings index=needOutput Yes|
			/setvar key=genSettings index=outputIsList No|
			/setvar key=genSettings index=useContext Yes|
			/setvar key=extra []|
			/ife ( appearanceFeatures != 'None') {:
				/addvar key=extra "- Features: {{getvar::appearanceFeatures}}"|
			:}|
			/addvar key=extra "- Body: {{getvar::appearanceBody}}"|
			/ife ( appearanceBreasts != 'None') {:
				/addvar key=extra "- Breasts: {{getvar::appearanceBreasts}}"|
			:}|
			/setvar key=genSettings index=extraContext {{getvar::extra}}|
			/setvar key=extra []|
			/:"CMC Logic.Get Basic Type Context"|
			/ife (extra != '') {:
				/setvar key=genSettings index=contextKey {{getvar::extra}}|
			:}|
			/flushvar extra|
			/wait {{getvar::wait}}|
			
			/ife (( characterArchetype != 'Human') and ( characterArchetype != 'Android')) {:
				/setvar key=logicBasedInstruction "8. If {{getvar::appearanceFeatures}} includes wings, tail bases, dorsal fins, fur crests, or unusual body shapes, describe how the garment is shaped or opened to accommodate those features."|
			:}|
			/elseif (( characterArchetype == 'Human') or ( characterArchetype == 'Android')) {:
				/setvar key=logicBasedInstruction "8. If {{getvar::appearanceFeatures}} includes medical gear, prosthetics, or cybernetics on the torso or pelvis, describe how the garment adjusts to fit, support, or conceal them."|
			:}|
			
			/getvar key=genSettings index=inputIsList|
			/let key=inputIsList {{pipe}}|
			/getvar key=genSettings index=inputIsList|
			/let key=outputIsList {{pipe}}|
			
			/ife ((inputIsList == 'Yes') or (outputIsList == 'Yes')) {:
				/setvar as=array key={{var::variableName}} []|
			:}|
			/else {:
				/setvar as=string key={{var::variableName}} {{noop}}|
			:}|
			//[[Generate with Prompt]]|
			
			/:"CMC Logic.GenerateWithPrompt"|
			/setvar key={{var::variableName}} {{getvar::output}}|
			
			/addvar key=dataBaseNames {{var::variableName}}|
			/flushvar output|
			/flushvar logicBasedInstruction|
			/flushvar guidance|
			/flushvar genOrder|
			/flushvar genContent|
			/flushvar genSettings|
		:}|
		/else {:
			/addvar key=dataBaseNames {{var::variableName}}|
		:}|
	:}|
	/else {:
		/setvar key=outfitTopDescription None|
		/addvar key=dataBaseNames outfitTopDescription|
	:}|
	//--------|
	
	
	//Outfit Top|
	/var key=do No|
	/var key=variableName "outfitTop"|
	/ife ({{var::variableName}} == '') {:
	    /var key=do Yes|
	:}|
	/elseif (skip == 'Update') {:
	    /getvar key={{var::variableName}}|
	    /buttons labels=["Yes", "No"] Do you want to set or redo {{var::variableName}} (current value: {{pipe}})?|
	    /var key=do {{pipe}}|
	    /ife (do == '') {:
	        /echo Aborting |
	        /abort
	    :}|
	:}|
	/ife ( do == 'Yes' ) {:
		/setvar key=genSettings index=wi_book_key "Outfit Top"|
		/setvar key=genSettings index=genIsList Yes|
		/setvar key=genSettings index=inputIsTaskList No|
		/setvar key=genSettings index=genIsSentence No|
		/setvar key=genSettings index=needOutput Yes|
		/setvar key=genSettings index=outputIsList No|
		/setvar key=genSettings index=useContext Yes|
		/setvar key=extra []|
		/:"CMC Logic.Get Basic Type Context"|
		/ife (extra != '') {:
			/setvar key=genSettings index=contextKey {{getvar::extra}}|
		:}|
		/flushvar extra|
		/wait {{getvar::wait}}|
		
		/getvar key=genSettings index=inputIsList|
		/let key=inputIsList {{pipe}}|
		/getvar key=genSettings index=inputIsList|
		/let key=outputIsList {{pipe}}|
		
		/setvar key=guidance "The response should be guided toward: {{var::overallOutfit}}"|
		
		/ife ((outputIsList == 'Yes') or (outputIsList == 'Yes')) {:
			/setvar as=array key={{var::variableName}} []|
		:}|
		/else {:
			/setvar as=string key={{var::variableName}} {{noop}}|
		:}|
		//[[Generate with Prompt]]|
		/:"CMC Logic.GenerateWithPrompt"|
		/setvar key={{var::variableName}} {{getvar::output}}|
		
		/addvar key=dataBaseNames {{var::variableName}}|
		/flushvar output|
		/flushvar guidance|
		/flushvar genOrder|
		/flushvar genContent|
		/flushvar genSettings|
	:}|
	/else {:
		/addvar key=dataBaseNames {{var::variableName}}|
	:}|
	//--------|
	
	//Outfit Top Description|
	/ife (outfitTop != 'None') {:
		/var key=do No|
		/var key=variableName "outfitTopDescription"|
		/ife ({{var::variableName}} == '') {:
		    /var key=do Yes|
		:}|
		/elseif (skip == 'Update') {:
		    /getvar key={{var::variableName}}|
		    /buttons labels=["Yes", "No"] Do you want to set or redo {{var::variableName}} (current value: {{pipe}})?|
		    /var key=do {{pipe}}|
		    /ife (do == '') {:
		        /echo Aborting |
		        /abort
		    :}|
		:}|
		/ife ( do == 'Yes' ) {:
			/setvar key=genSettings index=wi_book_key "Outfit Top Description"|
			/setvar key=genSettings index=genIsList No|
			/setvar key=genSettings index=inputIsList No|
			/setvar key=genSettings index=inputIsTaskList No|
			/setvar key=genSettings index=genIsSentence Yes|
			/setvar key=genSettings index=needOutput Yes|
			/setvar key=genSettings index=outputIsList No|
			/setvar key=genSettings index=useContext Yes|
			/setvar key=extra []|
			/ife ( appearanceFeatures != 'None') {:
				/addvar key=extra "- Features: {{getvar::appearanceFeatures}}"|
			:}|
			/addvar key=extra "- Body: {{getvar::appearanceBody}}"|
			/ife ( appearanceBreasts != 'None') {:
				/addvar key=extra "- Breasts: {{getvar::appearanceBreasts}}"|
			:}|
			/setvar key=genSettings index=extraContext {{getvar::extra}}|
			/setvar key=extra []|
			/:"CMC Logic.Get Basic Type Context"|
			/ife (extra != '') {:
				/setvar key=genSettings index=contextKey {{getvar::extra}}|
			:}|
			/flushvar extra|
			/wait {{getvar::wait}}|
			
			/ife (( characterArchetype != 'Human') and ( characterArchetype != 'Android')) {:
				/setvar key=logicBasedInstruction "8. If {{getvar::appearanceFeatures}} includes wings, tail bases, dorsal fins, fur crests, or unusual body shapes, describe how the top is shaped or adapted to fit those features comfortably or functionally."|
			:}|
			/elseif (( characterArchetype == 'Human') or ( characterArchetype == 'Android')) {:
				/setvar key=logicBasedInstruction "8. If {{getvar::appearanceFeatures}} includes medical supports, prosthetics, or cybernetics on the torso or arms, describe how the top accommodates or interacts with them."|
			:}|
			
			/getvar key=genSettings index=inputIsList|
			/let key=inputIsList {{pipe}}|
			/getvar key=genSettings index=inputIsList|
			/let key=outputIsList {{pipe}}|
			
			/ife ((inputIsList == 'Yes') or (outputIsList == 'Yes')) {:
				/setvar as=array key={{var::variableName}} []|
			:}|
			/else {:
				/setvar as=string key={{var::variableName}} {{noop}}|
			:}|
			//[[Generate with Prompt]]|
			
			/:"CMC Logic.GenerateWithPrompt"|
			/setvar key={{var::variableName}} {{getvar::output}}|
			
			/addvar key=dataBaseNames {{var::variableName}}|
			/flushvar output|
			/flushvar logicBasedInstruction|
			/flushvar guidance|
			/flushvar genOrder|
			/flushvar genContent|
			/flushvar genSettings|
		:}|
		/else {:
			/addvar key=dataBaseNames {{var::variableName}}|
		:}|
	:}|
	/else {:
		/setvar key=outfitTopDescription None|
		/addvar key=dataBaseNames outfitTopDescription|
	:}|
	//--------|
	
	//Outfit Bottom|
	/var key=do No|
	/var key=variableName "outfitBottom"|
	/ife ({{var::variableName}} == '') {:
	    /var key=do Yes|
	:}|
	/elseif (skip == 'Update') {:
	    /getvar key={{var::variableName}}|
	    /buttons labels=["Yes", "No"] Do you want to set or redo {{var::variableName}} (current value: {{pipe}})?|
	    /var key=do {{pipe}}|
	    /ife (do == '') {:
	        /echo Aborting |
	        /abort
	    :}|
	:}|
	/ife ( do == 'Yes' ) {:
		/setvar key=genSettings index=wi_book_key "Outfit Bottom"|
		/setvar key=genSettings index=genIsList Yes|
		/setvar key=genSettings index=inputIsTaskList No|
		/setvar key=genSettings index=genIsSentence No|
		/setvar key=genSettings index=needOutput Yes|
		/setvar key=genSettings index=outputIsList No|
		/setvar key=genSettings index=useContext Yes|
		/setvar key=extra []|
		/:"CMC Logic.Get Basic Type Context"|
		/ife (extra != '') {:
			/setvar key=genSettings index=contextKey {{getvar::extra}}|
		:}|
		/flushvar extra|
		/wait {{getvar::wait}}|
		
		/getvar key=genSettings index=inputIsList|
		/let key=inputIsList {{pipe}}|
		/getvar key=genSettings index=inputIsList|
		/let key=outputIsList {{pipe}}|
		
		/setvar key=guidance "The response should be guided toward: {{var::overallOutfit}}"|
		
		/ife ((outputIsList == 'Yes') or (outputIsList == 'Yes')) {:
			/setvar as=array key={{var::variableName}} []|
		:}|
		/else {:
			/setvar as=string key={{var::variableName}} {{noop}}|
		:}|
		//[[Generate with Prompt]]|
		/:"CMC Logic.GenerateWithPrompt"|
		/setvar key={{var::variableName}} {{getvar::output}}|
		
		/addvar key=dataBaseNames {{var::variableName}}|
		/flushvar output|
		/flushvar guidance|
		/flushvar genOrder|
		/flushvar genContent|
		/flushvar genSettings|
	:}|
	/else {:
		/addvar key=dataBaseNames {{var::variableName}}|
	:}|
	//--------|
	
	//Outfit Bottom Description|
	/ife (outfitTop != 'None') {:
		/var key=do No|
		/var key=variableName "outfitBottomDescription"|
		/ife ({{var::variableName}} == '') {:
		    /var key=do Yes|
		:}|
		/elseif (skip == 'Update') {:
		    /getvar key={{var::variableName}}|
		    /buttons labels=["Yes", "No"] Do you want to set or redo {{var::variableName}} (current value: {{pipe}})?|
		    /var key=do {{pipe}}|
		    /ife (do == '') {:
		        /echo Aborting |
		        /abort
		    :}|
		:}|
		/ife ( do == 'Yes' ) {:
			/setvar key=genSettings index=wi_book_key "Outfit Bottom Description"|
			/setvar key=genSettings index=genIsList No|
			/setvar key=genSettings index=inputIsList No|
			/setvar key=genSettings index=inputIsTaskList No|
			/setvar key=genSettings index=genIsSentence Yes|
			/setvar key=genSettings index=needOutput Yes|
			/setvar key=genSettings index=outputIsList No|
			/setvar key=genSettings index=useContext Yes|
			/setvar key=extra []|
			/ife ( appearanceFeatures != 'None') {:
				/addvar key=extra "- Features: {{getvar::appearanceFeatures}}"|
			:}|
			/addvar key=extra "- Body: {{getvar::appearanceBody}}"|
			/setvar key=genSettings index=extraContext {{getvar::extra}}|
			/setvar key=extra []|
			/:"CMC Logic.Get Basic Type Context"|
			/ife (extra != '') {:
				/setvar key=genSettings index=contextKey {{getvar::extra}}|
			:}|
			/flushvar extra|
			/wait {{getvar::wait}}|
			
			/ife (( characterArchetype != 'Human') and ( characterArchetype != 'Android')) {:
				/setvar key=logicBasedInstruction "7. If {{getvar::appearanceFeatures}} includes tails, fur, multiple legs, or digitigrade limbs, describe how {{getvar::outfitBottom}} adapts to the species-specific lower anatomy."|
			:}|
			/elseif (( characterArchetype == 'Human') or ( characterArchetype == 'Android')) {:
				/setvar key=logicBasedInstruction "7. If {{getvar::appearanceFeatures}} includes braces, prosthetics, or assistive gear on the lower body, describe how {{getvar::outfitBottom}} fits or adjusts to accommodate them."|
			:}|
			
			/getvar key=genSettings index=inputIsList|
			/let key=inputIsList {{pipe}}|
			/getvar key=genSettings index=inputIsList|
			/let key=outputIsList {{pipe}}|
			
			/ife ((inputIsList == 'Yes') or (outputIsList == 'Yes')) {:
				/setvar as=array key={{var::variableName}} []|
			:}|
			/else {:
				/setvar as=string key={{var::variableName}} {{noop}}|
			:}|
			//[[Generate with Prompt]]|
			
			/:"CMC Logic.GenerateWithPrompt"|
			/setvar key={{var::variableName}} {{getvar::output}}|
			
			/addvar key=dataBaseNames {{var::variableName}}|
			/flushvar output|
			/flushvar logicBasedInstruction|
			/flushvar guidance|
			/flushvar genOrder|
			/flushvar genContent|
			/flushvar genSettings|
		:}|
		/else {:
			/addvar key=dataBaseNames {{var::variableName}}|
		:}|
	:}|
	/else {:
		/setvar key=outfitBottomDescription None|
		/addvar key=dataBaseNames outfitBottomDescription|
	:}|
	//--------|
	
	//Outfit Legs|
	/var key=do No|
	/var key=variableName "outfitLegs"|
	/ife ({{var::variableName}} == '') {:
	    /var key=do Yes|
	:}|
	/elseif (skip == 'Update') {:
	    /getvar key={{var::variableName}}|
	    /buttons labels=["Yes", "No"] Do you want to set or redo {{var::variableName}} (current value: {{pipe}})?|
	    /var key=do {{pipe}}|
	    /ife (do == '') {:
	        /echo Aborting |
	        /abort
	    :}|
	:}|
	/ife ( do == 'Yes' ) {:
		/setvar key=genSettings index=wi_book_key "Outfit Legwear"|
		/setvar key=genSettings index=genIsList Yes|
		/setvar key=genSettings index=inputIsTaskList No|
		/setvar key=genSettings index=genIsSentence No|
		/setvar key=genSettings index=needOutput Yes|
		/setvar key=genSettings index=outputIsList No|
		/setvar key=genSettings index=useContext Yes|
		/setvar key=extra []|
		/:"CMC Logic.Get Basic Type Context"|
		/ife (extra != '') {:
			/setvar key=genSettings index=contextKey {{getvar::extra}}|
		:}|
		/flushvar extra|
		/wait {{getvar::wait}}|
		
		/getvar key=genSettings index=inputIsList|
		/let key=inputIsList {{pipe}}|
		/getvar key=genSettings index=inputIsList|
		/let key=outputIsList {{pipe}}|
		
		/setvar key=guidance "The response should be guided toward: {{var::overallOutfit}}"|
		
		/ife ((outputIsList == 'Yes') or (outputIsList == 'Yes')) {:
			/setvar as=array key={{var::variableName}} []|
		:}|
		/else {:
			/setvar as=string key={{var::variableName}} {{noop}}|
		:}|
		//[[Generate with Prompt]]|
		/:"CMC Logic.GenerateWithPrompt"|
		/setvar key={{var::variableName}} {{getvar::output}}|
		
		/addvar key=dataBaseNames {{var::variableName}}|
		/flushvar output|
		/flushvar guidance|
		/flushvar genOrder|
		/flushvar genContent|
		/flushvar genSettings|
	:}|
	/else {:
		/addvar key=dataBaseNames {{var::variableName}}|
	:}|
	//--------|
	
	//Outfit Legs Description|
	/ife (outfitLegs != 'None') {:
		/var key=do No|
		/var key=variableName "outfitLegsDescription"|
		/ife ({{var::variableName}} == '') {:
		    /var key=do Yes|
		:}|
		/elseif (skip == 'Update') {:
		    /getvar key={{var::variableName}}|
		    /buttons labels=["Yes", "No"] Do you want to set or redo {{var::variableName}} (current value: {{pipe}})?|
		    /var key=do {{pipe}}|
		    /ife (do == '') {:
		        /echo Aborting |
		        /abort
		    :}|
		:}|
		/ife ( do == 'Yes' ) {:
			/setvar key=genSettings index=wi_book_key "Outfit Legwear Description"|
			/setvar key=genSettings index=genIsList No|
			/setvar key=genSettings index=inputIsList No|
			/setvar key=genSettings index=inputIsTaskList No|
			/setvar key=genSettings index=genIsSentence Yes|
			/setvar key=genSettings index=needOutput Yes|
			/setvar key=genSettings index=outputIsList No|
			/setvar key=genSettings index=useContext Yes|
			/setvar key=extra []|
			/ife ( appearanceFeatures != 'None') {:
				/addvar key=extra "- Features: {{getvar::appearanceFeatures}}"|
			:}|
			/addvar key=extra "- Body: {{getvar::appearanceBody}}"|
			/setvar key=genSettings index=extraContext {{getvar::extra}}|
			/setvar key=extra []|
			/:"CMC Logic.Get Basic Type Context"|
			/ife (extra != '') {:
				/setvar key=genSettings index=contextKey {{getvar::extra}}|
			:}|
			/flushvar extra|
			/wait {{getvar::wait}}|
			
			/ife (( characterArchetype != 'Human') and ( characterArchetype != 'Android')) {:
				/setvar key=logicBasedInstruction "7. If {{getvar::appearanceFeatures}} includes tails, fur, hooves, digitigrade structure, or multiple limbs, describe how {{getvar::outfitLegs}} adjusts to those features in fit or structure."|
			:}|
			/elseif (( characterArchetype == 'Human') or ( characterArchetype == 'Android')) {:
				/setvar key=logicBasedInstruction "7. If {{getvar::appearanceFeatures}} includes prosthetics, braces, or medical support on the legs, mention how {{getvar::outfitLegs}} accommodates or interacts with them."|
			:}|
			
			/getvar key=genSettings index=inputIsList|
			/let key=inputIsList {{pipe}}|
			/getvar key=genSettings index=inputIsList|
			/let key=outputIsList {{pipe}}|
			
			/ife ((inputIsList == 'Yes') or (outputIsList == 'Yes')) {:
				/setvar as=array key={{var::variableName}} []|
			:}|
			/else {:
				/setvar as=string key={{var::variableName}} {{noop}}|
			:}|
			//[[Generate with Prompt]]|
			
			/:"CMC Logic.GenerateWithPrompt"|
			/setvar key={{var::variableName}} {{getvar::output}}|
			
			/addvar key=dataBaseNames {{var::variableName}}|
			/flushvar output|
			/flushvar logicBasedInstruction|
			/flushvar guidance|
			/flushvar genOrder|
			/flushvar genContent|
			/flushvar genSettings|
		:}|
		/else {:
			/addvar key=dataBaseNames {{var::variableName}}|
		:}|
	:}|
	/else {:
		/setvar key=outfitLegsDescription None|
		/addvar key=dataBaseNames outfitLegsDescription|
	:}|
	//--------|
	
	//Outfit Shoes|
	/var key=do No|
	/var key=variableName "outfitShoes"|
	/ife ({{var::variableName}} == '') {:
	    /var key=do Yes|
	:}|
	/elseif (skip == 'Update') {:
	    /getvar key={{var::variableName}}|
	    /buttons labels=["Yes", "No"] Do you want to set or redo {{var::variableName}} (current value: {{pipe}})?|
	    /var key=do {{pipe}}|
	    /ife (do == '') {:
	        /echo Aborting |
	        /abort
	    :}|
	:}|
	/ife ( do == 'Yes' ) {:
		/setvar key=genSettings index=wi_book_key "Outfit Shoes"|
		/setvar key=genSettings index=genIsList Yes|
		/setvar key=genSettings index=inputIsTaskList No|
		/setvar key=genSettings index=genIsSentence No|
		/setvar key=genSettings index=needOutput Yes|
		/setvar key=genSettings index=outputIsList No|
		/setvar key=genSettings index=useContext Yes|
		/setvar key=extra []|
		/:"CMC Logic.Get Basic Type Context"|
		/ife (extra != '') {:
			/setvar key=genSettings index=contextKey {{getvar::extra}}|
		:}|
		/flushvar extra|
		/wait {{getvar::wait}}|
		
		/getvar key=genSettings index=inputIsList|
		/let key=inputIsList {{pipe}}|
		/getvar key=genSettings index=inputIsList|
		/let key=outputIsList {{pipe}}|
		
		/setvar key=guidance "The response should be guided toward: {{var::overallOutfit}}"|
		
		/ife ((outputIsList == 'Yes') or (outputIsList == 'Yes')) {:
			/setvar as=array key={{var::variableName}} []|
		:}|
		/else {:
			/setvar as=string key={{var::variableName}} {{noop}}|
		:}|
		//[[Generate with Prompt]]|
		/:"CMC Logic.GenerateWithPrompt"|
		/setvar key={{var::variableName}} {{getvar::output}}|
		
		/addvar key=dataBaseNames {{var::variableName}}|
		/flushvar output|
		/flushvar guidance|
		/flushvar genOrder|
		/flushvar genContent|
		/flushvar genSettings|
	:}|
	/else {:
		/addvar key=dataBaseNames {{var::variableName}}|
	:}|
	//--------|
	
	//Outfit Shoes Description|
	/ife (outfitShoes != 'None') {:
		/var key=do No|
		/var key=variableName "outfitShoesDescription"|
		/ife ({{var::variableName}} == '') {:
		    /var key=do Yes|
		:}|
		/elseif (skip == 'Update') {:
		    /getvar key={{var::variableName}}|
		    /buttons labels=["Yes", "No"] Do you want to set or redo {{var::variableName}} (current value: {{pipe}})?|
		    /var key=do {{pipe}}|
		    /ife (do == '') {:
		        /echo Aborting |
		        /abort
		    :}|
		:}|
		/ife ( do == 'Yes' ) {:
			/setvar key=genSettings index=wi_book_key "Outfit Shoes Description"|
			/setvar key=genSettings index=genIsList No|
			/setvar key=genSettings index=inputIsList No|
			/setvar key=genSettings index=inputIsTaskList No|
			/setvar key=genSettings index=genIsSentence Yes|
			/setvar key=genSettings index=needOutput Yes|
			/setvar key=genSettings index=outputIsList No|
			/setvar key=genSettings index=useContext Yes|
			/setvar key=extra []|
			/ife ( appearanceFeatures != 'None') {:
				/addvar key=extra "- Features: {{getvar::appearanceFeatures}}"|
			:}|
			/addvar key=extra "- Body: {{getvar::appearanceBody}}"|
			/setvar key=genSettings index=extraContext {{getvar::extra}}|
			/setvar key=extra []|
			/:"CMC Logic.Get Basic Type Context"|
			/ife (extra != '') {:
				/setvar key=genSettings index=contextKey {{getvar::extra}}|
			:}|
			/flushvar extra|
			/wait {{getvar::wait}}|
			
			/ife (( characterArchetype != 'Human') and ( characterArchetype != 'Android')) {:
				/setvar key=logicBasedInstruction "7. If {{getvar::appearanceFeatures}} includes paws, claws, hooves, or digitigrade limbs, describe how {{getvar::outfitShoes}} adjusts to their non-human foot structure."|
			:}|
			/elseif (( characterArchetype == 'Human') or ( characterArchetype == 'Android')) {:
				/setvar key=logicBasedInstruction "7. If {{getvar::appearanceFeatures}} includes prosthetics or corrective devices, describe how {{getvar::outfitShoes}} accommodates or enhances support."|
			:}|
			
			/getvar key=genSettings index=inputIsList|
			/let key=inputIsList {{pipe}}|
			/getvar key=genSettings index=inputIsList|
			/let key=outputIsList {{pipe}}|
			
			/ife ((inputIsList == 'Yes') or (outputIsList == 'Yes')) {:
				/setvar as=array key={{var::variableName}} []|
			:}|
			/else {:
				/setvar as=string key={{var::variableName}} {{noop}}|
			:}|
			//[[Generate with Prompt]]|
			
			/:"CMC Logic.GenerateWithPrompt"|
			/setvar key={{var::variableName}} {{getvar::output}}|
			
			/addvar key=dataBaseNames {{var::variableName}}|
			/flushvar output|
			/flushvar logicBasedInstruction|
			/flushvar guidance|
			/flushvar genOrder|
			/flushvar genContent|
			/flushvar genSettings|
		:}|
		/else {:
			/addvar key=dataBaseNames {{var::variableName}}|
		:}|
	:}|
	/else {:
		/setvar key=outfitShoesDescription None|
		/addvar key=dataBaseNames outfitShoesDescription|
	:}|
	//--------|
	
	/ife (breasts != 'None') {:
		//Outfit Underwear (Top)|
		/var key=do No|
		/var key=variableName "outfitUnderwearTop"|
		/ife ({{var::variableName}} == '') {:
		    /var key=do Yes|
		:}|
		/elseif (skip == 'Update') {:
		    /getvar key={{var::variableName}}|
		    /buttons labels=["Yes", "No"] Do you want to set or redo {{var::variableName}} (current value: {{pipe}})?|
		    /var key=do {{pipe}}|
		    /ife (do == '') {:
		        /echo Aborting |
		        /abort
		    :}|
		:}|
		/ife ( do == 'Yes' ) {:
			/setvar key=genSettings index=wi_book_key "Outfit Underwear Top"|
			/setvar key=genSettings index=genIsList Yes|
			/setvar key=genSettings index=inputIsTaskList No|
			/setvar key=genSettings index=genIsSentence No|
			/setvar key=genSettings index=needOutput Yes|
			/setvar key=genSettings index=outputIsList No|
			/setvar key=genSettings index=useContext Yes|
			/setvar key=extra []|
			/:"CMC Logic.Get Basic Type Context"|
			/ife (extra != '') {:
				/setvar key=genSettings index=contextKey {{getvar::extra}}|
			:}|
			/flushvar extra|
			/wait {{getvar::wait}}|
			
			/getvar key=genSettings index=inputIsList|
			/let key=inputIsList {{pipe}}|
			/getvar key=genSettings index=inputIsList|
			/let key=outputIsList {{pipe}}|
			
			/setvar key=guidance "The response should be guided toward: {{var::overallOutfit}}"|
			
			/ife ((outputIsList == 'Yes') or (outputIsList == 'Yes')) {:
				/setvar as=array key={{var::variableName}} []|
			:}|
			/else {:
				/setvar as=string key={{var::variableName}} {{noop}}|
			:}|
			//[[Generate with Prompt]]|
			/:"CMC Logic.GenerateWithPrompt"|
			/setvar key={{var::variableName}} {{getvar::output}}|
			
			/addvar key=dataBaseNames {{var::variableName}}|
			/flushvar output|
			/flushvar guidance|
			/flushvar genOrder|
			/flushvar genContent|
			/flushvar genSettings|
		:}|
		/else {:
			/addvar key=dataBaseNames {{var::variableName}}|
		:}|
		//--------|
		
		//Outfit Underwear (Top) Description|
		/ife (outfitLegs != 'None') {:
			/var key=do No|
			/var key=variableName "outfitUnderwearTopDescription"|
			/ife ({{var::variableName}} == '') {:
			    /var key=do Yes|
			:}|
			/elseif (skip == 'Update') {:
			    /getvar key={{var::variableName}}|
			    /buttons labels=["Yes", "No"] Do you want to set or redo {{var::variableName}} (current value: {{pipe}})?|
			    /var key=do {{pipe}}|
			    /ife (do == '') {:
			        /echo Aborting |
			        /abort
			    :}|
			:}|
			/ife ( do == 'Yes' ) {:
				/setvar key=genSettings index=wi_book_key "Outfit Underwear Top Description"|
				/setvar key=genSettings index=genIsList No|
				/setvar key=genSettings index=inputIsList No|
				/setvar key=genSettings index=inputIsTaskList No|
				/setvar key=genSettings index=genIsSentence Yes|
				/setvar key=genSettings index=needOutput Yes|
				/setvar key=genSettings index=outputIsList No|
				/setvar key=genSettings index=useContext Yes|
				/setvar key=extra []|
				/ife ( appearanceFeatures != 'None') {:
					/addvar key=extra "- Features: {{getvar::appearanceFeatures}}"|
				:}|
				/addvar key=extra "- Body: {{getvar::appearanceBody}}"|
				/ife ( appearanceBreasts != 'None') {:
					/addvar key=extra "- Breasts: {{getvar::appearanceBreasts}}"|
				:}|
				/setvar key=genSettings index=extraContext {{getvar::extra}}|
				/setvar key=extra []|
				/:"CMC Logic.Get Basic Type Context"|
				/ife (extra != '') {:
					/setvar key=genSettings index=contextKey {{getvar::extra}}|
				:}|
				/flushvar extra|
				/wait {{getvar::wait}}|
				
				/ife (( characterArchetype != 'Human') and ( characterArchetype != 'Android')) {:
					/setvar key=logicBasedInstruction "7. If {{getvar::appearanceFeatures}} includes fur, scales, extra limbs, or an unusual torso shape, describe how {{getvar::outfitUnderwearTop}} adapts to or works with these features."|
				:}|
				/elseif (( characterArchetype == 'Human') or ( characterArchetype == 'Android')) {:
					/setvar key=logicBasedInstruction "7. If {{getvar::appearanceFeatures}} includes medical gear, scars, or prosthetics, note how {{getvar::outfitUnderwearTop}} provides comfort or coverage in those areas."|
				:}|
				
				/getvar key=genSettings index=inputIsList|
				/let key=inputIsList {{pipe}}|
				/getvar key=genSettings index=inputIsList|
				/let key=outputIsList {{pipe}}|
				
				/ife ((inputIsList == 'Yes') or (outputIsList == 'Yes')) {:
					/setvar as=array key={{var::variableName}} []|
				:}|
				/else {:
					/setvar as=string key={{var::variableName}} {{noop}}|
				:}|
				//[[Generate with Prompt]]|
				
				/:"CMC Logic.GenerateWithPrompt"|
				/setvar key={{var::variableName}} {{getvar::output}}|
				
				/addvar key=dataBaseNames {{var::variableName}}|
				/flushvar output|
				/flushvar logicBasedInstruction|
				/flushvar guidance|
				/flushvar genOrder|
				/flushvar genContent|
				/flushvar genSettings|
			:}|
			/else {:
				/addvar key=dataBaseNames {{var::variableName}}|
			:}|
		:}|
		/else {:
			/setvar key=outfitUnderwearTopDescription None|
			/addvar key=dataBaseNames outfitUnderwearTopDescription|
		:}|
		//--------|
	:}|
	/else {:
		/setvar key=outfitUnderwearTop Skip|
		/setvar key=outfitUnderwearTopDescription Skip|
		/addvar key=dataBaseNames outfitUnderwearTop|
		/addvar key=dataBaseNames outfitUnderwearTopDescription|
	:}|
	
	//Outfit Underwear (Bottom)|
	/var key=do No|
	/var key=variableName "outfitUnderwearBottom"|
	/ife ({{var::variableName}} == '') {:
	    /var key=do Yes|
	:}|
	/elseif (skip == 'Update') {:
	    /getvar key={{var::variableName}}|
	    /buttons labels=["Yes", "No"] Do you want to set or redo {{var::variableName}} (current value: {{pipe}})?|
	    /var key=do {{pipe}}|
	    /ife (do == '') {:
	        /echo Aborting |
	        /abort
	    :}|
	:}|
	/ife ( do == 'Yes' ) {:
		/setvar key=genSettings index=wi_book_key "Outfit Underwear Bottom"|
		/setvar key=genSettings index=genIsList Yes|
		/setvar key=genSettings index=inputIsTaskList No|
		/setvar key=genSettings index=genIsSentence No|
		/setvar key=genSettings index=needOutput Yes|
		/setvar key=genSettings index=outputIsList No|
		/setvar key=genSettings index=useContext Yes|
		/setvar key=extra []|
		/:"CMC Logic.Get Basic Type Context"|
		/ife (extra != '') {:
			/setvar key=genSettings index=contextKey {{getvar::extra}}|
		:}|
		/flushvar extra|
		/wait {{getvar::wait}}|
		
		/getvar key=genSettings index=inputIsList|
		/let key=inputIsList {{pipe}}|
		/getvar key=genSettings index=inputIsList|
		/let key=outputIsList {{pipe}}|
		
		/setvar key=guidance "The response should be guided toward: {{var::overallOutfit}}"|
		
		/ife ((outputIsList == 'Yes') or (outputIsList == 'Yes')) {:
			/setvar as=array key={{var::variableName}} []|
		:}|
		/else {:
			/setvar as=string key={{var::variableName}} {{noop}}|
		:}|
		//[[Generate with Prompt]]|
		/:"CMC Logic.GenerateWithPrompt"|
		/setvar key={{var::variableName}} {{getvar::output}}|
		
		/addvar key=dataBaseNames {{var::variableName}}|
		/flushvar output|
		/flushvar guidance|
		/flushvar genOrder|
		/flushvar genContent|
		/flushvar genSettings|
	:}|
	/else {:
		/addvar key=dataBaseNames {{var::variableName}}|
	:}|
	//--------|
	
	//Outfit Underwear (Bottom) Description|
	/ife (outfitUnderwearBottom != 'None') {:
		/var key=do No|
		/var key=variableName "outfitUnderwearBottomDescription"|
		/ife ({{var::variableName}} == '') {:
		    /var key=do Yes|
		:}|
		/elseif (skip == 'Update') {:
		    /getvar key={{var::variableName}}|
		    /buttons labels=["Yes", "No"] Do you want to set or redo {{var::variableName}} (current value: {{pipe}})?|
		    /var key=do {{pipe}}|
		    /ife (do == '') {:
		        /echo Aborting |
		        /abort
		    :}|
		:}|
		/ife ( do == 'Yes' ) {:
			/setvar key=genSettings index=wi_book_key "Outfit Underwear Bottom Description"|
			/setvar key=genSettings index=genIsList No|
			/setvar key=genSettings index=inputIsList No|
			/setvar key=genSettings index=inputIsTaskList No|
			/setvar key=genSettings index=genIsSentence Yes|
			/setvar key=genSettings index=needOutput Yes|
			/setvar key=genSettings index=outputIsList No|
			/setvar key=genSettings index=useContext Yes|
			/setvar key=extra []|
			/ife ( appearanceFeatures != 'None') {:
				/addvar key=extra "- Features: {{getvar::appearanceFeatures}}"|
			:}|
			/addvar key=extra "- Body: {{getvar::appearanceBody}}"|
			/setvar key=genSettings index=extraContext {{getvar::extra}}|
			/setvar key=extra []|
			/:"CMC Logic.Get Basic Type Context"|
			/ife (extra != '') {:
				/setvar key=genSettings index=contextKey {{getvar::extra}}|
			:}|
			/flushvar extra|
			/wait {{getvar::wait}}|
			
			/ife (( characterArchetype != 'Human') and ( characterArchetype != 'Android')) {:
				/setvar key=logicBasedInstruction "7. If {{getvar::appearanceFeatures}} includes tails, fur, digitigrade legs, extra limbs, or tauric anatomy, mention how {{getvar::outfitUnderwearBottom}} accommodates or wraps around them."|
			:}|
			/elseif (( characterArchetype == 'Human') or ( characterArchetype == 'Android')) {:
				/setvar key=logicBasedInstruction "7. If {{getvar::appearanceFeatures}} includes scars, braces, or prosthetics around the hips or legs, describe how {{getvar::outfitUnderwearBottom}} adjusts or provides comfort."|
			:}|
			
			/getvar key=genSettings index=inputIsList|
			/let key=inputIsList {{pipe}}|
			/getvar key=genSettings index=inputIsList|
			/let key=outputIsList {{pipe}}|
			
			/ife ((inputIsList == 'Yes') or (outputIsList == 'Yes')) {:
				/setvar as=array key={{var::variableName}} []|
			:}|
			/else {:
				/setvar as=string key={{var::variableName}} {{noop}}|
			:}|
			//[[Generate with Prompt]]|
			
			/:"CMC Logic.GenerateWithPrompt"|
			/setvar key={{var::variableName}} {{getvar::output}}|
			
			/addvar key=dataBaseNames {{var::variableName}}|
			/flushvar output|
			/flushvar logicBasedInstruction|
			/flushvar guidance|
			/flushvar genOrder|
			/flushvar genContent|
			/flushvar genSettings|
		:}|
		/else {:
			/addvar key=dataBaseNames {{var::variableName}}|
		:}|
	:}|
	/else {:
		/setvar key=outfitUnderwearBottomDescription None|
		/addvar key=dataBaseNames outfitUnderwearBottomDescription|
	:}|
	//--------|
	
	/setvar key=outfit []|
	/addvar key=outfit "{{getvar::outfitHeadDescription}}"|
	/addvar key=outfit "{{getvar::parsedAccessories}}"|
	/addvar key=outfit "{{getvar::parsedMakeup}}"|
	/addvar key=outfit "{{getvar::outfitNeckDescription}}"|
	/addvar key=outfit "{{getvar::outfitTopDescription}}"|
	/addvar key=outfit "{{getvar::outfitBottomDescription}}"|
	/addvar key=outfit "{{getvar::outfitLegsDescription}}"|
	/addvar key=outfit "{{getvar::outfitShoesDescription}}"|
	/ife (outfitUnderwearTopDescription != 'Skip') {:
		/addvar key=outfit "{{getvar::outfitUnderwearTopDescription}}"|
	:}|
	/addvar key=outfit "{{getvar::outfitUnderwearBottomDescription}}"|
	
	/ifempty value={{getvar::outfits}} {{noop}}|
	/var key=outfitsCheck {{pipe}}|
	/ife (outfitsCheck == '') {:
		/setvar key=outfits index="Main Outfit" {{getvar::outfit}}|
	:}|
	/else {:
		/input What would you like to call this outfit?|
		/let key=outfitName {{pipe}}|
		/setvar key=outfits index={{var::outfitName}} {{getvar::outfit}}|
	:}|
	/*
	/buttons labels=["Yes", "No"] Do you want to add more outfits?|
	/setvar key=outfitsDone {{pipe}}|
	/ife ( outfitsDone == ''){:
		/echo Aborting |
		/abort
	:}|
	*|
	/setvar key=outfitsDone No|
:}|

/:"CMC Logic.JEDParse"|

/:"CMC Logic.Save DataBase"|

/setvar key=stepDone Yes|
/qr-list CMC Main|
/getat index=1 {{pipe}}|
/var qrlabel {{pipe}}|
/qr-get set="CMC Main" label={{var::qrlabel}}|
/getat index="message" {{pipe}}|
/qr-update set="CMC Main" label={{var::qrlabel}} newlabel="Start Generating Mental Traits & Personality" {{pipe}}|
/forcesave|