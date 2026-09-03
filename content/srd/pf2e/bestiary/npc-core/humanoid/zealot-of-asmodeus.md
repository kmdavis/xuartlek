---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Zealot of Asmodeus"
tags:
  - pf2e/creature/level/4
  - pf2e/creature/trait/human
  - pf2e/creature/trait/humanoid
  - pf2e/creature/trait/unholy
  - pf2e/creature/trait/medium
statblock: inline
name: "Zealot of Asmodeus"
level: 4
source: "NPC Core"
aon_id: "creature-3444"
aon_url: "https://2e.aonprd.com/NPCs.aspx?ID=3444"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "NPC"
name: "Zealot of Asmodeus"
level: "Creature 4"
size: "Medium"
trait_01: "Human"
trait_02: "Humanoid"
trait_03: "Unholy"
modifier: 9
perception:
  - name: "Perception"
    desc: "Perception +9"
languages: "[[srd/pf2e/compendium/rules-elements/languages#Common|Common]]"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/athletics|Athletics]] +9, [[srd/pf2e/compendium/rules-elements/skills/deception|Deception]] +10, [[srd/pf2e/compendium/rules-elements/skills/intimidation|Intimidation]] +10, [[srd/pf2e/compendium/rules-elements/skills/religion|Religion]] +12, [[srd/pf2e/compendium/rules-elements/skills/society|Society]] +7"
abilityMods: [4, 1, 1, 0, 3, 2]
abilities_top:
  - name: "Items"
    desc: "Composite Shortbow (20 arrows), Half Plate, Mace, Steel Shield (Hardness 5, HP 20, BT 10)"
ac: 22
armorclass:
  - name: "AC"
    desc: "22; __Fort__: +9; __Ref__: +7; __Will__: +11"
hp: 60
health:
  - name: "HP"
    desc: "60"
abilities_mid:
  - name: "Shield Block"
    desc: "⬲"
  - name: "Swear Vengeance"
    desc: "⬲"
  - name: "Trigger"
    desc: "A creature the zealot can see damages a follower of Asmodeus other than the zealot"
  - name: "Effect"
    desc: "The zealot is affected by a [[srd/pf2e/compendium/spells/rank-1/sure-strike|_sure strike_]] spell. If the zealot makes an attack roll against anyone other than the triggering creature, the _sure strike_ ends with no effect."
speed: "20 feet"
attacks:
  - name: "Melee"
    desc: "⬻ mace +12 ([[srd/pf2e/compendium/rules-elements/traits/player-core/shove|Shove]]) __Damage__ 1d8+4 bludgeoning"
  - name: "Melee"
    desc: "⬻ fist +12 ([[srd/pf2e/compendium/rules-elements/traits/player-core/agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/nonlethal|Nonlethal]], [[srd/pf2e/compendium/rules-elements/traits/player-core/unarmed|Unarmed]]) __Damage__ 1d4+4 bludgeoning"
  - name: "Ranged"
    desc: "⬻ composite shortbow +9 ([[srd/pf2e/compendium/rules-elements/traits/player-core/deadly|deadly 1d10]], [[srd/pf2e/compendium/rules-elements/traits/player-core/propulsive|Propulsive]], range increment 60 feet, reload 0) __Damage__ 1d6+2 piercing"
abilities_bot:
  - name: "Channel Smite"
    desc: "⬺ ([[srd/pf2e/compendium/rules-elements/traits/player-core/divine|Divine]])"
  - name: "Cost"
    desc: "the zealot expends a [[srd/pf2e/compendium/spells/rank-1/harm|_harm_]] spell"
  - name: "Effect"
    desc: "The zealot makes a melee Strike. If it hits, they damage the target with a 1-action _harm_ spell. The target automatically gets a failure (or a critical failure if the Strike was a critical hit). The spell doesn't have the [[srd/pf2e/compendium/rules-elements/traits/player-core/manipulate|manipulate]] trait when cast this way."
  - name: "Deadly Simplicity"
    desc: "The zealot deals 1d8 damage with their mace instead of 1d6."
spellcasting:
  - name: "Divine Prepared Spells"
    desc: "DC 19, attack +11 - __Cantrips (2nd)__ [[srd/pf2e/compendium/spells/cantrips/detect-magic|Detect Magic]], [[srd/pf2e/compendium/spells/cantrips/divine-lance|Divine Lance]], [[srd/pf2e/compendium/spells/cantrips/forbidding-ward|Forbidding Ward]], [[srd/pf2e/compendium/spells/cantrips/read-aura|Read Aura]], [[srd/pf2e/compendium/spells/cantrips/sigil|Sigil]] - __1st__ [[srd/pf2e/compendium/spells/rank-1/command|Command]], [[srd/pf2e/compendium/spells/rank-1/runic-weapon|Runic Weapon]], [[srd/pf2e/compendium/spells/rank-1/spirit-link|Spirit Link]] - __2nd__ [[srd/pf2e/compendium/spells/rank-2/cleanse-affliction|Cleanse Affliction]], [[srd/pf2e/compendium/spells/rank-1/harm|Harm]] (×4), [[srd/pf2e/compendium/spells/rank-2/see-the-unseen|See the Unseen]], [[srd/pf2e/compendium/spells/rank-2/share-life|Share Life]]"
sourcebook: "_NPC Core_, page 31."
```

```encounter-table
name: Zealot of Asmodeus
creatures:
  - 1: Zealot of Asmodeus
```
