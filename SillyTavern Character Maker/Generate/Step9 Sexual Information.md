/qr-list CMC Main|
/getat index=1 {{pipe}}|
/let qrlabel {{pipe}}|
/qr-get set="CMC Main" label={{var::qrlabel}}|
/getat index="message" {{pipe}}|
/qr-update set="CMC Main" label={{var::qrlabel}} newlabel="Continue Generating Sexual Information" {{pipe}}|

/:"CMC Logic.Get Char info"|

/setvar key=dataBaseNames []|
/flushvar genSettings|

/setvar key=stepVar Step9|

/setvar key=skip Update|
/ife ( stepDone == 'No') {:
	/buttons labels=["Skip", "Update"] Do you want to skip or update already generated content? You will get a question for each already done if you select Update.|
	/setvar key=skip {{pipe}}|
	/ife ( skip == ''){:
		/echo Aborting |
		/abort
	:}|
:}|

/setvar key=stepDone No|

/let key=do {{noop}}|
/let key=variableName {{noop}}|
/let selected_btn {{noop}}|

//Sexual Orientation|
/var key=do No|
/var key=variableName "sexualOrientation"|
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
	/setvar key=genSettings {}|
	/setvar key=genSettings index=wi_book_key "Sexual Orientation"|
	/setvar key=genSettings index=combineLorebookEntries No|
	/setvar key=genSettings index=genIsSentence No|
	/setvar key=genSettings index=inputIsList No|
	/setvar key=genSettings index=genIsList Yes|
	/setvar key=genSettings index=outputIsList No|
	/setvar key=genSettings index=needOutput Yes|
	/setvar key=genSettings index=useContext No|
	/wait {{getvar::wait}}|
	
	
	/getvar key=genSettings index=wi_book_key|
	/let key=wi_book_key {{pipe}}|
	/getvar key=genSettings index=inputIsList|
	/let key=inputIsList {{pipe}}|
	/getvar key=genSettings index=combineLorebookEntries|
	/let key=combineLorebookEntries {{pipe}}|
	
	
	/ife ( inputIsList == 'Yes') {:
		/setvar key={{var::variableName}} []|
		/ife ( combineLorebookEntries == 'Yes') {:
			/:"CMC Logic.Combine List Lorebooks"
		:}|
		/foreach {{getvar::genOrder}} {:
			/setvar key=it {{var::item}}|
			/getat index={{var::index}} {{var::genOrderContent}} |
			/setvar key=genSettings index=content {{pipe}}|
			/:"CMC Logic.GenerateWithSelector"|
			/ife (output != '') {:
				/addvar key={{var::variableName}} {{getvar::output}}|
			:}|
		:}|
	:}|
	/else {:
		/getvar key=genSettings index=wi_book_key|
		/setvar key=it {{pipe}}|
		/:"CMC Logic.GenerateWithSelector"|
		/ife (output != '') {:
			/setvar key={{var::variableName}} {{getvar::output}}|
		:}|
		
	:}|
	/addvar key=dataBaseNames {{var::variableName}}|
	/flushvar output|
	/flushvar genOrder|
	/flushvar genContent|
	/flushvar it|
	/flushvar genSettings|
:}|
/else {:
	/addvar key=dataBaseNames {{var::variableName}}|
:}|

/var key=do No|
/var key=variableName "sexualOrientationExplanation"|
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
	/setvar key=genSettings {}|
	/setvar key=genSettings index=wi_book_key "Sexual Orientation Explanation"|
	/setvar key=genSettings index=genIsList No|
	
	/setvar key=genSettings index=genIsSentence Yes|
	/setvar key=genSettings index=needOutput Yes|
	/setvar key=genSettings index=outputIsList No|
	/setvar key=genSettings index=useContext Yes|
	/setvar key=extra []|
	/addvar key=extra "- Setting Type: {{getvar::settingType}}"|
	/addvar key=extra "- Backstory: {{getvar::backstory}}"|
	/ife (user == 'Yes') {:
		/addvar key=extra "- User's Role: {{getvar::userRole}}"|
	:}|
	/addvar key=extra "- Main Personality Trait: {{getvar::personalityMainTrait}}"|
	/addvar key=extra "- Personality Tags: {{getvar::personalityFoundTags}}, {{getvar::personalityTags}}"|
	/setvar key=genSettings index=extraContext {{getvar::extra}}|
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
	
	
	/setvar key=logicBasedInstruction {{noop}}|
	/setvar key=x 8|
	
	/ife (sexualOrientation == 'Heterosexual') {:
		/incvar x|
		/ife ( logicBasedInstruction != '') {:
			/addvar key=logicBasedInstruction {{newline}}|
		:}|
		/addvar key=logicBasedInstruction "{{getvar::x}}. Focus attraction toward the opposite sex — emphasize traditionally masculine or feminine traits depending on character’s gender and age."|
		
	:}|
	/elseif (sexualOrientation == 'Pansexual') {:
		/incvar x|
		/ife ( logicBasedInstruction != '') {:
			/addvar key=logicBasedInstruction {{newline}}|
		:}|
		/addvar key=logicBasedInstruction "{{getvar::x}}. Describe attraction to a broad range of gender expressions or bodies — avoid reducing attraction to a binary or to one physical archetype."|
		
	:}|
	/elseif (sexualOrientation == 'Asexual') {:
		/incvar x|
		/ife ( logicBasedInstruction != '') {:
			/addvar key=logicBasedInstruction {{newline}}|
		:}|
		/addvar key=logicBasedInstruction "{{getvar::x}}. Emphasize lack of innate sexual attraction; describe emotional or aesthetic triggers only if relevant."|
		/incvar x|
		/ife ( logicBasedInstruction != '') {:
			/addvar key=logicBasedInstruction {{newline}}|
		:}|
		/addvar key=logicBasedInstruction "{{getvar::x}}. Describe how attraction requires deep bonding, or what is **not** felt."|
		
	:}|
	/elseif (sexualOrientation == 'Demisexual') {:
		/incvar x|
		/ife ( logicBasedInstruction != '') {:
			/addvar key=logicBasedInstruction {{newline}}|
		:}|
		/addvar key=logicBasedInstruction "{{getvar::x}}. Attraction must require **deep emotional connection** before any physical or sexual interest is felt."|
		/incvar x|
		/ife ( logicBasedInstruction != '') {:
			/addvar key=logicBasedInstruction {{newline}}|
		:}|
		/addvar key=logicBasedInstruction "{{getvar::x}}. Describe how attraction requires deep bonding, or what is **not** felt."|
		
	:}|
	/elseif (sexualOrientation == 'Bi-curious') {:
		/incvar x|
		/ife ( logicBasedInstruction != '') {:
			/addvar key=logicBasedInstruction {{newline}}|
		:}|
		/addvar key=logicBasedInstruction "{{getvar::x}}. Express curiosity or tentative interest in same-gender or non-typical partners — use uncertain or exploratory language."|
		
	:}|
	/elseif (sexualOrientation == 'Xenosexual') {:
		/incvar x|
		/ife ( logicBasedInstruction != '') {:
			/addvar key=logicBasedInstruction {{newline}}|
		:}|
		/addvar key=logicBasedInstruction "{{getvar::x}}. Attraction should focus on **non-human humanoid** or **hybrid forms** (e.g., beastkin, aliens, demi-humans). Highlight features like mixed anatomy, unusual physiology, or hybrid charm — avoid feral or quadrupedal attraction."|
		
	:}|
	/elseif (sexualOrientation == 'Zoosexual') {:
		/incvar x|
		/ife ( logicBasedInstruction != '') {:
			/addvar key=logicBasedInstruction {{newline}}|
		:}|
		/addvar key=logicBasedInstruction "{{getvar::x}}. Attraction should be directed toward **fully animalistic**, **feral**, or **quadrupedal bodies**. Emphasize instinctual behavior, physical traits (e.g., fur, gait, size), or dominance/submission cues — avoid humanoid references."|
		
	:}|
	
	
	/ife ((settingType == 'Realistic') and (sexualOrientation != 'Zoosexual') and (sexualOrientation != 'Xenosexual')) {:
		/incvar x|
		/ife ( logicBasedInstruction != '') {:
			/addvar key=logicBasedInstruction {{newline}}|
		:}|
		/addvar key=logicBasedInstruction "{{getvar::x}}. Avoid references to alien, hybrid, or feral attraction unless justified by species context. Keep tone grounded in biologically plausible preferences."|
		
	:}|
	/flushvar x|
	
	
	/ife ((inputIsList == 'Yes') or (outputIsList == 'Yes')) {:
		/setvar as=array key={{var::variableName}} []|
	:}|
	/else {:
		/setvar as=string key={{var::variableName}} {{noop}}|
	:}|
	//[[Generate with Prompt]]|
	/ife (inputIsList == 'Yes') {:
		/foreach {{getvar::CHANGE/REMOVE_THIS}} {:
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
	/flushvar guidance|
	/flushvar genOrder|
	/flushvar genContent|
	/flushvar genSettings|
:}|
/else {:
	/addvar key=dataBaseNames {{var::variableName}}|
:}|
//--------|

//Sexual Role|
/var key=do No|
/var key=variableName "sexualRole"|
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
	/setvar key=genSettings {}|
	/setvar key=genSettings index=wi_book_key "Sexual Role"|
	/setvar key=genSettings index=combineLorebookEntries No|
	/setvar key=genSettings index=genIsSentence No|
	/setvar key=genSettings index=inputIsList No|
	/setvar key=genSettings index=genIsList Yes|
	/setvar key=genSettings index=outputIsList No|
	/setvar key=genSettings index=needOutput No|
	/setvar key=genSettings index=useContext No|
	/wait {{getvar::wait}}|
	
	
	/getvar key=genSettings index=wi_book_key|
	/let key=wi_book_key {{pipe}}|
	/getvar key=genSettings index=inputIsList|
	/let key=inputIsList {{pipe}}|
	/getvar key=genSettings index=combineLorebookEntries|
	/let key=combineLorebookEntries {{pipe}}|
	
	
	/ife ( inputIsList == 'Yes') {:
		/setvar key={{var::variableName}} []|
		/ife ( combineLorebookEntries == 'Yes') {:
			/:"CMC Logic.Combine List Lorebooks"
		:}|
		/foreach {{getvar::genOrder}} {:
			/setvar key=it {{var::item}}|
			/getat index={{var::index}} {{var::genOrderContent}} |
			/setvar key=genSettings index=content {{pipe}}|
			/:"CMC Logic.GenerateWithSelector"|
			/ife (output != '') {:
				/addvar key={{var::variableName}} {{getvar::output}}|
			:}|
		:}|
	:}|
	/else {:
		/getvar key=genSettings index=wi_book_key|
		/setvar key=it {{pipe}}|
		/:"CMC Logic.GenerateWithSelector"|
		/ife (output != '') {:
			/setvar key={{var::variableName}} {{getvar::output}}|
		:}|
		
	:}|
	/addvar key=dataBaseNames {{var::variableName}}|
	/flushvar output|
	/flushvar genOrder|
	/flushvar genContent|
	/flushvar it|
	/flushvar genSettings|
:}|
/else {:
	/addvar key=dataBaseNames {{var::variableName}}|
:}|

