---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Sylph Sneak"
tags:
  - pf2e/creature/level/1
  - pf2e/creature/trait/human
  - pf2e/creature/trait/humanoid
  - pf2e/creature/trait/sylph
  - pf2e/creature/trait/medium
statblock: inline
name: "Sylph Sneak"
level: 1
source: "Monster Core 2"
aon_id: "creature-4510"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=4510"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC2"
name: "Sylph Sneak"
level: "Creature 1"
size: "Medium"
trait_01: "Human"
trait_02: "Humanoid"
trait_03: "Sylph"
modifier: 5
perception:
  - name: "Perception"
    desc: "Perception +5"
languages: "[[srd/pf2e/compendium/rules-elements/languages#Common|Common]], [[srd/pf2e/compendium/rules-elements/languages#Sussuran|Sussuran]]"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/acrobatics|Acrobatics]] +7, [[srd/pf2e/compendium/rules-elements/skills/deception|Deception]] +6, [[srd/pf2e/compendium/rules-elements/skills/diplomacy|Diplomacy]] +6, [[srd/pf2e/compendium/rules-elements/skills/society|Society]] +4, [[srd/pf2e/compendium/rules-elements/skills/stealth|Stealth]] +7, [[srd/pf2e/compendium/rules-elements/skills/thievery|Thievery]] +7"
abilityMods: [0, 4, 1, 1, 0, 3]
abilities_top:
  - name: "Items"
    desc: "Leather Armor, Starknife"
ac: 16
armorclass:
  - name: "AC"
    desc: "16; __Fort__: +4; __Ref__: +9; __Will__: +8"
hp: 17
health:
  - name: "HP"
    desc: "17"
abilities_mid:
  - name: "Deflecting Gale"
    desc: "⬲ ([[srd/pf2e/compendium/rules-elements/traits/player-core/air|air]], [[srd/pf2e/compendium/rules-elements/traits/player-core/primal|primal]])"
  - name: "Trigger"
    desc: "The sylph sneak is the target of a physical ranged attack"
  - name: "Requirements"
    desc: "The sylph sneak is aware of the attack"
  - name: "Effect"
    desc: "A swift gale whips up between the sylph sneak and the source of the ranged attack, giving the sneak a +3 status bonus to AC against the triggering attack. If the attack misses, the wind deflected it. The wind can't deflect unusually large or heavy ranged projectiles (such as boulders or ballista bolts)."
speed: "25 feet"
attacks:
  - name: "Melee"
    desc: "⬻ starknife +9 ([[srd/pf2e/compendium/rules-elements/traits/player-core/agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/deadly|deadly d6]], [[srd/pf2e/compendium/rules-elements/traits/player-core/finesse|Finesse]], [[srd/pf2e/compendium/rules-elements/traits/player-core/versatile|versatile S]]) __Damage__ 1d4+2 piercing"
  - name: "Ranged"
    desc: "⬻ starknife +9 ([[srd/pf2e/compendium/rules-elements/traits/player-core/agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/deadly|deadly d6]], [[srd/pf2e/compendium/rules-elements/traits/player-core/thrown|thrown 30 feet]], [[srd/pf2e/compendium/rules-elements/traits/player-core/versatile|versatile S]]) __Damage__ 1d4+2 piercing"
abilities_bot:
  - name: "Sneak Attack"
    desc: "The sylph sneak's Strikes deal an additional 1d6 precision damage to [[srd/pf2e/compendium/rules-elements/conditions#Off-Guard|off-guard]] creatures."
  - name: "Surprise Attacker"
    desc: "On the first round of combat, creatures that haven't acted yet are [[srd/pf2e/compendium/rules-elements/conditions#Off-Guard|off-guard]] to the sylph sneak."
  - name: "Wind's Guidance"
    desc: "When the sylph sneak attacks with a [[srd/pf2e/compendium/rules-elements/traits/player-core/thrown|thrown]] weapon, the range increment increases by 10 feet."
sourcebook: "_Monster Core 2_, page 252."
```

```encounter-table
name: Sylph Sneak
creatures:
  - 1: Sylph Sneak
```
