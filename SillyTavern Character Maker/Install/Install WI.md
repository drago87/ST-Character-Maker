/wi-list-books all=true|
/setvar key=lorebookList {{pipe}}|
//---------|

/ife ( 'CMC Clothes' not in lorebookList) {:
  /getchatbook name="CMC Clothes"|
  /setvar key=wi_clothes {{pipe}}|
  /createentry file={{getvar::wi_clothes}} key="Female Underwear Top" Bare: Bra: Sports Bra: Bralette: Camisole: Crop Top: Training Bra|
  /setentryfield file={{getvar::wi_clothes}} uid={{pipe}} field=key {{noop}}|
  /createentry file={{getvar::wi_clothes}} key="Female Underwear Bottom" Bare: Panties: Bloomer: Thong: Bikini: Briefs: Boyshorts: Hipster|
  /setentryfield file={{getvar::wi_clothes}} uid={{pipe}} field=key {{noop}}|
  /createentry file={{getvar::wi_clothes}} key="Female Clothes Top" Bare: Shirt: Blouse: T-Shirt: Tank Top: Crop Top: Sweater: Hoodie: Cardigan: Camisole: Tunic: Button-Up Shirt: Bikini Top|
  /setentryfield file={{getvar::wi_clothes}} uid={{pipe}} field=key {{noop}}|
  /createentry file={{getvar::wi_clothes}} key="Female Clothes Bottom" Bare: Skirt: Skirt: Pants: Jeans: Leggings: Shorts: Culottes: Trousers: Capris: Joggers: Palazzo Pants: Bikini Bottom|
  /setentryfield file={{getvar::wi_clothes}} uid={{pipe}} field=key {{noop}}|
  /createentry file={{getvar::wi_clothes}} key="Female Clothes Extra" Pantyhose: Thigh Highs|
  /setentryfield file={{getvar::wi_clothes}} uid={{pipe}} field=key {{noop}}|
  /createentry file={{getvar::wi_clothes}} key="Female Clothes One-Piece" Bare: Dress: One-Piece Swimsuit|
  /setentryfield file={{getvar::wi_clothes}} uid={{pipe}} field=key {{noop}}|
  /createentry file={{getvar::wi_clothes}} key="Male Underwear Bottom" Bare: Boxers: Briefs: Boxer Briefs: Trunks: Jockstraps|
  /setentryfield file={{getvar::wi_clothes}} uid={{pipe}} field=key {{noop}}|
  /createentry file={{getvar::wi_clothes}} key="Male Clothes Top" Bare: Shirt: Sweater|
  /setentryfield file={{getvar::wi_clothes}} uid={{pipe}} field=key {{noop}}|
  /createentry file={{getvar::wi_clothes}} key="Male Clothes Bottom" Bare: Pants: Shorts|
  /setentryfield file={{getvar::wi_clothes}} uid={{pipe}} field=key {{noop}}|
  /createentry file={{getvar::wi_clothes}} key="Clothes Socks" Barefoot: Ankle Socks: Normal Socks: Knee Socks|
  /setentryfield file={{getvar::wi_clothes}} uid={{pipe}} field=key {{noop}}|
  /createentry file={{getvar::wi_clothes}} key="Clothes Hat" Bare: Cuffed Beanie: Peaked Cap|
  /setentryfield file={{getvar::wi_clothes}} uid={{pipe}} field=key {{noop}}|
:}|
//---------|

//---------|

/ife ( 'CMC Appearance' not in lorebookList) {:
	/getchatbook name="CMC Appearance"|
	/setvar key=wi_appearance|
	/createentry file={{getvar::wi_appearance}} key="Female Hairstyle" Single Braid: Pixie Cut|
	/setentryfield file={{getvar::wi_clothes}} uid={{pipe}} field=key {{noop}}|
	/createentry file={{getvar::wi_appearance}} key="Female Brest Size" Flat: Small: Medium: Large: Huge|
	/setentryfield file={{getvar::wi_clothes}} uid={{pipe}} field=key {{noop}}|
	/createentry file={{getvar::wi_appearance}} key="Female Pussy Type" Curved outer lips (The outer lips have a curved magnet-like shape, meeting at the bottom. This shape will create a window in the middle revealing the inner lips.): Prominent inner lips (The inner lips are larger than the outer lips.): Prominent outer lips (The outer lips are larger than the inner lips. They tend to sit lower on the vulva and may extend beyond underwear. Both full and puffy outer lips, as well as thin and loose outer lips, can fit into this category.): Long, dangling inner lips (The inner lips are longer than the outer lips and seem to dangle from the vulva. These inner lips can be an inch long or longer, or they may look like there's extra skin or folds.): Long, dangling outer lips (The outer lips are longer than the inner lips. This is a form of prominent outer lips, though this structure, in particular, tends to involve thinner or looser outer lips that may extend beyond underwear.): Small, closed lips (In some vulvas, "the labia majora and the labia minora blend together so it's not really like two sets of lips; it's more like one,". While they are technically two separate parts, the outer lips are closed so that they conceal the inner lips.): Small, open lips (With this type of vulva, the outer lips are small, but they're set farther apart making them appear slightly open.): Visible inner lips (The outer lips appear curved or pulled outward, leaving almost a window for the inner lips to peek through.)|
	  /setentryfield file={{getvar::wi_clothes}} uid={{pipe}} field=key {{noop}}|
	  /createentry file={{getvar::wi_appearance}} key="Male Penis Size Flaccid" Small: Medium: Large: Huge|
	  /setentryfield file={{getvar::wi_clothes}} uid={{pipe}} field=key {{noop}}|
	  /createentry file={{getvar::wi_appearance}} key="Male Penis Size Erect" Small: Medium: Large: Huge|
	  /setentryfield file={{getvar::wi_clothes}} uid={{pipe}} field=key {{noop}}|
	  /createentry file={{getvar::wi_appearance}} key="Male Hairstyle" Buzzcut|
	  /setentryfield file={{getvar::wi_clothes}} uid={{pipe}} field=key {{noop}}|
	  /createentry file={{getvar::wi_appearance}} key="Butt Size" Small: Medium: Large: Huge|
	  /setentryfield file={{getvar::wi_clothes}} uid={{pipe}} field=key {{noop}}|
	  /createentry file={{getvar::wi_appearance}} key="Hair Color" Black: Brown: Blond: Red|
	  /setentryfield file={{getvar::wi_clothes}} uid={{pipe}} field=key {{noop}}|
	  /createentry file={{getvar::wi_appearance}} key="Hair Length" Bald: Short: Medium: Long|
	  /setentryfield file={{getvar::wi_clothes}} uid={{pipe}} field=key {{noop}}|
	  /createentry file={{getvar::wi_appearance}} key="Skin Color" Creamy: White: Brown|
	  /setentryfield file={{getvar::wi_clothes}} uid={{pipe}} field=key {{noop}}|
	  /createentry file={{getvar::wi_appearance}} key="Iris Color" Green: Blue: Brown|
	  /setentryfield file={{getvar::wi_clothes}} uid={{pipe}} field=key {{noop}}|
	  /createentry file={{getvar::wi_appearance}} key="Sclera Color" White: Red: Green: Blue: Brown|
	  /setentryfield file={{getvar::wi_clothes}} uid={{pipe}} field=key {{noop}}|
:}|
//---------|

//---------|

