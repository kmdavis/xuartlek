---
noteType: pf2eMonster
aliases: "Nuckelavee"
tags:
  - pf2e/creature/level/9
  - pf2e/creature/trait/amphibious
  - pf2e/creature/trait/fey
  - pf2e/creature/trait/large
statblock: inline
name: "Nuckelavee"
level: 9
source: "Monster Core"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=3110"
socialImage: og-image.png
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC"
name: "Nuckelavee"
level: "Creature 9"
size: "Large"
trait_01: "Amphibious"
trait_02: "Fey"
modifier: 16
perception:
  - name: "Perception"
    desc: "+16; low-light vision"
languages: "[[srd/pf2e/compendium/rules-elements/Languages#Aklo|Aklo]], [[srd/pf2e/compendium/rules-elements/Languages#Common|Common]], [[srd/pf2e/compendium/rules-elements/Languages#Fey|Fey]]"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/Athletics|Athletics]] +19, [[srd/pf2e/compendium/rules-elements/skills/Intimidation|Intimidation]] +19, [[srd/pf2e/compendium/rules-elements/skills/Nature|Nature]] +16, [[srd/pf2e/compendium/rules-elements/skills/Stealth|Stealth]] +18, [[srd/pf2e/compendium/rules-elements/skills/Survival|Survival]] +16"
abilityMods: [6, 3, 4, 1, 3, 4]
abilities_top:
  - name: "Items"
    desc: "_+1 [[srd/pf2e/compendium/equipment/runes/Striking|striking]] [[srd/pf2e/compendium/equipment/weapons/sword/Bastard Sword|bastard sword]]_"
ac: 28
armorclass:
  - name: "AC"
    desc: "28; __Fort__: +19; __Ref__: +16; __Will__: +20"
hp: 190
health:
  - name: "HP"
    desc: "190; __Immunities__ [[srd/pf2e/compendium/rules-elements/traits/player-core/Disease|disease]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Poison|poison]]; __Weaknesses__ cold iron 10"
abilities_mid:
  - name: "Frightful Presence"
    desc: "([[srd/pf2e/compendium/rules-elements/traits/player-core/Aura|aura]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Emotion|emotion]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Fear|fear]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Mental|mental]]) 30 feet, DC 25"
  - name: "Purity Vulnerability"
    desc: "Unpolluted fresh water burns a nuckelavee like acid, dealing 1d6 damage to it and causing it to be [[srd/pf2e/compendium/rules-elements/Conditions#Sickened|sickened 2]]. A nuckelavee can't heal from damage when it's in an area that isn't polluted (subject to GM discretion)."
  - name: "Reactive Strike"
    desc: "⬲"
speed: "40 feet, swim 40 feet"
attacks:
  - name: "Melee"
    desc: "⬻ _bastard sword_ +21 ([[srd/pf2e/compendium/rules-elements/traits/player-core/Magical|Magical]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Reach|reach 10 feet]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Two-Hand|two-hand d12]]) __Damage__ 2d8+12 slashing plus 1d6 poison and mortasheen"
  - name: "Melee"
    desc: "⬻ jaws +20 ([[srd/pf2e/compendium/rules-elements/traits/player-core/Agile|Agile]]) __Damage__ 2d8+12 piercing plus 1d6 poison and mortasheen"
  - name: "Melee"
    desc: "⬻ hoof +20 __Damage__ 2d6+12 bludgeoning plus mortasheen"
abilities_bot:
  - name: "Blight Breath"
    desc: "⬺ ([[srd/pf2e/compendium/rules-elements/traits/player-core/Disease|Disease]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Poison|Poison]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Primal|Primal]]) The nuckelavee breathes a 30-foot cone of foulness, dealing 8d6 void damage to living creatures in the area with a DC 28 basic Fortitude save. A creature that fails also takes 2d6 persistent bleed damage. The nuckelavee can't use Blight Breath again for 1d4 rounds."
  - name: "Mortasheen"
    desc: "([[srd/pf2e/compendium/rules-elements/traits/player-core/Disease|Disease]]) The target can't recover from the [[srd/pf2e/compendium/rules-elements/Conditions#Fatigued|fatigued]] condition caused by mortasheen until the disease is cured. Mortasheen gains the [[srd/pf2e/compendium/rules-elements/traits/gm-core/Virulent|virulent]] trait against [[srd/pf2e/compendium/rules-elements/traits/player-core/Animal|animals]] and [[srd/pf2e/compendium/rules-elements/traits/player-core/Plant|plants]]"
  - name: "Saving Throw"
    desc: "DC 28 Fortitude"
  - name: "Stage 1"
    desc: "Carrier with no ill effect (1 day)"
  - name: "Stage 2"
    desc: "[[srd/pf2e/compendium/rules-elements/Conditions#Drained|drained 1]] and fatigued (1 day)"
  - name: "Stage 3"
    desc: "drained 2 and fatigued (1 day)"
  - name: "Stage 4"
    desc: "dead"
  - name: "Trample"
    desc: "⬽ Medium or smaller, hoof, DC 28 Unfortunate Victims Nuckelavees are equally delighted to murder and feed upon both hapless peasants and altruistic naturalists engaged in the process of cleaning up pollution. Indeed, those who would seek to purify such sites are often regarded as the greater threat by a nuckelavee, as without a befouled land to dwell in, the foul fey would wither away."
spellcasting:
  - name: "Primal Innate Spells"
    desc: "DC 28 - __3rd__ [[srd/pf2e/compendium/spells/rank-3/Aqueous Orb|Aqueous Orb]] - __5th__ [[srd/pf2e/compendium/spells/rank-5/Control Water|Control Water]]"
  - name: "Rituals"
    desc: "DC 28 - __4th__ Blight"
sourcebook: "_Monster Core_, page 243."
```

```encounter-table
name: Nuckelavee
creatures:
  - 1: Nuckelavee
```