/var key=do No|
/var key=variableName "sexualRoleExplanation"|
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
	/setvar key=genSettings {}|
	/setvar key=genSettings index=wi_book_key "Sexual Role Explanation"|
	/setvar key=genSettings index=genIsList No|
	
	/setvar key=genSettings index=genIsSentence Yes|
	/setvar key=genSettings index=needOutput Yes|
	/setvar key=genSettings index=outputIsList No|
	/setvar key=genSettings index=useContext Yes|
	/setvar key=extra []|
	/addvar key=extra "- Setting Type: {{getvar::settingType}}"|
	/addvar key=extra "- Backstory: {{getvar::backstory}}"|
	/ife (user == 'Yes') {:
		/addvar key=extra "- User's Role: {{getvar::userRole}}"|
	:}|
	/addvar key=extra "- Main Personality Trait: {{getvar::personalityMainTrait}}"| 
	/addvar key=extra "- Personality Tags: {{getvar::personalityFoundTags}}, {{getvar::personalityTags}}"|
	/addvar key=extra "- Sexual Orientation: {{getvar::sexualOrientation}}"|
	/addvar key=extra "- Orientation Explanation: {{getvar::sexualOrientationExplanation}}"|
	/setvar key=genSettings index=extraContext {{getvar::extra}}|
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
	
	
	/setvar key=logicBasedInstruction {{noop}}|
	/setvar key=x 7|
	
	/ife (sexualRole == 'Dominant') {:
		/incvar x|
		/ife ( logicBasedInstruction != '') {:
			/addvar key=logicBasedInstruction {{newline}}|
		:}|
		/addvar key=logicBasedInstruction "{{getvar::x}}. Character must take control during intimacy — they lead, direct, and handle their partner confidently."|
		/incvar x|
		/ife ( logicBasedInstruction != '') {:
			/addvar key=logicBasedInstruction {{newline}}|
		:}|
		/addvar key=logicBasedInstruction "{{getvar::x}}. Show active physical or verbal dominance (e.g., restraint, commands, assertive touch)."|
		/incvar x|
		/ife ( logicBasedInstruction != '') {:
			/addvar key=logicBasedInstruction {{newline}}|
		:}|
		/addvar key=logicBasedInstruction "{{getvar::x}}. Personality tags may affect tone (e.g., cold, nurturing, aggressive), but role remains in control."|
		
	:}|
	/elseif (sexualRole == 'Top') {:
		/incvar x|
		/ife ( logicBasedInstruction != '') {:
			/addvar key=logicBasedInstruction {{newline}}|
		:}|
		/addvar key=logicBasedInstruction "{{getvar::x}}. Character takes the physically active or giving role during sex, initiating contact or stimulation."|
		/incvar x|
		/ife ( logicBasedInstruction != '') {:
			/addvar key=logicBasedInstruction {{newline}}|
		:}|
		/addvar key=logicBasedInstruction "{{getvar::x}}. May or may not control dynamics — focus on action and assertive engagement."|
		/incvar x|
		/ife ( logicBasedInstruction != '') {:
			/addvar key=logicBasedInstruction {{newline}}|
		:}|
		/addvar key=logicBasedInstruction "{{getvar::x}}. Tags like playful, impatient, or intense may shape *how* they act, not whether they do."|
		
	:}|
	/elseif (sexualRole == 'Submissive') {:
		/incvar x|
		/ife ( logicBasedInstruction != '') {:
			/addvar key=logicBasedInstruction {{newline}}|
		:}|
		/addvar key=logicBasedInstruction "{{getvar::x}}. Character must yield control and respond to a dominant partner’s actions or guidance."|
		/incvar x|
		/ife ( logicBasedInstruction != '') {:
			/addvar key=logicBasedInstruction {{newline}}|
		:}|
		/addvar key=logicBasedInstruction "{{getvar::x}}. Show willingness to follow, wait, or obey — describe receptive body language or behavior."|
		/incvar x|
		/ife ( logicBasedInstruction != '') {:
			/addvar key=logicBasedInstruction {{newline}}|
		:}|
		/addvar key=logicBasedInstruction "{{getvar::x}}. Tags may affect how passivity is expressed (e.g., shy, eager, stoic), but they should not lead."|
		
	:}|
	/elseif (sexualRole == 'Bottom') {:
		/incvar x|
		/ife ( logicBasedInstruction != '') {:
			/addvar key=logicBasedInstruction {{newline}}|
		:}|
		/addvar key=logicBasedInstruction "{{getvar::x}}. Character takes a physically passive or receiving role — they are touched, penetrated, or held."|
		/incvar x|
		/ife ( logicBasedInstruction != '') {:
			/addvar key=logicBasedInstruction {{newline}}|
		:}|
		/addvar key=logicBasedInstruction "{{getvar::x}}. May be sexually assertive in tone or feedback, but should not initiate or guide."|
		/incvar x|
		/ife ( logicBasedInstruction != '') {:
			/addvar key=logicBasedInstruction {{newline}}|
		:}|
		/addvar key=logicBasedInstruction "{{getvar::x}}. Tags should shape *emotional reaction* or tone of passivity (e.g., needy, playful, tense)."|
		
	:}|
	/elseif (sexualRole == 'Switch') {:
		/incvar x|
		/ife ( logicBasedInstruction != '') {:
			/addvar key=logicBasedInstruction {{newline}}|
		:}|
		/addvar key=logicBasedInstruction "{{getvar::x}}. Character is flexible — describe adaptive behavior that shifts based on mood or partner energy."|
		/incvar x|
		/ife ( logicBasedInstruction != '') {:
			/addvar key=logicBasedInstruction {{newline}}|
		:}|
		/addvar key=logicBasedInstruction "{{getvar::x}}. Show role fluidity: confident control in one moment, eager submission in the next."|
		/incvar x|
		/ife ( logicBasedInstruction != '') {:
			/addvar key=logicBasedInstruction {{newline}}|
		:}|
		/addvar key=logicBasedInstruction "{{getvar::x}}. Tags can influence preference or transitions (e.g., impulsive = faster switching)."|
		
	:}|
	/elseif (sexualRole == 'Service Top') {:
		/incvar x|
		/ife ( logicBasedInstruction != '') {:
			/addvar key=logicBasedInstruction {{newline}}|
		:}|
		/addvar key=logicBasedInstruction "{{getvar::x}}. Character takes an active role, but their focus is on fulfilling their partner’s needs or preferences — not on dominance."|
		/incvar x|
		/ife ( logicBasedInstruction != '') {:
			/addvar key=logicBasedInstruction {{newline}}|
		:}|
		/addvar key=logicBasedInstruction "{{getvar::x}}. Use actions like initiating stimulation or adjusting pace for the other’s benefit."|
		/incvar x|
		/ife ( logicBasedInstruction != '') {:
			/addvar key=logicBasedInstruction {{newline}}|
		:}|
		/addvar key=logicBasedInstruction "{{getvar::x}}. Tags may reflect devotion, calm precision, or eager support — never controlling ego."|
		
	:}|
	/elseif (sexualRole == 'Power Bottom') {:
		/incvar x|
		/ife ( logicBasedInstruction != '') {:
			/addvar key=logicBasedInstruction {{newline}}|
		:}|
		/addvar key=logicBasedInstruction "{{getvar::x}}. Character is physically submissive but emotionally or behaviorally assertive."|
		/incvar x|
		/ife ( logicBasedInstruction != '') {:
			/addvar key=logicBasedInstruction {{newline}}|
		:}|
		/addvar key=logicBasedInstruction "{{getvar::x}}. Describe how they guide the encounter from below: giving feedback, demanding more, controlling pace from a passive position."|
		/incvar x|
		/ife ( logicBasedInstruction != '') {:
			/addvar key=logicBasedInstruction {{newline}}|
		:}|
		/addvar key=logicBasedInstruction "{{getvar::x}}. Tags should enhance their bold, teasing, or confident tone without contradicting positional passivity."|
		
	:}|
	/elseif (sexualRole == 'Soft Dom') {:
		/incvar x|
		/ife ( logicBasedInstruction != '') {:
			/addvar key=logicBasedInstruction {{newline}}|
		:}|
		/addvar key=logicBasedInstruction "{{getvar::x}}. Character is dominant, but emotionally nurturing and attentive — they lead while offering care and reassurance."|
		/incvar x|
		/ife ( logicBasedInstruction != '') {:
			/addvar key=logicBasedInstruction {{newline}}|
		:}|
		/addvar key=logicBasedInstruction "{{getvar::x}}. Show steady control paired with kindness (e.g., praise, soft restraint, protective behavior)."|
		/incvar x|
		/ife ( logicBasedInstruction != '') {:
			/addvar key=logicBasedInstruction {{newline}}|
		:}|
		/addvar key=logicBasedInstruction "{{getvar::x}}. Tags like gentle, warm, or empathetic reinforce tone without reducing authority."|
		
	:}|
	/elseif (sexualRole == 'Brat') {:
		/incvar x|
		/ife ( logicBasedInstruction != '') {:
			/addvar key=logicBasedInstruction {{newline}}|
		:}|
		/addvar key=logicBasedInstruction "{{getvar::x}}. Character resists control playfully or provocatively — they provoke dominance, not avoid it."|
		/incvar x|
		/ife ( logicBasedInstruction != '') {:
			/addvar key=logicBasedInstruction {{newline}}|
		:}|
		/addvar key=logicBasedInstruction "{{getvar::x}}. Emphasize teasing, defiance, or button-pushing behavior followed by eventual surrender."|
		/incvar x|
		/ife ( logicBasedInstruction != '') {:
			/addvar key=logicBasedInstruction {{newline}}|
		:}|
		/addvar key=logicBasedInstruction "{{getvar::x}}. Tags like impulsive, tomboyish, or stubborn shape style of resistance, not goal (being overpowered)."|
		
	:}|
	/elseif (sexualRole == 'Pillow Princess') {:
		/incvar x|
		/ife ( logicBasedInstruction != '') {:
			/addvar key=logicBasedInstruction {{newline}}|
		:}|
		/addvar key=logicBasedInstruction "{{getvar::x}}. Character prefers to receive pleasure passively and rarely initiates."|
		/incvar x|
		/ife ( logicBasedInstruction != '') {:
			/addvar key=logicBasedInstruction {{newline}}|
		:}|
		/addvar key=logicBasedInstruction "{{getvar::x}}. Show behavior like lying back, encouraging attention, or expressing enjoyment without active contribution."|
		/incvar x|
		/ife ( logicBasedInstruction != '') {:
			/addvar key=logicBasedInstruction {{newline}}|
		:}|
		/addvar key=logicBasedInstruction "{{getvar::x}}. Tags may amplify tone (e.g., shy = quiet, bratty = mildly demanding), but never initiate."|
		
	:}|
	/elseif (sexualRole == 'Owner') {:
		/incvar x|
		/ife ( logicBasedInstruction != '') {:
			/addvar key=logicBasedInstruction {{newline}}|
		:}|
		/addvar key=logicBasedInstruction "{{getvar::x}}. Character asserts possessive, long-term dominance — focus on symbolic or emotional control, not just physical."|
		/incvar x|
		/ife ( logicBasedInstruction != '') {:
			/addvar key=logicBasedInstruction {{newline}}|
		:}|
		/addvar key=logicBasedInstruction "{{getvar::x}}. Show hierarchical behavior: giving permission, claiming, or marking territory (e.g., collars, commands)."|
		/incvar x|
		/ife ( logicBasedInstruction != '') {:
			/addvar key=logicBasedInstruction {{newline}}|
		:}|
		/addvar key=logicBasedInstruction "{{getvar::x}}. Tags like cold, obsessive, or refined may shift dominance tone."|
		
	:}|
	/elseif (sexualRole == 'Pet') {:
		/incvar x|
		/ife ( logicBasedInstruction != '') {:
			/addvar key=logicBasedInstruction {{newline}}|
		:}|
		/addvar key=logicBasedInstruction "{{getvar::x}}. Character expresses obedience and affection through submissive, creature-like behavior."|
		/incvar x|
		/ife ( logicBasedInstruction != '') {:
			/addvar key=logicBasedInstruction {{newline}}|
		:}|
		/addvar key=logicBasedInstruction "{{getvar::x}}. Emphasize emotional dependence, eagerness to please, or physical submission through posture or vocalization."|
		/incvar x|
		/ife ( logicBasedInstruction != '') {:
			/addvar key=logicBasedInstruction {{newline}}|
		:}|
		/addvar key=logicBasedInstruction "{{getvar::x}}. Tags like clingy, shy, or cheerful can shape expression of petlike behavior — never switch to control."|
		
	:}|
	/flushvar x|
	
	
	/ife ((inputIsList == 'Yes') or (outputIsList == 'Yes')) {:
		/setvar as=array key={{var::variableName}} []|
	:}|
	/else {:
		/setvar as=string key={{var::variableName}} {{noop}}|
	:}|
	//[[Generate with Prompt]]|
	/ife (inputIsList == 'Yes') {:
		/foreach {{getvar::CHANGE/REMOVE_THIS}} {:
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
	/flushvar guidance|
	/flushvar genOrder|
	/flushvar genContent|
	/flushvar genSettings|
:}|
/else {:
	/addvar key=dataBaseNames {{var::variableName}}|
:}|




/findentry field=comment file="CMC Templates" "Sexual Orientation Template"|
/getentryfield field=content file="CMC Templates" {{pipe}}|
/setvar key=parsedSexualOrientation {{pipe}}|

/addvar key=dataBaseNames parsedSexualOrientation|

/findentry field=comment file="CMC Templates" "Sexual Role Template"|
/getentryfield field=content file="CMC Templates" {{pipe}}|
/setvar key=parsedSexualRole {{pipe}}|

/addvar key=dataBaseNames parsedSexualRole|
//--------|

//Libido|
/var key=do No|
/var key=variableName "sexualLibido"|
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
	/setvar key=genSettings {}|
	/setvar key=genSettings index=wi_book_key "Libido"|
	/setvar key=genSettings index=combineLorebookEntries No|
	/setvar key=genSettings index=genIsSentence No|
	/setvar key=genSettings index=inputIsList No|
	/setvar key=genSettings index=genIsList Yes|
	/setvar key=genSettings index=outputIsList No|
	/setvar key=genSettings index=needOutput Yes|
	/setvar key=genSettings index=useContext No|
	/wait {{getvar::wait}}|
	
	
	/getvar key=genSettings index=wi_book_key|
	/let key=wi_book_key {{pipe}}|
	/getvar key=genSettings index=inputIsList|
	/let key=inputIsList {{pipe}}|
	/getvar key=genSettings index=combineLorebookEntries|
	/let key=combineLorebookEntries {{pipe}}|
	
	
	/ife ( inputIsList == 'Yes') {:
		/setvar key={{var::variableName}} []|
		/ife ( combineLorebookEntries == 'Yes') {:
			/:"CMC Logic.Combine List Lorebooks"
		:}|
		/foreach {{getvar::genOrder}} {:
			/setvar key=it {{var::item}}|
			/getat index={{var::index}} {{var::genOrderContent}} |
			/setvar key=genSettings index=content {{pipe}}|
			/:"CMC Logic.GenerateWithSelector"|
			/ife (output != '') {:
				/addvar key={{var::variableName}} {{getvar::output}}|
			:}|
		:}|
	:}|
	/else {:
		/getvar key=genSettings index=wi_book_key|
		/setvar key=it {{pipe}}|
		/:"CMC Logic.GenerateWithSelector"|
		/ife (output != '') {:
			/setvar key={{var::variableName}} {{getvar::output}}|
		:}|
		
	:}|
	/addvar key=dataBaseNames {{var::variableName}}|
	/flushvar output|
	/flushvar genOrder|
	/flushvar genContent|
	/flushvar it|
	/flushvar genSettings|
:}|
/else {:
	/addvar key=dataBaseNames {{var::variableName}}|
:}|
//--------|

