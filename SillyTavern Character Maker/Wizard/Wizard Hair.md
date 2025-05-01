/let getEntry {: entry= hairS= 
	/let x {{var::hairS}}|
	/let y {{var::entry}}|
	/findentry field=comment file="CMC Appearance" {{var::y}}|
	/getentryfield field=content file="CMC Appearance" {{pipe}}|
	/split find="/\n/" {{pipe}}|
	/let key=a {{pipe}}|
	/wait 1|
	/find index=true {{var::a}} {:
		/test left={{var::item}} rule=in right={{var::x}}|
	:}|
	/getat index={{pipe}} {{var::a}}|
	/split find="/{{var::x}}:/g" {{pipe}}|
	/var key=a {{pipe}}|
	/wait 1|
	/getat index=1 {{var::a}}|
	/return {{pipe}}|
:}||

/let lenghtList {{noop}}|
/let hairLength {{noop}}|
/let styleList {{noop}}|
/let hairStyle {{noop}}|
/let textureList {{noop}}|
/let hairTexture {{noop}}|
/let hairColor {{noop}}|
/let colorList {{noop}}|


/wizard title="Hair Generation" {:
	/wiz-nav prev=true next=false stop=true|
	/wiz-page title=Lenght {:
		/wiz-page-text Select the Hair length you want|
		/findentry field=comment file="CMC Appearance" Hair Length|
		/getentryfield file="CMC Appearance" {{pipe}}|
		/split find=":" {{pipe}}|
		/var key=lenghtList {{pipe}}|
		/wait 100|
		/foreach {{var::lenghtList}} {:
			/wiz-page-button small=true label={{var::item}} {: /var key=hairLength {{var::item}}| /wiz-cmd-next| :}|
		:}|
	:}|
	/wiz-page title="Hairstyle" {:
		/wiz-page-text Select the Hairstyle you want. You have selected {{var:hairLength}}|
		/findentry field=comment file="CMC Appearance" Hairstyle: {{var::hairLength}}|
		/getentryfield file="CMC Appearance" {{pipe}}|
		/split find=":" {{pipe}}|
		/var key=styleList {{pipe}}|
		/wait 100|
		/foreach {{var::styleList}} {:
			/wiz-page-button small=true label={{var::item}} {: /var key=hairStyle {{var::item}}| /wiz-cmd-next| :}|
		:}|
	:}|
	/wiz-page title="Hair texture" {:
		/wiz-page-text Select the Hair texture you want. You have selected {{var:hairLength}} and {{var:hairStyle}}|
		/:getEntry hairS={{var::hairStyle}} entry="Hair texture"|
		/split find=":" {{pipe}}|
		/var key=textureList {{pipe}}|
		/wait 100|
		/foreach {{var::textureList}} {:
			/wiz-page-button small=true label={{var::item}} {: /var key=hairTexture {{var::item}}| /wiz-cmd-next| :}|
		:}|
	:}|
	/wiz-page title=Color {:
		/wiz-page-text Select the Hair Color you want|
		/findentry field=comment file="CMC Appearance" Hair Color|
		/getentryfield file="CMC Appearance" {{pipe}}|
		/split find=":" {{pipe}}|
		/var key=colorList {{pipe}}|
		/foreach {{getvar::colorList}} {:
			/wiz-page-button small=true label={{var::item}} {: /var key=hairColor {{var::item}}| /wiz-cmd-next| :}|
		:}|
	:}|
	/wiz-after {:
		/setvar key=hairLength {{wizvar::hairLength}}|
		/setvar key=hairColor {{wizvar::hairColor}}|
	:}|
:}|