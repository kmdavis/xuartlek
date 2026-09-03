---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Accuser Agent"
tags:
  - pf2e/creature/level/9
  - pf2e/creature/trait/human
  - pf2e/creature/trait/humanoid
  - pf2e/creature/trait/medium
statblock: inline
name: "Accuser Agent"
level: 9
source: "NPC Core"
aon_id: "creature-3565"
aon_url: "https://2e.aonprd.com/NPCs.aspx?ID=3565"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "NPC"
name: "Accuser Agent"
level: "Creature 9"
size: "Medium"
trait_01: "Human"
trait_02: "Humanoid"
modifier: 19
perception:
  - name: "Perception"
    desc: "Perception +19; (21 to [[srd/pf2e/compendium/rules-elements/actions/player-core#Sense Motive|Sense Motive]])"
languages: "[[srd/pf2e/compendium/rules-elements/languages#Common|Common]]; up to 3 additional languages"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/deception|Deception]] +20, [[srd/pf2e/compendium/rules-elements/skills/diplomacy|Diplomacy]] +18, [[srd/pf2e/compendium/rules-elements/skills/intimidation|Intimidation]] +18, [[srd/pf2e/compendium/rules-elements/skills/lore|Legal Lore]] +20, [[srd/pf2e/compendium/rules-elements/skills/stealth|Stealth]] +17, [[srd/pf2e/compendium/rules-elements/skills/society|Society]] +18, [[srd/pf2e/compendium/rules-elements/skills/thievery|Thievery]] +19"
abilityMods: [0, 4, 0, 3, 4, 3]
abilities_top:
  - name: "Insightful"
    desc: "When the accuser agent succeeds at a Perception check, they critically succeed instead."
  - name: "Items"
    desc: "_+1 [[srd/pf2e/compendium/equipment/runes/striking-major|striking]] [[srd/pf2e/compendium/equipment/weapons/knife/dagger|dagger]]_, Scholarly Journal, _+1 [[srd/pf2e/compendium/equipment/runes/striking-major|striking]] [[srd/pf2e/compendium/equipment/weapons/sword/sword-cane|sword cane]]_, Writing Set"
ac: 28
armorclass:
  - name: "AC"
    desc: "28; __Fort__: +15; __Ref__: +19; __Will__: +19"
hp: 115
health:
  - name: "HP"
    desc: "115 __Objection!__ ⬲ ([[srd/pf2e/compendium/rules-elements/traits/player-core/auditory|auditory]], [[srd/pf2e/compendium/rules-elements/traits/player-core/linguistic|linguistic]])"
abilities_mid:
  - name: "Trigger"
    desc: "A creature within 30 feet takes an action with the [[srd/pf2e/compendium/rules-elements/traits/player-core/linguistic|linguistic]] trait"
  - name: "Effect"
    desc: "The triggering creature must succeed a DC 28 Will saving throw or their action is [[srd/pf2e/books/player-core/chapter-8-playing-the-game/actions#Disrupting Actions|disrupted]]."
speed: "25 feet"
attacks:
  - name: "Melee"
    desc: "⬻ _dagger_ +20 ([[srd/pf2e/compendium/rules-elements/traits/player-core/agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/deadly|deadly d6]], [[srd/pf2e/compendium/rules-elements/traits/player-core/finesse|Finesse]], [[srd/pf2e/compendium/rules-elements/traits/player-core/magical|Magical]], [[srd/pf2e/compendium/rules-elements/traits/player-core/versatile|versatile S]]) __Damage__ 2d4+8 piercing"
  - name: "Melee"
    desc: "⬻ _sword cane_ +20 ([[srd/pf2e/compendium/rules-elements/traits/player-core/agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/concealable|Concealable]], [[srd/pf2e/compendium/rules-elements/traits/player-core/finesse|Finesse]], [[srd/pf2e/compendium/rules-elements/traits/player-core/magical|Magical]]) __Damage__ 2d8+8 piercing"
  - name: "Melee"
    desc: "⬻ fist +20 ([[srd/pf2e/compendium/rules-elements/traits/player-core/agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/finesse|Finesse]], [[srd/pf2e/compendium/rules-elements/traits/player-core/nonlethal|Nonlethal]], [[srd/pf2e/compendium/rules-elements/traits/player-core/unarmed|Unarmed]]) __Damage__ 1d4+8 bludgeoning"
  - name: "Ranged"
    desc: "⬻ _dagger_ +20 ([[srd/pf2e/compendium/rules-elements/traits/player-core/agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/deadly|deadly d6]], [[srd/pf2e/compendium/rules-elements/traits/player-core/finesse|Finesse]], [[srd/pf2e/compendium/rules-elements/traits/player-core/magical|Magical]], [[srd/pf2e/compendium/rules-elements/traits/player-core/thrown|thrown 20 feet]], [[srd/pf2e/compendium/rules-elements/traits/player-core/versatile|versatile S]]) __Damage__ 2d4+8 piercing"
abilities_bot:
  - name: "Debilitating Sneak Attack"
    desc: "The accuser agent's Strikes deal an extra 3d6 precision damage to [[srd/pf2e/compendium/rules-elements/conditions#Off-Guard|off-guard]] creatures. A target who takes this additional precision damage also either becomes [[srd/pf2e/compendium/rules-elements/conditions#Enfeebled|enfeebled 1]] or takes a –10-foot status penalty to its Speeds until the end of the agent's next turn."
sourcebook: "_NPC Core_, page 118."
```

```encounter-table
name: Accuser Agent
creatures:
  - 1: Accuser Agent
```
