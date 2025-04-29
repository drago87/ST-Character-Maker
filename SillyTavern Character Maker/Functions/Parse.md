/re-replace find="/\b{{char}}\b\|--FirstName--/g" replace="{\\\\\{char}}" {{getvar::t}}|
/re-replace find="/\b{{user}}\b\|--User--/g" replace="{\\\\{user}}" {{pipe}}|
/return {{pipe}}|