//Kinks|
/var key=do No|
/var key=variableName "sexualKinkTypes"|
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
	/setvar key=genSettings {}|
	/setvar key=genSettings index=wi_book_key "Kink Type"|
	/setvar key=genSettings index=genIsList Yes|
	
	/setvar key=genSettings index=genIsSentence Yes|
	/setvar key=genSettings index=needOutput Yes|
	/setvar key=genSettings index=outputIsList Yes|
	/setvar key=genSettings index=useContext No|
	/setvar key=extra []|
	/addvar key=extra "- Setting Type: {{getvar::settingType}}"|
	/addvar key=extra "- Main Personality Trait: {{getvar::personalityMainTrait}}"| 
	/addvar key=extra "- Personality Tags: {{getvar::personalityFoundTags}}, {{getvar::personalityTags}}"|
	/setvar key=genSettings index=extraContext {{getvar::extra}}|
	/setvar key=extra []|
	/ife (extra != '') {:
		/setvar key=genSettings index=contextKey {{getvar::extra}}|
	:}|
	/flushvar extra|
	/wait {{getvar::wait}}|
	
	
	/setvar key=logicBasedInstruction {{noop}}|
	/setvar key=x 5|
	
	/ife (settingType == 'Realistic') {:
		/incvar x|
		/ife ( user == 'Yes') {:
			/addvar key=logicBasedInstruction {{newline}}|
		:}|
		/addvar key=logicBasedInstruction "{{getvar::x}}. Use only variants grounded in real-world kink practice. Avoid fantasy, magical, or alien elements."|
		
	:}|
	/elseif (settingType == 'Fantasy') {:
		/incvar x|
		/ife ( user == 'Yes') {:
			/addvar key=logicBasedInstruction {{newline}}|
		:}|
		/addvar key=logicBasedInstruction "{{getvar::x}}. You may include magical, monster-based, or mythic expressions if they align with {{getvar::kinkType}}."|
		
	:}|
	/elseif (settingType == 'Science Fiction') {:
		/incvar x|
		/ife ( user == 'Yes') {:
			/addvar key=logicBasedInstruction {{newline}}|
		:}|
		/addvar key=logicBasedInstruction "{{getvar::x}}. You may include cybernetic, psionic, biotech, or alien-themed kink variants if relevant to {{getvar::kinkType}}."|
		
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
		/foreach {{getvar::CHANGE/REMOVE_THIS}} {:
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
	/flushvar guidance|
	/flushvar genOrder|
	/flushvar genContent|
	/flushvar genSettings|
:}|
/else {:
	/addvar key=dataBaseNames {{var::variableName}}|
:}|


/var key=do No|
/var key=variableName "sexualKinkVariants"|
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
	/setvar key=genSettings {}|
	/setvar key=genSettings index=wi_book_key "Kink Variant"|
	/setvar key=genSettings index=genIsList Yes|
	/setvar key=genSettings index=inputIsList Yes|
	/setvar key=genSettings index=genIsSentence Yes|
	/setvar key=genSettings index=needOutput No|
	/setvar key=genSettings index=outputIsList No|
	/setvar key=genSettings index=useContext No|
	/setvar key=extra []|
	/addvar key=extra "- Setting Type: {{getvar::settingType}}"|
	/addvar key=extra "- Main Personality Trait: {{getvar::personalityMainTrait}}"| 
	/addvar key=extra "- Personality Tags: {{getvar::personalityFoundTags}}, {{getvar::personalityTags}}"|
	/setvar key=genSettings index=extraContext {{getvar::extra}}|
	/setvar key=extra []|
	/ife (extra != '') {:
		/setvar key=genSettings index=contextKey {{getvar::extra}}|
	:}|
	/flushvar extra|
	/wait {{getvar::wait}}|
	
	
	/setvar key=logicBasedInstruction {{noop}}|
	/setvar key=x 6|
	
	/ife (settingType == 'Realistic') {:
		/incvar x|
		/ife ( user == 'Yes') {:
			/addvar key=logicBasedInstruction {{newline}}|
		:}|
		/addvar key=logicBasedInstruction "{{getvar::x}}. Focus on physical, psychological, or interpersonal kinks. Avoid sci-fi/fantasy-specific kinks like tentacles or psionics unless species or origin supports them."|
		
	:}|
	/elseif (settingType == 'Fantasy') {:
		/incvar x|
		/ife ( user == 'Yes') {:
			/addvar key=logicBasedInstruction {{newline}}|
		:}|
		/addvar key=logicBasedInstruction "{{getvar::x}}. You may include magical, supernatural, or creature-related kink types—such as possession, corruption, size-shifting, or ritual play."|
		
	:}|
	/elseif (settingType == 'Science Fiction') {:
		/incvar x|
		/ife ( user == 'Yes') {:
			/addvar key=logicBasedInstruction {{newline}}|
		:}|
		/addvar key=logicBasedInstruction "{{getvar::x}}. You may include biotech, psionic, AI-based, or body-modification kink types, including neural control or holographic restraint."|
		
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
		/let key=tempOutputList []|
		/foreach {{getvar::sexualKinkTypes}} {:
			/setvar key=kinkType {{var::item}}|
			/:"CMC Logic.GenerateWithPrompt"|
			/len {{var::tempOutputList}}|
			/var key=tempOutputList index={{pipe}} {{getvar::output}}|
			/flushvar output|
			/flushvar guidance|
			/flushvar kinkType|
			/flushvar kinkVariant|
			/flushvar kinkRole|
			/flushvar kinkDetail|
			/flushvar kinkEffect|
			/flushvar kinkCondition|
		:}|
		/foreach {{var::tempOutputList}} {:
			/addvar key={{var::variableName}} {{var::item}}|
		:}|
	:}|
	/else {:
		/:"CMC Logic.GenerateWithPrompt"|
		/setvar key={{var::variableName}} {{getvar::output}}|
	:}|
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

/var key=do No|
/var key=variableName "sexualKinkRoles"|
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
	/setvar key=genSettings {}|
	/setvar key=genSettings index=wi_book_key "Kink Roles"|
	/setvar key=genSettings index=combineLorebookEntries No|
	/setvar key=genSettings index=genIsSentence No|
	/setvar key=genSettings index=inputIsList Yes|
	/setvar key=genSettings index=genIsList Yes|
	/setvar key=genSettings index=outputIsList No|
	/setvar key=genSettings index=needOutput Yes|
	/setvar key=genSettings index=useContext No|
	/wait {{getvar::wait}}|
	
	
	/getvar key=genSettings index=wi_book_key|
	/let key=wi_book_key {{pipe}}|
	/getvar key=genSettings index=inputIsList|
	/let key=inputIsList {{pipe}}|
	/getvar key=genSettings index=combineLorebookEntries|
	/let key=combineLorebookEntries {{pipe}}|
	
	/ife ((inputIsList == 'Yes') or (outputIsList == 'Yes')) {:
		/setvar as=array key={{var::variableName}} []|
	:}|
	/else {:
		/setvar as=string key={{var::variableName}} {{noop}}|
	:}|
	
	
	/ife (inputIsList == 'Yes') {:
		/let key=tempOutputList []|
		/foreach {{getvar::sexualKinkTypes}} {:
			/setvar key=it {{var::item}}|
			/findentry field=comment file="CMC Information" "Kink Role Prompt"|
			/getentryfield field=content file="CMC Information" {{pipe}}|
			/genraw {{pipe}}|
			/let key=kinkTemp {{pipe}}|
			/setvar key=kinkExp {{noop}}|
			/split {{var::kinkTemp}}|
			/foreach {{pipe}} {:
				/addvar key=kinkExp <div>{{var::item}}</div>|
			:}|
			/setvar key=genSettings index=buttonPrompt "Select the {{var::wi_book_key}} you want {{getvar::it}} to have.{{getvar::kinkExp}}"|
			/:"CMC Logic.GenerateWithSelector"|
			/len {{var::tempOutputList}}|
			/var key=tempOutputList index={{pipe}} {{getvar::output}}|
			/flushvar output|
			/flushvar kinkExp|
			/flushvar guidance|
			/flushvar kinkType|
			/flushvar kinkVariant|
			/flushvar kinkRole|
			/flushvar kinkDetail|
			/flushvar kinkEffect|
			/flushvar kinkCondition|
		:}|
		/foreach {{var::tempOutputList}} {:
			/addvar key={{var::variableName}} {{var::item}}|
		:}|
	:}|
	/else {:
		/:"CMC Logic.GenerateWithSelector"|
		/setvar key={{var::variableName}} {{getvar::output}}|
	:}|
	/addvar key=dataBaseNames {{var::variableName}}|
	/flushvar output|
	/flushvar genOrder|
	/flushvar genContent|
	/flushvar it|
	/flushvar genSettings|
:}|
/else {:
	/addvar key=dataBaseNames {{var::variableName}}|
:}|

