---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Demonbane Warrior"
tags:
  - pf2e/creature/level/5
  - pf2e/creature/trait/elf
  - pf2e/creature/trait/humanoid
  - pf2e/creature/trait/medium
statblock: inline
name: "Demonbane Warrior"
level: 5
source: "NPC Core"
aon_id: "creature-3632"
aon_url: "https://2e.aonprd.com/NPCs.aspx?ID=3632"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "NPC"
name: "Demonbane Warrior"
level: "Creature 5"
size: "Medium"
trait_01: "Elf"
trait_02: "Humanoid"
modifier: 13
perception:
  - name: "Perception"
    desc: "Perception +13; low-light vision"
languages: "[[srd/pf2e/compendium/rules-elements/languages#Chthonian|Chthonian]], [[srd/pf2e/compendium/rules-elements/languages#Common|Common]], [[srd/pf2e/compendium/rules-elements/languages#Elven|Elven]]"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/acrobatics|Acrobatics]] +13, [[srd/pf2e/compendium/rules-elements/skills/lore|Demon Lore]] +12, [[srd/pf2e/compendium/rules-elements/skills/religion|Religion]] +11, [[srd/pf2e/compendium/rules-elements/skills/stealth|Stealth]] +10, [[srd/pf2e/compendium/rules-elements/skills/survival|Survival]] +11"
abilityMods: [3, 4, 2, 1, 2, 0]
abilities_top:
  - name: "Sin Sense"
    desc: "A demonbane warrior automatically learns all weaknesses of a [[srd/pf2e/compendium/rules-elements/traits/player-core/demon|demon]] they've identified by [[srd/pf2e/compendium/rules-elements/actions/player-core#Recall Knowledge|Recalling Knowledge]]."
  - name: "Items"
    desc: "Chain Shirt, Composite Shortbow (20 arrows), cold iron elven branched spear"
ac: 22
armorclass:
  - name: "AC"
    desc: "22; __Fort__: +11; __Ref__: +13; __Will__: +11"
hp: 76
health:
  - name: "HP"
    desc: "76"
speed: "30 feet"
attacks:
  - name: "Melee"
    desc: "⬻ cold iron elven branched spear +15 ([[srd/pf2e/compendium/rules-elements/traits/player-core/deadly|deadly d8]], [[srd/pf2e/compendium/rules-elements/traits/player-core/finesse|Finesse]], [[srd/pf2e/compendium/rules-elements/traits/player-core/reach|Reach]]) __Damage__ 1d6+9 piercing"
  - name: "Melee"
    desc: "⬻ fist +15 ([[srd/pf2e/compendium/rules-elements/traits/player-core/agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/finesse|Finesse]], [[srd/pf2e/compendium/rules-elements/traits/player-core/nonlethal|Nonlethal]], [[srd/pf2e/compendium/rules-elements/traits/player-core/unarmed|Unarmed]]) __Damage__ 1d4+9 bludgeoning"
  - name: "Ranged"
    desc: "⬻ composite shortbow +15 ([[srd/pf2e/compendium/rules-elements/traits/player-core/deadly|deadly d10]], [[srd/pf2e/compendium/rules-elements/traits/player-core/propulsive|Propulsive]], range increment 60 feet, reload 0) __Damage__ 1d6+7 piercing"
abilities_bot:
  - name: "Demonbane"
    desc: "A demonbane warrior gains a +1 circumstance bonus to damage rolls against [[srd/pf2e/compendium/rules-elements/traits/player-core/demon|demons]]. If their actions force a demon to take damage from its sin vulnerability, increase the damage from the vulnerability by 2."
  - name: "Imbue Righteousness"
    desc: "⬻ ([[srd/pf2e/compendium/rules-elements/traits/player-core/divine|Divine]], [[srd/pf2e/compendium/rules-elements/traits/player-core/holy|Holy]]) The warrior imbues a weapon they wield with holy energy. Until the start of their next turn, their Strikes with that weapon gain the [[srd/pf2e/compendium/rules-elements/traits/player-core/holy|holy]] trait and deal an additional 1d6 spirit damage to [[srd/pf2e/compendium/rules-elements/traits/player-core/unholy|unholy]] creatures."
sourcebook: "_NPC Core_, page 179."
```

```encounter-table
name: Demonbane Warrior
creatures:
  - 1: Demonbane Warrior
```
