---
noteType: pf2eMonster
aliases: "Qarna"
tags:
  - pf2e/creature/level/4
  - pf2e/creature/trait/archon
  - pf2e/creature/trait/celestial
  - pf2e/creature/trait/holy
  - pf2e/creature/trait/medium
statblock: inline
name: "Qarna"
level: 4
source: "Monster Core"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=2833"
socialImage: og-image.png
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC"
name: "Qarna"
level: "Creature 4"
size: "Medium"
trait_01: "Archon"
trait_02: "Celestial"
trait_03: "Holy"
modifier: 11
perception:
  - name: "Perception"
    desc: "+11; darkvision"
languages: "[[srd/pf2e/compendium/rules-elements/Languages#Diabolic|Diabolic]], [[srd/pf2e/compendium/rules-elements/Languages#Draconic|Draconic]], [[srd/pf2e/compendium/rules-elements/Languages#Empyrean|Empyrean]], Utopian; [[srd/pf2e/compendium/spells/rank-5/Truespeech|_truespeech_]]"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/Acrobatics|Acrobatics]] +12, [[srd/pf2e/compendium/rules-elements/skills/Intimidation|Intimidation]] +11, [[srd/pf2e/compendium/rules-elements/skills/Nature|Nature]] +11, [[srd/pf2e/compendium/rules-elements/skills/Religion|Religion]] +9, [[srd/pf2e/compendium/rules-elements/skills/Stealth|Stealth]] +10, [[srd/pf2e/compendium/rules-elements/skills/Survival|Survival]] +11, [[srd/pf2e/compendium/rules-elements/skills/Athletics|Athletics]] +11"
abilityMods: [3, 4, 3, 1, 3, 1]
abilities_top:
  - name: "Items"
    desc: "Composite Longbow (20 arrows)"
ac: 22
armorclass:
  - name: "AC"
    desc: "22; __Fort__: +11; __Ref__: +10; __Will__: +11 +1 status to all saves vs. [[srd/pf2e/compendium/rules-elements/traits/player-core/Magical|magic]]"
hp: 65
health:
  - name: "HP"
    desc: "65; __Immunities__ [[srd/pf2e/compendium/rules-elements/traits/player-core/Fear|fear]]; __Weaknesses__ [[srd/pf2e/compendium/rules-elements/traits/player-core/Unholy|unholy]] 5"
abilities_mid:
  - name: "Archon's Protection"
    desc: "⬲"
  - name: "Trigger"
    desc: "An enemy damages the archon's ally and both are within 15 feet of the archon"
  - name: "Effect"
    desc: "The ally gains resistance 5 to all damage against the triggering damage and the archon can make a Strike against the enemy."
speed: "35 feet"
attacks:
  - name: "Melee"
    desc: "⬻ horn +13 ([[srd/pf2e/compendium/rules-elements/traits/player-core/Holy|Holy]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Magical|Magical]]) __Damage__ 1d8+9 piercing plus Push"
  - name: "Ranged"
    desc: "⬻ composite longbow +14 ([[srd/pf2e/compendium/rules-elements/traits/player-core/Holy|Holy]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Deadly|deadly d10]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Magical|Magical]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Propulsive|Propulsive]], range increment 100 feet, [[srd/pf2e/compendium/rules-elements/traits/player-core/Volley|volley 30 feet]]) __Damage__ 1d8+7 piercing"
abilities_bot:
  - name: "Archon's Pursuit"
    desc: "⬺"
  - name: "Frequency"
    desc: "once per day"
  - name: "Requirements"
    desc: "The qarna saw another creature teleport within the last round and has at least one [[srd/pf2e/compendium/spells/rank-4/Translocate|_translocate_]] spell remaining"
  - name: "Effect"
    desc: "The qarna casts one of their _translocate_ spells, which is heightened to 5th rank and causes the qarna to arrive in an unoccupied space it chooses within 30 feet of the creature it's pursuing. If the creature is too far away, the qarna arrives as close as possible."
  - name: "Distracting Arrow"
    desc: "⬺ ([[srd/pf2e/compendium/rules-elements/traits/player-core/Divine|Divine]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Mental|Mental]]) The qarna makes a composite longbow Strike. If it hits, the arrow lodges in the target and that creature's senses focus on the archon, leaving all else blurry. That creature takes a –2 status penalty to attack rolls and Perception checks against any target other than the qarna. The creature can Interact to remove the arrow, which ends the effect."
  - name: "Touch of Charity"
    desc: "⬻ ([[srd/pf2e/compendium/rules-elements/traits/player-core/Divine|Divine]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Healing|Healing]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Manipulate|Manipulate]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Vitality|Vitality]]) The qarna touches a willing living creature to take on that creature's wounds. The qarna transfers up to 30 of their own HP to the touched creature. (The qarna can't transfer more HP than they currently have.)"
spellcasting:
  - name: "Divine Innate Spells"
    desc: "DC 21 - __Cantrips (2nd)__ [[srd/pf2e/compendium/spells/cantrips/Light|Light]] - __1st__ [[srd/pf2e/compendium/spells/rank-1/Charm|Charm]] (animals only; ×3), [[srd/pf2e/compendium/spells/rank-1/Sure Strike|Sure Strike]] (×3) - __2nd__ [[srd/pf2e/compendium/spells/rank-2/Animal Messenger|Animal Messenger]] (×3) - __4th__ [[srd/pf2e/compendium/spells/rank-4/Translocate|Translocate]] (×3) - __Constant (5th)__ [[srd/pf2e/compendium/spells/rank-5/Truespeech|Truespeech]]"
sourcebook: "_Monster Core_, page 27."
```

```encounter-table
name: Qarna
creatures:
  - 1: Qarna
```
