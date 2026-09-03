---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Painted Stag"
tags:
  - pf2e/creature/level/9
  - pf2e/creature/trait/elemental
  - pf2e/creature/trait/plant
  - pf2e/creature/trait/wood
  - pf2e/creature/trait/huge
statblock: inline
name: "Painted Stag"
level: 9
source: "Rage of Elements"
aon_id: "creature-2678"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=2678"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "RoE"
name: "Painted Stag"
level: "Creature 9"
size: "Huge"
trait_01: "Elemental"
trait_02: "Plant"
trait_03: "Wood"
modifier: 21
perception:
  - name: "Perception"
    desc: "Perception +21"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/athletics|Athletics]] +18, [[srd/pf2e/compendium/rules-elements/skills/intimidation|Intimidation]] +23, [[srd/pf2e/compendium/rules-elements/skills/nature|Nature]] +18"
abilityMods: [7, 3, 5, 2, 1, 4]
ac: 27
armorclass:
  - name: "AC"
    desc: "27; __Fort__: +18; __Ref__: +12; __Will__: +21"
hp: 175
health:
  - name: "HP"
    desc: "175 , regeneration 10 (deactivated by [[srd/pf2e/compendium/rules-elements/traits/player-core/fire|fire]]); __Immunities__ bleed, [[srd/pf2e/compendium/rules-elements/conditions#Paralyzed|paralyzed]], [[srd/pf2e/compendium/rules-elements/traits/player-core/poison|poison]], [[srd/pf2e/compendium/rules-elements/traits/player-core/sleep|sleep]]; __Weaknesses__ axes 10, fire 10"
speed: "45 feet, climb 60 feet"
attacks:
  - name: "Melee"
    desc: "⬻ antler +20 __Damage__ 2d12+7 piercing plus Grab"
  - name: "Melee"
    desc: "⬻ hooves +20 __Damage__ 2d10+7 bludgeoning"
abilities_bot:
  - name: "Mauler"
    desc: "A painted stag gains a +5 circumstance bonus to damage rolls against creatures it has [[srd/pf2e/compendium/rules-elements/conditions#Grabbed|grabbed]]."
  - name: "Painted Dance"
    desc: "⬺ ([[srd/pf2e/compendium/rules-elements/traits/player-core/auditory|Auditory]], [[srd/pf2e/compendium/rules-elements/traits/player-core/mental|Mental]], [[srd/pf2e/compendium/rules-elements/traits/player-core/plant|Plant]], [[srd/pf2e/compendium/rules-elements/traits/player-core/primal|Primal]], [[srd/pf2e/compendium/rules-elements/traits/player-core/visual|Visual]]) The stag shakes the wooden plating along its body in a cacophonous clatter that sets its painted patterns dancing. All creatures within 60 feet of the painted stag who can see or hear it must attempt a DC 28 Will save; a creature [[srd/pf2e/compendium/rules-elements/conditions#Grabbed|grabbed]] by the stag takes a –4 circumstance penalty to its save. Regardless of the result of its save, each creature is temporarily immune for 1 hour."
  - name: "Critical Success"
    desc: "The creature is unaffected."
  - name: "Success"
    desc: "The creature is [[srd/pf2e/compendium/rules-elements/conditions#Fascinated|fascinated]] by the painted stag for 1 round."
  - name: "Failure"
    desc: "The creature is stunned 2 and fascinated by the painted stag for as long as it's stunned."
  - name: "Critical Failure"
    desc: "As failure, except stunned 4. Artistic Exchange Though few know it, painted stags paint their own markings—making their sporadic appearances in elven art and tattoos, particularly in those cultures descended from the lost nation of Mierani in Varisia, all the more appropriate. Many modern depictions, however, erroneously portray them as benevolent protectors of the forest. Only Darklands tattoo cultures consistently depict them as the relentless predators they truly are."
sourcebook: "_Rage of Elements_, page 210."
```

```encounter-table
name: Painted Stag
creatures:
  - 1: Painted Stag
```