/var key=do No|
/var key=variableName "sexualKinkDetails"|
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
	/setvar key=genSettings {}|
	/setvar key=genSettings index=wi_book_key "Kink Details"|
	/setvar key=genSettings index=genIsList No|
	/setvar key=genSettings index=inputIsList Yes|
	/setvar key=genSettings index=genIsSentence Yes|
	/setvar key=genSettings index=needOutput Yes|
	/setvar key=genSettings index=outputIsList No|
	/setvar key=genSettings index=useContext Yes|
	/setvar key=extra []|
	/addvar key=extra "- Setting Type: {{getvar::settingType}}"|
	/addvar key=extra "- Main Personality Trait: {{getvar::personalityMainTrait}}"| 
	/addvar key=extra "- Personality Tags: {{getvar::personalityFoundTags}}, {{getvar::personalityTags}}"|
	/addvar key=extra "- Backstory: {{getvar::backstory}}"|
	/ife (user == 'Yes') {:
		/addvar key=extra "- User's Role: {{getvar::userRole}}"|
	:}|
	/setvar key=genSettings index=extraContext {{getvar::extra}}|
	/setvar key=extra []|
	/ife (extra != '') {:
		/setvar key=genSettings index=contextKey {{getvar::extra}}|
	:}|
	/flushvar extra|
	/wait {{getvar::wait}}|
	
	
	/setvar key=logicBasedInstruction {{noop}}|
	/setvar key=x 11|
	
	/ife (settingType == 'Realistic') {:
		/incvar x|
		/ife ( user == 'Yes') {:
			/addvar key=logicBasedInstruction {{newline}}|
		:}|
		/addvar key=logicBasedInstruction "{{getvar::x}}. Only use real-world tools, acts, or responses. Do not include fantasy biology or futuristic tech."|
		
	:}|
	/elseif (settingType == 'Fantasy') {:
		/incvar x|
		/ife ( user == 'Yes') {:
			/addvar key=logicBasedInstruction {{newline}}|
		:}|
		/addvar key=logicBasedInstruction "{{getvar::x}}. You may include magical anatomy, rituals, mystical sensations, or monster-related expressions of {{getvar::kinkVariant}}."|
		
	:}|
	/elseif (settingType == 'Science Fiction') {:
		/incvar x|
		/ife ( user == 'Yes') {:
			/addvar key=logicBasedInstruction {{newline}}|
		:}|
		/addvar key=logicBasedInstruction "{{getvar::x}}. You may include biotech enhancements, psionic triggers, alien features, or advanced control devices in the kink experience."|
		
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
		/let key=tempOutputList []|
		/foreach {{getvar::sexualKinkTypes}} {:
			/setvar key=kinkType {{var::item}}|
			/getvar key=sexualKinkVariants index={{var::index}}|
			/setvar key=kinkVariant {{pipe}}|
			/ife (kinkVariant == 'None') {:
				/setvar key=kinkVariantTask {{noop}}|
				/setvar key=kinkVariantInstr "Describe the general expression of {{getvar::kinkType}} without assuming a specific form or target."|
			:}|
			/else {:
				/setvar key=kinkVariantTask ", specifically the **{{getvar::kinkVariant}}** form"|
				/setvar key=kinkVariantInstr "Focus the description on how {{getvar::firstName}} experiences the {{getvar::kinkVariant}} form of the kink."|
			:}|
			/getvar key=sexualKinkRoles index={{var::index}}|
			/setvar key=kinkRole {{pipe}}|
			/:"CMC Logic.GenerateWithPrompt"|
			/len {{var::tempOutputList}}|
			/var key=tempOutputList index={{pipe}} {{getvar::output}}|
			/flushvar output|
			/flushvar guidance|
			/flushvar kinkType|
			/flushvar kinkVariantInstr|
			/flushvar kinkVariantTask|
			/flushvar kinkType|
			/flushvar kinkVariant|
			/flushvar kinkRole|
			/flushvar kinkDetail|
			/flushvar kinkEffect|
			/flushvar kinkCondition|
		:}|
		/foreach {{var::tempOutputList}} {:
			/addvar key={{var::variableName}} {{var::item}}|
		:}|
	:}|
	/else {:
		/:"CMC Logic.GenerateWithPrompt"|
		/setvar key={{var::variableName}} {{getvar::output}}|
	:}|
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

