```json
{
	"instruction": "Provide creature metadata with full schema.",
	"input": "Define the creature category 'Dragons' with its major variants.",
	"output": {
		"category": "Dragons",
		"creatures": [
			{
				"name": "Dragon",
				"type": "Western Dragon",
				"description": "Large, quadrupedal dragons with two wings and limited fine use of the forelimbs. Typically scale-covered and capable of breath weapons.",
				"variants": [
					"Metallic Dragon",
					"Elemental Dragon",
					"Furred Dragon"
				],
				"biology": {
					"body_structure": "Four-legged body plan with two large wings. Heavy, muscular frame built for terrestrial locomotion and short bursts of flight.",
					"locomotion": "Primarily walks on all four limbs. Wings provide lift and gliding capability.",
					"integument": "Usually armored scales; varies by subgroup (metallic, elemental, furred).",
					"special_capabilities": "Most Western Dragons can breathe fire; elemental or metallic variants possess subtype-specific abilities.",
					"reproduction": {
						"female_genital_structure": "Females have a horizontal cloaca. The opening is closed and surrounded by softer scales. The scales are still hard enough to stimulate the male genitalia when it is inserted or removed. Inside the cloaca, a labyrinth of ridges and grooves mirror the enchanting patterns found on the exterior of the dragon's body. As the male penetrates, he's met with an array of tactile sensations, making each encounter a unique and thrilling experience.",
						"male_genital_structure": "Males have a horizontal cloaca for excretion and a vertical slit for their unique, curved genitalia. The penis is retracted into the vertical slit when not in use. The surface is a complex tapestry of raised ridges, bumps, and segmented patterns, mirroring the magnificent body of a dragon. The narrower end is punctuated by layered, organic shapes and ridges, enhancing its enchanting appearance. As the penis thickens, it reveals intricate, asymmetric surface details, including grooves, scales, and ribbed sections, creating a intense experience during sex for the female. The base, is also adorned with irregular bumps or nodules, adding to its magical allure.",
						"notes": "Reproductive traits are consistent across Western Dragon subtypes unless modified by species-specific biology."
					}
				},
				"notes": "All naming conventions for specialized forms follow the format: 'Fire Dragon', 'Water Dragon', 'Gold Dragon', etc."
			},
			{
				"name": "Metallic Dragon",
				"type": "Western Dragon",
				"description": "A group of Western Dragons whose scale composition visually and structurally resembles metals. Individual species carry names such as Gold Dragon, Silver Dragon, Platinum Dragon, etc.",
				"variants": [
					"Gold Dragon",
					"Silver Dragon",
					"Bronze Dragon",
					"Platinum Dragon",
					"Copper Dragon"
				],
				"biology": {
					"body_structure": "Standard Western Dragon morphology.",
					"locomotion": "Quadrupedal walking with powered gliding or flying.",
					"integument": "Scales exhibit metallic sheen and hardness; coloration and elemental resonance depend on subtype.",
					"special_capabilities": "Certain metallic variants possess metal-related magical affinity (e.g., gold’s heat resistance, silver’s purity effects).",
					"reproduction": {
						"genital_structure": "Follows Western Dragon norms but is usually harder and spikier.",
						"notes": "Metallic scale composition does not alter reproductive structure."
					}
				},
				"notes": "Metallic naming convention always uses the metal name first: 'Gold Dragon', 'Silver Dragon', etc."
			},
			{
				"name": "Elemental Dragon",
				"type": "Western Dragon",
				"description": "A group of Western Dragons attuned to a primordial element. Individual species are named for their attuned element, such as Fire Dragon, Water Dragon, or Earth Dragon.",
				"variants": [
					"Fire Dragon",
					"Water Dragon",
					"Earth Dragon",
					"Air Dragon",
					"Lightning Dragon",
					"Ice Dragon"
				],
				"biology": {
					"body_structure": "Standard Western Dragon morphology with elemental modifications.",
					"locomotion": "Quadrupedal movement and flight.",
					"integument": "Scales influenced by elemental affinity (e.g., fire-resistant keratin, water-slick scales, stone-like plating).",
					"special_capabilities": "Element-specific breath weapon and biological adaptations.",
					"reproduction": {
						"genital_structure": "Same as Western Dragon baseline.",
						"notes": "Elemental traits do not modify primary reproductive anatomy."
					}
				},
				"notes": "Elemental Dragons are usually named directly after their attuned element (e.g., 'Fire Dragon')."
			},
			{
				"name": "Furred Dragon",
				"type": "Furred Western Dragon",
				"description": "A smaller, more animal-like subspecies of Western Dragon covered in fur rather than scales. Retains wings and quadrupedal structure but exhibits mammalian anatomical traits.",
				"variants": [
					"Canine Dragon",
					"Feline Dragon"
				],
				"biology": {
					"body_structure": "Quadrupedal with wings; lighter frame than scaled Western Dragons.",
					"locomotion": "Capable of bounding, climbing, and agile short-distance flight.",
					"integument": "Dense fur covering the full body; fur type varies by subtype.",
					"special_capabilities": "Retains breath weapon capabilities, though typically reduced in intensity compared to scaled Western Dragons.",
					"reproduction": {
						"genital_structure": "Follows mammalian genital and anal structure.",
						"notes": "Secondary sexual characteristics vary strongly by subtype."
					}
				},
				"notes": "Furred Dragon variants take their naming scheme from their closest mammalian analogue."
			},
			{
				"name": "Dragon",
				"type": "Eastern Dragon",
				"description": "Long, serpentine dragons shaped like giant, scaled serpents with forelimbs, horns, and the ability to swim through the air without wings.",
				"variants": [],
				"biology": {
					"body_structure": "Elongated serpentine body with two articulate forelimbs and no hind legs.",
					"locomotion": "Air-swimming locomotion; highly fluid and graceful. Forelimbs are fully functional for manipulation.",
					"integument": "Fine scales; often smooth, sometimes ornate.",
					"special_capabilities": "Levitation or air-swimming; weather manipulation in many traditions.",
					"reproduction": {
						"genital_structure": "Follows ophidian (snake-based) reproductive anatomy.",
						"notes": "Internal structures extend during mating; morphology varies slightly between lineages."
					}
				},
				"notes": "Often associated with wisdom, storms, or rivers in mythology."
			}
		]
	}
}
```
```json
{
	"instruction": "Provide creature metadata with full schema.",
	"input": "Define the creature category 'Mermaids' with its major variants.",
	"output": {
		"id": "creature_mermaid",
		"name": "Mermaid",
		"category": ["Creature", "Fantasy", "Aquatic"],
		"description": "Mermaids are sapient aquatic humanoids with a human upper body and a serpentine, fish-like tail instead of legs. They are adapted for underwater life while retaining humanoid intelligence and dexterity.",

		"common_traits": {
			"intelligence_level": "Sapient",
			"social_structure": "Small pods, coastal communities, or solitary individuals",
			"habitat": ["Oceans", "Seas", "Reefs", "Deep waters"],
			"diet": "Primarily piscivorous with omnivorous flexibility",
			"lifespan": "Comparable to or slightly longer than humans",
			"size_range": "Human upper-body proportions with a long, powerful tail",
			"movement": "Swimming via tail propulsion; no terrestrial locomotion",
			"notes": "Mermaids are fully aquatic in movement and rely on their tails for all lower-body motion and physical interaction."
		},

		"variants": [
			{
				"id": "mermaid_female",
				"name": "Mermaid",
				"type": "Aquatic Humanoid",
				"description": "A female mermaid with a humanoid upper body and a scaled, serpentine tail, combining human external anatomy with internal mammalian reproductive biology.",
				
				"physical_structure": {
					"body_plan": "Humanoid upper body with a single continuous tail",
					"limbs": {
						"forelimbs": "Two humanoid arms with full manual dexterity",
						"hind_limbs": "Absent; replaced entirely by a tail",
						"wings": "None",
						"tail": "Long, muscular, scaled tail used for propulsion and physical interaction"
					},
					"skin_covering": "Fine overlapping fish scales covering the tail; humanoid skin texture on the upper body",
					"head_features": ["Humanoid facial structure", "Aquatic-adapted ears"],
					"notes": "No legs, knees, feet, or thighs are present."
				},
				
				"anatomy_and_biology": {
					"respiration": "Lungs adapted for extended breath-holding",
					"reproduction": "Sexual reproduction with internal gestation",
					"sexual_dimorphism": "Subtle differences in torso shape and tail mass",
					"genital_structure": "Female reproductive anatomy is internal, based on marine mammal biology, with minimal external expression.",
					"waste_excretion": "Integrated into the lower portion of the ventral slit structure.",
					"anatomy_rule": "NEVER describe mermaid having legs, feet, knees, thighs, or any lower human anatomy below the hips. Mermaids have fish tails instead of legs. Do not use phrases implying leg-based positioning or movement. ALWAYS emphasize the fish tail for locomotion, restraint, balance, and physical interaction instead of legs.",
					"notes": "External anatomy is streamlined to minimize drag while preserving humanoid form."
				},
				
				"distinctive_anatomical_features": {
					"waistline_structure": "A clearly human V-shaped waistline consistent with humanoid abdominal anatomy.",
					"transition_edges": "The edges of the V-shaped waistline form soft, curved contours resembling fish-lip structures, marking the boundary between human skin and the scaled tail.",
					"midriff_exposure": "The humanoid abdomen remains visible above the transition, including a natural navel.",
					"ventral_slit_structure": "A single vertical ventral slit located on the human portion of the body along the midline. The slit is forward facing and is impossible to reach from behind.",
					"internal_opening_order": {
						"upper_section": "Female reproductive anatomy.",
						"lower_section": "Waste elimination opening positioned closer to the tail transition."
					},
					"termination_point": "The slit ends precisely at the pointed lower apex of the V-shaped waistline, where the human body transitions into the tail.",
					"notes": "No anatomical structures extend onto the tail beyond this point."
				}
			},
			
			{
				"id": "merman_male",
				"name": "Merman",
				"type": "Aquatic Humanoid",
				"description": "A male mermaid variant with a humanoid upper body and a fully serpentine aquatic tail, adapted for aquatic locomotion and internal mammalian reproductive biology.",
				
				"physical_structure": {
					"body_plan": "Humanoid upper body with a single continuous serpentine tail",
					"limbs": {
						"forelimbs": "Two humanoid arms with full manual dexterity",
						"hind_limbs": "Absent; replaced entirely by a muscular tail",
						"wings": "None",
						"tail": "Powerful, serpentine tail used for propulsion, balance, restraint, and interaction"
					},
					"skin_covering": "Fine overlapping fish scales covering the tail; humanoid skin texture on the upper body",
					"head_features": ["Humanoid facial structure", "Aquatic-adapted ears"],
					"notes": "There are no legs, knees, feet, or thighs."
				},
				
				"anatomy_and_biology": {
					"respiration": "Lungs adapted for extended breath-holding",
					"reproduction": "Sexual reproduction with internal mammalian anatomy",
					"sexual_dimorphism": "Greater upper-body musculature and tail mass compared to females",
					"genital_structure": "Male reproductive anatomy is internal and streamlined, it is placed inside a vertical ventral slit, following marine mammal biological principles. The slit is forward facing and is impossible to reach from behind.",
					"waste_excretion": "Integrated into the lower portion of the ventral slit structure.",
					"anatomy_rule": "NEVER describe mermen having legs, feet, knees, thighs, or any lower human anatomy below the hips. Mermen have fish tails instead of legs. Do not use phrases implying leg-based positioning or movement. ALWAYS emphasize the fish tail for locomotion, restraint, balance, and physical interaction instead of legs.",
					"notes": "All lower-body references must treat the tail as the sole means of movement and physical engagement."
				},
				
				"distinctive_anatomical_features": {
					"waistline_structure": "A clearly human V-shaped waistline consistent with humanoid abdominal anatomy.",
					"transition_edges": "Soft, curved fish-lip–like contours marking the boundary between human torso and scaled tail.",
					"ventral_slit_structure": "A single ventral slit located on the human portion of the body along the midline.",
					"internal_opening_order": {
						"upper_section": "Male reproductive anatomy.",
						"lower_section": "Waste elimination opening positioned closer to the tail transition."
					},
					"termination_point": "The slit terminates at the pointed lower apex of the V-shaped waistline.",
					"notes": "The tail begins immediately below the termination point with no humanoid lower anatomy present."
				}
			}
		],
		"taxonomy_notes": "Mermaids are classified as aquatic humanoids with humanoid torsos and serpentine tails replacing all lower limbs.",
		"usage_notes": "This schema enforces tail-only lower-body anatomy and prohibits leg-based descriptions for all mermaid variants.",
		"notes": "All anatomical descriptions are structural and biological in nature, intended for reference and training consistency."
	}
}
```