---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Hobgoblin Spellbreaker"
tags:
  - pf2e/creature/level/3
  - pf2e/creature/trait/hobgoblin
  - pf2e/creature/trait/humanoid
  - pf2e/creature/trait/medium
statblock: inline
name: "Hobgoblin Spellbreaker"
level: 3
source: "NPC Core"
aon_id: "creature-3648"
aon_url: "https://2e.aonprd.com/NPCs.aspx?ID=3648"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "NPC"
name: "Hobgoblin Spellbreaker"
level: "Creature 3"
size: "Medium"
trait_01: "Hobgoblin"
trait_02: "Humanoid"
modifier: 9
perception:
  - name: "Perception"
    desc: "Perception +9; darkvision, arcane magic sense (imprecise) 60 feet"
languages: "Common, Goblin"
skills:
  - name: "Skills"
    desc: "Acrobatics +9, Arcana +10, Athletics +10, Intimidation +9, Stealth +9"
abilityMods: [3, 1, 1, 3, 1, 1]
abilities_top:
  - name: "Arcane Magic Sense"
    desc: "The hobgoblin spellbreaker can detect the source of any arcane magic within range as an imprecise sense."
  - name: "Items"
    desc: "Breaching Pike, Crossbow (10 bolts), Scale Mail, Shortsword"
ac: 18
armorclass:
  - name: "AC"
    desc: "18; __Fort__: +12; __Ref__: +6; __Will__: +9"
hp: 50
health:
  - name: "HP"
    desc: "50"
abilities_mid:
  - name: "Spellbreaking Reactive Strike"
    desc: "⬲ As Reactive Strike, but if it was triggered by a creature casting an arcane spell, the target must succeed at a DC 11 flat check or the spell is disrupted. If the Strike was a critical hit, the spell is disrupted automatically."
speed: "25 feet"
attacks:
  - name: "Melee"
    desc: "⬻ breaching pike +12 (Razing, Reach) __Damage__ 1d6+6 piercing"
  - name: "Melee"
    desc: "⬻ shortsword +12 (Agile, versatile S) __Damage__ 1d6+6 piercing"
  - name: "Melee"
    desc: "⬻ fist +12 (Agile, Nonlethal, Unarmed) __Damage__ 1d4+6 bludgeoning"
  - name: "Ranged"
    desc: "⬻ crossbow +10 (range increment 120 feet, reload 1) __Damage__ 1d8+3 piercing"
abilities_bot:
  - name: "Shatter Spell"
    desc: "⬺ The hobgoblin spellbreaker attempts a melee Strike against a creature under the effects of a beneficial arcane spell. If the Strike hits and deals damage, the hobgoblin spellbreaker can attempt to counteract a single arcane spell or arcane magical effect on the target (counteract rank 2, counteract modifier +10). If it fails, the hobgoblin spellbreaker can't attempt to counteract the same effect for 1 hour."
sourcebook: "_NPC Core_, page 194."
```

```encounter-table
name: Hobgoblin Spellbreaker
creatures:
  - 1: Hobgoblin Spellbreaker
```