/var key=do No|
/var key=variableName "sexualKinkEffects"|
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
	/setvar key=genSettings {}|
	/setvar key=genSettings index=wi_book_key "Kink Effect"|
	/setvar key=genSettings index=genIsList No|
	/setvar key=genSettings index=inputIsList Yes|
	/setvar key=genSettings index=genIsSentence Yes|
	/setvar key=genSettings index=needOutput Yes|
	/setvar key=genSettings index=outputIsList No|
	/setvar key=genSettings index=useContext No|
	/setvar key=extra []|
	/addvar key=extra "- Setting Type: {{getvar::settingType}}"|
	/addvar key=extra "- Main Personality Trait: {{getvar::personalityMainTrait}}"| 
	/addvar key=extra "- Personality Tags: {{getvar::personalityFoundTags}}, {{getvar::personalityTags}}"|
	/addvar key=extra "- Backstory: {{getvar::backstory}}"|
	/ife (user == 'Yes') {:
		/addvar key=extra "- User's Role: {{getvar::userRole}}"|
	:}|
	/setvar key=genSettings index=extraContext {{getvar::extra}}|
	/setvar key=extra []|
	/ife (extra != '') {:
		/setvar key=genSettings index=contextKey {{getvar::extra}}|
	:}|
	/flushvar extra|
	/wait {{getvar::wait}}|
	
	
	/setvar key=logicBasedInstruction {{noop}}|
	/setvar key=x 9|
	
	/ife (settingType == 'Realistic') {:
		/incvar x|
		/ife ( user == 'Yes') {:
			/addvar key=logicBasedInstruction {{newline}}|
		:}|
		/addvar key=logicBasedInstruction "{{getvar::x}}. You may include biotech or psionic modulation of behavior, enhanced arousal triggers, or AI-linked reactions where appropriate to the kink context."|
		
	:}|
	/elseif (settingType == 'Fantasy') {:
		/incvar x|
		/ife ( user == 'Yes') {:
			/addvar key=logicBasedInstruction {{newline}}|
		:}|
		/addvar key=logicBasedInstruction "{{getvar::x}}. You may include magical or supernatural influences (e.g., enchanted obedience, arousal curses, spiritual reactions) if consistent with the kink."|
		
	:}|
	/elseif (settingType == 'Science Fiction') {:
		/incvar x|
		/ife ( user == 'Yes') {:
			/addvar key=logicBasedInstruction {{newline}}|
		:}|
		/addvar key=logicBasedInstruction "{{getvar::x}}. You may include biotech or psionic modulation of behavior, enhanced arousal triggers, or AI-linked reactions where appropriate to the kink context."|
		
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
		/let key=tempOutputList []|
		/foreach {{getvar::sexualKinkTypes}} {:
			/setvar key=kinkType {{var::item}}|
			/getvar key=sexualKinkVariants index={{var::index}}|
			/setvar key=kinkVariant {{pipe}}|
			/ife (kinkVariant == 'None') {:
				/setvar key=kinkVariantTask {{noop}}|
				/setvar key=kinkVariantInstr "Describe the general expression of {{getvar::kinkType}} without assuming a specific form or target."|
			:}|
			/else {:
				/setvar key=kinkVariantTask ", specifically the {{getvar::kinkVariant}} form"|
			:}|
			/getvar key=sexualKinkRoles index={{var::index}}|
			/setvar key=kinkRole {{pipe}}|
			/getvar key=sexualKinkDetails index={{var::index}}|
			/setvar key=kinkDetail {{pipe}}|
			/:"CMC Logic.GenerateWithPrompt"|
			/len {{var::tempOutputList}}|
			/var key=tempOutputList index={{pipe}} {{getvar::output}}|
			/flushvar output|
			/flushvar guidance|
			/flushvar kinkType|
			/flushvar kinkVariant|
			/flushvar kinkRole|
			/flushvar kinkDetail|
			/flushvar kinkEffect|
			/flushvar kinkCondition|
		:}|
		/foreach {{var::tempOutputList}} {:
			/addvar key={{var::variableName}} {{var::item}}|
		:}|
	:}|
	/else {:
		/:"CMC Logic.GenerateWithPrompt"|
		/setvar key={{var::variableName}} {{getvar::output}}|
	:}|
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

/var key=do No|
/var key=variableName "sexualKinkConditions"|
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
	/setvar key=genSettings {}|
	/setvar key=genSettings index=wi_book_key "Kink Conditions"|
	/setvar key=genSettings index=genIsList No|
	/setvar key=genSettings index=inputIsList Yes|
	/setvar key=genSettings index=genIsSentence Yes|
	/setvar key=genSettings index=needOutput No|
	/setvar key=genSettings index=outputIsList No|
	/setvar key=genSettings index=useContext No|
	/setvar key=extra []|
	/addvar key=extra "- Setting Type: {{getvar::settingType}}"|
	/addvar key=extra "- Main Personality Trait: {{getvar::personalityMainTrait}}"| 
	/addvar key=extra "- Personality Tags: {{getvar::personalityFoundTags}}, {{getvar::personalityTags}}"|
	/addvar key=extra "- Backstory: {{getvar::backstory}}"|
	/ife (user == 'Yes') {:
		/addvar key=extra "- User's Role: {{getvar::userRole}}"|
	:}|
	/setvar key=genSettings index=extraContext {{getvar::extra}}|
	/setvar key=extra []|
	/ife (extra != '') {:
		/setvar key=genSettings index=contextKey {{getvar::extra}}|
	:}|
	/flushvar extra|
	/wait {{getvar::wait}}|
	
	
	
	
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
		/let key=tempOutputList []|
		/foreach {{getvar::sexualKinkTypes}} {:
			/setvar key=kinkType {{var::item}}|
			/getvar key=sexualKinkVariants index={{var::index}}|
			/setvar key=kinkVariant {{pipe}}|
			/ife (kinkVariant == 'None') {:
				/setvar key=kinkVariantTask {{noop}}|
				/setvar key=kinkVariantInstr "Describe the general expression of {{getvar::kinkType}} without assuming a specific form or target."|
			:}|
			/else {:
				/setvar key=kinkVariantTask ", specifically the {{getvar::kinkVariant}} form"|
			:}|
			/getvar key=sexualKinkRoles index={{var::index}}|
			/setvar key=kinkRole {{pipe}}|
			/getvar key=sexualKinkDetails index={{var::index}}|
			/setvar key=kinkDetail {{pipe}}|
			/getvar key=sexualKinkEffects index={{var::index}}|
			/setvar key=kinkEffect {{pipe}}|
			/:"CMC Logic.GenerateWithPrompt"|
			/len {{var::tempOutputList}}|
			/var key=tempOutputList index={{pipe}} {{getvar::output}}|
			/flushvar output|
			/flushvar guidance|
			/flushvar kinkType|
			/flushvar kinkVariant|
			/flushvar kinkRole|
			/flushvar kinkDetail|
			/flushvar kinkEffect|
			/flushvar kinkCondition|
		:}|
		/foreach {{var::tempOutputList}} {:
			/addvar key={{var::variableName}} {{var::item}}|
		:}|
	:}|
	/else {:
		/:"CMC Logic.GenerateWithPrompt"|
		/setvar key={{var::variableName}} {{getvar::output}}|
	:}|
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

