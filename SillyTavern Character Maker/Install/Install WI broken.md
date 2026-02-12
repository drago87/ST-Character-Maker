/wi-list-books all=true|
/let key=lorebookList {{pipe}}|
//---------|

/ife ( 'CMC Clothes' not in lorebookList) {:
	/echo Creating Lorebook 1/5 "CMC Clothes"|
	/getchatbook name="CMC Clothes"|
	/let key=wi_clothes {{pipe}}|
	/wait 100|
	/createentry file={{var::wi_clothes}} key="Female Underwear Top" Bare: Bra: Sports Bra: Bralette: Camisole: Crop Top: Training Bra|
	/setentryfield file={{var::wi_clothes}} uid={{pipe}} field=key {{noop}}|
	/wait 100|
	/createentry file={{var::wi_clothes}} key="Female Underwear Bottom" Bare: Panties: Bloomer: Thong: Bikini: Briefs: Boyshorts: Hipster|
	/setentryfield file={{var::wi_clothes}} uid={{pipe}} field=key {{noop}}|
	/wait 100|
	/createentry file={{var::wi_clothes}} key="Female Clothes Top" Bare: Shirt: Blouse: T-Shirt: Tank Top: Crop Top: Sweater: Hoodie: Cardigan: Camisole: Tunic: Button-Up Shirt: Bikini Top|
	/setentryfield file={{var::wi_clothes}} uid={{pipe}} field=key {{noop}}|
	/wait 100|
	/createentry file={{var::wi_clothes}} key="Female Clothes Bottom" Bare: Skirt: Skirt: Pants: Jeans: Leggings: Shorts: Culottes: Trousers: Capris: Joggers: Palazzo Pants: Bikini Bottom|
	/setentryfield file={{var::wi_clothes}} uid={{pipe}} field=key {{noop}}|
	/wait 100|
	/createentry file={{var::wi_clothes}} key="Female Clothes Extra" Pantyhose: Thigh Highs|
	/setentryfield file={{var::wi_clothes}} uid={{pipe}} field=key {{noop}}|
	/wait 100|
	/createentry file={{var::wi_clothes}} key="Female Clothes One-Piece" Bare: Dress: One-Piece Swimsuit|
	/setentryfield file={{var::wi_clothes}} uid={{pipe}} field=key {{noop}}|
	/wait 100|
	/createentry file={{var::wi_clothes}} key="Male Underwear Bottom" Bare: Boxers: Briefs: Boxer Briefs: Trunks: Jockstraps|
	/setentryfield file={{var::wi_clothes}} uid={{pipe}} field=key {{noop}}|
	/wait 100|
	/createentry file={{var::wi_clothes}} key="Male Clothes Top" Bare: Shirt: Sweater|
	/setentryfield file={{var::wi_clothes}} uid={{pipe}} field=key {{noop}}|
	/wait 100|
	/createentry file={{var::wi_clothes}} key="Male Clothes Bottom" Bare: Pants: Shorts|
	/setentryfield file={{var::wi_clothes}} uid={{pipe}} field=key {{noop}}|
	/wait 100|
	/createentry file={{var::wi_clothes}} key="Clothes Socks" Barefoot: Ankle Socks: Normal Socks: Knee Socks|
	/setentryfield file={{var::wi_clothes}} uid={{pipe}} field=key {{noop}}|
	/wait 100|
	/createentry file={{var::wi_clothes}} key="Clothes Hat" Bare: Cuffed Beanie: Peaked Cap|
	/setentryfield file={{var::wi_clothes}} uid={{pipe}} field=key {{noop}}|
	/wait 100|
:}|
//---------|

//---------|

