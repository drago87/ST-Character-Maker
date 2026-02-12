/wi-list-books all=true|
/let key=lorebookList {{pipe}}|
/setvar key=cur 0|
/let counter {: max=12 
	/incvar cur|
	/echo {{getvar::cur}}/{{var::max}}|
:}|


/ife ( 'CMC Appearance' not in lorebookList) {:
	/echo Creating Lorebook "CMC Appearance"|
	/getchatbook name="CMC Appearance"|
	/let key=wi_appearance|
	/wait 100|
	/:counter|
	/createentry file={{var::wi_appearance}} key="Female Hairstyle" Single Braid: Pixie Cut|
	/setentryfield file={{var::wi_appearance}} uid={{pipe}} field=key {{noop}}|
	/wait 100|
	/:counter|
	/createentry file={{var::wi_appearance}} key="Female Brest Size" Flat: Small: Medium: Large: Huge|
	/setentryfield file={{var::wi_appearance}} uid={{pipe}} field=key {{noop}}|
	/wait 100|
	/:counter|
	/createentry file={{var::wi_appearance}} key="Female Pussy Type" Curved outer lips (The outer lips have a curved magnet-like shape, meeting at the bottom. This shape will create a window in the middle revealing the inner lips.): Prominent inner lips (The inner lips are larger than the outer lips.): Prominent outer lips (The outer lips are larger than the inner lips. They tend to sit lower on the vulva and may extend beyond underwear. Both full and puffy outer lips, as well as thin and loose outer lips, can fit into this category.): Long, dangling inner lips (The inner lips are longer than the outer lips and seem to dangle from the vulva. These inner lips can be an inch long or longer, or they may look like there's extra skin or folds.): Long, dangling outer lips (The outer lips are longer than the inner lips. This is a form of prominent outer lips, though this structure, in particular, tends to involve thinner or looser outer lips that may extend beyond underwear.): Small, closed lips (In some vulvas, "the labia majora and the labia minora blend together so it's not really like two sets of lips; it's more like one,". While they are technically two separate parts, the outer lips are closed so that they conceal the inner lips.): Small, open lips (With this type of vulva, the outer lips are small, but they're set farther apart making them appear slightly open.): Visible inner lips (The outer lips appear curved or pulled outward, leaving almost a window for the inner lips to peek through.)|
	/setentryfield file={{var::wi_appearance}} uid={{pipe}} field=key {{noop}}|
	/wait 100|
	/:counter|
	/createentry file={{var::wi_appearance}} key="Male Penis Size Flaccid" Small: Medium: Large: Huge|
	/setentryfield file={{var::wi_appearance}} uid={{pipe}} field=key {{noop}}|
	/wait 100|
	/:counter|
	/createentry file={{var::wi_appearance}} key="Male Penis Size Erect" Small: Medium: Large: Huge|
	/setentryfield file={{var::wi_appearance}} uid={{pipe}} field=key {{noop}}|
	/wait 100|
	/:counter|
	/createentry file={{var::wi_appearance}} key="Male Hairstyle" Buzzcut|
	/setentryfield file={{var::wi_appearance}} uid={{pipe}} field=key {{noop}}|
	/wait 100|
	/:counter|
	/createentry file={{var::wi_appearance}} key="Butt Size" Small: Medium: Large: Huge|
	/setentryfield file={{var::wi_appearance}} uid={{pipe}} field=key {{noop}}|
	/wait 100|
	/:counter|
	/createentry file={{var::wi_appearance}} key="Hair Color" Black: Brown: Blond: Red|
	/setentryfield file={{var::wi_appearance}} uid={{pipe}} field=key {{noop}}|
	/wait 100|
	/:counter|
	/createentry file={{var::wi_appearance}} key="Hair Length" Bald: Short: Medium: Long|
	/setentryfield file={{var::wi_appearance}} uid={{pipe}} field=key {{noop}}|
	/wait 100|
	/:counter|
	/createentry file={{var::wi_appearance}} key="Skin Color" Creamy: White: Brown|
	/setentryfield file={{var::wi_appearance}} uid={{pipe}} field=key {{noop}}|
	/wait 100|
	/:counter|
	/createentry file={{var::wi_appearance}} key="Iris Color" Green: Blue: Brown|
	/setentryfield file={{var::wi_appearance}} uid={{pipe}} field=key {{noop}}|
	/wait 100|
	/:counter|
	/createentry file={{var::wi_appearance}} key="Sclera Color" White: Red: Green: Blue: Brown|
	/setentryfield file={{var::wi_appearance}} uid={{pipe}} field=key {{noop}}|
:}|
/popup Make sure to remove the Chat lore that is bound to this chat by opening the character and pressing the <i class="fa-solid fa-passport"></i> (Chat Lore) button. The browser page will reload when you press ok.|
/reload-page