This is the generation order for the character
Generation can only use information from things above it


  Character Setup below here (Done)
  
1. **Gender** Male or Female, Part of Base Context
2. **Futanari** Yes or No
3. **Character Archetype** Human, Anthropomorphic, Demi-Human, Tauric, Beastkin, Animalistic, Pokémon, Digimon, Android, Part of Base Context
4. **Character Type** Pokémon, Digimon, Animalistic
5. **Animal Base** Humanoid (For Human), Synthetic (For Android), Mammal, Reptile, Bird, Fish, Amphibian, Invertebrate, Fantasy
6. **Species Group** See list at the end
7. **Privates Female** Same as Species Group
8. **Privates Male** Same as Species Group
9. **Real** Yes or No See end for information, Part of Base Context
   
   Basic about the Character below here

10. **Time Period** See end, No Base Context, No ExtraInput, No Type Context
11. **Setting Type** Realistic, Fantasy or Science Fiction
12. **Species** No Base Context, No ExtraInput, No Type Context, Part of Base Context
13. **Nationality**  Base Context, No ExtraInput, No Type Context, (Only for Human, Android), Part of Base Context
14. **Ethnicity** Base Context, No ExtraInput, No Type Context, (Only for Human, Android), Part of Base Context
15. **Life Stage** See the end, No Base Context, No ExtraInput, No Type Context, Part of Base Context
16. **Age** Base Context, No ExtraInput, Life Stage Context (Instead of Type Context, See the end), Part of Base Context
17. **Human Equivalent Age** If not Human (Characters mental age in comparison to a Human), Part of Base Context
18. **First Name** Base Context, No ExtraInput, No Type Context, Part of Base Context
19. **Last Name** Base Context, No ExtraInput, No Type Context, Part of Base Context
20. **Alias** Base Context, No ExtraInput, No Type Context
    
    Would Info Below this (Done)

21. **Season** Spring, Summer, Autumn, Winter or None (If None will not be included in Base Context or ExtraInput)
22. **World Type** No Base Context, No ExtraInput, No Type Context
23. **World Details** No Base Context, No ExtraInput, No Type Context
24. **User Role**  Base Context, ExtraInput (if user is a Narrator: --User-- is a Narrator), No Type Context
    Sets the guidance for User Role depending on what the user want to have for gender