/ife ( 'CMC Appearance' not in lorebookList) {:
	/echo Creating Lorebook "CMC Appearance"|
	/getchatbook name="CMC Appearance"|
	/let key=wi_appearance|
	/wait 100|
	/echo 1/12|
	/createentry file={{var::wi_appearance}} key="Female Hairstyle" Single Braid: Pixie Cut|
	/setentryfield file={{var::wi_appearance}} uid={{pipe}} field=key {{noop}}|
	/wait 100|
	/echo 2/12|
	/createentry file={{var::wi_appearance}} key="Female Brest Size" Flat: Small: Medium: Large: Huge|
	/setentryfield file={{var::wi_appearance}} uid={{pipe}} field=key {{noop}}|
	/wait 100|
	/echo 3/12|
	/createentry file={{var::wi_appearance}} key="Female Pussy Type" Curved outer lips (The outer lips have a curved magnet-like shape, meeting at the bottom. This shape will create a window in the middle revealing the inner lips.): Prominent inner lips (The inner lips are larger than the outer lips.): Prominent outer lips (The outer lips are larger than the inner lips. They tend to sit lower on the vulva and may extend beyond underwear. Both full and puffy outer lips, as well as thin and loose outer lips, can fit into this category.): Long, dangling inner lips (The inner lips are longer than the outer lips and seem to dangle from the vulva. These inner lips can be an inch long or longer, or they may look like there's extra skin or folds.): Long, dangling outer lips (The outer lips are longer than the inner lips. This is a form of prominent outer lips, though this structure, in particular, tends to involve thinner or looser outer lips that may extend beyond underwear.): Small, closed lips (In some vulvas, "the labia majora and the labia minora blend together so it's not really like two sets of lips; it's more like one,". While they are technically two separate parts, the outer lips are closed so that they conceal the inner lips.): Small, open lips (With this type of vulva, the outer lips are small, but they're set farther apart making them appear slightly open.): Visible inner lips (The outer lips appear curved or pulled outward, leaving almost a window for the inner lips to peek through.)|
	/setentryfield file={{var::wi_appearance}} uid={{pipe}} field=key {{noop}}|
	/wait 100|
	/echo 4/12|
	/createentry file={{var::wi_appearance}} key="Male Penis Size Flaccid" Small: Medium: Large: Huge|
	/setentryfield file={{var::wi_appearance}} uid={{pipe}} field=key {{noop}}|
	/wait 100|
	/echo 5/12|
	/createentry file={{var::wi_appearance}} key="Male Penis Size Erect" Small: Medium: Large: Huge|
	/setentryfield file={{var::wi_appearance}} uid={{pipe}} field=key {{noop}}|
	/wait 100|
	/echo 6/12|
	/createentry file={{var::wi_appearance}} key="Male Hairstyle" Buzzcut|
	/setentryfield file={{var::wi_appearance}} uid={{pipe}} field=key {{noop}}|
	/wait 100|
	/echo 7/12|
	/createentry file={{var::wi_appearance}} key="Butt Size" Small: Medium: Large: Huge|
	/setentryfield file={{var::wi_appearance}} uid={{pipe}} field=key {{noop}}|
	/wait 100|
	/echo 8/12|
	/createentry file={{var::wi_appearance}} key="Hair Color" Black: Brown: Blond: Red|
	/setentryfield file={{var::wi_appearance}} uid={{pipe}} field=key {{noop}}|
	/wait 100|
	/echo 9/12|
	/createentry file={{var::wi_appearance}} key="Hair Length" Bald: Short: Medium: Long|
	/setentryfield file={{var::wi_appearance}} uid={{pipe}} field=key {{noop}}|
	/wait 100|
	/echo 10/12|
	/createentry file={{var::wi_appearance}} key="Skin Color" Creamy: White: Brown|
	/setentryfield file={{var::wi_appearance}} uid={{pipe}} field=key {{noop}}|
	/wait 100|
	/echo 11/12|
	/createentry file={{var::wi_appearance}} key="Iris Color" Green: Blue: Brown|
	/setentryfield file={{var::wi_appearance}} uid={{pipe}} field=key {{noop}}|
	/wait 100|
	/echo 12/12|
	/createentry file={{var::wi_appearance}} key="Sclera Color" White: Red: Green: Blue: Brown|
	/setentryfield file={{var::wi_appearance}} uid={{pipe}} field=key {{noop}}|
:}|
//---------|

//---------|

