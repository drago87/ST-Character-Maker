/let x ["Test1": "Test2"]|
/let y ["Test3": "Test4": "Test5": "Test2"]|
/let t {{var::x}}|
/foreach {{var::y}} {:
	/ife ( item not in t) {:
		/len {{var::t}}|
		/var key=t index={{pipe}} {{var::item}}|
	:}|
:}|
/var y {{var::t}}|
/setvar key=a {{var::y}}|

**Level: Very Dumb**

Struggles to understand complex instructions and often forgets basic tasks: but remains cheerful and eager to help.

**Species: Dog**

**Example: Infant**  
0.0–0.04 years _(0–2 weeks)_

**Example: Toddler**  
0.04–0.08 years _(2–4 weeks)_

**Example: Preschooler**  
0.08–0.17 years _(1–2 months)_

**Example: Grade Schooler**  
0.17–0.42 years _(2–5 months)_

**Example: Preteen**  
0.5–0.75 years _(6–9 months)_

**Example: Teen**  
0.83–1.5 years _(10–18 months)_

**Example: Young Adult**  
1.5–3.0 years

**Example: Adult**  
4–6 years

**Example: Middle Aged**  
7–9 years

**Example: Senior**  
10–12 years

**Example: Elderly**  
13+ years

---

### 🐉 **Species: Dragon (long-lived fantasy type)**

**Example: Infant**  
0–10 years

**Example: Toddler**  
10–25 years

**Example: Preschooler**  
25–50 years

**Example: Grade Schooler**  
50–100 years

**Example: Preteen**  
100–200 years

**Example: Teen**  
200–400 years

**Example: Young Adult**  
400–800 years

**Example: Adult**  
800–1200 years

**Example: Middle Aged**  
1200–1800 years

**Example: Senior**  
1800–2500 years

**Example: Elderly**  
2500+ years