25. **Residence** Base Context, ExtraInput (- Time Period  {{getvar::timePeriod}} — Season: {{getvar::seasons}} ( — Season: {{getvar::seasons}} removed if Season == None), - World Type: {{getvar::worldType}}, - World Details: {{getvar::worldDetails}}, - --User--'s Role: {{getvar::userRole}}(Only if user is not a Narrator)), No Type Context
26. **Occupation** Base Context, ExtraInput (- Time Period: {{getvar::timePeriod}} —  World Type: {{getvar::worldType}}, - World Details: {{getvar::worldDetails}}, - Residence: {{getvar::residence}}), No Type Context
27. **Occupation Duties** Base Context, ExtraInput (- Time Period: {{getvar::timePeriod}} —  World Type: {{getvar::worldType}}, - World Details: {{getvar::worldDetails}}, - Residence: {{getvar::residence}})
28. **Occupation Skills** Base Context, ExtraInput (- Occupation: {{getvar::occupationBase}}, - Duties: {{getvar::occupationDuties}}, - Time Period: {{getvar::timePeriod}} —  World Type: {{getvar::worldType}}, - World Details: {{getvar::worldDetails}}), No Type Context
29. **Lore** Base Context, ExtraInput (- Time/Period: {{getvar::timePeriod}} ,{{getvar::seasons}} ( ,{{getvar::seasons}} only if seasons != None), - World Type: {{getvar::worldType}}, - World Details: {{getvar::worldDetails}}), No Type Context
30. **Backstory** Base Context, ExtraInput (- Time Period: {{getvar::timePeriod}} — Season: {{getvar::seasons}} ( — Season: {{getvar::seasons}} only if seasons != None), - World Type: {{getvar::worldType}}, - World Details: {{getvar::worldDetails}}, - --User--'s Role: {{getvar::userRole}} (Only if user is not Narrator)), No Type Context
31. **Scenario Overview** Base Context, ExtraInput (- Time Period: {{getvar::timePeriod}} — Season: {{getvar::seasons}} ( — Season: {{getvar::seasons}} only if seasons != None), - World Type: {{getvar::worldType}}, ,- World Details: {{getvar::worldDetails}}, - Residence: {{getvar::residence}}, - Backstory: {{getvar::backstory}}, - --User--'s Role: {{getvar::userRole}} (Only if user is not Narrator)), No Type Context
    
    Appearance Below this (Mostly done. I only need to run it and see so that it works and don't give weird outputs)

32. **Unit Type** Metric or Imperial
33. **Length** Only if characterArchetype == Animalistic or Pokémon or Digimon or Tauric, Base Context, ExtraInput (- Unit Type: {{getvar::unitType}}), Type Context
34. **Height** only when appropriate, Base Context, ExtraInput (- Unit Type: {{getvar::unitType}}), Type Context
35. **Face** Base Context, No ExtraInput, Type Context
36. **Hair** Base Context, No ExtraInput, Type Context
37. **Eyes** Base Context, No ExtraInput, Type Context
38. **Features** Base Context, No ExtraInput, Type Context
39. **Body** Base Context, ExtraInput (- Features: {{getvar::appearanceFeatures}}), Type Context
40. **Breasts** If Female, Base Context, ExtraInput (- Body: {{getvar::appearanceBody}}, - Features: {{getvar::appearanceFeatures}}), Type Context
41. **Nipples** If Female, Base Context, ExtraInput (- Breasts: {{getvar::appearanceBreasts}}, - Body: {{getvar::appearanceBody}}, - Features: {{getvar::appearanceFeatures}}), Type Context
42. **Pussy** If Female or Futanari, Base Context, ExtraInput (- Body: {{getvar::appearanceBody}}, - Features: {{getvar::appearanceFeatures}}, - Pussy Appearance: {{getvar::appearancePussy}} (Only if Futanari), - Male Genital Type:: {{getvar::privatesMale}}, - Species Group: {{getvar::speciesGroup}}, Important: {{getvar::firstName}} is a futanari, so she has both a pussy and a cock. (Only if Futanari)), Type Context
43. **Cock** If Male or Futanari, Base Context, ExtraInput (- Body: {{getvar::appearanceBody}}, - Features: {{getvar::appearanceFeatures}}, - Female  Genital Type: {{getvar::privatesFemale}}, - Species Group: {{getvar::speciesGroup}}, Important: {{getvar::firstName}} is a futanari, so she has both a pussy and a cock. (Only if Futanari)), Type Context
44. **Genitals Sync** If Futanari, Base Context, ExtraInput (- Body: {{getvar::appearanceBody}}, - Features: {{getvar::appearanceFeatures}}, - Pussy Appearance: {{getvar::appearancePussy}}, - Female Genital Type:: {{getvar::privatesFemale}}, - Cock Appearance: {{getvar::appearanceCock}}, - Male Genital Type:: {{getvar::privatesMale}}, - Species Group: {{getvar::speciesGroup}}),Type Context
45. **Anus**  Base Context, ExtraInput (- Body: {{getvar::appearanceBody}}, - Features: {{getvar::appearanceFeatures}}, - Species Group: {{getvar::speciesGroup}}), Type Context
46. **Appearance Traits**  Base Context, No ExtraInput, No Type Context
47. **Appearance Traits Details** Base Context, No ExtraInput, Type Context
48. **Appearance Traits Effect** Base Context, No ExtraInput, Type Context
    
    Outfit Below this (Done)

49. **Outfit Head** 
50. **Outfit Accessories** 
51. **Outfit Makeup** 
52. **Outfit Neck** 
53. **Outfit Top** 
54. **Outfit Bottom** 
55. **Outfit Legs** 
56. **Outfit Shoes** 
57. **Outfit Underwear (Top)** 
58. **Outfit Underwear (Top)** 
    
    Personality Below this Done)

59. **Archetype** 
60. **Archetype Details** 
61. **Reasoning** 
62. **Alignment** 
63. **Alignment Details** 
64. **Ideals** 
65. **Personality Tags** 
66. **Intelligence Level** 
67. **Cognitive Abilities** 
68. **Social Behavior** 
69. **Social Skills and Integration** 
    
    Aspiration and Personality Traits (Done)

70. **Main Aspiration** 
71. **Aspiration Details**  
72. **Aspiration Goals**  
73. **Unique Trait(s)**  
74. **Unique Trait Effect(s)**  
    
    Speech (Done)

75. **Speech Style** 
76. **Speech Quirks** 
77. **Speech Tics** 
    
    An extra category for stuff not fitting above (Done)

78. **Connections** 
79. **Abilities** 
80. **Items / Equipment** 
81. **Secrets** 
    
    NSFW Stuff (Done)

82. **Sexual Orientation** 
83. **Sexual Role** 
84. **Libido**
85. **Abilities** 
86. **Items / Equipment** 
87. **Kinks** 
88. **Sexual Notes** 
    
    Ending Stuff (Done)

89. **Behavior Notes** (Done)
90. **Speech Examples** (Done)
91. **Appearance Q&A** (Dona)
92. **Personality Q&A**  (Done)
93. **Sexuality Q&A** (Done)
94. **Story Plan** 
95. **Previously...** 
96. **Notes** (Done)
97. **Synonyms** 
98. **Extra Characters** 


Species Group can be one of these depending on what the user picked for Animal Base  
None (Automatically set for Human, Demi-Human and Android. Cannot be select for anyone else)  
Bovine  
Canine  
Cervine  
Cetacean  
Chiropteran  
Chiropteran  
Equine  
Feline  
Leporidae  
Marsupial  
Murine  
Mustelid  
Primate  
Proboscidean  
Ursine  
Chelonian  
Crocodilian  
Lacertilian  
Reptilian  
Serpentine  
Anserine  
Aviary  
Passerine  
Raptor  
Ratite  
Chondrichthyan  
Osteichthyan  
Piscean  
Poeciliid  
Anuran  
Caudate  
Annelid  
Arachnid  
Arthropod  
Cephalopod  
Gastropod  
Insectoid  
Lepidopteran  
Alien  
Chimeric  
Demonic  
Draconic

or Species Group can be these if the user wants to use a more broad generation  
Mammal  
Reptile  
Bird  
Fish  
Amphibian  
Invertebrate  
Fantasy

Privates Female will be set freely from the Animal Base and Species Group (Except None)

Privates Male will be set freely from the Animal Base and Species Group (Except None)

Demi-Human characters Privates Female and Privates Male will be set to the generated Species (After having generated the Species) unless already set

Real
If No will have no impact on the generation
If Yes will add
{{getvar::name}} is a character from the {{getvar::media_type}} _{{getvar::media_name}}_. Use your knowledge about {{getvar::name}} and the {{getvar::media_type}} _{{getvar::media_name}}_ when doing the assigned **TASK**

to the end of Base Context

name is the characters full name (First and Last)
media_type is the type of media (Anime, Manga, TV-Show, Movie etc..)
media_name is the name of the show (Naruto, Naruto Shippuden, One Piece, The Matrix etc..)

Life Stage (If characterArchetype != Animalistic)
Infant, Toddler, Preschooler,  Grade Schooler, Preteen, Teen, Young Adult, Adult, Middle Aged, Senior, Elderly

Life Stage ( If characterArchetype == Animalistic)
Newborn, Infant, Juvenile, Adolescent, Young Adult, Adult, Mature Adult, Senior, Elderly

Life Stage Animalistic Context ( If characterArchetype == Animalistic)
Newborn (birth to a few days, sexuality: undeveloped)
Infant (still nursing, eyes possibly closed, sexuality: undeveloped)
Juvenile (starting to explore, weaned, sexuality: not yet developed)
Adolescent (learning independence, not yet sexually mature, sexuality: developing hormones, pre-reproductive)
Young Adult (just reached sexual maturity, sexuality: newly reproductive, may seek mates)
Adult (fully grown, prime of life, sexuality: active, regularly reproductive)
Mature Adult (older, possibly breeding prime, sexuality: experienced, peak fertility or declining slightly)
Senior (aging, slower, less active, sexuality: reduced fertility and mating behavior)
Elderly (frail, nearing end of life, sexuality: largely inactive, post-reproductive)

Life Stage Humanoid Context  (If characterArchetype != Animalistic)
Infant (newborn, completely dependent, sexuality: undeveloped)
Toddler (walking, basic speech, high curiosity, sexuality: undeveloped)
Preschooler (early learning, social development, sexuality: undeveloped)
Grade Schooler (basic education, growing independence, sexuality: emerging awareness)
Preteen (transitional stage before adolescence, sexuality: early self-awareness, identity exploration begins)
Teen (puberty, identity development, sexuality: developing orientation and expression)
Young Adult (legal adulthood, emerging independence, sexuality: typically active, identity stabilizing)
Adult (stable career/family building, sexuality: established identity, variable activity)
Middle Aged (peak experience, possible life reassessment, sexuality: may shift in expression or priority)
Senior (retirement age, early aging signs, sexuality: reduced activity, identity stable)
Elderly (advanced aging, increased frailty, sexuality: limited activity, identity enduring)


Time Period ( or a user input)
Prehistoric, Babylon, Ancient Egypt, Ancient Rome, Early Middle Ages, High Middle Ages, Late Middle Ages, Renaissance, Age of Discovery, Baroque period, Enlightenment, Victorian era, Edwardian era, Belle Époque, The Roaring Twenties, Interwar period, Post-WWII era, Cold War era, 1960s, 1970s, 1980s, 1990s, 2000s, Modern Day, Steampunk, Cyberpunk, Space Age, Post-Apocalyptic, Dystopian, Lovecraftian, Eldritch