/ife ( 'CMC Variables' not in lorebookList) {:
	/echo Creating Lorebook 3/5 "CMC Variables"|
	/getchatbook name="CMC Variables"|
	/let key=wi_variables|
	
	
	/createentry file={{var::wi_variables}} key="Covering Anthro" The covering of a  is the same covering as the normal  except for on the face, chest, paws and genitalia area where it is generally less.

A Andromorphic animal stands on two legs and is mostly formed like a Human except for the  features such as the ears and tail etc...|
	/setentryfield file={{var::wi_variables}} uid={{pipe}} field=key {{noop}}|
	
	/createentry file={{var::wi_variables}} key="Covering Furry" The covering of a  is the same covering as the normal  but it will only cover part of the body. Such as the ears, tail, shoulders, stomach, upper arms, calves and feet. There could also be a small amount on the breasts and genitalia area.

A Furry animal stands on two legs and is mostly formed like a Human except for the  features such as the ears and tail etc...|
	/setentryfield file={{var::wi_variables}} uid={{pipe}} field=key {{noop}}|
	
	/createentry file={{var::wi_variables}} key="Exclude from gen" Exclude Character Development or Self-Discovery from your reply.
Exclude emotional or interpretative phrases from your reply.
Exclude enchanting qualities or highlights from your reply.
Exclude origins or age from your reply.
Exclude future speculations from your reply.|
	/setentryfield file={{var::wi_variables}} uid={{pipe}} field=key {{noop}}|

	/createentry file={{var::wi_variables}} key="Guide prompt" The reply should be about: |
	/setentryfield file={{var::wi_variables}} uid={{pipe}} field=key {{noop}}|

	/createentry file={{var::wi_variables}} key="Seasons: List" Spring: Summer: Autumn: Winter|
	/setentryfield file={{var::wi_variables}} uid={{pipe}} field=key {{noop}}|

	/createentry file={{var::wi_variables}} key="Type Guide" Human is a standard human.
Anthro is a animal that have a human form.
Mythfolk is races that mostly looks like humans like Dwarfs, Elves etc...
Furry is animal like humans that mostly looks like humans but have certain animal parts.
Feral is standard animals, fantasy animals or monsters.
Pokémon is the creatures from the Pokémon games and anime.
Digimon is the creatures from the Digimon games and anime.
	/setentryfield file={{var::wi_variables}} uid={{pipe}} field=key {{noop}}|

	/createentry file={{var::wi_variables}} key="Scenario prompt" .
Always use '{\{user}}' instead of '{\{user}}'. Never use 'the {\{user}}'.
The reply should be from 's point of view.
[Never act or talk as {\{user}}.]
End the scenario where {\{user}} can make a choice or act silently implying that it is {\{user}}'s turn.
Now make a scenario. While making the scenario keeping the text airy and the text informal.|
	/setentryfield file={{var::wi_variables}} uid={{pipe}} field=key {{noop}}|

	/createentry file={{var::wi_variables}} key="Anthropomorphic Animals" Anthro (Anthropomorphic) beings combine humanoid structure with animalistic traits.
They retain the general body structure of a bipedal humanoid, with a torso, two arms, and two legs, but incorporate features from their species.
Common traits include digitigrade or plantigrade legs, a tail for balance, species-specific head shapes (such as muzzles or beaks), and grasping hands with claws or fingers.
Their feet resemble those of their species but are adapted for upright movement.
Wings, if present, are structured for flight or display and are non-retractable.
Anthros interact with their environment in a human-like manner, using tools and gestures.
They may have fur, scales, feathers, or other coverings based on their species.|
	/setentryfield file={{var::wi_variables}} uid={{pipe}} field=key {{noop}}|

	/createentry file={{var::wi_variables}} key="Furry" Furry=Singular
Furries=Multiple Furry
Furries is are essentially humans with animal heads and tails. Their hands are human hands, and their feet are human feet with animal-like toes. They can wear human clothing and engaging in any human activity. They have less  {{getvar::coverType}} throughout their body but the {{getvar::coverType}} is emphasized on the tail and ears. They commonly have human hair styles on their head.|
	/setentryfield file={{var::wi_variables}} uid={{pipe}} field=key {{noop}}|

	/createentry file={{var::wi_variables}} key="Feral" Ferals are basically animals, or the "normal" version of common mythical and fantasy creatures. They may or may not be sentient, and typically do not wear clothes or accessories. Ferals are often described in dramatic poses to emphasize their markings and overall appearance.|
	/setentryfield file={{var::wi_variables}} uid={{pipe}} field=key {{noop}}|


	/createentry file={{var::wi_variables}} key="Appearance Trait Template" - Appearance Trait: --apperanceTrait--
  ↳ Details: --apperanceTraitDetails--
  ↳ Effect: --apperanceTraitEffect--|
	/setentryfield file={{var::wi_variables}} uid={{pipe}} field=key {{noop}}|

	/createentry file={{var::wi_variables}} key="Apperance Q&A: Template" Q: --Question--
A: --Answer--|
	/setentryfield file={{var::wi_variables}} uid={{pipe}} field=key {{noop}}|

	/createentry file={{var::wi_variables}} key="Item: Template" "- Item: --item--
  ↳ Details: --itemDetails--"|
	/setentryfield file={{var::wi_variables}} uid={{pipe}} field=key {{noop}}|
	
	/createentry file={{var::wi_variables}} key="Ability; " "- Ability: --ability--
  ↳ Details: --abilityDetails--"|
	/setentryfield file={{var::wi_variables}} uid={{pipe}} field=key {{noop}}|

	/fetch https://raw.githubusercontent.com/drago87/ST-Character-Maker/refs/heads/Fetch-Files/SillyTavern%20Character%20Maker/Templates/JED%2B%20Clean%20Template.md|
	/createentry file={{var::wi_variables}} key="Character Template" {{pipe}}|
	/setentryfield file={{var::wi_variables}} uid={{pipe}} field=key {{noop}}|

:}|
//---------|

