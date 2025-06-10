/ife ('{{char}}' == 'Character Maker QR') {:
	/qr-set-list chat|
	/let key=qrChatLabels {{pipe}}|
	/ife ('CMC Main' not in qrChatLabels) {:
		/qr-chat-set-on CMC Main|
	:}|
:}|