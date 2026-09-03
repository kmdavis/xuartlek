---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Nosferatu Thrall"
tags:
  - pf2e/creature/level/8
  - pf2e/creature/trait/human
  - pf2e/creature/trait/humanoid
  - pf2e/creature/trait/uncommon
  - pf2e/creature/trait/unholy
  - pf2e/creature/trait/medium
statblock: inline
name: "Nosferatu Thrall"
level: 8
source: "Monster Core 2"
aon_id: "creature-4601"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=4601"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC2"
name: "Nosferatu Thrall"
level: "Creature 8"
size: "Medium"
trait_01: "Human"
trait_02: "Humanoid"
trait_03: "Uncommon"
trait_04: "Unholy"
modifier: 16
perception:
  - name: "Perception"
    desc: "Perception +16"
languages: "[[srd/pf2e/compendium/rules-elements/languages#Common|Common]]"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/acrobatics|Acrobatics]] +13, [[srd/pf2e/compendium/rules-elements/skills/athletics|Athletics]] +14, [[srd/pf2e/compendium/rules-elements/skills/deception|Deception]] +15, [[srd/pf2e/compendium/rules-elements/skills/religion|Religion]] +14"
abilityMods: [4, 3, 2, 2, 2, 1]
abilities_top:
  - name: "Items"
    desc: "_[[srd/pf2e/compendium/equipment/weapons/magic-weapon-3-major-striking|+1 striking]] [[srd/pf2e/compendium/equipment/weapons/club/greatclub|greatclub]]_"
ac: 26
armorclass:
  - name: "AC"
    desc: "26; __Fort__: +16; __Ref__: +17; __Will__: +14"
hp: 135
health:
  - name: "HP"
    desc: "135 (fast healing 5); __Weaknesses__ [[srd/pf2e/compendium/rules-elements/traits/player-core/mental|mental]] 10"
abilities_mid:
  - name: "Mindbound"
    desc: "([[srd/pf2e/compendium/rules-elements/traits/player-core/divine|divine]]) A nosferatu master exerts a fierce hold over their thrall's mind. If any creature other than the thrall's master targets them with an effect that would give them the [[srd/pf2e/compendium/rules-elements/conditions#Controlled|controlled]] condition, the thrall's master rolls a [[srd/pf2e/books/player-core/chapter-7-spells/counteracting|counteract]] check against it using their Dominate DC – 10 as the counteract check modifier."
  - name: "Mortal Shield"
    desc: "⬲"
  - name: "Trigger"
    desc: "The thrall's master would take damage from a Strike or spell attack and is in an adjacent square"
  - name: "Effect"
    desc: "The thrall throws themself in front of their master, taking half the damage of the attack (before applying any weaknesses or resistances). The thrall's master takes the remaining damage, applying any weaknesses or resistances as normal."
  - name: "Rally"
    desc: "⬲"
  - name: "Trigger"
    desc: "The thrall ends their turn more than 30 feet away from their master"
  - name: "Effect"
    desc: "The thrall [[srd/pf2e/compendium/rules-elements/actions/player-core#Stride|Strides]] up to their Speed toward their master."
speed: "25 feet"
attacks:
  - name: "Melee"
    desc: "⬻ _greatclub_ +19 ([[srd/pf2e/compendium/rules-elements/traits/player-core/backswing|Backswing]], [[srd/pf2e/compendium/rules-elements/traits/player-core/magical|magical]], [[srd/pf2e/compendium/rules-elements/traits/player-core/shove|shove]]) __Damage__ 2d10+10 bludgeoning"
  - name: "Melee"
    desc: "⬻ fist +18 ([[srd/pf2e/compendium/rules-elements/traits/player-core/agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/nonlethal|nonlethal]]) __Damage__ 2d6+10 bludgeoning"
abilities_bot:
  - name: "Swing Back"
    desc: "⬻"
  - name: "Frequency"
    desc: "once per round"
  - name: "Requirements"
    desc: "The nosferatu thrall's last action was a greatclub Strike that missed"
  - name: "Effect"
    desc: "The nosferatu thrall makes another greatclub Strike against the same target, using the previous Strike's multiple attack penalty."
sourcebook: "_Monster Core 2_, page 340."
```

```encounter-table
name: Nosferatu Thrall
creatures:
  - 1: Nosferatu Thrall
```
