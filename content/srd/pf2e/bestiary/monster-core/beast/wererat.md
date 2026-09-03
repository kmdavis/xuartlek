---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Wererat"
tags:
  - pf2e/creature/level/2
  - pf2e/creature/trait/beast
  - pf2e/creature/trait/human
  - pf2e/creature/trait/humanoid
  - pf2e/creature/trait/werecreature
  - pf2e/creature/trait/medium
statblock: inline
name: "Wererat"
level: 2
source: "Monster Core"
aon_id: "creature-3235"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=3235"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC"
name: "Wererat"
level: "Creature 2"
size: "Medium"
trait_01: "Beast"
trait_02: "Human"
trait_03: "Humanoid"
trait_04: "Werecreature"
modifier: 8
perception:
  - name: "Perception"
    desc: "Perception +8; low-light vision, scent (imprecise) 30 feet"
languages: "[[srd/pf2e/compendium/rules-elements/languages#Common|Common]]; rat empathy"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/acrobatics|Acrobatics]] +8, [[srd/pf2e/compendium/rules-elements/skills/athletics|Athletics]] +6, [[srd/pf2e/compendium/rules-elements/skills/deception|Deception]] +5, [[srd/pf2e/compendium/rules-elements/skills/society|Society]] +4, [[srd/pf2e/compendium/rules-elements/skills/stealth|Stealth]] +8"
abilityMods: [2, 4, 2, 0, 2, 1]
abilities_top:
  - name: "Rat Empathy"
    desc: "The wererat can communicate with rodents."
  - name: "Items"
    desc: "Hand Crossbow (20 bolts), Leather Armor, Shortsword"
ac: 19
armorclass:
  - name: "AC"
    desc: "19; __Fort__: +6; __Ref__: +10; __Will__: +8"
hp: 45
health:
  - name: "HP"
    desc: "45; __Weaknesses__ silver 5"
abilities_mid:
  - name: "Nimble Dodge"
    desc: "⬲"
  - name: "Trigger"
    desc: "A creature targets the wererat with an attack and the wererat can see the attacker"
  - name: "Effect"
    desc: "The wererat gains a +2 circumstance bonus to AC against the triggering attack."
speed: "25 feet"
attacks:
  - name: "Melee"
    desc: "⬻ shortsword +10 ([[srd/pf2e/compendium/rules-elements/traits/player-core/agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/finesse|Finesse]], [[srd/pf2e/compendium/rules-elements/traits/player-core/versatile|versatile S]]) __Damage__ 1d6+4 piercing"
  - name: "Melee"
    desc: "⬻ claw +10 ([[srd/pf2e/compendium/rules-elements/traits/player-core/agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/finesse|Finesse]]) __Damage__ 1d6+2 slashing"
  - name: "Melee"
    desc: "⬻ jaws +10 ([[srd/pf2e/compendium/rules-elements/traits/player-core/finesse|Finesse]]) __Damage__ 1d8+2 piercing plus curse of the wererat"
  - name: "Ranged"
    desc: "⬻ hand crossbow +10 (range increment 60 feet, reload 1) __Damage__ 1d6 piercing"
abilities_bot:
  - name: "Change Shape"
    desc: "⬻ ([[srd/pf2e/compendium/rules-elements/traits/player-core/concentrate|Concentrate]], [[srd/pf2e/compendium/rules-elements/traits/player-core/polymorph|Polymorph]], [[srd/pf2e/compendium/rules-elements/traits/player-core/primal|Primal]]) Human with fist +10 for 1d4+2 bludgeoning, or Small rat with Speed 30 feet, climb 10 feet"
  - name: "Curse of the Wererat"
    desc: "([[srd/pf2e/compendium/rules-elements/traits/player-core/curse|Curse]], [[srd/pf2e/compendium/rules-elements/traits/player-core/primal|Primal]])"
  - name: "Saving Throw"
    desc: "DC 15 Fortitude"
  - name: "Moon Frenzy"
    desc: "([[srd/pf2e/compendium/rules-elements/traits/player-core/polymorph|Polymorph]], [[srd/pf2e/compendium/rules-elements/traits/player-core/primal|Primal]])"
  - name: "Sneak Attack"
    desc: "The wererat deals 1d6 extra precision damage to [[srd/pf2e/compendium/rules-elements/conditions#Off-Guard|off-guard]] creatures"
sourcebook: "_Monster Core_, page 345."
```

```encounter-table
name: Wererat
creatures:
  - 1: Wererat
```
