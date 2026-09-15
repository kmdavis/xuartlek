---
noteType: pf2eMonster
aliases: "Pugwampi"
tags:
  - pf2e/creature/level/0
  - pf2e/creature/trait/fey
  - pf2e/creature/trait/gremlin
  - pf2e/creature/trait/tiny
statblock: inline
name: "Pugwampi"
level: 0
source: "Monster Core"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=3032"
socialImage: og-image.png
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC"
name: "Pugwampi"
level: "Creature 0"
size: "Tiny"
trait_01: "Fey"
trait_02: "Gremlin"
modifier: 6
perception:
  - name: "Perception"
    desc: "+6; (-2 to hear things) darkvision"
languages: "[[srd/pf2e/compendium/rules-elements/Languages#Kholo|Kholo]], [[srd/pf2e/compendium/rules-elements/Languages#Sakvroth|Sakvroth]]"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/Crafting|Crafting]] +2, [[srd/pf2e/compendium/rules-elements/skills/Deception|Deception]] +2, [[srd/pf2e/compendium/rules-elements/skills/Nature|Nature]] +4, [[srd/pf2e/compendium/rules-elements/skills/Stealth|Stealth]] +5, [[srd/pf2e/compendium/rules-elements/skills/Thievery|Thievery]] +5"
abilityMods: [-3, 3, 0, 0, 2, -2]
abilities_top:
  - name: "Items"
    desc: "Shortbow (60 arrows), Shortsword"
ac: 14
armorclass:
  - name: "AC"
    desc: "14; __Fort__: +5; __Ref__: +8; __Will__: +6"
hp: 17
health:
  - name: "HP"
    desc: "17; __Weaknesses__ cold iron 2"
abilities_mid:
  - name: "Unluck Aura"
    desc: "([[srd/pf2e/compendium/rules-elements/traits/player-core/Aura|aura]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Mental|mental]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Misfortune|misfortune]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Primal|primal]]) 20 feet. When a creature that isn't an [[srd/pf2e/compendium/rules-elements/traits/player-core/Animal|animal]], [[srd/pf2e/compendium/gm/creature-families/Gremlin|gremlin]], or [[srd/pf2e/compendium/gm/creature-families/Kholo|kholo]] enters the aura, it might become unlucky. It attempts a DC 16 Will save; it must roll twice and take the worse result. On a success, the creature is temporarily immune to pugwampi unluck auras for 24 hours. On a failure, the creature must roll twice and take the worse result on all checks as long as it's within the aura."
speed: "25 feet"
attacks:
  - name: "Melee"
    desc: "⬻ shortsword +8 ([[srd/pf2e/compendium/rules-elements/traits/player-core/Agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Finesse|Finesse]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Reach|reach 0 feet]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Versatile|versatile S]]) __Damage__ 1d6–3 slashing"
  - name: "Ranged"
    desc: "⬻ shortbow +8 ([[srd/pf2e/compendium/rules-elements/traits/player-core/Deadly|deadly d10]], range increment 60 feet, reload 0) __Damage__ 1d6 piercing"
spellcasting:
  - name: "Primal Innate Spells"
    desc: "DC 16 - __Cantrips (1st)__ [[srd/pf2e/compendium/spells/cantrips/Prestidigitation|Prestidigitation]] - __2nd__ [[srd/pf2e/compendium/spells/rank-2/Speak with Animals|Speak with Animals]] (at will)"
sourcebook: "_Monster Core_, page 180."
```

```encounter-table
name: Pugwampi
creatures:
  - 1: Pugwampi
```