//---------|

/ife ( 'CMC Personality' not in lorebookList) {:
	/echo Creating Lorebook 4/5 "CMC Personality"|
	/getchatbook name="CMC Personality"|
	/let key=wi_personality {{pipe}}|
	
	/createentry file={{var::wi_personality}} key="Both Young Main" Lively: Curious: Bouncy: Cheery: Vivid: Spry|
	/setentryfield file={{var::wi_personality}} uid={{pipe}} field=key {{noop}}|
	
	/createentry file={{var::wi_personality}} key="Both Teen Main" Rebellious: Impulsive: Quirky: Defiant: Ebullient: Restless: Fervent|
	/setentryfield file={{var::wi_personality}} uid={{pipe}} field=key {{noop}}|
	
	/createentry file={{var::wi_personality}} key="Both Adult Main" Mature: Resolute: Experienced: Pragmatic: Seasoned: Earnest|
	/setentryfield file={{var::wi_personality}} uid={{pipe}} field=key {{noop}}|
	
	/createentry file={{var::wi_personality}} key="Both General Main" Cool: Charismatic: Witty: Resourceful: Heroic: Adventurous: Mysterious: Dynamic: Optimistic: Balanced|
	/setentryfield file={{var::wi_personality}} uid={{pipe}} field=key {{noop}}|
	
	/createentry file={{var::wi_personality}} key="Male Young Main" Sporty: Rascal: Brave: Tough: Impish: Rowdy|
	/setentryfield file={{var::wi_personality}} uid={{pipe}} field=key {{noop}}|
	
	/createentry file={{var::wi_personality}} key="Male Teen Main" Edgy: Somber: Angsty: Daring: Unruly: Fierce|
	/setentryfield file={{var::wi_personality}} uid={{pipe}} field=key {{noop}}|
	
	/createentry file={{var::wi_personality}} key="Male Adult Main" Stoic: Professional: Dependable: Courageous: Wise: Gentlemanly: Authoritative|
	/setentryfield file={{var::wi_personality}} uid={{pipe}} field=key {{noop}}|
	
	/createentry file={{var::wi_personality}} key="Male General Main" Gallant: Valiant: Rugged: Steadfast: colonnding: Innovative: Assertive: Dignified|
	/setentryfield file={{var::wi_personality}} uid={{pipe}} field=key {{noop}}|
	
	/createentry file={{var::wi_personality}} key="Female Young Main" Cute: Bubbly: Sweet: Darling: Peppy: Sparkling|
	/setentryfield file={{var::wi_personality}} uid={{pipe}} field=key {{noop}}|
	
	/createentry file={{var::wi_personality}} key="Female Teen Main" Tsundere: Spunky: Feisty: Passionate: Vibrant: Mischievous: Dreamy|
	/setentryfield file={{var::wi_personality}} uid={{pipe}} field=key {{noop}}|
	
	/createentry file={{var::wi_personality}} key="Female Adult Main" Elegant: Sophisticated: Graceful: Independent: Compassionate: Refined|
	/setentryfield file={{var::wi_personality}} uid={{pipe}} field=key {{noop}}|
	
	/createentry file={{var::wi_personality}} key="Female General Main" Tomboy: Sassy: Stylish: Empowered: Resilient: Magnetic: Voguish: Alluring: Confident: Radiant|
	/setentryfield file={{var::wi_personality}} uid={{pipe}} field=key {{noop}}|
	
	/createentry file={{var::wi_personality}} key="Both Positive" Compassionate: Empathetic: Generous: Optimistic: Altruistic: Honest: Trustworthy: Loyal: Encouraging: Understanding
	/setentryfield file={{var::wi_personality}} uid={{pipe}} field=key {{noop}}|
	
	/createentry file={{var::wi_personality}} key="Both Negative" Arrogant: Selfish: Impulsive: Pessimistic: Cynical: Manipulative: Indifferent: Stubborn: Deceitful: Reckless
	/setentryfield file={{var::wi_personality}} uid={{pipe}} field=key {{noop}}|
	
	/createentry file={{var::wi_personality}} key="Both Neutral" Reserved: Practical: Indecisive: Matter-of-fact: Unassuming: Pragmatic: Observant: Reflective: Realistic: Analytical
	/setentryfield file={{var::wi_personality}} uid={{pipe}} field=key {{noop}}|
	
	/createentry file={{var::wi_personality}} key="Male Positive" Assertive: Courageous: Chivalrous: Dependable: Resilient: Ambitious: Protective: Disciplined: Resourceful: Determined
	/setentryfield file={{var::wi_personality}} uid={{pipe}} field=key {{noop}}|
	
	/createentry file={{var::wi_personality}} key="Male Negative" Aggressive: Domineering: Callous: Self-centered: Unsympathetic: Rigid: Controlling: Belligerent: Inconsiderate: Harsh
	/setentryfield file={{var::wi_personality}} uid={{pipe}} field=key {{noop}}|
	
	/createentry file={{var::wi_personality}} key="Male Neutral" Stoic: Silent: Detached: Logical: Clinical: Unflappable: Objective: Structured: Inexpressive: Discerning
	/setentryfield file={{var::wi_personality}} uid={{pipe}} field=key {{noop}}|
	
	/createentry file={{var::wi_personality}} key="Female Positive" Nurturing: Warm: Graceful: Delicate: Intuitive: Supportive: Patient: Caring: Sincere: Spirited
	/setentryfield file={{var::wi_personality}} uid={{pipe}} field=key {{noop}}|
	
	/createentry file={{var::wi_personality}} key="Female Negative" Overcritical: Moody: Indecisive: Anxious: Self-doubting: Submissive: Perfectionist: Jealous: Vindictive: Temperamental
	/setentryfield file={{var::wi_personality}} uid={{pipe}} field=key {{noop}}|
	
	/createentry file={{var::wi_personality}} key="Female Neutral" Quiet: Discreet: Composed: Thoughtful: Cautious: Grounded: Mellow: Reticent: Measured: Serene
	/setentryfield file={{var::wi_personality}} uid={{pipe}} field=key {{noop}}|
:}|
//---------|

