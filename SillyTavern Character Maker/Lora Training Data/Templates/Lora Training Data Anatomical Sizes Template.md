```json
{
	"schema_type": "anatomical_size",
	
	"instruction": "Define an anatomical size descriptor.",
	"input": "What does '<size_name>' mean for <anatomy_name>?",
	
	"output": {
		"id": "<anatomy_id>",
		"name": "<anatomy_name>",
		
		"scope": "All size ranges reflect adult anatomy unless otherwise specified.",
		
		"synonyms": [
			// anatomical, colloquial, and descriptive variants
		],
		
		"description": "<high-level description of the anatomical feature and what the size system represents>",
		
		"scale_ordering": "ascending",
		
		"size_scale": [
			{
				"id": "<size_id>",
				"name": "<size_name>",
				
				"synonyms": [
					// natural language cues implying this size
				],
				
				"description": "<clear description of visual, spatial, or mass-related characteristics>",
				
				"relative_scale": {
					// symbolic, descriptive, or approximate measurements as appropriate
				},
				
				"movement_profile": "<optional — describe movement, inertia, deformation, or lack thereof>",
				
				"scale_order": "<numbered_ascending>" 
				// (Lower numbers represent smaller sizes; values must increase monotonically)
				
				"notes": "<edge cases, clothing impact, posture effects, or narrative implications>"
			}
		]
	}
}
```