Update this prompt
```
### **EXAMPLES (do not copy names or exact phrases – these are only structural references):**

#### **Example – Realistic:**
Flexibility, Deep-Throating, High Focus Under Pressure, Marksman, Endurance, Insertions

#### **Example – Fantasy:**
Flame Affinity, Void Magic, Blood of the Fae, Dream Echo, Dragon’s Tongue

#### **Example – Science Fiction:**
Neural Threading, Mild Telekinetic Pulse, Pulse Weapon Familiarity, Bio-Adaptive Reflexes, Zero-G Acrobat

## **TASK:**
Generate a single short, title-style **Ability Name** that reflects {{getvar::firstName}}’s physical, mental, magical, or trained talents. The name must match the logic of their setting type, species, personality, and backstory.  
{{getvar::guidance}}

### **INSTRUCTIONS:**
- Output **only one ability name** — no list, commas, or formatting.
- The ability name must be **2–5 words long** and title-style (e.g., capitalized appropriately).
- Do **not** include descriptions, parenthetical notes (e.g., “(Advanced)”), or level indicators.
- The ability must suit {{getvar::firstName}}’s species, personality, setting, and backstory.
- The ability must reflect one or more categories: physical, mental, magical (if allowed), or trained skill.
- Do **not** generate items or tools — this is an **internal trait or ability**, not a weapon or object.
- Avoid vague labels or euphemisms (e.g., “Special Skill”, “Adventurous Mouth”). Instead, name **actionable, character-usable traits** (e.g., “Oral Stamina”, “Pain Resistance”).
- Do **not** include or repeat anything from this list: `{{getvar::excludedList}}`
- Return only the ability name — no commentary, explanation, or punctuation.
{{getvar::logicBasedInstruction}}
```

here is the logic and rules for logicBasedInstruction (You dont need to update the logic only the Rules if needed)
```
/setvar key=logicBasedInstruction {{noop}}|
	
/ife (settingType == 'Realistic') {:
	
	/ife ( logicBasedInstruction != '') {:
		/addvar key=logicBasedInstruction {{newline}}|
	:}|
	/addvar key=logicBasedInstruction "- Abilities must be fully plausible in the real world. This includes advanced flexibility, sensory focus, pain tolerance, emotional control, or exceptional training. Do not include magic, psionics, supernatural phenomena, or any kind of proficiency level."|
	
:}|
/elseif (settingType == 'Fantasy') {:
	
	/ife ( logicBasedInstruction != '') {:
		/addvar key=logicBasedInstruction {{newline}}|
	:}|
	/addvar key=logicBasedInstruction "- Abilities may include elemental powers, curses, divine traits, inherited magic, or arcane disciplines. Do not include tiers, mastery labels, or strength modifiers—those are handled in a later step."|
	
:}|
/elseif (settingType == 'Science Fiction') {:
	
	/ife ( logicBasedInstruction != '') {:
		/addvar key=logicBasedInstruction {{newline}}|
	:}|
	/addvar key=logicBasedInstruction "- Abilities may include psionics, gene traits, mental enhancements, or biotech-integrated skills. Do not include levels, size indicators, or parenthetical ranks—those will be generated separately."|
	
:}|
```