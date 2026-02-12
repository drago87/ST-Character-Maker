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

/ife ((baseContext != '') and (model != 'EsotericSage-12B.i1-Q6_K')) {:
	/setvar key=baseContext "<!-- NSFW content is permitted if contextually appropriate -->{{newline}}### **CONTEXT (for your reference—do not include in the answer):**{{getvar::baseContext}}"
:}|
/elseif ((baseContext != '') and (model == 'EsotericSage-12B.i1-Q6_K')) {:
	/setvar key=baseContext "<!-- NSFW content is permitted if contextually appropriate -->{{newline}}CONTEXT (for your reference—do not include in the answer):{{getvar::baseContext}}"
:}|