/*
Step0 Generate Basic information
Step1 Generate Core Identity
Step2 Generate World-Setting Information
Step3 Generate Appearance-Anatomy
Step4 Generate Mental Traits-Personality
Step5 Generate Aspirational-Unique Traits
Step6 Generate Speech Patterns
Step7 Generate External Interaction
Step8 Generate Sexual Information
Step9 Generate Extras
*|

/ife ( (stepVar == 'Step0') or (stepVar == '')) {:
	/ife (stepDone == 'Yes') {:
		//Load Step1|
		/:"CMC Generate.Step1 Generate Core Identity"|
	:}|
	/else {:
		//Load Step0|
		/:"CMC Main.New Character"|
	:}|
:}|
/elseif ( stepVar == 'Step1') {:
	/ife (stepDone == 'Yes') {:
		//Load Step2|
		/:"CMC Generate.Step2 Generate World-Setting Information"|
	:}|
	/else {:
		//Load Step1|
		/:"CMC Generate.Step1 Generate Core Identity"|
	:}|
:}|
/elseif ( stepVar == 'Step2') {:
	/ife (stepDone == 'Yes') {:
		//Load Step3|
		/:"CMC Generate.Step3 Generate Appearance-Anatomy"|
	:}|
	/else {:
		//Load Step2|
		/:"CMC Generate.Step2 Generate World-Setting Information"|
	:}|
:}|
/elseif ( stepVar == 'Step3') {:
	/ife (stepDone == 'Yes') {:
		//Load Step4|
		/:"CMC Generate.Step4 Generate Mental Traits-Personality"|
	:}|
	/else {:
		//Load Step3|
		/:"CMC Generate.Step3 Generate Appearance-Anatomy"|
	:}|
:}|
/elseif ( stepVar == 'Step4') {:
	/ife (stepDone == 'Yes') {:
		//Load Step5|
		/:"CMC Generate.Step5 Generate Aspirational-Unique Traits"|
	:}|
	/else {:
		//Load Step4|
		/:"CMC Generate.Step4 Generate Mental Traits-Personality"|
	:}|
:}|
/elseif ( stepVar == 'Step5') {:
	/ife (stepDone == 'Yes') {:
		//Load Step6|
		/:"CMC Generate.Step6 Generate Speech Patterns"|
	:}|
	/else {:
		//Load Step5|
		/:"CMC Generate.Step5 Generate Aspirational-Unique Traits"|
	:}|
:}|
/elseif ( stepVar == 'Step6') {:
	/ife (stepDone == 'Yes') {:
		//Load Step7|
		/:"CMC Generate.Step7 Generate External Interaction"|
	:}|
	/else {:
		//Load Step6|
		/:"CMC Generate.Step6 Generate Speech Patterns"|
	:}|
:}|
/elseif ( stepVar == 'Step7') {:
	/ife (stepDone == 'Yes') {:
		//Load Step8|
		/:"CMC Generate.Step8 Generate Sexual Information"|
	:}|
	/else {:
		//Load Step7|
		/:"CMC Generate.Step7 Generate External Interaction"|
	:}|
:}|
/elseif ( stepVar == 'Step8') {:
	/ife (stepDone == 'Yes') {:
		//Load Step9|
		/:"CMC Generate.Step9 Generate Extras"|
	:}|
	/else {:
		//Load Step8|
		/:"CMC Generate.Step8 Generate Sexual Information"|
	:}|
:}|
/elseif ( stepVar == 'Step9') {:
	/ife (stepDone == 'Yes') {:
		//Load Step10|
		//:"CMC Generate."|
	:}|
	/else {:
		//Load Step9|
		/:"CMC Generate.Step9 Generate Extras"|
	:}|
:}|
/elseif ( stepVar == 'Step10') {:
	/ife (stepDone == 'No') {:
		//Load Step10|
		//:"CMC Generate."|
	:}|
:}|