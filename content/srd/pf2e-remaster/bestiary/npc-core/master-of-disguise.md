---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Master Of Disguise"
tags:
  - pf2e/creature/level/7
  - pf2e/creature/trait/human
  - pf2e/creature/trait/humanoid
  - pf2e/creature/trait/medium
statblock: inline
name: "Master Of Disguise"
level: 7
source: "NPC Core"
aon_id: "creature-3433"
aon_url: "https://2e.aonprd.com/NPCs.aspx?ID=3433"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "NPC"
name: "Master Of Disguise"
level: "Creature 7"
size: "Medium"
trait_01: "Human"
trait_02: "Humanoid"
modifier: 17
perception:
  - name: "Perception"
    desc: "Perception +17; (21 to Sense Motive)"
languages: "Common, Dwarven, Elven, Gnomish, Halfling"
skills:
  - name: "Skills"
    desc: "Deception +18, Diplomacy +16, Performance +16, Society +17, Stealth +17, Thievery +15, Underworld Lore +15"
abilityMods: [0, 4, 0, 2, 3, 5]
abilities_top:
  - name: "Deep Cover"
    desc: "At most times, a master of disguise has infiltrated a specific organization, gaining a +2 circumstance bonus to Gather Information, Impersonate, Lie, or Request when dealing with its members."
  - name: "Disguise Specialist"
    desc: "For social encounters involving impersonation, the master of disguise is a 10th-level challenge."
  - name: "Items"
    desc: "Dagger (5), elite disguise kit, _masquerade scarf_"
ac: 25
armorclass:
  - name: "AC"
    desc: "25; __Fort__: +11; __Ref__: +17; __Will__: +16"
hp: 110
health:
  - name: "HP"
    desc: "110"
speed: "25 feet"
attacks:
  - name: "Melee"
    desc: "⬻ dagger +16 (Agile, Finesse, versatile S) __Damage__ 1d4+6 piercing"
  - name: "Melee"
    desc: "⬻ fist +16 (Agile, Finesse, Nonlethal, Unarmed) __Damage__ 1d4+6 bludgeoning"
  - name: "Ranged"
    desc: "⬻ dagger +16 (Agile, thrown 10 feet, versatile S) __Damage__ 1d4+6 piercing"
abilities_bot:
  - name: "Double Take"
    desc: "If the master of disguise and the creature they're Impersonating are in each others' presence, the genuine creature must Lie if they're vouching for their own identity, and are treated as though they were Impersonating themself if someone Seeks in an attempt to pierce their disguise. The genuine creature can use their Deception modifier, Diplomacy modifier, or a +15 modifier, whichever is highest."
  - name: "Impeccable Disguise"
    desc: "⬽ The master of disguise creates a disguise and Impersonates. They gain a +5 status bonus to Deception checks to Impersonate or to tell a Lie that helps them maintain their disguise. When a spell or magical effect tries to read their mind, detect whether they're lying, or reveal their identity, they can attempt a Deception check against the spell or effect's DC. If they succeed, the effect reveals information appropriate to their cover identity or nothing (the GM determines which)."
  - name: "Shocking Reveal"
    desc: "⬻ (Manipulate) The master of disguise removes their disguise with a dramatic gesture. Any creatures that previously failed to see through the disguise is off-guard to the master of disguise until the end of the turn."
  - name: "Sneak Attack"
    desc: "The master of disguise deals an additional 3d6 precision damage to off-guard creatures. Know Your Enemy A master of disguise presents an opportunity for GMs to make past events relevant again. An NPC who was previously significant may well have been a master of disguise who is now revealing themself to the PCs years later, opening a web of connections the PCs never knew existed until now."
sourcebook: "_NPC Core_, page 22."
```

```encounter-table
name: Master Of Disguise
creatures:
  - 1: Master Of Disguise
```
