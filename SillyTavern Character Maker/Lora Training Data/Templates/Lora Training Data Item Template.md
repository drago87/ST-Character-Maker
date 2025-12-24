```json
{
	"instruction": "Provide item metadata with full schema.",
	"input": "What is <item_name>?",
	"output": {
		"id": "<item_id>",
		"name": "<item_name>",
		"category": ["<category_from_list>"],
		"type": "<type_of_item_or_subcategory>",
		"description": "<describe_what_the_item_is>",
		"intended_use": "<why_and_where_it_is_used>",
		"operation": "<how_to_use_or_apply_item>",
		"materials": "<common_materials>",
		"safety_notes": "<safety_or_warnings>",
		"variants": [
			{
				"name": "<optional_variants_or_sizes>"
			}
		],
		"metadata": {
			"size": "<size_information>",
			"weight": "<weight_information>",
			"color_options": ["<available_colors>"],
			"compatibility": ["<compatibility_notes_or_restrictions>"]
		},
		"notes": "<optional_additional_notes>"
	}
}
```