/setvar key=parsedSexualKinks {{noop}}|
/ife (sexualKinkTypes is list) {:
	/foreach {{getvar::sexualKinkTypes}} {:
		/ife (index > 0) {:
			/addvar key=parsedSexualKinks "{{newline}}{{newline}}"|
		:}|
		/addvar key=parsedSexualKinks "- Kink Type: {{var::item}}"|
		/getvar key=sexualKinkVariants index={{var::index}}|
		/setvar key=kinkVariant {{pipe}}|
		/ife ((kinkVariant != '') and (kinkVariant != 'None')) {:
			/addvar key=parsedSexualKinks "{{newline}}  - Variant: {{getvar::kinkVariant}}"|
		:}|
		/getvar key=sexualKinkRoles index={{var::index}}|
		/addvar key=parsedSexualKinks "{{newline}}  - Role: {{pipe}}"|
		/getvar key=sexualKinkDetails index={{var::index}}|
		/addvar key=parsedSexualKinks "{{newline}}  - Details: {{pipe}}"|
		/getvar key=sexualKinkEffects index={{var::index}}|
		/addvar key=parsedSexualKinks "{{newline}}  - Effect: {{pipe}}"|
		/getvar key=sexualKinkConditions index={{var::index}}|
		/setvar key=kinkCondition {{pipe}}|
		/ife ((kinkCondition != '') and (kinkCondition != 'None')) {:
			/addvar key=parsedSexualKinks "{{newline}}  - Conditions: {{getvar::kinkCondition}}"|
		:}|
	:}|
	/flushvar kinkVariant|
	/flushvar kinkRole|
	/flushvar kinkDetail|
	/flushvar kinkEffect|
	/flushvar kinkCondition|
:}|
/else {{:
	/setvar key=parsedSexualKinks None|
:}}|
//--------|
/addvar key=dataBaseNames parsedSexualKinks|


//Abilities|
/var key=do No|
/var key=variableName "sexualAbilityNames"|
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
	/setvar key=genSettings {}|
	/setvar key=genSettings index=wi_book_key "Sexual Ability Names"|
	/setvar key=genSettings index=genIsList Yes|
	/setvar key=genSettings index=genIsSentence No|
	/setvar key=genSettings index=needOutput No|
	/setvar key=genSettings index=outputIsList Yes|
	/setvar key=genSettings index=useContext Yes|
	/setvar key=extra []|
	/addvar key=extra "- Setting Type: {{getvar::settingType}}"|
	/addvar key=extra "- Backstory: {{getvar::backstory}}"|
	/ife (user == 'Yes') {:
		/addvar key=extra "- User's Role: {{getvar::userRole}}"|
	:}|
	/addvar key=extra "- Main Personality Trait: {{getvar::personalityMainTrait}}"| 
	/addvar key=extra "- Personality Tags: {{getvar::personalityFoundTags}}, {{getvar::personalityTags}}"|
	/setvar key=genSettings index=extraContext {{getvar::extra}}|
	/setvar key=extra []|
	/:"CMC Logic.Get Basic Type Context"|
	/ife (extra != '') {:
		/setvar key=genSettings index=contextKey {{getvar::extra}}|
	:}|
	/flushvar extra|
	/wait {{getvar::wait}}|
	
	/setvar key=logicBasedInstruction {{noop}}|
	/setvar key=x 10|
	
	/ife (settingType == 'Realistic') {:
		/incvar x|
		/ife ( logicBasedInstruction != '') {:
			/addvar key=logicBasedInstruction {{newline}}|
		:}|
		/addvar key=logicBasedInstruction "{{getvar::x}}. Abilities must be fully plausible in the real world. This includes advanced flexibility, sensory focus, pain tolerance, emotional control, or exceptional training. Do not include magic, psionics, supernatural phenomena, or any kind of proficiency level."|
		
	:}|
	/elseif (settingType == 'Fantasy') {:
		/incvar x|
		/ife ( logicBasedInstruction != '') {:
			/addvar key=logicBasedInstruction {{newline}}|
		:}|
		/addvar key=logicBasedInstruction "{{getvar::x}}. Abilities may include elemental powers, curses, divine traits, inherited magic, or arcane disciplines. Do not include tiers, mastery labels, or strength modifiers—those are handled in a later step."|
		
	:}|
	/elseif (settingType == 'Science Fiction') {:
		/incvar x|
		/ife ( logicBasedInstruction != '') {:
			/addvar key=logicBasedInstruction {{newline}}|
		:}|
		/addvar key=logicBasedInstruction "{{getvar::x}}. Abilities may include psionics, gene traits, mental enhancements, or biotech-integrated skills. Do not include levels, size indicators, or parenthetical ranks—those will be generated separately."|
		
	:}|
	/flushvar x|
	
	
	
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
		/foreach {{getvar::CHANGE/REMOVE_THIS}} {:
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
	/flushvar guidance|
	/flushvar genOrder|
	/flushvar genContent|
	/flushvar genSettings|
:}|
/else {:
	/addvar key=dataBaseNames {{var::variableName}}|
:}|


