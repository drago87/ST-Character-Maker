### 1. **Core Identity**

Establishes the biological, cultural, and temporal framework of the character.

1. **Species**
    
2. **Nationality**
    
3. **Ethnicity**
    
4. **Gender**
    
5. **Age**
    
6. **Name** (`--FirstName--`, `--LastName--`, `--Alias--`)

### 2. World & Setting Information

7. **TimePeriod**
    
8. **Season**
    
9. **World Type** (`--WorldType--`)
    
10. **World Details** (`--WorldDetails--`)
    
11. **Residence**
    
12. **Lore**
    
13. **Backstory**
    
14. **Scenario Overview**
    

---

### 🧍 3. **Appearance & Anatomy**

Builds physical traits dependent on species, age, and gender.

15. **Height**
    
16. **Face**, **Hair**, **Eyes**
    
17. **Body**
    
18. **Features**
    
19. **Nipples**, **Breasts**, **Privates**, **Anus** _(if applicable)_
    
20. **Appearance Traits**
    
21. **Outfit Parts** (`--OutfitHead--` → `--OutfitUnderwear--`)
    

---

### 🧠 4. **Mental Traits & Personality**

Informed by age, species, backstory, and alignment.

22. **Archetype** (`Modifier + Archetype + Addition`)
    
23. **Archetype Details**
    
24. **Reasoning** (psychological background for behavior)
    
25. **Alignment**
    
26. **Alignment Details**
    
27. **Ideals**
    
28. **Personality Tags**
    
29. **Intelligence Level**
    
30. **Cognitive Abilities**
    
31. **Social Behavior**
    
32. **Social Skills and Integration**
    

---

### 🌟 5. **Aspirational & Unique Traits**

Defines goals, internal rules, and magical/abnormal states.

33. **Main Aspiration**
    
34. **Aspiration Details**
    
35. **Aspiration Goals**
    
36. **Unique Trait(s)**
    
37. **Unique Trait Effect(s)**
    

---

### 💬 6. **Speech Patterns**

Based on age, intelligence, archetype, and social level.

38. **Speech Style**
    
39. **Speech Quirks**
    
40. **Speech Tics**
    
41. **Speech Examples**
    

---

### 🧩 7. **External Interaction**

How the character fits into the world and with others.

42. **Connections**
    
43. **Abilities**
    
44. **Items / Equipment**
    
45. **Secrets**
    
46. **Reputation** _(optional expansion from alignment/social behavior)_
    

---

### 🔥 8. **Sexual Information** _(if applicable)_

Informed by age, gender, maturity, and world tone.

47. **Sexual Orientation**
    
48. **Sexual Role**
    
49. **Kinks**
    
50. **Sexual Notes**
    

---

### 🧠 9. **Optional Extras**

Narrative scaffolding and additional logic or design hooks.

51. **Behavior Notes**
    
52. **Appearance QA List**
    
53. **Personality QA**
    
54. **Sexuality QA**
    
55. **Story Plan**
    
56. **Previously...**
    
57. **Notes**
    
58. **Synonyms**
    
59. **Extra Characters**
    
60. **--User1--** (handled last for external interactions)



## 🌍 World & Setting Information

| Trait                                  | Recommended Dependencies                                                                                                                                                      |
| -------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **TimePeriod**                         | Base Information, **Species** _(determines available technology, culture, and naming conventions)_                                                                            |
| **Season**                             | Base Information _(affects current climate, outfit choices, emotional tone)_                                                                                                  |
| **World Type** (`--WorldType--`)       | **TimePeriod**, **Species** _(defines fantasy, sci-fi, or realistic logic)_                                                                                                   |
| **World Details** (`--WorldDetails--`) | **World Type**, **TimePeriod**, **Nationality**, **Species** _(adds magic, history, conflicts, geography)_                                                                    |
| **Residence**                          | **World Details**, **Species**, **Nationality**, **Ethnicity** _(determines environment and local norms)_                                                                     |
| **Lore**                               | **World Type**, **World Details**, **TimePeriod**, **Species**, optionally **Residence**                                                                                      |
| **Backstory**                          | **Base Information**, **Species**, **TimePeriod**, **World Details**, **Residence**, **Age**, **Gender** _(provides emotional + narrative foundation for behavior and goals)_ |
| **Scenario Overview**                  | **Backstory**, **World Details**, **Residence**, **TimePeriod**                                                                                                               |

---
## 📏 Appearance Section

