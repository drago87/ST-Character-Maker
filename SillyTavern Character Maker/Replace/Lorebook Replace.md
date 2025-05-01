/re-replace find="/\b{{char}}\b\|--FirstName--\|{{ char}}/g" replace="{/{char}}" {{getvar::t}}|
/re-replace find="/\b{{user}}\b\|--User--\|{{ user}}/g" replace="{/{user}}" {{pipe}}||