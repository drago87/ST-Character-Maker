/*
/echo timeout=0 extendedTimeout=0 awaitDismissal=true Test|

/genraw **CONTEXT (for your reference—do not include in the answer):**
- Name: Suzuki Suzuki
- Life Stage: Teen
- Age: 20 years-old — roughly 18 years-old in human years.
- Gender: Female
- Species: Kemonomimi T-rex
- Intelligence Level: Dumb
- Social Behavior: Innocent

**EXAMPLES (for your reference—do not include in the answer):**

**Example: Unique Trait**
Phantom Pain, Cum Craving, Succubi Feeding Frenzy Trance, Womb Seal Brand, Cute Moan Reflex, Pet Mode, Lewd Surge

**TASK:**  
Generate a list of potential unique traits that describe unusual states, mental conditions, curses, or compulsive cravings — each one should suggest both a clear trigger and a behavioral or physical effect.

**INSTRUCTIONS:**  
1. Output a single line of **comma-separated** trait names.  
2. Each trait should sound like a **named condition, curse, transformation, or craving** — something that could be triggered and would change how the character behaves or feels.  
3. Aim for traits that **imply both a cause and a consequence** (e.g., “Cum Craving” implies a sensory trigger and obsessive effect; “Womb Seal Brand” suggests internal pressure and resistance to release).  
4. Use 2–5 words per trait. Names should be stylized but not vague.  
5. Avoid vague metaphors (e.g., “Ink Vortex”) or items without emotional or mystical context (e.g., “Sketchbook Spellbook”).  
6. Avoid personality summaries or tags (e.g., “Playful Curiosity”, “Dumb Urge”).  
7. You may draw inspiration from altered mental states, magical rituals, bodily transformations, cravings, or trauma responses — but stylize them into evocative names.  
8. Only output the list — no labels, commentary, or formatting. Do **not** end with a comma.|
/setvar key=00a {{pipe}}|

/split {{getvar::00a}}|
/buttons multiple=true labels={{pipe}} Test|
/setvar key=00b {{pipe}}|
/foreach {{getvar::00b}} {:
	/setvar key=uniqueTraitsEffectsItem {{var::item}}|
	/genraw **CONTEXT (for your reference—do not include in the answer):**
- Name: Suzuki Suzuki
- Life Stage: Teen
- Age: 20 years-old — roughly 18 years-old in human years.
- Gender: Female
- Species: Kemonomimi T-rex

- Archetype: Playful Tomboy who always carries a sketchbook
  ↳ Archetype Details: Suzuki, a playful teenage T-rex kemonomimi with a sketchbook always in tow, often charges into spontaneous adventures fueled by her boundless curiosity.
  ↳ Reasoning: As an only child growing up, Suzuki developed a sketchbook to cope with feelings of isolation and a craving for adventure.

- Alignment: Chaotic good
  ↳ Alignment Details: Suzuki's alignment is Chaotic good - as a young, curious and adventurous T-rex with a playful tomboy streak, her creative spirit often leads her to pursue her interests (like drawing in her sketchbook)
  ↳ Ideals: Suzuki, being chaotically good, lives by the ideal of letting curiosity lead her to explore new worlds in her drawings and beyond, embracing a playful and adventurous spirit.

- Intelligence Level: Dumb
- Cognitive Abilities: Suzuki approaches the world with an infectious enthusiasm and curiosity, even if she often struggles to comprehend more complex concepts or follow multi-step instructions.

- Social Behavior: Innocent
- Social Skills and Integration Into Society: In social situations, Suzuki approaches others with a disarming innocence and eagerness to connect. Her playful, curious nature draws people in, though her childlike exuberance can sometimes leave her a bit naive.
  
  **EXAMPLES (for your reference—do not include in the answer):**

**Example: Succubi Feeding Frenzy Trance**  
As soon as a drop of cum touches her tongue, her mind shifts into an uncontrollable trance — a feeding frenzy. Her pupils dilate, her breathing quickens, and she no longer thinks — only acts.  

**Example: Womb Whisper Trigger**
If her internals are being stretched or under pressure causes her unfiltered inner thoughts to leak out verbally; moans, fantasies, or emotional confessions emerge involuntarily

**Example: Cum Craving**
The smell of cum..

**Example: Desire Overload**
When triggered, Suzuki becomes fixated on satisfying a sudden, overpowering urge — whether for touch, attention, or sensation. Her thoughts spiral toward the object of desire, and she struggles to focus on anything else until the craving gets an outlet.

**Example: Fetish Frenzy**
A surge of obsessive energy overtakes her whenever the trait is triggered, narrowing her thoughts onto a single indulgence or fantasy. During this time, she becomes excitable, unfocused, and driven by impulse more than reason.

**TASK:**  
Describe how {{getvar::uniqueTraitsEffectsItem}} affects {{getvar::firstName}} when triggered — include both what causes it and what happens.

**INSTRUCTIONS:**  
1. Start by describing **what triggers** {{getvar::uniqueTraitsEffectsItem}} — what type of emotion, stimulus, contact, or context sets it off.  
2. Then describe the **effect** on {{getvar::firstName}}’s mind, body, or behavior.  
3. Write in a concise, neutral tone as if for a character sheet — not like a story or scene.  
4. Limit the full response to **2–3 clear sentences**, combining trigger and outcome.  
5. Do **not** repeat or reformat the trait name.   
6. Do **not** include bullet points, formatting, or labels — just the raw descriptive text.|
/setvar key=00c{{var::index}}{{var::item}}|
:}|
/flushvar uniqueTraitsEffectsItem|

/listvar scope=local return=object |
/let as=array key=flvars {{pipe}}|
/foreach {{var::flvars}} {:
	/getat index=key {{var::item}}|
	/let key=t {{pipe}}|
	/ife ('00c' in t) {:
		/flushvar {{var::t}}|
	:}|
:}|


*|


/let key=do No|
/let key=variableName "personalityQA"|
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
	/setvar key=genSettings index=wi_book_key "Personality QA"|
	/setvar key=genSettings index=genIsList No|
	/setvar key=genSettings index=inputIsTaskList No|
	/setvar key=genSettings index=inputIsList Yes|
	/setvar key=genSettings index=genIsSentence Yes|
	/setvar key=genSettings index=needOutput Yes|
	/setvar key=genSettings index=outputIsList No|
	/setvar key=genSettings index=useContext No|
	/setvar key=extra []|
	/addvar key=extra "{{newline}}{{getvar::parsedArchetype}}"|
	/ife (parsedAlignment != 'None') {:
		/addvar key=extra "{{newline}}{{getvar::parsedAlignment}}{{newline}}"|
	:}|
	/addvar key=extra "- Intelligence Level: {{getvar::intelligenceLevel}}"|
	/ife (cognitiveAbilities != 'None') {:
		/addvar key=extra "- Cognitive Abilities: {{getvar::cognitiveAbilities}}{{newline}}"|
	:}|
	/addvar key=extra "- Social Behavior: {{getvar::socialBehavior}}"|
	/ife (socialSkills != 'None') {:
		/addvar key=extra "- Social Skills and Integration Into Society: {{getvar::socialSkills}}{{newline}}"|
	:}|
	/addvar key=extra "{{newline}}{{getvar::parsedAspiration}}"|
	/setvar key=genSettings index=extraContext {{getvar::extra}}|
	/flushvar extra|
	/setvar key=genSettings index=contextKey []|
	/wait {{getvar::wait}}|
	
	
	/ife (qestions == '') {: 
		/findentry field=comment file="CMC Questions" "Personality: Q"|
		/let key=wi_uid {{pipe}}|
		/getentryfield field=content file="CMC Questions" {{var::wi_uid}}|
		/let key=unfilteredQuestions {{pipe}}|
		/split find="/\n/" {{var::unfilteredQuestions}}|
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
	/ife (inputIsList == 'Yes') {:
		/let key=tempQ []|
		/foreach {{getvar::qestions}} {:
			/setvar key=question {{var::item}}|
			/:"CMC Logic.GenerateWithPrompt"|
			/len tempQ|
			/setat index={{pipe}} key=tempQ Q: {{getvar::question}}{{newline}}A: {{getvar::output}}|
			/flushvar output|
		:}|
		/setvar key={{var::variableName}} {{var::tempQ}}|
		/flushvar question|
	:}|
	/else {:
		/:"CMC Logic.GenerateWithPrompt"|
		/setvar key={{var::variableName}} {{getvar::output}}|
	:}|
	/addvar key=dataBaseNames {{var::variableName}}|
	/flushvar output|
	/flushvar genOrder|
	/flushvar genContent|
	/flushvar genSettings|
:}|
/else {:
	/addvar key=dataBaseNames {{var::variableName}}|
:}|
//--------|
/*
genIsList = No
inputIsTaskList = No
inputIsList = Yes
genIsSentence = Yes
needOutput = Yes
outputIsList = No
useContext = No
*|