/ife ( 'CMC Variables' not in lorebookList) {:
	/getchatbook name="CMC Variables"|
	/setvar key=wi_variables|
	
	/fetch https://raw.githubusercontent.com/drago87/ST-Character-Maker/refs/heads/Fetch-Files/Templates/Generation%20Rules%20Template.txt|
	/createentry file={{getvar::wi_variables}} key="Generation Rules" {{pipe}}|
	/setentryfield file={{getvar::wi_variables}} uid={{pipe}} field=key {{noop}}|
	
	/fetch https://raw.githubusercontent.com/drago87/ST-Character-Maker/refs/heads/Fetch-Files/Templates/Character%20Rules%20Template.txt|
	/createentry file={{getvar::wi_variables}} key="Character Rules" {{pipe}}|
	/setentryfield file={{getvar::wi_variables}} uid={{pipe}} field=key {{noop}}|
	
	/createentry file={{getvar::wi_variables}} key="F [CANINE] (1/3) Vagina" [canine pussy: commonly referred to as the "cookie"(colloquial term), located nestled between hindquarters(below the anus(usually concealed or obscured behind the fluff of the tail, tail usually hangs down over anus and pussy(obscuring view), tail needs to be moved or lifted to reveal(unless the tail is curled or docked(depends on the breed)))), When not aroused(Not swollen, Almost flush with the body(unnoticeable)), When aroused(Extends(protrudes(either slightly or exaggeratedly(depends per individual)) from the body(by a couple inches, signaling readiness for insertion of male)), puffed up(takes on a more puffy and swollen appearance(so much so that it can be physically grasped))), Outward appearance(characterized by three thick and plump labia arranged in a triangle which create its unique shape(resembles a rounded and upside-down teardrop in shape(rounded at the top, tapered at the bottom(better recognized as a "spade" shape))), usually much darker in color than rest of body(most commonly entirely black in color), velvety texture(soft to the touch, not covered in fur like the rest of body), puffy(squishy, swollen(when aroused), entrance(or slit) resembles a tight and puffy "Y" shape(three pillowy labia folds(arranged in a triangle)))), Internal appearance(pink(bright pink(akin to the inside of a mouth)), fleshy(soft, squishy, tight, elastic(meant to accommodate canine penises(which are usually larger than human penises)), moist(even more so when in heat)), clitoris(located at the bottom(nestled within southernmost labia fold(tapered end))), Vaginal tract(depth varies dramatically between breeds(average depth is between two and five inches(from entrance to cervix), will expand marginally when in heat)))];|
	/setentryfield file={{getvar::wi_variables}} uid={{pipe}} field=key {{noop}}|
	
	/createentry file={{getvar::wi_variables}} key="F [EQUINE] (2/4) Button" [equine winking: clear indicator of arousal(occurs when aroused or in heat(can be done manually)), clitoris/button(round, smooth, peach-shaped, grape-sized, bright pink coloration, referred to as a "button"(nestled within southernmost region of slit(within rounded fold, usually concealed behind pussy lips(but will occasionally reveal itself when mare is aroused(flexes and purses pussy lips(causing clitoris to briefly swell and become visible from between folds(referred to as "winking" or making the clit "wink")))))))];|
	/setentryfield file={{getvar::wi_variables}} uid={{pipe}} field=key {{noop}}|
	
	/createentry file={{getvar::wi_variables}} key="F [EQUINE] (1/4) Vagina" [equine pussy: located exposed between cheeks of flank(farthest end, posterior(not underneath body(facing outward from backside))), just below anus(connected by the same stretch of skin(connected via taint)), usually concealed or obscured behind the tail(tail usually hangs down over anus and pussy(obscuring view), tail needs to be moved or lifted to reveal(unless tail is already established to be styled or cut down)), Outward appearance(large(elastic, designed to accommodate a stallion's cock(massively larger than a human's(wider and longer slit(than human female))), unique shape(resembles an elongated and puffy teardrop in shape(pussy lips meet at top, curve around at bottom(pointed at top, rounded at bottom))), color varies per individual(typically of a darker shade of color than surrounding coat of fur(can also be entirely black in color)), hairless(entire vulva possesses no fur(unlike surrounding flank)), Puffy(always appears soft swollen(inviting)), pussy lips(puffy(protrudes slightly from body), velvety(soft to the touch), muscular(clenching power, designed to withstand a stallion's powerful cock), internal appearance(pink(bright pink(akin to the inside of a mouth)), fleshy(soft, squishy, tight, incredibly elastic(meant to accommodate massive equine girth(which is usually massively larger than human penises)), Incredibly moist(produces abundance of natural lubricant(even more so when in heat))), spacious(akin to a moist deep fleshy tunnel), clitoris/button(bright pink coloration, referred to as a "button"(nestled within southernmost region of slit(within rounded fold, usually concealed behind lips(but will occasionally reveal itself when mare is aroused(flexes and purses pussy lips open and shut(causing clitoris to briefly swell and become visible from between folds(referred to as "winking" or making the clit "wink"))))))), Vaginal tract(depth varies dramatically within genus(average depth is between six and eight inches(from entrance to cervix(designed to handle stallion penis), will expand exponentially when in heat(to accommodate almost anything)))), anus/asshole(sits above pussy(just below base of tail), incredibly puffy(protrudes noticeably, very similar in appearance to a donut(referred to as the "ponut"(colloquial term)), tight(puckered tightly), connected via taint to slit of pussy, color matches that of connected pussy))];|
	/setentryfield file={{getvar::wi_variables}} uid={{pipe}} field=key {{noop}}|
	
	/createentry file={{getvar::wi_variables}} key="M [CANINE] (1/3) Penis" [canine cock: length and girth vary dramatically between breeds(average length anywhere between six and upwards of twelve inches(generally bigger than human's)), Outward appearance((flaccid(white coloration(not engorged with blood), knot is not prominently swollen(indicating lack of proper arousal or orgasm))), erect(pink and or red coloration(fully engorged with blood)), rigid(not as pliable as a human's(far stiffer(pure muscle))), smooth shaft(no ridges or wrinkles(possesses no foreskin(comprised entirely of smooth and firm muscle)), tapered tip(penis ends in a semi-blunt point(similar in appearance to the lid of a toddler's sippy cup)), prominent knot(indicating full erection(or close to orgasm)), when fully erect hangs and sways loosely from pelvis(giving a distinctly heavyweight appearance, low-slung)), slimy(slick, covered in thick layer of precum(natural lubricant(allows minimal friction))), discharges constant stream of precum(far more than typical human), ejaculation can and will last several long minutes(dog's cum in far higher volumes than humans)];|
	/setentryfield file={{getvar::wi_variables}} uid={{pipe}} field=key {{noop}}|
	
	/createentry file={{getvar::wi_variables}} key="M [CANINE] (2/3) Sheath" [canine sheath: dogs do not possess foreskin, instead utilize a sheath(akin to a foreskin), a short length of fluffy flesh that socks the flaccid penis(size of sheath depends on dog's endowment(bigger cock requires bigger sheath(can serve as an indication of potential size of dog's cock(big sheath implies big cock)))), located laying flush against lower belly(gradually protrudes from body(sheath is fused to belly(pointed forward towards chest))), serves to protect and constantly lubricate the penis when not engaging in sexual activities, will peel back to allow the lubricated length to slowly reveal itself when becoming erect(but can occasionally remain wrapped around the knot(swelling of the bulbous knot makes retraction over the wide bulb difficult(akin to getting an orange stuck inside of a sock(must be manually retracted to reveal the knot(can peel back natural during sex))))), Outward appearance(furry(just as furry and fluffy as the rest of the body), soft, squishy(made of skin)), inside the sheath(elastic(designed to contain the knot(even when swelled))), hot, moist(keeps penis lubricated), smooth(fleshy, squishy)];|
	/setentryfield file={{getvar::wi_variables}} uid={{pipe}} field=key {{noop}}|
	
	/createentry file={{getvar::wi_variables}} key="M [CANINE] (3/3) Knot" [canine knot: located at base of shaft, appears as two hard balls of muscle(one on either side of the shaft(culminating in plump bulb(size of which can vary(anywhere between the size of a tennis ball and upwards of the size of a grapefruit(generally relative to size of penis(bigger cock means bigger knot)))))), functions as a seal to trap and keep semen inside of recipient(designed to ensure copulation, impregnation), swells and expands exponentially when nearing or experiencing orgasm(inflates to seal against surrounding walls and lock penis firmly in place(akin to inflating a small balloon inside one's body(referred to as "knotting" or being "tied"(keeping both partners attached to each other(for a period of time))))), knot can sometimes prematurely expand outside before proper embedding occurs(will then have to be forcefully crammed into recipient to manually create proper seal(agonizingly slow and aggressive gesture(manhandling(akin to slowly cramming a baseball or a fist inside recipient(overwhelming pressure))))), sensation of resulting pressure varies dramatically(intense pain or intense pleasure(depends on recipient)), will only lock in place when penis is buried to the hilt(knot is located at bottom(base) of shaft), knot can function outside of penetrative sex(does not strictly require the act of penetrative sex(can be enjoyed and witnessed in manual stimulation(masturbation, like any other penis)))];|
	/setentryfield file={{getvar::wi_variables}} uid={{pipe}} field=key {{noop}}|
	
	/createentry file={{getvar::wi_variables}} key="M [EQUINE] (1/5) Penis" [equine cock: length and girth vary dramatically among genus(average length(long(length is usually emphasize over girth(anywhere between eighteen and upwards of twenty-two inches long(massively bigger than human's))))), outward appearance((flaccid(tucked away nestled within sheath(practically flush with body, barely visible or accessible from exterior, given an almost folded appearance(inaccessible(needs to be aroused to coax cock out))), wrinkly(skin of shaft bunched up, not engorged with blood(will stretch out slowly while finally becoming erect)))), (erect(long(typically hangs past the knees), thick(considerable girth), very heavy(pure muscle, sheer mass, curves downward under its own weight(swings and bounces loosely with movement(large flare makes shaft top-heavy)))), velvety texture(smooth and fleshy layer of skin(stretched taut around muscular penis(wrinkles are smoothed out(fully engorged with blood))))), skin color varies dramatically per individual(typically of a much darker shade than rest of body(most commonly black, brown, white), mottled(splotches of darker or brighter color(of similar shades to the rest of body) dotting surface(akin to vitiligo))), firm yet pliable(can be bent to a degree when erect(length allows maneuverability)), blunt tip(ends in a semi-blunt tip(does not possess a head(like that of a humans(instead entirely shaft is like that of a baseball bat)))))];|
	/setentryfield file={{getvar::wi_variables}} uid={{pipe}} field=key {{noop}}|
	
	/createentry file={{getvar::wi_variables}} key="M [EQUINE] (2/5) Sheath" [equine sheath: a short length of flesh that socks the soft flaccid, located laying flush against lower belly(gradually protrudes from body(sheath is fused to belly(pointed forward towards chest))), serves to protect and the penis when not engaging in sexual activities(while sheathed will be inaccessible(tucked inside(equine must be stimulated/aroused in order to coax cock out(flush with body when flaccid, extends free from folds when becoming erect))), will unfold to allow the wrinkled length to slowly reveal itself and grow taut when becoming erect, sheath becomes the medial ring as erection occurs(unrolling and stretching along with rest of skin around length)), Outward appearance(directly connected to ball sack(ball sack always matches color of sheath), soft, velvety(texture of smooth skin, not covered in fur), color of sheath complements rest of fur coat(typically much darker color than rest of body(usually slightly darker than color of penis itself(sheath sometimes can be dark brown or all black in color(white/pink in rare occasions(depending on brightness of fur coat))))), squishy(simply folds of skin)), testicles(located hanging between hind legs(just below sheath(sheath and testicles connected by same stretch of skin(seamless transition, same coloration))), big(plump, typically larger than humans(about the size of grapefruits)), very heavy(hang heavily between thighs(sheer mass, filled with semen(abundant))), smooth and velvety(same texture as rest of sheath, shiny(swollen(skin stretched taut around balls, appearance of two balloons))))];|
	/setentryfield file={{getvar::wi_variables}} uid={{pipe}} field=key {{noop}}|
	
	/createentry file={{getvar::wi_variables}} key="M [EQUINE] (4/5) Flare" [equine flare(a whole other beast to worry about): also referred to as the breeding bulb, the glans of a horse's cock, When not excited/aroused(almost nonexistent, unassuming(remains same thickness as rest of shaft)), When becoming excited/aroused(swells to a wide blunt tip(ends in a wide mushroom-like head(referred to as the "flare"(or the phenomenon itself referred to as "belling")), flare becomes the widest part of the penis(pronounced, much thicker than rest of shaft(similar in appearance to the widened end of a trumpet)), marginally squishy(spongy, not as firm as rest of shaft(is simply engorged with blood(as apposed to being made of muscle like rest of shaft)))), Primarily functions as a seal to trap and keep semen inside of recipient(designed to ensure copulation, impregnation), swells and expands exponentially when nearing or experiencing orgasm(inflates to seal flush against surrounding walls and lock penis deep inside(akin to inflating a balloon inside one's body(keeping both partners attached to each other(for a period of time))), flare will sometimes prematurely expand during bouts of arousal(commonly flares when aroused or anticipating sexual activity(creating difficulty in achieving penetration(flare becomes much larger than target entrance), will then need to be forcefully squished and crammed into recipient to achieve penetration for sex(agonizingly slow and aggressive gesture(manhandling(wide and blunt tip is more often than not far larger than entrance can stretch(slight squishiness of flare allows for some maneuverability))))), sensation of resulting pressure varies dramatically(intense pain or intense pleasure(depends on recipient))), flare can function outside of penetrative sex(does not strictly require the act of penetrative sex(can be enjoyed and witnessed in manual stimulation(masturbation, like any other penis))))), Flaring inside recipient(resulting expansion of glans will create extreme sensations of internal pressure(flare is biologically designed exclusively for equine mares(big enough to handle such pressure), can have absolutely devastating effects inside of a human(not designed to accommodate such an expansion(incompatible biology, will experience shifting and stretching of internal organs(and possible bulging of the abdominal(belly(indicator of flare's presence inside body)))), resulting sensations dramatically vary between recipient(either extreme pain or extreme pleasure(personal preferences and pain tolerance)))), When flared can not easily pull free from buried penis(forced dislodging of flare will result in pain or discomfort(for both partners), can not easily pull out(flare is locked in place via expansion and pressure(must simply endure until deflated)), will unload a staggering volume of semen(flare designed to keep semen from leaking out throughout), after ejaculation has concluded flare will slowly begin to deflate(only then will it be able to dislodge and pop out(flare will still be uncomfortable wide(necessitating aggressive dislodge from tight orifice entrance), audible pop, overwhelming release of pressure(satisfying), extremely messy(absence of flare allows free flow of deposited semen)))))];|
	/setentryfield file={{getvar::wi_variables}} uid={{pipe}} field=key {{noop}}|
	
	/createentry file={{getvar::wi_variables}} key="M [EQUINE] (3/5) Medial ring" [equine cock's medial ring(and its colloquial usage as a depth milestone): prominent ring of skin around shaft(smooth bump of flesh around circumstance of girth), marks the halfway point(roughly) of the penis(signifies the "end" of the shaft(remainder of shaft onward consists of sheath, insertion of shaft past this point is redundant(but can be pushed further for further stimulation))), located about halfway up shaft(lower half(near base of shaft(about a third of the way up))), created as result of the sheath stretching with the growing shaft(indicating transition point from sheath to shaft, medial ring is remnant of sheath(akin to the fold created when pulling back human foreskin)), only manifests when becoming erect(not visible when flaccid(penis is hidden inside sheath)), medial ring is cosmetic(serves no functional purpose aside from visual marker(and once being the sheath itself)), the point from medial ring and downward(slightly darker in color than upper threshold of shaft, slightly thicker and fleshier than rest of shaft(lower threshold is simply the sheath itself having been stretched out), commonly used as a depth milestone during penetrative sex(equine penises are notoriously long, taking such a cock(in any orifice) to the medial ring is considered an great achievement(medial ring located on lower portion signifies significant length of cock has been sheathed within orifice(does not mean cock is hilted or balls deep(still a length to go)))))];|
	/setentryfield file={{getvar::wi_variables}} uid={{pipe}} field=key {{noop}}|
		
	/createentry file={{getvar::wi_variables}} key="F [FELINE] (1/1) Vagina" [Feline pussy: located nestled between hindquarters(below the anus(usually concealed or obscured behind the tail(tail usually hangs down over anus and pussy(obscuring view), tail needs to be moved or lifted to reveal)), When not aroused(Not swollen, Almost flush with the body(unnoticeable, resembles a furry slit against body), labia concealed within slit(color of labia varies between individual((typically bright pink(but can be darker or entirely black in color on big cats(panthers, lionesses, ect.))))), When aroused(puffs up marginally(takes on a more puffy and swollen appearance(furry surroundings make for a pillowy appearance)), labia swells and become visible(pink reveals itself from between slit, vaguely resembles a human vagina)), Outward appearance(small(opening typically small and dainty(designed for feline penises(generally much smaller than human penises(only a couple inches)))), soft and furry(petite, covered in fur(surrounding body fur(almost blends in)))), Internal appearance(pink(bright pink(akin to the inside of a mouth)), fleshy(soft, squishy, tight, shallow(not that deep(doesn't need to be, adapted for feline cocks(feline cocks aren't that long, doubtful to fit anything bigger))), moist(even more so when in heat)), clitoris(located nestled within labia fold(usually hidden unless aroused and swollen)), Vaginal tract(depth varies dramatically between breeds, usually very shallow(average depth is between two and four inches(from entrance to cervix), will expand marginally when in heat)))];|
	/setentryfield file={{getvar::wi_variables}} uid={{pipe}} field=key {{noop}}|
	
	/createentry file={{getvar::wi_variables}} key="F [CANINE] (3/3) Teats (Milkers)" [canine teats/breasts: canine have a set of eight tits(in pairs of two(two by four configuration)), overall size varies dramatically between individual, located across underside(stretching from rib cage to groin area, laid out in even pairs of two across underbelly in eight-pack fashion(almost resembling a pack of big puffy bread buns in appearance))), outward appearance(plump, pillowy(swollen and plump with milk), heavy(dangles and sways from body), oblong(takes on a sagging yet perky spheroid shape(weight pulls teats downward), squishy(pliable, soft and pleasant to handle(like that of any set of boobs)), nipples(perky, stiff, elongated(usually the most notable and striking feature), typically of a darker coloration(depending on surrounding coat of fur), located at tips of either teat(lowest point)))];|
	/setentryfield file={{getvar::wi_variables}} uid={{pipe}} field=key {{noop}}|
	
	/createentry file={{getvar::wi_variables}} key="F [CANINE] (2/3) eats (Standard)" [canine teats/breasts: canine have a set of eight tits(in pairs of two(two by four configuration)), overall size varies between individual(typically rather flat(flush with body, not very swollen(unless pregnant or nursing))), located across underside(stretching from rib cage to groin area, laid out in even pairs of two across underbelly in eight-pack fashion(almost resembling a pack of bread buns in appearance))), outward appearance(plump, modest(like that of A-cup or AA-cup sized human breasts), perky, squishy(soft and pleasant to handle(like that of any set of boobs(though lack any substantial fullness or weight(like that typically associated with human females))))), nipples(small, perky(nodule, usually the only indicator that breasts are even there), stiff, typically of a darker coloration(depending on surroundings coat of fur)))];|
	/setentryfield file={{getvar::wi_variables}} uid={{pipe}} field=key {{noop}}|
	
	/createentry file={{getvar::wi_variables}} key="F [EQUINE] (4/4) Teats (Milkers)" [equine teats/breasts: mammary glands(exclusive to mares, produce milk), set of two(pair), overall size varies dramatically between individual, located lower belly(lower abdomen(crotch area(not located on the chest area(as one might expect)), nestled just between hind legs(hang down from body, (tends to squish and knead intimately between legs))), outward appearance(plump, huge(swollen and plump with milk, typically much larger than human boobs), heavy(dangles and sways from body), oblong(takes on a sagging yet perky spheroid shape(akin to bloated footballs(weight pulls teats downward), squishy(pliable, like giant hanging water balloons, soft and pleasant to handle(like that of any set of boobs))), nipples(perky, typically of a darker coloration, small or wide areola, located at tips of either teat(lowest point)))];|
	/setentryfield file={{getvar::wi_variables}} uid={{pipe}} field=key {{noop}}|
	
	/createentry file={{getvar::wi_variables}} key="M [FELINE] (1/2) Penis" [Feline cock: length and girth vary dramatically between individuals(domestic cat or big cat), size is typically relative to size of cat(average length anywhere between two and upwards of four inches(generally very short and stubby in relation to body(does not require long endowments(barbs of shaft ensure semen is reliably deposited(make up for it)))), Outward appearance(Flaccid(hidden within sheath, almost nonexistent), Erect(pink and or red coloration(fully engorged with blood)), rigid(not as pliable as a human's(far stiffer), barbed shaft(distinctive, shaft is covered in short spines(backwards facing, most prominent near and around base), barbs designed to(anchors penis within, ensure penis does not slip free during sex(barbs catch against surrounding walls(akin to Velcro)), stimulate recipient’s inner walls(dragging and catching(assists in sexual reciprocation(potentially triggers contractions), sensation varies dramatically between individuals(irritation and pain, stimulation and pleasure)))), tapered(cone shaped(starts with a wide base, ends in a point(head of penis is not blunt or bulbous))), stubby(thickest at base of shaft, thinnest at tip of shaft)];|
	/setentryfield file={{getvar::wi_variables}} uid={{pipe}} field=key {{noop}}|
	
	/createentry file={{getvar::wi_variables}} key="M [FELINE] (2/2) Sheath " [Feline sheath: cats do not possess foreskin, instead utilize a sheath(akin to a foreskin), a short length of fluffy flesh that socks the flaccid penis(size of sheath depends on cat's endowment(bigger cock requires bigger sheath(can serve as an indication of potential size of cat's cock(big sheath implies big cock)))), located laying flush against lower belly(gradually protrudes from body(sheath is fused to belly(pointed forward towards chest))), serves to protect and constantly lubricate the penis when not engaging in sexual activities, will peel back to allow the lubricated length to slowly reveal itself when becoming erect, Outward appearance(furry(just as furry and fluffy as the rest of the body), soft, squishy(made of skin)), inside the sheath(hot, moist(keeps penis lubricated), smooth(fleshy, squishy)];|
	/setentryfield file={{getvar::wi_variables}} uid={{pipe}} field=key {{noop}}|
	
	/createentry file={{getvar::wi_variables}} key="M [EQUINE] (5/5) [E] Flaring " [The flair is inflating and wedging into place(and what that means for its unfortunate recipient): Flaring inside recipient(resulting expansion of glans will create extreme sensations of internal pressure, rapidly ballooning flare guaranteed to bulge abdomen(flare is biologically designed exclusively for equine mares(big enough to handle such pressure), can have absolutely detrimental effects inside of a human(not designed to accommodate such an expansion(incompatible biology, will experience shifting and stretching of internal organs(and possible bulging of the abdominal(belly(indicator of flare's presence inside body)))), resulting sensations dramatically vary between recipient(either extreme pain or extreme pleasure(personal preferences and pain tolerance)))), When flared can not easily pull free(forced dislodging of flare may result in pain or discomfort(for both partners), can not easily pull out(flare is locked in place via pressure(must simply endure)), will unload a staggering volume of semen(flare designed to keep semen from leaking out throughout), after ejaculation as concluded flare will slowly begin to deflate(only then will it be able to dislodge and pop out(audible pop, overwhelming release of pressure(satisfying), extremely messy(absence of flare allows free flow of deposited semen)))))];|
	/setentryfield file={{getvar::wi_variables}} uid={{pipe}} field=key {{noop}}|
	
	/createentry file={{getvar::wi_variables}} key="M [PIG] (1/3) Penis" [Porcine cock: uniquely shaped, incredibly slender and long(important for function, length varies dramatically between individuals(average length anywhere between twelve inches and upwards of twenty inches(designed to reach deepest possible depths))), lack of thickness(thin, not at all thick or girthy(slender, length emphasized over girth, thinness typical akin to that of a hotdog wiener(can be thinner(pencil thin)))), does not possess a typical bulbous head(instead penis ends drill-like(thin coiled tip designed to penetrate and bypass female cervix(narrow and usually sturdy barrier to the womb), does not actually spin like a drill however(will instead violently coil back and forth(semi-rotary, repeatedly(until contact and forceful penetration of cervix is successful(will utilize spiral tip to forcefully drill its way into womb(pushes further still, allowing rest of immense length to snake inside)))))), will extend deeper still into vaginal tract(aggressively, fast), will continue to twist and writhe wildly even after entering womb(will continue feeding and sliding even more of its length through(for the purpose of feeling around and mapping out the space of womb(sensation akin to a long worm invading and squirming wildly within(pleasure or discomfort is dramatically subjective))))), Outward appearance(bright pink or red coloration, tapered(thicker at base, tip ends in a coiled point), shaft(rigid, smooth, moist(covered in thin mucus(slimier and more viscous than typical precum)), texture akin to the inside of a mouth(possesses no foreskin), single prominent vein spiraling coiling up length(winding, blue, purple, begins at base ends at tip)), tip of penis(upper portion of penis is coiled(helically, corkscrew shaped(counterclockwise), can also occasionally take on a very curly “S” shape)))];|
	/setentryfield file={{getvar::wi_variables}} uid={{pipe}} field=key {{noop}}|
	
	/createentry file={{getvar::wi_variables}} key="M [PIG] (2/3) Sheath" [Porcine sheath: also called the "pouch", houses penis when not erect, keeps penis lubricated until needed, located(lower belly), outward appearance(fleshy, fuzzy(like rest of body), protrudes marginally from body(mostly flush with body), color matches rest of body)), Balls/testicles(massive(size like that of two cantaloupes), disproportionately large, very heavy(swing and sways heavily between legs, contain massive amounts of semen(specifically designed to perform multiple consecutive mating sessions(powerhouse))))];|
	/setentryfield file={{getvar::wi_variables}} uid={{pipe}} field=key {{noop}}|
	
	/createentry file={{getvar::wi_variables}} key="M [PIG] (3/3) Cum" [Porcine cum: viscous, off-white coloration(slightly translucent(in comparison to human semen)), smell(pungent, powerful, potentially nauseating), taste(surprisingly sweet), abundant(ejaculation releases overwhelming mass quantities(pressurized, rapid(constant and steady stream(liken to a water hose)))), unique ejaculation and sealing process(ejaculation can last anywhere from ten and upwards of thirty minuets, when ejaculation is finally complete(penis ejects one last special gelling agent(thick and gel-like cement within lining and entrance of cervix(effectively locking and sealing flood within womb(preventing a single drop of abundant deposit from escaping, designed to guarantee insemination(impossible to relive one’s self of bloated pressure(cement seal lasts upwards of three days(where it naturally devolves), simply must endure)))))))];|
	/setentryfield file={{getvar::wi_variables}} uid={{pipe}} field=key {{noop}}|
	
	/createentry file={{getvar::wi_variables}} key="M [REP/GENERIC] (1/4) Penis" [Reptile cock: length and girth vary wildly between species(not every species share the same size metric, average length anywhere between one and upwards of eight inches(size is relatively proportional to size of reptile)), Outward appearance(flaccid(hidden nestled deep within the slit(inaccessible or visible from the outside)), erect(typically of a white and or pink coloration(slightly more vibrant than flaccid coloration(but can and will most likely be of any color or pattern depending on individual))), remarkably squishy and yielding(more pliable than a human's(far softer(spongy, squishy))), smooth shaft(not covered in scales(entirely different from rest of body), no ridges or wrinkles(possesses no foreskin, no tactile veins(comprised entirely of smooth and firm muscle(texture akin to the inside of ones mouth, moist and fleshy))), tapered tip(penis begins at a broad base(where it emerged) and ends in a point(liken to the appearance and shape of a slippery featureless tentacle))), slick and slimy(surface covered in thick layer of natural lubricant(having been stewing within slit until emerging))];|
	/setentryfield file={{getvar::wi_variables}} uid={{pipe}} field=key {{noop}}|
	
	/createentry file={{getvar::wi_variables}} key="M [REP] (2/4) Hemipenes" [STATUS EFFECT:  does not have one but two separate penises(reptiles and their dual cocks(Hemipenes)): diphallism, cocks exist side by side next to each other(horizontally), both penises occupy the same space within and emerge from same slit(connected to the same base(each penis can potentially be of its own unique size or shape(generally mirror image in most cases))), one penis may emerge first for penetration while the other might stay outside initially(depending on the reptile species and individual mating behavior), typically one penis(dominant) is tasked with entering a partner while the other(subdominant) remains left outside(similar to being right or left handed, subdominant cock tends to flop and jump around outside between bodies), having two penises far from hindrance(unparalleled sexual capabilities(dual nature of their penises can achieve unique sexual positions and manipulations that other animals simply can not), typical advantages being(double penetration(one penis enters the vagina while the other enters the anus(overwhelming sensations and unique experience(for both parties)), can potentially cram both penises into one singular orifice(brutal stretch(essentially fitting a cock twice its original girth(fitting the combined girth of both penises inside a single orifice)), exceptionally snug fit(primarily enjoyed in more aggressive sex))), simultaneous partners(dual mating, each penis penetrates its own partner entirely(have sex with two people at the same time), maximum reproductive potential, evolutionary advantage), visual aesthetics(simply looks hot(perceived as hyper virile or hyper masculine))))];|
	/setentryfield file={{getvar::wi_variables}} uid={{pipe}} field=key {{noop}}|
	
	/createentry file={{getvar::wi_variables}} key="M [REP] (3/4) Knot" [Reptile knot: located at base of shaft, appears as two hard balls of muscle(one on either side of the shaft(culminating in plump bulb(size of which can vary(anywhere between the size of a tennis ball and upwards of the size of a grapefruit(generally relative to size of penis(bigger cock means bigger knot)))))), functions as a seal to trap and keep semen inside of recipient(designed to ensure copulation, impregnation), swells and expands exponentially when nearing or experiencing orgasm(inflates to seal against surrounding walls and lock penis firmly in place(akin to inflating a small balloon inside one's body(referred to as "knotting" or being "tied"(keeping both partners attached to each other(for a period of time))))), knot can sometimes prematurely expand outside before proper embedding occurs(will then have to be forcefully crammed into recipient to manually create proper seal(agonizingly slow and aggressive gesture(manhandling(akin to slowly cramming a baseball or a fist inside recipient(overwhelming pressure))))), sensation of resulting pressure varies dramatically(intense pain or intense pleasure(depends on recipient)), will only lock in place when penis is buried to the hilt(knot is located at bottom(base) of shaft), knot can function outside of penetrative sex(does not strictly require the act of penetrative sex(can be enjoyed and witnessed in manual stimulation(masturbation, like any other penis)))];|
	/setentryfield file={{getvar::wi_variables}} uid={{pipe}} field=key {{noop}}|
	
	/createentry file={{getvar::wi_variables}} key="Covering Anthro" The covering of a  is the same covering as the normal  except for on the face, chest, paws and genitalia area where it is generally less.

A Andromorphic animal stands on two legs and is mostly formed like a Human except for the  features such as the ears and tail etc...|
	/setentryfield file={{getvar::wi_variables}} uid={{pipe}} field=key {{noop}}|
	
	/createentry file={{getvar::wi_variables}} key="Covering Furry" The covering of a  is the same covering as the normal  but it will only cover part of the body. Such as the ears, tail, shoulders, stomach, upper arms, calves and feet. There could also be a small amount on the breasts and genitalia area.

A Furry animal stands on two legs and is mostly formed like a Human except for the  features such as the ears and tail etc...|
	/setentryfield file={{getvar::wi_variables}} uid={{pipe}} field=key {{noop}}|
	
	/createentry file={{getvar::wi_variables}} key="Exclude from gen" Exclude Character Development or Self-Discovery from your reply.
Exclude emotional or interpretative phrases from your reply.
Exclude enchanting qualities or highlights from your reply.
Exclude origins or age from your reply.
Exclude future speculations from your reply.|
	/setentryfield file={{getvar::wi_variables}} uid={{pipe}} field=key {{noop}}|

	/createentry file={{getvar::wi_variables}} key="Guide prompt" The reply should be about: |
	/setentryfield file={{getvar::wi_variables}} uid={{pipe}} field=key {{noop}}|

	/createentry file={{getvar::wi_variables}} key="Seasons: List" Spring: Summer: Autumn: Winter|
	/setentryfield file={{getvar::wi_variables}} uid={{pipe}} field=key {{noop}}|

	/createentry file={{getvar::wi_variables}} key="Type Guide" Human is a standard human.
Anthro is a animal that have a human form.
Demi-Human is races that mostly looks like humans like Dwarfs, Elves etc...
Furry is animal like humans that mostly looks like humans but have certain animal parts.
Feral is standard animals, fantasy animals or monsters.|
Pokémon is the creatures from the Pokémon games and anime.
Digimon is the creatures from the Digimon games and anime.
	/setentryfield file={{getvar::wi_variables}} uid={{pipe}} field=key {{noop}}|

	/createentry file={{getvar::wi_variables}} key="Scenario prompt" .
Always use '{\{user}}' instead of '{\{user}}'. Never use 'the {\{user}}'.
The reply should be from 's point of view.
[Never act or talk as {\{user}}.]
End the scenario where {\{user}} can make a choice or act silently implying that it is {\{user}}'s turn.
Now make a scenario. While making the scenario keeping the text airy and the text informal.|
	/setentryfield file={{getvar::wi_variables}} uid={{pipe}} field=key {{noop}}|
	
	/createentry file={{getvar::wi_variables}} key="F [EQUINE] (3/4) Teats (Standard)" [equine teats/breasts: mammary glands(exclusive to mares), set of two(pair), overall size varies dramatically between individual(typically modest(akin to B-cups(on average))), located lower belly(lower abdomen, not located on the chest area(as one might expect), nestled just between hind legs(crotch area, protrude from body(tends to squish and knead intimately between legs))), outward appearance(plump(like that of A, to B-cup sized human breasts), perky, squishy(soft and pleasant to handle(like that of any set of boobs))), nipples(typically of a darker coloration, located at tips of either teat))];|
	/setentryfield file={{getvar::wi_variables}} uid={{pipe}} field=key {{noop}}|
	
	/createentry file={{getvar::wi_variables}} key="F [PIG] (1/1) Vagina" [Porcine pussy: located nestled between hindquarters(below the anus(usually out and open for all to see(short curly tail incapable of shrouding))), eerily indistinguishable from human vagina(surprisingly similar in appearance), When not aroused(Not swollen, Almost flush with the body(unnoticeable)), When aroused(Extends(protrudes slightly from the body(by a couple inches, signaling readiness for insertion of male)), puffed up(takes on a more puffy and swollen appearance)), Outward appearance(usually same color as rest of body(can also be slightly darker in coloration), velvety texture, incredibly puffy(squishy, swollen(when aroused), entrance(or slit) possesses a lip(lower lip, tapered extension of labia(giving vagina a bowed appearance(puffiest at the bottom(causing upwards angle)))))), Internal appearance(pink(bright pink(akin to the inside of a mouth)), fleshy(soft, squishy, tight, elastic(meant to accommodate porcine penises(which are usually longer than human penises(but far more narrow))), moist(even more so when in heat)), clitoris(located at the bottom(nestled within southernmost labia fold(tapered end))), Vaginal tract(deep(designed to accommodate the usually immense porcine lengths, average depth is between ten and twelve inches deep(from entrance to cervix), will expand marginally when in heat)))];|
	/setentryfield file={{getvar::wi_variables}} uid={{pipe}} field=key {{noop}}|
	
	/createentry file={{getvar::wi_variables}} key="F [REP] (1/1) Vagina" [Reptile pussy: also referred to as the "slit", both male and female reptiles have a slit, in males(reptile penises are not external by default, instead hide within a slit(or "cloaca" to house penis, slit eerily liken to a female vagina(in appearance(male and female reptile slits look exactly the same until aroused(making it difficult to determine the sex of a reptile at first glance(especially if said reptile is particularly effeminate or lacks masculine traits(visually ambiguous)))))), in females(slit leads to womb(as is typical of a female vagina)), outward appearance(rim of slit covered in soft scales(scales are surprisingly less abrasive along folds than rest of body(as is typical of the soft underbelly of a reptile)), rim of slit is incredibly tight(scale lining isn't exactly flexible, rigid rim creates particularly straining initial penetration(akin to pushing ones penis between a narrow vice)), inside the slit(elastic(designed to accommodate any potential size of penis(penis size of mate can vary wildly)), moist(kept constantly lubricated), smooth(fleshy, squishy(near identical to the inside of the female vagina(albeit far squishier))), vaginal tract(depth varies dramatically between species(average depth is anywhere between one inch(shallow) and upwards of 12 inches deep(from entrance to cervix, depth of tract relative to size of reptile), will expand marginally when in heat))];|
	/setentryfield file={{getvar::wi_variables}} uid={{pipe}} field=key {{noop}}|
	
	/createentry file={{getvar::wi_variables}} key="F [SERP] (1/1) Vagina" [Serpent pussy: cloaca(better referred to as the "slit"), located near very end of body(close to thin tail-end), When not aroused(Not swollen, Almost flush with the body(unnoticeable, almost impossible to find)), When aroused(slide widens and opens up(soft flesh if pink orifice puffs out and becoming visible, protruding marginally from between hard slit(signaling readiness for insertion))), Outward appearance(aligned horizontally(sideways, as apposed to the more common vertical vagina(like all mammals and humans have)), entrance is near hidden(slit is thin and blends in with segmented pattern of underbelly, rarely because visually obvious until aroused), rim of slit covered in soft scales(scales are surprisingly less abrasive along folds than rest of body(as is typical of the soft underbelly of a reptile))), Internal appearance(pink(bright pink(akin to the inside of a mouth)), fleshy(soft, squishy, tight, incredibly elastic(capable of accommodating any penis size and length(even those of inhumane shapes and sizes without struggle or stress(almost boringly adept at handling cock, large size of body of serpent means that any potential partner's cock size would be comparatively small and potentially unfulfilling to them(downside of being larger)))), moist(even more so when in heat)), remarkably tight(despite overall size of body and vagina suggesting a loose fit, space within vaginal tract relative to size and length of serpent(small body would mean tighter insides, larger body would mean more forgiving tightness)), Vaginal tract(a serpents vaginal tract is essentially the entirety of its body(practically one long fleshy tube, meaning that the depth of vagina is virtually endless))];|
  /createentry file={{getvar::wi_variables}} key="F [SNAKE] (1/1) Vagina" [Snake pussy: cloaca(better referred to as the "slit"), located near very end of body(close to thin tail-end), When not aroused(Not swollen, Almost flush with the body(unnoticeable, almost impossible to find)), When aroused(slide widens and opens up(soft flesh if pink orifice puffs out and becoming visible, protruding marginally from between hard slit(signaling readiness for insertion))), Outward appearance(aligned horizontally(sideways, as apposed to the more common vertical vagina(like all mammals and humans have)), entrance is near hidden(slit is thin and blends in with segmented pattern of underbelly, rarely because visually obvious until aroused), rim of slit covered in soft scales(scales are surprisingly less abrasive along folds than rest of body(as is typical of the soft underbelly of a reptile))), Internal appearance(pink(bright pink(akin to the inside of a mouth)), fleshy(soft, squishy, tight, incredibly elastic(capable of accommodating any penis size and length(even those of inhumane shapes and sizes(albeit with a bit of strain))), moist(even more so when in heat)), remarkably tight(space within vaginal tract relative to size and length of snake(thin body would mean tight fit, short body would mean shallow tract)), Vaginal tract(a snake can be boiled down to a living fleshlight(colloquially referred to as a "cock sock"), a snakes vaginal tract is essentially the entirety of its body(practically one long fleshy tube, meaning that the depth of vagina is virtually endless)), Cock-sock effect(body of snake is beautifully elastic(stretches and reshapes naturally when devouring oversized prey or laying eggs), this trait translates wonderfully to the act of taking one's cock(when being penetrated(rim of vagina will stretch brutally to accommodate length(entrance is naturally small and tight), body of snake will bloat and shape to contours of cock(scales shifting and skin stretching as more length is inserted, similar visually to how a snake looks when consuming oversized prey), body of snake essentially becomes a living fleshlight(becoming socked over length of cock like a fleshy condom, leads to an almost unreal degree of snug fit, forces body of snake to assume exact rigidity and shape of the seated cock(minimal space left between the walls and the shaft)))))];|
	/setentryfield file={{getvar::wi_variables}} uid={{pipe}} field=key {{noop}}|
	
	/createentry file={{getvar::wi_variables}} key="F []" |
	/setentryfield file={{getvar::wi_variables}} uid={{pipe}} field=key {{noop}}|
	
	/createentry file={{getvar::wi_variables}} key="M [REP] (4/4) Testicles" [STATUS EFFECT: {{getvaf::firstName}} technically has no balls(Reptile testicles(or lack there of)): reptiles do in fact have testicles however they are NEVER visible, reptile testicles reside inside their body(internal, because reptiles are naturally cold blooded they do not rest outside as one would expect or assume(must keep them as warm as possible), inaccessible to both themselves and anyone else(can not be seen or touched)), for all intents and purposes their nut sack and balls simply do not exist, lack of visible nut sack and consequential featureless crotch adds to the gender ambiguity and potential confusion of discerning a reptile's sex(especially coupled with their slit(both male and female crotches look exactly the same until arousal occurs))];|
	/setentryfield file={{getvar::wi_variables}} uid={{pipe}} field=key {{noop}}|

	/createentry file={{getvar::wi_variables}} key="M [REP/DRAGON] Penis (1/4)" [Reptile cock: length and girth vary wildly between species(not every species share the same size metric, average length anywhere between one and upwards of eight inches(size is relatively proportional to size of reptile)), Outward appearance(flaccid(hidden nestled deep within the slit(inaccessible or visible from the outside)), erect(bears a striking resemblance to a canine penis(albeit much more robust and intimidating in appearance), typically of a pink and or red coloration(slightly more vibrant than flaccid coloration(but can and will most likely be of any color or pattern depending on individual))), rigid(not as pliable as a human's(far stiffer)), ribbed shaft(length of cock is segmented in harsh ridges(backwards facing(towards base), similar to the texture of exotic dildos, makes the sensation of drag during sex particularly intense)), tapered tip(penis ends in a semi-blunt point(arrowhead shape, similar in appearance to the lid of a toddler's sippy cup)), barbed(large soft barbs lining segments of ribbed shaft(aesthetically pleasing in appearance(downward linear pattern), barbs are firm yet yielding(far from uncomfortable), designed for pleasure(like that of a specialty ribbed sex toy)), most prominent ring encircling perimeter of head of penis(corona glans, giving the flared rim of head of penis a daunting spiked appearance(akin the the outer edges of a ravioli pasta(albeit far more menacing)), provide an exhilarating sensation during the drag of thrusting(barbs rub and stimulate surrounding walls))), slick and slimy(surface covered in thick layer of natural lubricant(having been stewing within slit until emerging))];|
	/setentryfield file={{getvar::wi_variables}} uid={{pipe}} field=key {{noop}}|

	/createentry file={{getvar::wi_variables}} key="M []" |
	/setentryfield file={{getvar::wi_variables}} uid={{pipe}} field=key {{noop}}|

	/createentry file={{getvar::wi_variables}} key="Char is TINY" [STATUS EFFECT: {\{getvar::firstName}} scale override({\{getvar::firstName}} is relatively minuscule compared to {\{user}}(and how such a size dynamic and discrepancy dramatically affects their interactions(both practically and intimately))): {\{getvar::firstName}} is tiny(comically shorter than{\{user}}(akin to the size of a real-world mouse, capable of settling within the palm of {\{user}}'s hand(palm-sized))), {\{getvar::firstName}} is eye-level with {\{user}}'s heels when standing straight(must crane neck to meet {\{user}}'s eyes, staggeringly short, incapable of reaching {\{user}}'s knees or higher without assistance(stepping upon a platform, {\{user}} physically lifting {\{getvar::firstName}}(more than capable of lifting or overpowering({\{getvar::firstName}} is generally feather-light, easy to lift(weight relative to size(not much)))))), diminutive size dynamic poses massive anatomical discrepancies(the world around {\{getvar::firstName}} is massive(tiny vantage point means everything is perceptually monumental(towering, awesome)), {\{getvar::firstName}} incapable or struggles to preform "normal" tasks(reaching(the seats of chairs/couches, counters tops, doorknobs, the zipper or belt(or the general removal of any clothing article) of another, ect.), handling or operating items and objects(writing utensils, eating utensils, {\{getvar::firstName}}'s size means everything feels far too large and heavy for comfort(unwieldy(unless made tailored to {\{getvar::firstName}}'s specific size)))), awkward size of {\{getvar::firstName}} compared to {\{user}} means sexual acts are ultimately impossible to preform(anatomy is mismatched to the point of impracticality, {\{user}}'s genitals are relatively massive in the eyes of {\{getvar::firstName}}(daunting, overwhelming({\{getvar::firstName}} would likely be roughly the same size as the genitals themselves)), {\{getvar::firstName}}'s orifices are relatively dainty and shallow in the eyes of {\{user}}(impossible to properly penetrate), mutual masturbation being the only viable option when engaging in intimacy), power dynamic predestined to be in {\{user}}'s favor({\{user}} is simply bigger and stronger, effortlessly capable of overpowering)];|
	/setentryfield file={{getvar::wi_variables}} uid={{pipe}} field=key {{noop}}|

	/createentry file={{getvar::wi_variables}} key="Char is SMALL" [STATUS EFFECT: {\{getvar::firstName}} scale override({\{getvar::firstName}} is relatively minuscule compared to {\{user}}(and how such a size dynamic and discrepancy dramatically affects their interactions(both practically and intimately))): {\{getvar::firstName}} is small(comically shorter than{\{user}}(akin to the size of a large real-world hare)), {\{getvar::firstName}} is eye-level with {\{user}}'s knees when standing straight(must crane neck to meet {\{user}}'s eyes, staggeringly short, incapable of reaching {\{user}}'s chest or higher without assistance(stepping upon a platform, {\{user}} physically lifting {\{getvar::firstName}}(more than capable of lifting or overpowering({\{getvar::firstName}} is generally lightweight, easy to lift(weight relative to size(not much)))))), diminutive size dynamic poses massive anatomical discrepancies({\{getvar::firstName}} incapable or struggles to preform "normal" tasks(reaching(the seats of chairs/couches, counters tops, doorknobs, the zipper or belt(or the general removal of any clothing article) of another, ect.), handling or operating items and objects({\{getvar::firstName}}'s size means everything feels too large for comfort(unwieldy(unless made tailored to {\{getvar::firstName}}'s specific size)))), awkward size of {\{getvar::firstName}} compared to {\{user}} means sexual acts are near impossible to preform(anatomy feels to be mismatched to the point of impracticality, {\{user}}'s genitals are relatively large in the eyes of {\{getvar::firstName}}(daunting, potentially overwhelming), {\{getvar::firstName}}'s orifices are relatively dainty and shallow in the eyes of {\{user}}), power dynamic predestined to be in {\{user}}'s favor({\{user}} is simply bigger and stronger, effortlessly capable of overpowering)];|
	/setentryfield file={{getvar::wi_variables}} uid={{pipe}} field=key {{noop}}|

	/createentry file={{getvar::wi_variables}} key="Char is SHORT" [STATUS EFFECT: {\{getvar::firstName}} scale override({\{getvar::firstName}} is relatively diminutive compared to {\{user}}(and how such a size dynamic and discrepancy dramatically affects their interactions(both practically and intimately))): {\{getvar::firstName}} is short(blatantly shorter than{\{user}}(akin to the size of large dog(more easily recognized as the "short stack" body type))), {\{getvar::firstName}} is eye-level with {\{user}}'s waist when standing straight(must crane neck to meet {\{user}}'s eyes, staggeringly short, incapable of reaching {\{user}}'s chest or higher without assistance(stepping upon a platform, {\{user}} physically lifting {\{getvar::firstName}}(taxing for {\{user}}({\{getvar::firstName}} is surprisingly heavy for their size)))), diminutive size dynamic poses noticeable anatomical discrepancies({\{getvar::firstName}} potentially awkward to preform "normal" tasks(reaching(top shelves, tall counters tops, the zipper or belt(or the general removal of any clothing article) of another, ect.), handling or operating certain items and objects({\{getvar::firstName}}'s size means everything feels awkwardly large for comfort(unwieldy(unless made tailored to {\{getvar::firstName}}'s specific size)))), awkward size of {\{getvar::firstName}} compared to {\{user}} means sexual acts are problematic or potentially uncomfortable to preform(anatomy feels to be mismatched to the point of impracticality, {\{user}}'s genitals are relatively large in the eyes of {\{getvar::firstName}}(daunting, potentially overwhelming), {\{getvar::firstName}}'s orifices are relatively dainty and shallow in the eyes of {\{user}}), power dynamic predestined to be in {\{user}}'s favor({\{user}} is simply bigger and stronger, effortlessly capable of overpowering)];|
	/setentryfield file={{getvar::wi_variables}} uid={{pipe}} field=key {{noop}}|

	/createentry file={{getvar::wi_variables}} key="Char is HUGE" [STATUS EFFECT: {\{getvar::firstName}} scale override({\{getvar::firstName}} is relatively hulking compared to {\{user}}(and how such a size dynamic and discrepancy dramatically affects their interactions(both practically and intimately))): {\{getvar::firstName}} is large(staggeringly bigger than {\{user}}(akin to the size of a real-world bear)), {\{getvar::firstName}} surpasses {\{user}} in height({\{getvar::firstName}} need to look down to meet {\{user}}'s eyes, physicality lean or crouch down to become eye-level with {\{user}}), {\{getvar::firstName}} is generally heavyweight, difficult or impossible to lift or even move(weight relative to size(quite large)), daunting size dynamic poses massive anatomical discrepancies({\{getvar::firstName}} incapable or struggles to preform "normal" tasks(handling or operating items and objects({\{getvar::firstName}}'s size means everything feels too small for comfort(unwieldy(unless made tailored to {\{getvar::firstName}}'s specific size)))), awkward size of {\{getvar::firstName}} compared to {\{user}} means sexual acts are awkward or impossible to preform(anatomy feels to be mismatched to the point of impracticality, {\{user}}'s genitals are relatively small in the eyes of {\{getvar::firstName}}(unimpressive, potentially unsatisfying), {\{getvar::firstName}}'s orifices are relatively big and deep in the eyes of {\{user}}), power dynamic predestined to be in {\{getvar::firstName}}'s favor({\{getvar::firstName}} is simply bigger and stronger, effortlessly capable of overpowering)];|
	/setentryfield file={{getvar::wi_variables}} uid={{pipe}} field=key {{noop}}|

	/createentry file={{getvar::wi_variables}} key="Anthropomorphic Animals" Anthro (Anthropomorphic) beings combine humanoid structure with animalistic traits.
They retain the general body structure of a bipedal humanoid, with a torso, two arms, and two legs, but incorporate features from their species.
Common traits include digitigrade or plantigrade legs, a tail for balance, species-specific head shapes (such as muzzles or beaks), and grasping hands with claws or fingers.
Their feet resemble those of their species but are adapted for upright movement.
Wings, if present, are structured for flight or display and are non-retractable.
Anthros interact with their environment in a human-like manner, using tools and gestures.
They may have fur, scales, feathers, or other coverings based on their species.|
	/setentryfield file={{getvar::wi_variables}} uid={{pipe}} field=key {{noop}}|

	/createentry file={{getvar::wi_variables}} key="Furry" Furry=Singular
Furries=Multiple Furry
Furries is are essentially humans with animal heads and tails. Their hands are human hands, and their feet are human feet with animal-like toes. They can wear human clothing and engaging in any human activity. They have less  {{getvar::coverType}} throughout their body but the {{getvar::coverType}} is emphasized on the tail and ears. They commonly have human hair styles on their head.|
	/setentryfield file={{getvar::wi_variables}} uid={{pipe}} field=key {{noop}}|

	/createentry file={{getvar::wi_variables}} key="Feral" Ferals are basically animals, or the "normal" version of common mythical and fantasy creatures. They may or may not be sentient, and typically do not wear clothes or accessories. Ferals are often described in dramatic poses to emphasize their markings and overall appearance.|
	/setentryfield file={{getvar::wi_variables}} uid={{pipe}} field=key {{noop}}|

	/fetch https://raw.githubusercontent.com/drago87/ST-Character-Maker/refs/heads/Fetch-Files/Templates/Empty%20Character%20Card%20Template.json|
	/createentry file={{getvar::wi_variables}} key="Empty Character Card: Template" {{pipe}}|
	/setentryfield file={{getvar::wi_variables}} uid={{pipe}} field=key {{noop}}|

	/createentry file={{getvar::wi_variables}} key="Appearance Trait Template" - Appearance Trait: --apperanceTrait--
  ↳ Details: --apperanceTraitDetails--
  ↳ Effect: --apperanceTraitEffect--|
	/setentryfield file={{getvar::wi_variables}} uid={{pipe}} field=key {{noop}}|

	/createentry file={{getvar::wi_variables}} key="Apperance Q&A: Template" Q: --Question--
A: --Answer--|
	/setentryfield file={{getvar::wi_variables}} uid={{pipe}} field=key {{noop}}|

	/createentry file={{getvar::wi_variables}} key="Item: Template" "- Item: --item--
  ↳ Details: --itemDetails--"|
	/setentryfield file={{getvar::wi_variables}} uid={{pipe}} field=key {{noop}}|
	
	/createentry file={{getvar::wi_variables}} key="Ability; " "- Ability: --ability--
  ↳ Details: --abilityDetails--"|
	/setentryfield file={{getvar::wi_variables}} uid={{pipe}} field=key {{noop}}|

	/createentry file={{getvar::wi_variables}} key="Character Template" |
	/setentryfield file={{getvar::wi_variables}} uid={{pipe}} field=key {{noop}}|

:}|
//---------|

//---------|

/ife ( 'CMC Personality' not in lorebookList) {:
	/getchatbook name="CMC Personality"|
	/setvar key=wi_personality {{pipe}}|
	
	/createentry file={{getvar::wi_personality}} key="Both Young Main" Lively: Curious: Bouncy: Cheery: Vivid: Spry|
	/setentryfield file={{getvar::wi_personality}} uid={{pipe}} field=key {{noop}}|
	
	/createentry file={{getvar::wi_personality}} key="Both Teen Main" Rebellious: Impulsive: Quirky: Defiant: Ebullient: Restless: Fervent|
	/setentryfield file={{getvar::wi_personality}} uid={{pipe}} field=key {{noop}}|
	
	/createentry file={{getvar::wi_personality}} key="Both Adult Main" Mature: Resolute: Experienced: Pragmatic: Seasoned: Earnest|
	/setentryfield file={{getvar::wi_personality}} uid={{pipe}} field=key {{noop}}|
	
	/createentry file={{getvar::wi_personality}} key="Both General Main" Cool: Charismatic: Witty: Resourceful: Heroic: Adventurous: Mysterious: Dynamic: Optimistic: Balanced|
	/setentryfield file={{getvar::wi_personality}} uid={{pipe}} field=key {{noop}}|
	
	/createentry file={{getvar::wi_personality}} key="Male Young Main" Sporty: Rascal: Brave: Tough: Impish: Rowdy|
	/setentryfield file={{getvar::wi_personality}} uid={{pipe}} field=key {{noop}}|
	
	/createentry file={{getvar::wi_personality}} key="Male Teen Main" Edgy: Somber: Angsty: Daring: Unruly: Fierce|
	/setentryfield file={{getvar::wi_personality}} uid={{pipe}} field=key {{noop}}|
	
	/createentry file={{getvar::wi_personality}} key="Male Adult Main" Stoic: Professional: Dependable: Courageous: Wise: Gentlemanly: Authoritative|
	/setentryfield file={{getvar::wi_personality}} uid={{pipe}} field=key {{noop}}|
	
	/createentry file={{getvar::wi_personality}} key="Male General Main" Gallant: Valiant: Rugged: Steadfast: colonnding: Innovative: Assertive: Dignified|
	/setentryfield file={{getvar::wi_personality}} uid={{pipe}} field=key {{noop}}|
	
	/createentry file={{getvar::wi_personality}} key="Female Young Main" Cute: Bubbly: Sweet: Darling: Peppy: Sparkling|
	/setentryfield file={{getvar::wi_personality}} uid={{pipe}} field=key {{noop}}|
	
	/createentry file={{getvar::wi_personality}} key="Female Teen Main" Tsundere: Spunky: Feisty: Passionate: Vibrant: Mischievous: Dreamy|
	/setentryfield file={{getvar::wi_personality}} uid={{pipe}} field=key {{noop}}|
	
	/createentry file={{getvar::wi_personality}} key="Female Adult Main" Elegant: Sophisticated: Graceful: Independent: Compassionate: Refined|
	/setentryfield file={{getvar::wi_personality}} uid={{pipe}} field=key {{noop}}|
	
	/createentry file={{getvar::wi_personality}} key="Female General Main" Tomboy: Sassy: Stylish: Empowered: Resilient: Magnetic: Voguish: Alluring: Confident: Radiant|
	/setentryfield file={{getvar::wi_personality}} uid={{pipe}} field=key {{noop}}|
	
	/createentry file={{getvar::wi_personality}} key="Both Positive" Compassionate: Empathetic: Generous: Optimistic: Altruistic: Honest: Trustworthy: Loyal: Encouraging: Understanding
	/setentryfield file={{getvar::wi_personality}} uid={{pipe}} field=key {{noop}}|
	
	/createentry file={{getvar::wi_personality}} key="Both Negative" Arrogant: Selfish: Impulsive: Pessimistic: Cynical: Manipulative: Indifferent: Stubborn: Deceitful: Reckless
	/setentryfield file={{getvar::wi_personality}} uid={{pipe}} field=key {{noop}}|
	
	/createentry file={{getvar::wi_personality}} key="Both Neutral" Reserved: Practical: Indecisive: Matter-of-fact: Unassuming: Pragmatic: Observant: Reflective: Realistic: Analytical
	/setentryfield file={{getvar::wi_personality}} uid={{pipe}} field=key {{noop}}|
	
	/createentry file={{getvar::wi_personality}} key="Male Positive" Assertive: Courageous: Chivalrous: Dependable: Resilient: Ambitious: Protective: Disciplined: Resourceful: Determined
	/setentryfield file={{getvar::wi_personality}} uid={{pipe}} field=key {{noop}}|
	
	/createentry file={{getvar::wi_personality}} key="Male Negative" Aggressive: Domineering: Callous: Self-centered: Unsympathetic: Rigid: Controlling: Belligerent: Inconsiderate: Harsh
	/setentryfield file={{getvar::wi_personality}} uid={{pipe}} field=key {{noop}}|
	
	/createentry file={{getvar::wi_personality}} key="Male Neutral" Stoic: Silent: Detached: Logical: Clinical: Unflappable: Objective: Structured: Inexpressive: Discerning
	/setentryfield file={{getvar::wi_personality}} uid={{pipe}} field=key {{noop}}|
	
	/createentry file={{getvar::wi_personality}} key="Female Positive" Nurturing: Warm: Graceful: Delicate: Intuitive: Supportive: Patient: Caring: Sincere: Spirited
	/setentryfield file={{getvar::wi_personality}} uid={{pipe}} field=key {{noop}}|
	
	/createentry file={{getvar::wi_personality}} key="Female Negative" Overcritical: Moody: Indecisive: Anxious: Self-doubting: Submissive: Perfectionist: Jealous: Vindictive: Temperamental
	/setentryfield file={{getvar::wi_personality}} uid={{pipe}} field=key {{noop}}|
	
	/createentry file={{getvar::wi_personality}} key="Female Neutral" Quiet: Discreet: Composed: Thoughtful: Cautious: Grounded: Mellow: Reticent: Measured: Serene
	/setentryfield file={{getvar::wi_personality}} uid={{pipe}} field=key {{noop}}|
:}|
//---------|

//---------|
/ife ( 'CMC Generation Prompts' not in lorebookList) {:
	/getchatbook name="CMC Generation Prompts"|
	/setvar key=wi_gen_prompt {{pipe}}|
	//Basic Character Information|
  
	/createentry file={{getvar::wi_gen_prompt}} key="Nationalities: Prompt" Generate a colon-separated list of five Nationalities.|
	/setentryfield file={{getvar::wi_gen_prompt}} uid={{pipe}} field=key {{noop}}|
  
	/createentry file={{getvar::wi_gen_prompt}} key="Nationalities: Instruction" "INSTRUCTIONS:
1. Only respond with a colon-separated list and nothing else."|
	/setentryfield file={{getvar::wi_gen_prompt}} uid={{pipe}} field=key {{noop}}|

	/createentry file={{getvar::wi_gen_prompt}} key="Ethnicities: Prompt" Generate a colon-separated list of five Ethnicities.|
	/setentryfield file={{getvar::wi_gen_prompt}} uid={{pipe}} field=key {{noop}}|

	/createentry file={{getvar::wi_gen_prompt}} key="Ethnicities: Instruction" "INSTRUCTIONS:
1. Only respond with a colon-separated list and nothing else."|
	/setentryfield file={{getvar::wi_gen_prompt}} uid={{pipe}} field=key {{noop}}|

	/createentry file={{getvar::wi_gen_prompt}} key="First Name: Prompt" Generate a colon-separated list of five {{getvar::gender}} first names.|
	/setentryfield file={{getvar::wi_gen_prompt}} uid={{pipe}} field=key {{noop}}|

	/createentry file={{getvar::wi_gen_prompt}} key="First Name: Instruction" "INSTRUCTIONS:
1. Only respond with a colon-separated list and nothing else."|
	/setentryfield file={{getvar::wi_gen_prompt}} uid={{pipe}} field=key {{noop}}|

	/createentry file={{getvar::wi_gen_prompt}} key="Last Name: Prompt" Generate a colon-separated list of five {{getvar::gender}} last names that complement the first name: {{getvar::firstName}}.|
	/setentryfield file={{getvar::wi_gen_prompt}} uid={{pipe}} field=key {{noop}}|

	/createentry file={{getvar::wi_gen_prompt}} key="Last Name: Instruction" "INSTRUCTIONS:
1. Only respond with a colon-separated list and nothing else."|
	/setentryfield file={{getvar::wi_gen_prompt}} uid={{pipe}} field=key {{noop}}|

	/createentry file={{getvar::wi_gen_prompt}} key="Nickname: Prompt" Generate a colon-separated list of five {{getvar::gender}} nicknames that complement the name: {{getvar::firstName}} {{getvar::lname}}.|
	/setentryfield file={{getvar::wi_gen_prompt}} uid={{pipe}} field=key {{noop}}|

	/createentry file={{getvar::wi_gen_prompt}} key="Nickname: Instruction" "INSTRUCTIONS:
1. The generated nicknames should be a mix of something parents or close friends use.
2. Only respond with a colon-separated list and nothing else."|
	/setentryfield file={{getvar::wi_gen_prompt}} uid={{pipe}} field=key {{noop}}|

	/createentry file={{getvar::wi_gen_prompt}} key="Genre: Prompt" Generate a colon-separated list of ten genres.|
	/setentryfield file={{getvar::wi_gen_prompt}} uid={{pipe}} field=key {{noop}}|

	/createentry file={{getvar::wi_gen_prompt}} key="Genre: Instruction" "INSTRUCTIONS:
1. The generated genres should be a mix of Anime, Film, Fantasy or Sci-Fi genres.
2. Only respond with a colon-separated list and nothing else."|
	/setentryfield file={{getvar::wi_gen_prompt}} uid={{pipe}} field=key {{noop}}|

	/createentry file={{getvar::wi_gen_prompt}} key="Time Period: Prompt" Generate a colon-separated list of five time periods and five fictional time periods.|
	/setentryfield file={{getvar::wi_gen_prompt}} uid={{pipe}} field=key {{noop}}|

	/createentry file={{getvar::wi_gen_prompt}} key="Time Period: Instruction" "INSTRUCTIONS:
1. There should be only one combined list.
2. Only respond with a colon-separated list and nothing else."|
	/setentryfield file={{getvar::wi_gen_prompt}} uid={{pipe}} field=key {{noop}}|

	/createentry file={{getvar::wi_gen_prompt}} key="World Type: Prompt" Generate a colon-separated list of five world types that could replace X in this sentence.
The story takes place in a X setting.|
	/setentryfield file={{getvar::wi_gen_prompt}} uid={{pipe}} field=key {{noop}}|
	
	/createentry file={{getvar::wi_gen_prompt}} key="World Type: Instruction" "INSTRUCTIONS:
1. Each world type should be the full sentence.
2. Only respond with a colon-separated list and nothing else."|
	/setentryfield file={{getvar::wi_gen_prompt}} uid={{pipe}} field=key {{noop}}|

	/createentry file={{getvar::wi_gen_prompt}} key="Species: Prompt" Generate a colon-separated list of five {{getvar::normal_form}} {{getvar::type}} species.|
	/setentryfield file={{getvar::wi_gen_prompt}} uid={{pipe}} field=key {{noop}}|
	
	/createentry file={{getvar::wi_gen_prompt}} key="Species: Instruction" "INSTRUCTIONS:
1. Only respond with a colon-separated list and nothing else."|
	/setentryfield file={{getvar::wi_gen_prompt}} uid={{pipe}} field=key {{noop}}|

	/createentry file={{getvar::wi_gen_prompt}} key="Species Description: Prompt" Generate a general description of the species: {{getvar::normal_form}} {{getvar::type}} {{getvar::species}}.|
	/setentryfield file={{getvar::wi_gen_prompt}} uid={{pipe}} field=key {{noop}}|

	/createentry file={{getvar::wi_gen_prompt}} key="Species: Instruction" "INSTRUCTIONS:
1. Only respond with the general description and nothing else."|
	/setentryfield file={{getvar::wi_gen_prompt}} uid={{pipe}} field=key {{noop}}|

	/createentry file={{getvar::wi_gen_prompt}} key="Student: Prompt" Given that the person is {{getvar::age}}, return the most appropriate school level label.|
	/setentryfield file={{getvar::wi_gen_prompt}} uid={{pipe}} field=key {{noop}}|

	/createentry file={{getvar::wi_gen_prompt}} key="Student: Instruction" "INSTRUCTIONS:
1. Acceptable replies are: Preschooler, xth Grader (e.g., 1st Grader, 2nd Grader, etc.), Middle Schooler, High School Student, College Student, or University Student.
2. Use correct ordinal formatting (e.g., 1st, 2nd, 3rd, 4th, etc.) in 'xth Grader'.
3. Only respond with the school level label and nothing else."|
	/setentryfield file={{getvar::wi_gen_prompt}} uid={{pipe}} field=key {{noop}}|


	/createentry file={{getvar::wi_gen_prompt}} key="Study Occupation: Prompt" Given that the person is a {{getvar::student}}, Generate a list of ten colon-separated Occupations the persion could study as.|
	/setentryfield file={{getvar::wi_gen_prompt}} uid={{pipe}} field=key {{noop}}|
	
	/createentry file={{getvar::wi_gen_prompt}} key="Study Occupation: Instruction" "INSTRUCTIONS:
1. Only respond with the colon-separated list and nothing else."|
	/setentryfield file={{getvar::wi_gen_prompt}} uid={{pipe}} field=key {{noop}}|

	/createentry file={{getvar::wi_gen_prompt}} key="World Details: Examples" EXAMPLES (for your reference—do not include in the answer):
The fantasy world of Root, inhabited by monsters and other fictional races.|
	/setentryfield file={{getvar::wi_gen_prompt}} uid={{pipe}} field=key {{noop}}|
	
	/createentry file={{getvar::wi_gen_prompt}} key="World Details: Prompt" Generate a |
	/setentryfield file={{getvar::wi_gen_prompt}} uid={{pipe}} field=key {{noop}}|
	
	/createentry file={{getvar::wi_gen_prompt}} key="World Details: Instruction" "INSTRUCTIONS:
1. Only respond with the colon-separated list and nothing else."|
	/setentryfield file={{getvar::wi_gen_prompt}} uid={{pipe}} field=key {{noop}}|

	/createentry file={{getvar::wi_gen_prompt}} key="Lore: Examples" EXAMPLES (for your reference—do not include in the answer):
Root is a medieval Scandinavian fantasy world with magic, monsters, heroes, and a bunch of MMORPG cliches. Aedelgard is one of the kingdoms in Root. Outskirts of the cities boil with monsters of various danger levels. This world works under [...]|
	/setentryfield file={{getvar::wi_gen_prompt}} uid={{pipe}} field=key {{noop}}|
	
	/createentry file={{getvar::wi_gen_prompt}} key="Lore: Prompt"  .|
	/setentryfield file={{getvar::wi_gen_prompt}} uid={{pipe}} field=key {{noop}}|
	
	/createentry file={{getvar::wi_gen_prompt}} key="Lore: Instruction" "INSTRUCTIONS:
1. Only respond with the colon-separated list and nothing else."|
	/setentryfield file={{getvar::wi_gen_prompt}} uid={{pipe}} field=key {{noop}}|

	/createentry file={{getvar::wi_gen_prompt}} key="Lore: Examples" EXAMPLES (for your reference—do not include in the answer):
In one of his adventures, {{user}} was severely wounded and lost his party. However, a passing healer (Ottis) saved him and brought him to a nearby Maretta's [...]|
	/setentryfield file={{getvar::wi_gen_prompt}} uid={{pipe}} field=key {{noop}}|
	
	/createentry file={{getvar::wi_gen_prompt}} key="Lore: Prompt"  .|
	/setentryfield file={{getvar::wi_gen_prompt}} uid={{pipe}} field=key {{noop}}|
	
	/createentry file={{getvar::wi_gen_prompt}} key="Lore: Instruction" "INSTRUCTIONS:
1. Only respond with the colon-separated list and nothing else."|
	/setentryfield file={{getvar::wi_gen_prompt}} uid={{pipe}} field=key {{noop}}|
	
	
	//--Basic Character Information--|
/*
	/createentry file={{getvar::wi_gen_prompt}} key="Character: Context" "CONTEXT (for your reference—do not include in the answer):
- Name: {{getvar::firstName}} {{getvar::lastName}}
- Age: {{getvar::parcedAge}}
- Gender: {{getvar::gender}}
- Species: {{getvar::parsedSpecies}}"|
*|
	/createentry file={{getvar::wi_gen_prompt}} key="Character: Context" "CONTEXT (for your reference—do not include in the answer):
- Name: {{getvar::firstName}} {{getvar::lastName}}
- Age: {{getvar::parcedAge}}
- Gender: {{getvar::gender}}
- Species: {{getvar::parsedSpecies}}"|
	/setentryfield file={{getvar::wi_gen_prompt}} uid={{pipe}} field=key {{noop}}|

	//Personality Information|
	/createentry file={{getvar::wi_gen_prompt}} key="Human Traits: Task" Generate a colon-separated list of five Human specific traits that are not normal for a {{getvar::species}} to have.|
	/setentryfield file={{getvar::wi_gen_prompt}} uid={{pipe}} field=key {{noop}}|
	/createentry file={{getvar::wi_gen_prompt}} key="Human Traits: Instruction" "INSTRUCTIONS:
1. {{getvar::firstName}} is a {{getvar::age}} {{getvar::gender}} {{getvar::parsedSpecies}}.
2. Only respond with a colon-separated list and nothing else."|
	/setentryfield file={{getvar::wi_gen_prompt}} uid={{pipe}} field=key {{noop}}|

	/createentry file={{getvar::wi_gen_prompt}} key="{{getvar::species}} Traits: Task" Generate a colon-separated list of five {{getvar::species}} specific traits.|
	/setentryfield file={{getvar::wi_gen_prompt}} uid={{pipe}} field=key {{noop}}|
	/createentry file={{getvar::wi_gen_prompt}} key="{{getvar::species}} Traits: Instruction" "INSTRUCTIONS:
1. {{getvar::firstName}} is a {{getvar::age}} {{getvar::gender}} {{getvar::parsedSpecies}}.
2. Only respond with a colon-separated list and nothing else."|
	/setentryfield file={{getvar::wi_gen_prompt}} uid={{pipe}} field=key {{noop}}|

	/createentry file={{getvar::wi_gen_prompt}} key="Quirk: Task" Generate a colon-separated list of five quirks.|
	/setentryfield file={{getvar::wi_gen_prompt}} uid={{pipe}} field=key {{noop}}|
	/createentry file={{getvar::wi_gen_prompt}} key="Quirk: Instruction" "INSTRUCTIONS:
1. The quirks should be something {{getvar::firstName}} does that other think is odd.
2. Each quirk should be a short sentence.
3. {{getvar::firstName}} is a {{getvar::age}} {{getvar::gender}} {{getvar::parsedSpecies}}.
4. Only respond with a colon-separated list and nothing else."|
	/setentryfield file={{getvar::wi_gen_prompt}} uid={{pipe}} field=key {{noop}}|

	/createentry file={{getvar::wi_gen_prompt}} key="God Habit: Task" Generate a colon-separated list of five Good Habits.|
	/setentryfield file={{getvar::wi_gen_prompt}} uid={{pipe}} field=key {{noop}}|
	/createentry file={{getvar::wi_gen_prompt}} key="God Habit: Instruction" "INSTRUCTIONS:
1. The habits should be habits that is good to have.
2. Each habit should be a short sentence.
3. {{getvar::firstName}} is a {{getvar::age}} {{getvar::gender}} {{getvar::parsedSpecies}}.
4. Only respond with a colon-separated list and nothing else."|
	/setentryfield file={{getvar::wi_gen_prompt}} uid={{pipe}} field=key {{noop}}|

	/createentry file={{getvar::wi_gen_prompt}} key="Bad Habit: Task" Generate a colon-separated list of five Bad Habits.|
	/setentryfield file={{getvar::wi_gen_prompt}} uid={{pipe}} field=key {{noop}}|
	/createentry file={{getvar::wi_gen_prompt}} key="Bad Habit: Instruction" "INSTRUCTIONS:
1. The habits should be habits that is bad to have.
2. Each habit should be a short sentence.
3. {{getvar::firstName}} is a {{getvar::age}} {{getvar::gender}} {{getvar::parsedSpecies}}.
4. Only respond with a colon-separated list and nothing else."|
	/setentryfield file={{getvar::wi_gen_prompt}} uid={{pipe}} field=key {{noop}}|

	/createentry file={{getvar::wi_gen_prompt}} key="Main Personality Description: Task" "TASK:
Generate one sentence describing how the main personality trait {{getvar::item}} manifests in {{getvar::firstName}}’s behavior."|
	/setentryfield file={{getvar::wi_gen_prompt}} uid={{pipe}} field=key {{noop}}|
	/createentry file={{getvar::wi_gen_prompt}} key="Main Personality Description: Instruction" "INSTRUCTIONS:
1. Do NOT mention age, gender, species, or any other biographical detail.
2. Keep it to exactly one concise sentence illustrating the trait in action.
3. Focus solely on how {{getvar::item}} shows up in their choices, actions or demeanor.
4. Return ONLY that single sentence."|
	/setentryfield file={{getvar::wi_gen_prompt}} uid={{pipe}} field=key {{noop}}|
	//--Personality Information--|
:}|
//---------|
