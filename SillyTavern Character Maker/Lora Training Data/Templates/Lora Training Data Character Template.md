```json
{
	"instruction": "Provide character metadata with full schema.",
	"input": "Who is <character_name>?",
	"output": {
		"id": "<character_id>",
		"name": "<character_name>",
		"aliases": ["<other_names_or_nicknames>"],
		"age": "<age_or_approximate_range>",
		"gender": "<gender>",
		"species": "<species>",
		"affiliations": ["<groups_or_organizations>"],
		"role_or_status": "<role_or_social_status>",
		"power_identifiers": ["<abilities_or_powers>"],
		"personality": {
			"traits": ["<personality_traits>"],
			"notes": "<additional_personality_notes>"
		},
		"appearance": {
			"general": {
				"height": "<height_or_description>",
				"build": "<slender/athletic/etc.>",
				"skin_color": "<skin_color>",
				"hair": {
				"color": "<hair_color>",
				"length": "<hair_length>",
				"style": "<hair_style>"
			},
			"eyes": {
				"color": "<eye_color>",
				"shape": "<eye_shape>"
			},
			"notable_features": ["<scars, tattoos, marks, etc.>"]
			},
			"clothing": {
				"head": "<headwear>",
				"neck": "<neckwear>",
				"one_piece": "<one_piece_clothing>",
				"two_piece_top": "<two_piece_top>",
				"two_piece_bottom": "<two_piece_bottom>",
				"leggings": "<leggings_or_pants>",
				"socks": "<socks>",
				"shoes": "<shoes>",
				"underwear_top": "<underwear_top_or_binding>",
				"underwear_bottom": "<underwear_bottom_or_fundoshi>"
			}
		},
		"notes": "<optional_additional_notes>"
	}
}

```