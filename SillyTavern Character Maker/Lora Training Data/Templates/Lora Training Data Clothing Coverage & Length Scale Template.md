```json
{
	"instruction": "Provide clothing coverage and length metadata with full schema.",
	"input": "Define the universal clothing length and coverage scale used across garment types.",
	"output": {
		"id": "clothing_coverage_length_scale",
		"name": "Universal Clothing Coverage and Length Scale",
		"description": "A standardized scale describing how much of the body a garment covers vertically and spatially, regardless of garment category. Used to determine exposure, movement behavior, restriction, and narrative implications.",

		"applies_to": [
			"one_piece",
			"two_piece_top",
			"two_piece_bottom",
			"outerwear",
			"legwear",
			"robes",
			"capes",
			"dresses",
			"skirts",
			"coats"
		],

		"coverage_axis_definition": {
			"reference_points": [
				"Upper torso",
				"Waist / hips",
				"Upper thigh",
				"Knees",
				"Calves",
				"Ankles",
				"Ground / trailing"
			],
			"direction": "Ascending scale_index values indicate increased coverage and length."
		},

		"length_scale": [
			{
				"id": "<length_id>",
				"scale_index": <number>,
				"name": "<length_name>",
				"synonyms": ["<synonym_1>", "<synonym_2>"],

				"approx_position": "<where_the_garment_ends_relative_to_the_body>",
				"coverage_description": "<which_body_regions_are_covered_or_exposed>",
				"movement_behavior": "<how_the_garment_moves_or_drapes_during_motion>",
				"movement_constraints": "<how_much_it_limits_stride_range_or_body_motion>",
				"common_use": "<contexts_or_garment_types_where_this_length_is_common>",
				"narrative_implications": "<what_this_level_of_coverage_signals_or_implies>",
				"notes": "<optional_additional_notes>"
			}
		],

		"usage_notes": "This scale is intended to be referenced by garments of any category. The same scale_index may correspond to different physical expressions depending on garment type (e.g., a coat vs. a skirt), but the relative coverage and restriction remain consistent.",

		"conditioning_guidance": {
			"scale_index_usage": "Lower scale_index values imply minimal coverage and freedom of movement. Higher values imply greater coverage, weight, or restriction.",
			"comparative_prompting": "Numeric indices may be used for comparisons (e.g., longer than index 5, minimal coverage under index 2).",
			"cross_schema_alignment": "Scale indices may be aligned with movement restriction, modesty signaling, or environmental interaction."
		}
	}
}

```