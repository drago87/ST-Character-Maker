```json
{
	"instruction": "Define breast size descriptor.",
	"input": "What does 'flat' mean for breast size?",
	"output":{
		"id": "anatomy_breasts",
		"name": "Breasts",
		"synonyms": [
			 "breasts",
			 "boobs",
			 "chest",
			 "bust"
		],
		 "description": "The mammary region of the torso. Used in the size system to determine visual fullness and mass.",
		 "size_scale": [
			 {
				 "id": "breast_size_flat",
				 "name": "Flat",
				 "synonyms": [
					 "flat chest",
					 "no breasts",
					 "minimal chest"
				],
				 "description": "Indicates minimal or no visible projection of breast tissue. The chest profile remains largely aligned with the ribcage surface.",
				 "relative_scale": "lowest",
				 "notes": "Used to describe individuals with undeveloped or very small breast volume."
			},
			 {
				"id": "breast_size_small",
				"name": "Small",
				"synonyms": [
					 "small breasts",
					 "petite chest"
				],
				"description": "Represents a slight projection of breast tissue with modest volume. Chest shape shows definition but remains compact.",
				"relative_scale": "below_average",
				"notes": "Does not significantly alter posture or require high-support garments."
			},
			{
				"id": "breast_size_medium",
				"name": "Medium",
				"synonyms": [
					"average breasts",
					"moderate chest"
				],
				"description": "A balanced, proportionate breast volume with moderate projection. Generally considered average among adults.",
				"relative_scale": "average",
				"notes": "Common reference point for clothing and uniform sizing."
			},
			{
				"id": "breast_size_large",
				"name": "Large",
				"synonyms": [
					"large breasts",
					"big bust"
				],
				"description": "Describes a larger, fuller breast volume with substantial projection. Noticeable curvature relative to torso profile.",
				"relative_scale": "above_average",
				"notes": "Often requires supportive garments for comfort."
			},
			{
				 "id": "breast_size_huge",
				 "name": "Huge",
				 "synonyms": [
					 "huge breasts",
					 "massive bust"
				],
				"description": "Indicates a significantly above-average breast volume with high projection and mass. Highly pronounced chest curvature.",
				"relative_scale": "highest_common_scale",
				"notes": "May require specialized clothing support."
			}
		  ]
	}
}
```
```json
{
	"instruction": "Define penis size descriptor.",
	"input": "What does 'small' mean for penis size?",
	"output":{
		"id": "anatomy_penis",
		"scope": "All size ranges reflect ADULT HUMAN baselines. For children scale it to 0.3",
		"name": "Penis",
		"synonyms": [
			"penis",
			"dick",
			"cock",
			"member",
			"shaft"
		],
		"description": "External male genital organ used for reproduction and urination. The size scale categorizes visible length and girth.",
		"size_scale": [
			{
				"id": "penis_size_small",
				"name": "Small",
				"synonyms": [
					"small penis",
					"small dick",
					"short dick"
				],
				"description": "A penis size below the general population mean in both length and girth.",
				"relative_scale": {
				"flaccid": {
					 "approx_length_cm": "2–6",
					 "approx_length_in": "0.8–2.4",
					 "girth_characterization": "slim"
				},
				"erect": {
					"approx_length_cm": "4–9",
					"approx_length_in": "1.5–3.5",
					"girth_characterization": "slim to narrow"
				}
				},
				"notes": "Natural-language cues include 'small', 'short', 'tiny', or descriptions emphasizing reduced size."
			},
			{
				"id": "penis_size_medium",
				"name": "Medium",
				"synonyms": [
					"average penis",
					"normal dick"
				],
				"description": "The central size range in population distribution, neither notably reduced nor notably enlarged.",
				"relative_scale": {
				"flaccid": {
					"approx_length_cm": "6–10",
					"approx_length_in": "2.4–4",
					"girth_characterization": "average"
				},
				"erect": {
					"approx_length_cm": "10–15",
					"approx_length_in": "4–6",
					"girth_characterization": "average"
				}
				},
				"notes": "Usually implied when no explicit size description is present in the source text."
			},
			{
				"id": "penis_size_large",
				"name": "Large",
				"synonyms": ["large penis",
					"big dick",
					"big cock"
				],
				"description": "A penis size above the common population range in either length or girth.",
				"relative_scale": {
				"flaccid": {
					"approx_length_cm": "10+",
					"approx_length_in": "4+",
					"girth_characterization": "full"
				},
				"erect": {
					"approx_length_cm": "16+",
					"approx_length_in": "6.5+",
					"girth_characterization": "thick to full"
				}
				},
				"notes": "Textual cues include 'large', 'big', 'well-endowed', or other descriptors indicating conspicuous size."
			}
		]
	}
}
```