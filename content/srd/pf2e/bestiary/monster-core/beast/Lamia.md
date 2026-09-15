---
noteType: pf2eMonster
aliases: "Lamia"
tags:
  - pf2e/creature/level/6
  - pf2e/creature/trait/beast
  - pf2e/creature/trait/humanoid
  - pf2e/creature/trait/large
statblock: inline
name: "Lamia"
level: 6
source: "Monster Core"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=3077"
socialImage: og-image.png
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC"
name: "Lamia"
level: "Creature 6"
size: "Large"
trait_01: "Beast"
trait_02: "Humanoid"
modifier: 13
perception:
  - name: "Perception"
    desc: "+13; darkvision"
languages: "[[srd/pf2e/compendium/rules-elements/Languages#Chthonian|Chthonian]], [[srd/pf2e/compendium/rules-elements/Languages#Common|Common]]"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/Athletics|Athletics]] +16, Cult Lore +11, [[srd/pf2e/compendium/rules-elements/skills/Deception|Deception]] +15, [[srd/pf2e/compendium/rules-elements/skills/Diplomacy|Diplomacy]] +11, [[srd/pf2e/compendium/rules-elements/skills/Intimidation|Intimidation]] +13, [[srd/pf2e/compendium/rules-elements/skills/Stealth|Stealth]] +15, [[srd/pf2e/compendium/rules-elements/skills/Survival|Survival]] +11"
abilityMods: [6, 3, 2, 1, 3, 3]
abilities_top:
  - name: "Items"
    desc: "Javelin (2), _+1 [[srd/pf2e/compendium/equipment/weapons/spear/Spear|spear]]_"
ac: 24
armorclass:
  - name: "AC"
    desc: "24; __Fort__: +12; __Ref__: +15; __Will__: +15"
hp: 95
health:
  - name: "HP"
    desc: "95"
speed: "40 feet"
attacks:
  - name: "Melee"
    desc: "⬻ _spear_ +17 __Damage__ 1d6+10 piercing"
  - name: "Melee"
    desc: "⬻ tail +16 ([[srd/pf2e/compendium/rules-elements/traits/player-core/Agile|Agile]]) __Damage__ 1d6+10 bludgeoning plus Grab"
  - name: "Ranged"
    desc: "⬻ _spear_ +14 ([[srd/pf2e/compendium/rules-elements/traits/player-core/Thrown|thrown 10 feet]]) __Damage__ 1d6+10 piercing"
  - name: "Ranged"
    desc: "⬻ javelin +13 ([[srd/pf2e/compendium/rules-elements/traits/player-core/Thrown|thrown 30 feet]]) __Damage__ 1d6+10 piercing"
abilities_bot:
  - name: "Lamia's Caress"
    desc: "⬺ ([[srd/pf2e/compendium/rules-elements/traits/player-core/Curse|Curse]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Mental|Mental]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Occult|Occult]]) The lamia touches a creature, who must succeed at a DC 23 Will save or become [[srd/pf2e/compendium/rules-elements/Conditions#Stupefied|stupefied 1]]. If the target fails additional saves against this ability, the condition value increases by 1 (to a maximum of stupefied 4). This condition value decreases by 1 every 24 hours."
spellcasting:
  - name: "Occult Innate Spells"
    desc: "DC 25 - __1st__ [[srd/pf2e/compendium/spells/rank-1/Illusory Disguise|Illusory Disguise]] (at will), [[srd/pf2e/compendium/spells/rank-1/Illusory Object|Illusory Object]] (at will), [[srd/pf2e/compendium/spells/rank-1/Ventriloquism|Ventriloquism]] (at will) - __2nd__ [[srd/pf2e/compendium/spells/rank-2/Blur|Blur]], [[srd/pf2e/compendium/spells/rank-2/Humanoid Form|Humanoid Form]] (at will) - __3rd__ [[srd/pf2e/compendium/spells/rank-1/Sleep|Sleep]] - __4th__ [[srd/pf2e/compendium/spells/rank-1/Charm|Charm]] (×3), [[srd/pf2e/compendium/spells/rank-4/Suggestion|Suggestion]]"
sourcebook: "_Monster Core_, page 214."
```

```encounter-table
name: Lamia
creatures:
  - 1: Lamia
```