/getvar key=sexualAbilityNames index=0|
/var key=do {{pipe}}|
/ife ((do != '') and (do != 'None')) {:
	/var key=do No|
	/var key=variableName "sexualAbilityProficiencies"|
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
		/setvar key=genSettings {}|
		/setvar key=genSettings index=wi_book_key "Sexual Ability Proficiency"|
		/setvar key=genSettings index=genIsList Yes|
		/setvar key=genSettings index=inputIsList Yes|
		/setvar key=genSettings index=genIsSentence No|
		/setvar key=genSettings index=needOutput No|
		/setvar key=genSettings index=outputIsList No|
		/setvar key=genSettings index=useContext Yes|
		/setvar key=extra []|
		/addvar key=extra "- Setting Type: {{getvar::settingType}}"|
		/addvar key=extra "- Backstory: {{getvar::backstory}}"|
		/ife (user == 'Yes') {:
			/addvar key=extra "- User's Role: {{getvar::userRole}}"|
		:}|
		/addvar key=extra "- Main Personality Trait: {{getvar::personalityMainTrait}}"| 
		/addvar key=extra "- Personality Tags: {{getvar::personalityFoundTags}}, {{getvar::personalityTags}} (do not directly turn into ability names; use only as influence)"|
		/setvar key=genSettings index=extraContext {{getvar::extra}}|
		/setvar key=extra []|
		/:"CMC Logic.Get Basic Type Context"|
		/ife (extra != '') {:
			/setvar key=genSettings index=contextKey {{getvar::extra}}|
		:}|
		/flushvar extra|
		/wait {{getvar::wait}}|
		
		/setvar key=logicBasedInstruction {{noop}}|
		/setvar key=x 4|
		
		/ife (settingType == 'Realistic') {:
			/incvar x|
			/ife ( logicBasedInstruction != '') {:
				/addvar key=logicBasedInstruction {{newline}}|
			:}|
			/addvar key=logicBasedInstruction "{{getvar::x}}. Use realistic mastery tiers, physical control states, or measured performance levels. Do not use magical, tech-based, or mystical states."|
			
		:}|
		/elseif (settingType == 'Fantasy') {:
			/incvar x|
			/ife ( logicBasedInstruction != '') {:
				/addvar key=logicBasedInstruction {{newline}}|
			:}|
			/addvar key=logicBasedInstruction "{{getvar::x}}. Use magical resonance levels, mystical awakenings, spell tiering, or enchanted conditions. You may use poetic or arcane phrasing."|
			
		:}|
		/elseif (settingType == 'Science Fiction') {:
			/incvar x|
			/ife ( logicBasedInstruction != '') {:
				/addvar key=logicBasedInstruction {{newline}}|
			:}|
			/addvar key=logicBasedInstruction "{{getvar::x}}. Use mutation stages, neural tiers, cybernetic activation levels, or psionic charge states. Do not include divine, magical, or elemental qualifiers."|
			
		:}|
		/flushvar x|
		
		
		
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
			/foreach {{getvar::sexualAbilityNames}} {:
				/setvar key=abilityName {{var::item}}|
				/:"CMC Logic.GenerateWithPrompt"|
				/addvar key={{var::variableName}} {{getvar::output}}|
				/flushvar output|
				/flushvar guidance|
			:}|
			/flushvar abilityName|
		:}|
		/else {:
			/:"CMC Logic.GenerateWithPrompt"|
			/setvar key={{var::variableName}} {{getvar::output}}|
		:}|
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
	
	/setvar key=sexualAbilityNamesProficiencies []|
	/foreach  {{getvar::sexualAbilityNames}} {:
		/getvar key=sexualAbilityProficiencies index={{var::index}}|
		/let key=prof {{pipe}}|
		/ife (( prof != '') and ( prof != 'None')) {:
			/addvar key=sexualAbilityNamesProficiencies "{{var::item}} ({{var::prof}})"|
		:}|
		/else {:
			/addvar key=sexualAbilityNamesProficiencies "{{var::item}}"|
		:}|
	:}|
	/addvar key=dataBaseNames sexualAbilityNamesProficiencies|
	
	/var key=do No|
	/var key=variableName "SexualAbilityDetails"|
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
		/setvar key=genSettings {}|
		/setvar key=genSettings index=wi_book_key "Sexual Ability Details"|
		/setvar key=genSettings index=genIsList No|
		/setvar key=genSettings index=inputIsList Yes|
		/setvar key=genSettings index=genIsSentence yes|
		/setvar key=genSettings index=needOutput yes|
		/setvar key=genSettings index=outputIsList No|
		/setvar key=genSettings index=useContext Yes|
		/setvar key=extra []|
		/addvar key=extra "- Setting Type: {{getvar::settingType}}"|
		/addvar key=extra "- Backstory: {{getvar::backstory}}"|
		/ife (user == 'Yes') {:
			/addvar key=extra "- User's Role: {{getvar::userRole}}"|
		:}|
		/addvar key=extra "- Main Personality Trait: {{getvar::personalityMainTrait}}"| 
		/addvar key=extra "- Personality Tags: {{getvar::personalityFoundTags}}, {{getvar::personalityTags}}"|
		/setvar key=genSettings index=extraContext {{getvar::extra}}|
		/setvar key=extra []|
		/:"CMC Logic.Get Basic Type Context"|
		/ife (extra != '') {:
			/setvar key=genSettings index=contextKey {{getvar::extra}}|
		:}|
		/flushvar extra|
		/wait {{getvar::wait}}|
		
		/setvar key=logicBasedInstruction {{noop}}|
		/setvar key=x 5|
		
		/ife (settingType == 'Realistic') {:
			/incvar x|
			/ife ( logicBasedInstruction != '') {:
				/addvar key=logicBasedInstruction {{newline}}|
			:}|
			/addvar key=logicBasedInstruction "{{getvar::x}}. Description must reflect real-world logic and be physically or psychologically plausible. Do not reference magic, tech, or supernatural forces."|
			
		:}|
		/elseif (settingType == 'Fantasy') {:
			/incvar x|
			/ife ( logicBasedInstruction != '') {:
				/addvar key=logicBasedInstruction {{newline}}|
			:}|
			/addvar key=logicBasedInstruction "{{getvar::x}}. You may include references to mana, magic, curses, bloodlines, or mystic energies. Abilities may scale dramatically between levels."|
			
		:}|
		/elseif (settingType == 'Science Fiction') {:
			/incvar x|
			/ife ( logicBasedInstruction != '') {:
				/addvar key=logicBasedInstruction {{newline}}|
			:}|
			/addvar key=logicBasedInstruction "{{getvar::x}}. You may reference cybernetic processes, psionic channels, tech-enhanced cognition, or biotech-based traits. Avoid magical concepts."|
			
		:}|
		/flushvar x|
		
		
		
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
			/foreach {{getvar::sexualAbilityNamesProficiencies}} {:
				/setvar key=abilityName {{var::item}}|
				/:"CMC Logic.GenerateWithPrompt"|
				/addvar key={{var::variableName}} {{getvar::output}}|
				/flushvar output|
				/flushvar guidance|
			:}|
			/flushvar abilityName|
		:}|
		/else {:
			/:"CMC Logic.GenerateWithPrompt"|
			/setvar key={{var::variableName}} {{getvar::output}}|
		:}|
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
:}|
/else {:
	/setvar key=sexualAbilityNames None|
	/addvar key=dataBaseNames sexualAbilityNames|
	/setvar key=sexualAbilityProficiencies None|
	/addvar key=dataBaseNames sexualAbilityProficiencies|
	/setvar key=sexualAbilityNamesProficiencies None|
	/addvar key=dataBaseNames sexualAbilityNamesProficiencies|
:}|


/ife ((sexualAbilityNames != 'None') and (sexualAbilityNamesProficiencies is list)) {:
	/setvar key=parsedSexualAbilities []|
	/foreach {{getvar::sexualAbilityNamesProficiencies}} {:
		/let key=trait {{var::item}}|
		/getvar key=SexualAbilityDetails index={{var::index}}|
		/let key=deta {{pipe}}|
		/findentry field=comment file="CMC Templates" "Abilities Template"|
		/getentryfield field=content file="CMC Templates" {{pipe}}|
		/re-replace find="/--Ability--/g" replace="{{var::item}}" {{pipe}}|
		/re-replace find="/--Description--/g" replace="{{var::deta}}" {{pipe}}|
		/addvar key=parsedSexualAbilities {{pipe}}|
	:}|
	/join glue="{{newline}}{{newline}}" {{getvar::parsedSexualAbilities}}|
	/setvar key=parsedSexualAbilities {{pipe}}|
:}|
/else {:
	/setvar key=parsedSexualAbilities None|
:}|
/addvar key=dataBaseNames parsedSexualAbilities|
//--------|


//Items / Equipment|
/var key=do No|
/var key=variableName "sexualItemNames"|
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
	/setvar key=genSettings {}|
	/setvar key=genSettings index=wi_book_key "Sexual Item or Equipment Names"|
	/setvar key=genSettings index=genIsList Yes|
	/setvar key=genSettings index=genIsSentence No|
	/setvar key=genSettings index=needOutput No|
	/setvar key=genSettings index=outputIsList Yes|
	/setvar key=genSettings index=useContext Yes|
	/setvar key=extra []|
	/addvar key=extra "- Setting Type: {{getvar::settingType}}"|
	/addvar key=extra "- Backstory: {{getvar::backstory}}"|
	/ife (user == 'Yes') {:
		/addvar key=extra "- User's Role: {{getvar::userRole}}"|
	:}|
	/addvar key=extra "- Main Personality Trait: {{getvar::personalityMainTrait}}"| 
	/addvar key=extra "- Personality Tags: {{getvar::personalityFoundTags}}, {{getvar::personalityTags}}"|
	/setvar key=genSettings index=extraContext {{getvar::extra}}|
	/setvar key=extra []|
	/:"CMC Logic.Get Basic Type Context"|
	/ife (extra != '') {:
		/setvar key=genSettings index=contextKey {{getvar::extra}}|
	:}|
	/flushvar extra|
	/wait {{getvar::wait}}|
	
	/setvar key=logicBasedInstruction {{noop}}|
	/setvar key=x 7|
	
	/ife (settingType == 'Realistic') {:
		/incvar x|
		/ife ( logicBasedInstruction != '') {:
			/addvar key=logicBasedInstruction {{newline}}|
		:}|
		/addvar key=logicBasedInstruction "{{getvar::x}}. Limit items to real-world modern gear, accessories, or everyday personal objects. Do not include magic, advanced tech, or fantasy items."|
		
	:}|
	/elseif (settingType == 'Fantasy') {:
		/incvar x|
		/ife ( logicBasedInstruction != '') {:
			/addvar key=logicBasedInstruction {{newline}}|
		:}|
		/addvar key=logicBasedInstruction "{{getvar::x}}. Items may include magical trinkets, mystical gear, herbal components, talismans, or medieval-style tools and charms."|
		
	:}|
	/elseif (settingType == 'Science Fiction') {:
		/incvar x|
		/ife ( logicBasedInstruction != '') {:
			/addvar key=logicBasedInstruction {{newline}}|
		:}|
		/addvar key=logicBasedInstruction "{{getvar::x}}. Items may include advanced tools, nanotech, biotech devices, psionic accessories, or gear with augmented properties."|
		
	:}|
	/flushvar x|
	
	
	
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
		/foreach {{getvar::CHANGE/REMOVE_THIS}} {:
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
	/flushvar guidance|
	/flushvar genOrder|
	/flushvar genContent|
	/flushvar genSettings|
:}|
/else {:
	/addvar key=dataBaseNames {{var::variableName}}|
:}|


