/setvar key=settingModifier {Modifier}|
/setvar key=settingArchetype {Archetype}|
/setvar key=settingAddition {Addition}|
//task and instruct is pulled from a WI in the real code|
/let key=task **TASK:**  
Generate a short sentence using the following structure:  
'{{getvar::settingModifier}} {{getvar::settingArchetype}} {{getvar::settingAddition}}'|
/let key=instruct **INSTRUCTIONS:**  
1. Use the exact **values** provided for each part:  
   - {{getvar::settingModifier}}  
   - {{getvar::settingArchetype}}  
   - {{getvar::settingAddition}}  
2. Do not reinterpret, alter, or mix these values. Simply place them together in a coherent sentence.  
3. If no value is provided for any part, you are free to generate creative alternatives for that missing part.  
4. Only output the resulting sentence — no additional explanation or information.|
/whilee ( output == '') {:
	//Same here task and instruct is pulled from a WI|
	/var key=task **TASK:**  
Generate a short sentence using the following structure:  
'{{getvar::settingModifier}} {{getvar::settingArchetype}} {{getvar::settingAddition}}'|
	/var key=instruct **INSTRUCTIONS:**  
5. Use the exact **values** provided for each part:  
   - {{getvar::settingModifier}}  
   - {{getvar::settingArchetype}}  
   - {{getvar::settingAddition}}  
2. Do not reinterpret, alter, or mix these values. Simply place them together in a coherent sentence.  
3. If no value is provided for any part, you are free to generate creative alternatives for that missing part.  
4. Only output the resulting sentence — no additional explanation or information.|
	
	/setvar key=genState []|
	/genraw length=50 "{{var::task}}{{newline}}{{newline}}{{var::instruct}}"|
	/addvar key=genState {{pipe}}|
	/addvar key=genState Generate new|
	/addvar key=genState ChangeVariables
	
	/buttons labels={{getvar::genState}} Select|
	/setvar temp {{pipe}}|
	
	Do Suff and change {{getvar::settingModifier}} {{getvar::settingArchetype}} {{getvar::settingAddition}}
	
:}|