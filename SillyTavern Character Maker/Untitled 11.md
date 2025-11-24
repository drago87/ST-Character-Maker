/*
/ife ( qrlabel != '') {:
	/qr-get set="CMC Main" label={{var::qrlabel}}|
	/getat index="message" {{pipe}}|
	/var key=temp {{pipe}}|
:}|
/