//---------|
/ife ( 'CMC Generation Prompts' not in lorebookList) {:
	/echo Creating Lorebook 5/5 "CMC Generation Prompts"|
	/getchatbook name="CMC Generation Prompts"|
	/let key=wi_gen_prompt {{pipe}}|
	//Basic Character Information|
  
	/createentry file={{var::wi_gen_prompt}} key="Nationalities: Prompt" Generate a colon-separated list of five Nationalities.|
	/setentryfield file={{var::wi_gen_prompt}} uid={{pipe}} field=key {{noop}}|
  
	/createentry file={{var::wi_gen_prompt}} key="Nationalities: Instruction" "INSTRUCTIONS:
1. Only respond with a colon-separated list and nothing else."|
	/setentryfield file={{var::wi_gen_prompt}} uid={{pipe}} field=key {{noop}}|

	/createentry file={{var::wi_gen_prompt}} key="Ethnicities: Prompt" Generate a colon-separated list of five Ethnicities.|
	/setentryfield file={{var::wi_gen_prompt}} uid={{pipe}} field=key {{noop}}|

	/createentry file={{var::wi_gen_prompt}} key="Ethnicities: Instruction" "INSTRUCTIONS:
1. Only respond with a colon-separated list and nothing else."|
	/setentryfield file={{var::wi_gen_prompt}} uid={{pipe}} field=key {{noop}}|

	/createentry file={{var::wi_gen_prompt}} key="First Name: Prompt" Generate a colon-separated list of five {{getvar::gender}} first names.|
	/setentryfield file={{var::wi_gen_prompt}} uid={{pipe}} field=key {{noop}}|

	/createentry file={{var::wi_gen_prompt}} key="First Name: Instruction" "INSTRUCTIONS:
1. Only respond with a colon-separated list and nothing else."|
	/setentryfield file={{var::wi_gen_prompt}} uid={{pipe}} field=key {{noop}}|

	/createentry file={{var::wi_gen_prompt}} key="Last Name: Prompt" Generate a colon-separated list of five {{getvar::gender}} last names that complement the first name: {{getvar::firstName}}.|
	/setentryfield file={{var::wi_gen_prompt}} uid={{pipe}} field=key {{noop}}|

	/createentry file={{var::wi_gen_prompt}} key="Last Name: Instruction" "INSTRUCTIONS:
1. Only respond with a colon-separated list and nothing else."|
	/setentryfield file={{var::wi_gen_prompt}} uid={{pipe}} field=key {{noop}}|

	/createentry file={{var::wi_gen_prompt}} key="Nickname: Prompt" Generate a colon-separated list of five {{getvar::gender}} nicknames that complement the name: {{getvar::firstName}} {{getvar::lname}}.|
	/setentryfield file={{var::wi_gen_prompt}} uid={{pipe}} field=key {{noop}}|

	/createentry file={{var::wi_gen_prompt}} key="Nickname: Instruction" "INSTRUCTIONS:
1. The generated nicknames should be a mix of something parents or close friends use.
2. Only respond with a colon-separated list and nothing else."|
	/setentryfield file={{var::wi_gen_prompt}} uid={{pipe}} field=key {{noop}}|

	/createentry file={{var::wi_gen_prompt}} key="Genre: Prompt" Generate a colon-separated list of ten genres.|
	/setentryfield file={{var::wi_gen_prompt}} uid={{pipe}} field=key {{noop}}|

	/createentry file={{var::wi_gen_prompt}} key="Genre: Instruction" "INSTRUCTIONS:
1. The generated genres should be a mix of Anime, Film, Fantasy or Sci-Fi genres.
2. Only respond with a colon-separated list and nothing else."|
	/setentryfield file={{var::wi_gen_prompt}} uid={{pipe}} field=key {{noop}}|

	/createentry file={{var::wi_gen_prompt}} key="Time Period: Prompt" Generate a colon-separated list of five time periods and five fictional time periods.|
	/setentryfield file={{var::wi_gen_prompt}} uid={{pipe}} field=key {{noop}}|

	/createentry file={{var::wi_gen_prompt}} key="Time Period: Instruction" "INSTRUCTIONS:
1. There should be only one combined list.
2. Only respond with a colon-separated list and nothing else."|
	/setentryfield file={{var::wi_gen_prompt}} uid={{pipe}} field=key {{noop}}|

	/createentry file={{var::wi_gen_prompt}} key="World Type: Prompt" Generate a colon-separated list of five world types that could replace X in this sentence.
The story takes place in a X setting.|
	/setentryfield file={{var::wi_gen_prompt}} uid={{pipe}} field=key {{noop}}|
	
	/createentry file={{var::wi_gen_prompt}} key="World Type: Instruction" "INSTRUCTIONS:
1. Each world type should be the full sentence.
2. Only respond with a colon-separated list and nothing else."|
	/setentryfield file={{var::wi_gen_prompt}} uid={{pipe}} field=key {{noop}}|

	/createentry file={{var::wi_gen_prompt}} key="Species: Prompt" Generate a colon-separated list of five {{getvar::normal_form}} {{getvar::type}} species.|
	/setentryfield file={{var::wi_gen_prompt}} uid={{pipe}} field=key {{noop}}|
	
	/createentry file={{var::wi_gen_prompt}} key="Species: Instruction" "INSTRUCTIONS:
1. Only respond with a colon-separated list and nothing else."|
	/setentryfield file={{var::wi_gen_prompt}} uid={{pipe}} field=key {{noop}}|

	/createentry file={{var::wi_gen_prompt}} key="Species Description: Prompt" Generate a general description of the species: {{getvar::normal_form}} {{getvar::type}} {{getvar::species}}.|
	/setentryfield file={{var::wi_gen_prompt}} uid={{pipe}} field=key {{noop}}|

	/createentry file={{var::wi_gen_prompt}} key="Species: Instruction" "INSTRUCTIONS:
2. Only respond with the general description and nothing else."|
	/setentryfield file={{var::wi_gen_prompt}} uid={{pipe}} field=key {{noop}}|

	/createentry file={{var::wi_gen_prompt}} key="Student: Prompt" Given that the person is {{getvar::age}}, return the most appropriate school level label.|
	/setentryfield file={{var::wi_gen_prompt}} uid={{pipe}} field=key {{noop}}|

	/createentry file={{var::wi_gen_prompt}} key="Student: Instruction" "INSTRUCTIONS:
1. Acceptable replies are: Preschooler, xth Grader (e.g., 1st Grader, 2nd Grader, etc.), Middle Schooler, High School Student, College Student, or University Student.
2. Use correct ordinal formatting (e.g., 1st, 2nd, 3rd, 4th, etc.) in 'xth Grader'.
3. Only respond with the school level label and nothing else."|
	/setentryfield file={{var::wi_gen_prompt}} uid={{pipe}} field=key {{noop}}|


	/createentry file={{var::wi_gen_prompt}} key="Study Occupation: Prompt" Given that the person is a {{getvar::student}}, Generate a list of ten colon-separated Occupations the persion could study as.|
	/setentryfield file={{var::wi_gen_prompt}} uid={{pipe}} field=key {{noop}}|
	
	/createentry file={{var::wi_gen_prompt}} key="Study Occupation: Instruction" "INSTRUCTIONS:
1. Only respond with the colon-separated list and nothing else."|
	/setentryfield file={{var::wi_gen_prompt}} uid={{pipe}} field=key {{noop}}|

	/createentry file={{var::wi_gen_prompt}} key="World Details: Examples" EXAMPLES (for your reference—do not include in the answer):
The fantasy world of Root, inhabited by monsters and other fictional races.|
	/setentryfield file={{var::wi_gen_prompt}} uid={{pipe}} field=key {{noop}}|
	
	/createentry file={{var::wi_gen_prompt}} key="World Details: Prompt" Generate a |
	/setentryfield file={{var::wi_gen_prompt}} uid={{pipe}} field=key {{noop}}|
	
	/createentry file={{var::wi_gen_prompt}} key="World Details: Instruction" "INSTRUCTIONS:
1. Only respond with the world description and nothing else."|
	/setentryfield file={{var::wi_gen_prompt}} uid={{pipe}} field=key {{noop}}|

	/createentry file={{var::wi_gen_prompt}} key="Lore: Examples" EXAMPLES (for your reference—do not include in the answer):
Root is a medieval Scandinavian fantasy world with magic, monsters, heroes, and a bunch of MMORPG cliches. Aedelgard is one of the kingdoms in Root. Outskirts of the cities boil with monsters of various danger levels. This world works under [...]|
	/setentryfield file={{var::wi_gen_prompt}} uid={{pipe}} field=key {{noop}}|
	
	/createentry file={{var::wi_gen_prompt}} key="Lore: Prompt"  .|
	/setentryfield file={{var::wi_gen_prompt}} uid={{pipe}} field=key {{noop}}|
	
	/createentry file={{var::wi_gen_prompt}} key="Lore: Instruction" "INSTRUCTIONS:
1. Only respond with the colon-separated list and nothing else."|
	/setentryfield file={{var::wi_gen_prompt}} uid={{pipe}} field=key {{noop}}|

	/createentry file={{var::wi_gen_prompt}} key="Lore: Examples" EXAMPLES (for your reference—do not include in the answer):
In one of his adventures, {{user}} was severely wounded and lost his party. However, a passing healer (Ottis) saved him and brought him to a nearby Maretta's [...]|
	/setentryfield file={{var::wi_gen_prompt}} uid={{pipe}} field=key {{noop}}|
	
	/createentry file={{var::wi_gen_prompt}} key="Lore: Prompt"  .|
	/setentryfield file={{var::wi_gen_prompt}} uid={{pipe}} field=key {{noop}}|
	
	/createentry file={{var::wi_gen_prompt}} key="Lore: Instruction" "INSTRUCTIONS:
1. Only respond with the colon-separated list and nothing else."|
	/setentryfield file={{var::wi_gen_prompt}} uid={{pipe}} field=key {{noop}}|
	
	
	//--Basic Character Information--|
/*
	/createentry file={{var::wi_gen_prompt}} key="Character: Context" "CONTEXT (for your reference—do not include in the answer):
- Name: {{getvar::firstName}} {{getvar::lastName}}
- Age: {{getvar::parcedAge}}
- Gender: {{getvar::gender}}
- Species: {{getvar::parsedSpecies}}"|
*|
	/createentry file={{var::wi_gen_prompt}} key="Character: Context" "CONTEXT (for your reference—do not include in the answer):
- Name: {{getvar::firstName}} {{getvar::lastName}}
- Age: {{getvar::parcedAge}}
- Gender: {{getvar::gender}}
- Species: {{getvar::parsedSpecies}}"|
	/setentryfield file={{var::wi_gen_prompt}} uid={{pipe}} field=key {{noop}}|

	//Personality Information|
	/createentry file={{var::wi_gen_prompt}} key="Human Traits: Task" Generate a colon-separated list of five Human specific traits that are not normal for a {{getvar::species}} to have.|
	/setentryfield file={{var::wi_gen_prompt}} uid={{pipe}} field=key {{noop}}|
	/createentry file={{var::wi_gen_prompt}} key="Human Traits: Instruction" "INSTRUCTIONS:
1. {{getvar::firstName}} is a {{getvar::age}} {{getvar::gender}} {{getvar::parsedSpecies}}.
2. Only respond with a colon-separated list and nothing else."|
	/setentryfield file={{var::wi_gen_prompt}} uid={{pipe}} field=key {{noop}}|

	/createentry file={{var::wi_gen_prompt}} key="{{getvar::species}} Traits: Task" Generate a colon-separated list of five {{getvar::species}} specific traits.|
	/setentryfield file={{var::wi_gen_prompt}} uid={{pipe}} field=key {{noop}}|
	/createentry file={{var::wi_gen_prompt}} key="{{getvar::species}} Traits: Instruction" "INSTRUCTIONS:
1. {{getvar::firstName}} is a {{getvar::age}} {{getvar::gender}} {{getvar::parsedSpecies}}.
2. Only respond with a colon-separated list and nothing else."|
	/setentryfield file={{var::wi_gen_prompt}} uid={{pipe}} field=key {{noop}}|

	/createentry file={{var::wi_gen_prompt}} key="Quirk: Task" Generate a colon-separated list of five quirks.|
	/setentryfield file={{var::wi_gen_prompt}} uid={{pipe}} field=key {{noop}}|
	/createentry file={{var::wi_gen_prompt}} key="Quirk: Instruction" "INSTRUCTIONS:
1. The quirks should be something {{getvar::firstName}} does that other think is odd.
2. Each quirk should be a short sentence.
3. {{getvar::firstName}} is a {{getvar::age}} {{getvar::gender}} {{getvar::parsedSpecies}}.
4. Only respond with a colon-separated list and nothing else."|
	/setentryfield file={{var::wi_gen_prompt}} uid={{pipe}} field=key {{noop}}|

	/createentry file={{var::wi_gen_prompt}} key="God Habit: Task" Generate a colon-separated list of five Good Habits.|
	/setentryfield file={{var::wi_gen_prompt}} uid={{pipe}} field=key {{noop}}|
	/createentry file={{var::wi_gen_prompt}} key="God Habit: Instruction" "INSTRUCTIONS:
1. The habits should be habits that is good to have.
2. Each habit should be a short sentence.
3. {{getvar::firstName}} is a {{getvar::age}} {{getvar::gender}} {{getvar::parsedSpecies}}.
4. Only respond with a colon-separated list and nothing else."|
	/setentryfield file={{var::wi_gen_prompt}} uid={{pipe}} field=key {{noop}}|

	/createentry file={{var::wi_gen_prompt}} key="Bad Habit: Task" Generate a colon-separated list of five Bad Habits.|
	/setentryfield file={{var::wi_gen_prompt}} uid={{pipe}} field=key {{noop}}|
	/createentry file={{var::wi_gen_prompt}} key="Bad Habit: Instruction" "INSTRUCTIONS:
1. The habits should be habits that is bad to have.
2. Each habit should be a short sentence.
3. {{getvar::firstName}} is a {{getvar::age}} {{getvar::gender}} {{getvar::parsedSpecies}}.
4. Only respond with a colon-separated list and nothing else."|
	/setentryfield file={{var::wi_gen_prompt}} uid={{pipe}} field=key {{noop}}|

	/createentry file={{var::wi_gen_prompt}} key="Main Personality Description: Task" "TASK:
Generate one sentence describing how the main personality trait {{getvar::item}} manifests in {{getvar::firstName}}’s behavior."|
	/setentryfield file={{var::wi_gen_prompt}} uid={{pipe}} field=key {{noop}}|
	/createentry file={{var::wi_gen_prompt}} key="Main Personality Description: Instruction" "INSTRUCTIONS:
1. Do NOT mention age, gender, species, or any other biographical detail.
2. Keep it to exactly one concise sentence illustrating the trait in action.
3. Focus solely on how {{getvar::item}} shows up in their choices, actions or demeanor.
4. Return ONLY that single sentence."|
	/setentryfield file={{var::wi_gen_prompt}} uid={{pipe}} field=key {{noop}}|
	//--Personality Information--|
:}|
//---------|