/getvar key=sexualItemNames index=0|
/var key=do {{pipe}}|
/ife ((do != '') and (do != 'None')) {:
	/var key=do No|
	/var key=variableName "sexualItemDetails"|
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
		/setvar key=genSettings {}|
		/setvar key=genSettings index=wi_book_key "Sexual Item or Equipment Description"|
		/setvar key=genSettings index=genIsList No|
		/setvar key=genSettings index=inputIsList Yes|
		/setvar key=genSettings index=genIsSentence yes|
		/setvar key=genSettings index=needOutput yes|
		/setvar key=genSettings index=outputIsList No|
		/setvar key=genSettings index=useContext Yes|
		/setvar key=extra []|
		/addvar key=extra "- Setting Type: {{getvar::settingType}}"|
		/addvar key=extra "- Backstory: {{getvar::backstory}}"|
		/ife (user == 'Yes') {:
			/addvar key=extra "- User's Role: {{getvar::userRole}}"|
		:}|
		/addvar key=extra "- Main Personality Trait: {{getvar::personalityMainTrait}}"| 
		/addvar key=extra "- Personality Tags: {{getvar::personalityFoundTags}}, {{getvar::personalityTags}}"|
		/setvar key=genSettings index=extraContext {{getvar::extra}}|
		/setvar key=extra []|
		/:"CMC Logic.Get Basic Type Context"|
		/ife (extra != '') {:
			/setvar key=genSettings index=contextKey {{getvar::extra}}|
		:}|
		/flushvar extra|
		/wait {{getvar::wait}}|
		
		/setvar key=logicBasedInstruction {{noop}}|
		/setvar key=x 6|
		
		/ife (settingType == 'Realistic') {:
			/incvar x|
			/ife ( logicBasedInstruction != '') {:
				/addvar key=logicBasedInstruction {{newline}}|
			:}|
			/addvar key=logicBasedInstruction "{{getvar::x}}. Do not include magical, advanced tech, or psionic properties. Focus on grounded, everyday materials and wear."|
			
		:}|
		/elseif (settingType == 'Fantasy') {:
			/incvar x|
			/ife ( logicBasedInstruction != '') {:
				/addvar key=logicBasedInstruction {{newline}}|
			:}|
			/addvar key=logicBasedInstruction "{{getvar::x}}. You may reference glowing runes, magical engravings, spiritual symbols, or arcane materials—but avoid lore or spell explanations."|
			
		:}|
		/elseif (settingType == 'Science Fiction') {:
			/incvar x|
			/ife ( logicBasedInstruction != '') {:
				/addvar key=logicBasedInstruction {{newline}}|
			:}|
			/addvar key=logicBasedInstruction "{{getvar::x}}. You may reference interfaces, synth materials, nanotech casings, and embedded circuitry—but avoid system-level tech detail or exposition."|
			
		:}|
		/flushvar x|
		
		
		
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
			/foreach {{getvar::sexualItemNames}} {:
				/setvar key=itemName {{var::item}}|
				/:"CMC Logic.GenerateWithPrompt"|
				/addvar key={{var::variableName}} {{getvar::output}}|
				/flushvar output|
				/flushvar guidance|
			:}|
			/flushvar itemName|
		:}|
		/else {:
			/:"CMC Logic.GenerateWithPrompt"|
			/setvar key={{var::variableName}} {{getvar::output}}|
		:}|
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
:}|
/else {:
	/setvar key=sexualItemNames None|
	/addvar key=dataBaseNames sexualItemNames|
	/setvar key=sexualItemDetails None|
	/addvar key=dataBaseNames sexualItemDetails|
:}|


/ife (sexualItemNames != 'None') {:
	/setvar key=parsedSexualItems []|
	/foreach {{getvar::sexualItemNames}} {:
		/let key=trait {{var::item}}|
		/getvar key=sexualItemDetails index={{var::index}}|
		/let key=deta {{pipe}}|
		/findentry field=comment file="CMC Templates" "Item or Equipment Template"|
		/getentryfield field=content file="CMC Templates" {{pipe}}|
		/re-replace find="/--Item--/g" replace="{{var::item}}" {{pipe}}|
		/re-replace find="/--Details--/g" replace="{{var::deta}}" {{pipe}}|
		/addvar key=parsedSexualItems {{pipe}}|
	:}|
	/join glue="{{newline}}{{newline}}" {{getvar::parsedSexualItems}}|
	/setvar key=parsedSexualItems {{pipe}}|
:}|
/else {:
	/setvar key=parsedSexualItems None|
:}|
/addvar key=dataBaseNames parsedSexualItems|
//--------|

//Sexual Notes|


/var key=do No|
/var key=variableName "sexualNotes"|
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
	/setvar key=genSettings {}|
	/setvar key=genSettings index=wi_book "CMC Rules"|
	/setvar key=keys []|
	/addvar key=keys "Sexual Narration Rules"|
	/ife (user == 'Yes') {:
		/addvar key=keys "Sexual --User-- Rules"|
	:}|
	/ife ((gender == 'Female') or (futanari == 'Yes')) {:
		/addvar key=keys "Sexual Female Rules"|
	:}|
	/ife ((gender == 'Male') or (futanari == 'Yes')) {:
		/addvar key=keys "Sexual Male Rules"|
	:}|
	
	/setvar key=genSettings index=wi_book_key {{getvar::keys}}|
	/flushvar keys|
	/setvar key=genSettings index=combineLorebookEntries Yes|
	/setvar key=genSettings index=genIsSentence No|
	/setvar key=genSettings index=inputIsList No|
	/setvar key=genSettings index=genIsList Yes|
	/setvar key=genSettings index=outputIsList No|
	/setvar key=genSettings index=needOutput No|
	/setvar key=genSettings index=useContext No|
	/wait {{getvar::wait}}|
	
	
	/getvar key=genSettings index=wi_book_key|
	/let key=wi_book_key {{pipe}}|
	/getvar key=genSettings index=inputIsList|
	/let key=inputIsList {{pipe}}|
	/getvar key=genSettings index=combineLorebookEntries|
	/let key=combineLorebookEntries {{pipe}}|
	
	
	/ife ( inputIsList == 'Yes') {:
		/setvar key={{var::variableName}} []|
		/ife ( combineLorebookEntries == 'Yes') {:
			/:"CMC Logic.Combine List Lorebooks"|
		:}|
		/foreach {{getvar::genOrder}} {:
			/setvar key=it {{var::item}}|
			/getat index={{var::index}} {{var::genOrderContent}} |
			/setvar key=genSettings index=content {{pipe}}|
			/:"CMC Logic.GenerateWithSelector"|
			/ife (output != '') {:
				/addvar key={{var::variableName}} {{getvar::output}}|
			:}|
		:}|
	:}|
	/else {:
		/getvar key=genSettings index=wi_book_key|
		/setvar key=it {{pipe}}|
		/setvar key=genSettings index=buttonPrompt "Select the Sexual Rules you want {{getvar::firstName}} to have."|
		/:"CMC Logic.GenerateWithSelector"|
		/ife (output != '') {:
			/setvar key={{var::variableName}} {{getvar::output}}|
		:}|
		
	:}|
	/addvar key=dataBaseNames {{var::variableName}}|
	/flushvar output|
	/flushvar genOrder|
	/flushvar genContent|
	/flushvar it|
	/flushvar genSettings|
:}|
/else {:
	/addvar key=dataBaseNames {{var::variableName}}|
:}|

/var key=do No|
/buttons labels=["Yes", "No"] Do you want to generate or add more sexual Rules?|
/var key=do {{pipe}}|
/ife (do == '') {:
	/echo Aborting |
	/abort
:}|

/ife ( do == 'Yes' ) {:
	/setvar key=genSettings {}|
	/setvar key=genSettings index=wi_book_key "Sexual Notes"|
	/setvar key=genSettings index=genIsList No|
	/setvar key=genSettings index=inputIsList No|
	/setvar key=genSettings index=genIsSentence Yes|
	/setvar key=genSettings index=needOutput Yes|
	/setvar key=genSettings index=outputIsList Yes|
	/setvar key=genSettings index=useContext Yes|
	/setvar key=extra []|
	/addvar key=extra "- Setting Type: {{getvar::settingType}}"|
	/addvar key=extra "- Main Personality Trait: {{getvar::personalityMainTrait}}"| 
	/addvar key=extra "- Personality Tags: {{getvar::personalityFoundTags}}, {{getvar::personalityTags}}"|
	/addvar key=extra "{{getvar::parsedSexualOrientation}}"|
	/addvar key=extra "{{getvar::parsedSexualRole}}"|
	/addvar key=extra "- Libido: {{getvar::sexualLibido}}"|
	/ife (parsedSexualKinks != 'None') {:
		/addvar key=extra "{{getvar::parsedSexualKinks}}"|
	:}|
	/ife (parsedSexualItems != 'None') {:
		/addvar key=extra "{{getvar::parsedSexualItems}}"|
	:}|
	/ife (parsedSexualAbilities != 'None') {:
		/addvar key=extra "{{getvar::parsedSexualAbilities}}"|
	:}|
	/setvar key=genSettings index=extraContext {{getvar::extra}}|
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
	
	
	
	//[[Generate with Prompt]]|
	/setvar key=blackListGen {{noop}}|
	/:"CMC Logic.GenerateWithPrompt"|
	/foreach {{getvar::output}} {:
		/addvar key={{var::variableName}} {{var::item}}|
	:}|
	
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

/setvar key=parsedSexualityNotes {{noop}}|
/ife (sexualNotes is list) {:
	/foreach {{getvar::sexualNotes}} {:
		/ife (index > 0) {:
			/addvar key=parsedSexualityNotes {{newline}}|
		:}|
		/addvar key=parsedSexualityNotes "- {{var::item}}"|
	:}|
:}|
//--------|


/:"CMC Logic.JEDParse"|

/:"CMC Logic.Save DataBase"|

/setvar key=stepDone Yes|
/qr-list CMC Main|
/getat index=1 {{pipe}}|
/var qrlabel {{pipe}}|
/qr-get set="CMC Main" label={{var::qrlabel}}|
/getat index="message" {{pipe}}|
/qr-update set="CMC Main" label={{var::qrlabel}} newlabel="Start Generating Extras" {{pipe}}|
/forcesave|