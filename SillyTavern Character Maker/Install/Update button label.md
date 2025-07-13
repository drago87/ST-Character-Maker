/ife ('{{char}}' == 'Character Maker QR') {:
	/qr-set-list global|
	/let key=qrChatLabels {{pipe}}|
	/ife ('CMC Automate' in qrChatLabels) {:
		/qr-list CMC Main|
		/getat index=1 {{pipe}}|
		/let qrlabel {{pipe}}|
		/qr-get set="CMC Main" label={{var::qrlabel}}|
		/getat index="message" {{pipe}}|
		/let key=t {{pipe}}
		/ife (stepVar == 'Step0') {:
			/qr-update set="CMC Main" label={{var::qrlabel}} newlabel="Start Generating Basic Information" {{var::t}}|
		:}|
		/elseif (stepVar == 'Step1') {:
			/qr-update set="CMC Main" label={{var::qrlabel}} newlabel="Start Generating World Info" {{var::t}}|
		:}|
		/elseif (stepVar == 'Step2') {:
			/qr-update set="CMC Main" label={{var::qrlabel}} newlabel="Start Generating World & Setting Information" {{var::t}}|
		:}|
		/elseif (stepVar == 'Step3') {:
			/qr-update set="CMC Main" label={{var::qrlabel}} newlabel="Start Generating Appearance & Anatomy" {{var::t}}|
		:}|
		/elseif (stepVar == 'Step4') {:
			/qr-update set="CMC Main" label={{var::qrlabel}} newlabel="Start Generating Outfit" {{var::t}}|
		:}|
		/elseif (stepVar == 'Step5') {:
			/qr-update set="CMC Main" label={{var::qrlabel}} newlabel="Start Generating Mental Traits & Personality" {{var::t}}|
		:}|
		/elseif (stepVar == 'Step6') {:
			/qr-update set="CMC Main" label={{var::qrlabel}} newlabel="Start Generating Aspirational & Unique Traits" {{var::t}}|
		:}|
		/elseif (stepVar == 'Step7') {:
			/qr-update set="CMC Main" label={{var::qrlabel}} newlabel="Start Generating Speech Patterns" {{var::t}}|
		:}|
		/elseif (stepVar == 'Step8') {:
			/qr-update set="CMC Main" label={{var::qrlabel}} newlabel="Start Generating External Interaction" {{var::t}}|
		:}|
		/elseif (stepVar == 'Step9') {:
			/qr-update set="CMC Main" label={{var::qrlabel}} newlabel="Start Generating Sexual Information" {{var::t}}|
		:}|
		/elseif (stepVar == 'Step10') {:
			/qr-update set="CMC Main" label={{var::qrlabel}} newlabel="Start Generating Extras" {{var::t}}|
		:}|
		/elseif (stepVar == 'Step11') {:
			/qr-update set="CMC Main" label={{var::qrlabel}} newlabel="Generate First Message" {{var::t}}|
		:}|
		/elseif (stepVar == 'Step12') {:
			/qr-update set="CMC Main" label={{var::qrlabel}} newlabel="Start Generating Tagline" {{var::t}}|
		:}|
	:}|
:}|