| Trait                                            | Recommended Dependencies                                                              |
| ------------------------------------------------ | ------------------------------------------------------------------------------------- |
| **Height**                                       | Base Information _(Age, Gender, Species define scale and stature)_                    |
| **Body**                                         | Base Information, **Height** _(build, proportion)_                                    |
| **Face**                                         | Base Information, **Species**                                                         |
| **Hair**                                         | Base Information, **Ethnicity**, **Age** _(texture, color trends)_                    |
| **Eyes**                                         | Base Information, **Species**, **Ethnicity** _(eye shape, rare traits)_               |
| **Features**                                     | Base Information, **Height**, **Body**, **Face** _(scars, tails, fangs, etc.)_        |
| **Appearance Traits**                            | Base Information, **Features**, **Body** _(quirky traits, stylized detail)_           |
| **Nipples**, **Breasts**, **Privates**, **Anus** | Base Information, **Gender**, **Body**, **Life Stage** _(anatomical maturity + type)_ |

---

## 🧍 Clothing (Outfit Parts)

|Trait|Recommended Dependencies|
|---|---|
|**OutfitHead → Underwear**|Base Information, **Gender**, **Species**, **Body**, **Features** _(cultural + anatomical compatibility)_|

---

## 🧠 Personality & Behavior

|Trait|Recommended Dependencies|
|---|---|
|**Archetype**|Base Information, **Life Stage**, **Species**|
|**Archetype Details**|Base Information, **Archetype**, **Age**|
|**Reasoning**|**Archetype**, **Backstory**, **Age**|
|**Alignment**|Base Information, **Archetype**|
|**Alignment Details**|**Alignment**, **Archetype**, **Behavior Traits**|
|**Ideals**|**Alignment**, **Life Stage**, **Archetype**|
|**Personality Tags**|**Archetype**, **Age**, **Gender**, **Species**|
|**Intelligence Level**|Base Information _(Age, Life Stage)_|
|**Cognitive Abilities**|**Intelligence Level**, **Age**, **Species**|
|**Social Behavior**|**Archetype**, **Gender**, **Age**, **Species**|
|**Social Skills**|**Social Behavior**, **Cognitive Abilities**|

---

## 🌟 Aspiration & Traits

|Trait|Recommended Dependencies|
|---|---|
|**Main Aspiration**|**Archetype**, **Age**, **Species**|
|**Aspiration Details**|**Aspiration**, **Archetype**, **Reasoning**|
|**Aspiration Goals**|**Aspiration**, **Aspiration Details**, **Personality Tags**|
|**Unique Trait**|**Species**, **Archetype**, **Age**, **Gender**|
|**Unique Trait Effects**|**Unique Trait**, **Cognitive Abilities**, **Social Behavior**|

---

## 💬 Speech

|Trait|Recommended Dependencies|
|---|---|
|**Speech Style**|**Age**, **Cognitive Abilities**, **Species**|
|**Speech Quirks**|**Archetype**, **Personality Tags**, **Speech Style**|
|**Speech Tics**|**Age**, **Speech Style**, **Speech Quirks**|
|**Speech Examples**|All the above|

---

## 🌍 Integration & World Logic

|Trait|Recommended Dependencies|
|---|---|
|**Backstory**|Base Information, **Species**, **World Details**|
|**World Details**|**Nationality**, **Time Period**, **Species**|
|**Residence**|**World Details**, **Species**|
|**Connections**|**Backstory**, **Social Behavior**|
|**Abilities**|**Species**, **Backstory**, **Age**|
|**Items / Equipment**|**Abilities**, **Species**, **Archetype**|
|**Secrets**|**Backstory**, **Archetype**, **Age**|
|**Reputation**|**Social Behavior**, **Alignment**, **Connections**|

---

## 🔥 Sexuality (if used)

|Trait|Recommended Dependencies|
|---|---|
|**Sexual Orientation**|**Gender**, **Species**, **Age**|
|**Sexual Role**|**Orientation**, **Personality Tags**, **Social Behavior**|
|**Kinks**|**Age**, **Orientation**, **Archetype**, **Species**|
|**Sexual Notes**|**Kinks**, **Social Skills**, **Unique Traits**|

---

## 🧠 Extras (for post-gen polish)

|Trait|Recommended Dependencies|
|---|---|
|**Behavior Notes**|**Archetype**, **Cognitive Abilities**, **Social Behavior**|
|**Appearance QA List**|**Features**, **Outfit**, **Body**|
|**Personality QA**|**Personality Tags**, **Archetype**, **Age**|
|**Sexuality QA**|**Sexual Notes**, **Orientation**|
|**Story Plan**|**Backstory**, **Aspiration**, **Connections**|
|**Previously**|**Story Plan**, **Reputation**|
|**Synonyms**|**Name**, **Archetype**|
