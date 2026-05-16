# Review Rubric

Use this taxonomy to classify findings.

## Critical Issues

Critical issues invalidate or seriously undermine a central claim.

Examples:

- wrong theorem statement or proof
- theorem conditions not satisfied
- circular reasoning in a core argument
- empirical result does not follow from the reported data
- citation directly contradicts the claim it is used to support
- benchmark, calibration, or experiment is invalid for the stated conclusion
- implementation bug that changes the result

Required evidence:

- exact artifact location
- what is wrong
- why it matters
- what would be needed to fix or rescue the claim

## Significant Concerns

Significant concerns weaken the artifact but do not necessarily break it.

Examples:

- missing comparison to important prior work
- overclaiming beyond evidence
- incomplete robustness checks
- unclear assumptions
- weak external validity
- under-specified model, dataset, or method
- plausible alternative interpretation not addressed

Required evidence:

- exact artifact location
- concrete explanation of the weakness
- likely impact on the artifact's contribution

## Minor Issues

Minor issues are local problems that should be fixed but do not affect the main contribution.

Examples:

- notation inconsistencies
- ambiguous wording
- typo or formatting problems
- broken references
- missing labels
- small citation metadata errors

Required evidence:

- exact location
- concise fix or clarification

## Questions For The Authors

Use this category when something looks wrong but may be intentional or recoverable with context.

Examples:

- hidden assumption may justify a step
- appendix may contain missing proof detail
- data transformation is unclear
- term appears to have a specialized meaning

Required evidence:

- exact location
- why the question matters
- what answer would resolve the concern
