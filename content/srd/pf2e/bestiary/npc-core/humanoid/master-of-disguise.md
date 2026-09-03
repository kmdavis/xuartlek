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
    desc: "Perception +17; (21 to [[srd/pf2e/compendium/rules-elements/actions/player-core#Sense Motive|Sense Motive]])"
languages: "[[srd/pf2e/compendium/rules-elements/languages#Common|Common]], [[srd/pf2e/compendium/rules-elements/languages#Dwarven|Dwarven]], [[srd/pf2e/compendium/rules-elements/languages#Elven|Elven]], [[srd/pf2e/compendium/rules-elements/languages#Gnomish|Gnomish]], [[srd/pf2e/compendium/rules-elements/languages#Halfling|Halfling]]"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/deception|Deception]] +18, [[srd/pf2e/compendium/rules-elements/skills/diplomacy|Diplomacy]] +16, [[srd/pf2e/compendium/rules-elements/skills/performance|Performance]] +16, [[srd/pf2e/compendium/rules-elements/skills/society|Society]] +17, [[srd/pf2e/compendium/rules-elements/skills/stealth|Stealth]] +17, [[srd/pf2e/compendium/rules-elements/skills/thievery|Thievery]] +15, [[srd/pf2e/compendium/rules-elements/skills/lore|Underworld Lore]] +15"
abilityMods: [0, 4, 0, 2, 3, 5]
abilities_top:
  - name: "Deep Cover"
    desc: "At most times, a master of disguise has infiltrated a specific organization, gaining a +2 circumstance bonus to [[srd/pf2e/compendium/rules-elements/actions/player-core#Gather Information|Gather Information]], [[srd/pf2e/compendium/rules-elements/actions/player-core#Impersonate|Impersonate]], [[srd/pf2e/compendium/rules-elements/actions/player-core#Lie|Lie]], or [[srd/pf2e/compendium/rules-elements/actions/player-core#Request|Request]] when dealing with its members."
  - name: "Disguise Specialist"
    desc: "For social encounters involving impersonation, the master of disguise is a 10th-level challenge."
  - name: "Items"
    desc: "Dagger (5), elite disguise kit, [[srd/pf2e/compendium/equipment/worn-items/masquerade-scarf-greater|_masquerade scarf_]]"
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
    desc: "⬻ dagger +16 ([[srd/pf2e/compendium/rules-elements/traits/player-core/agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/finesse|Finesse]], [[srd/pf2e/compendium/rules-elements/traits/player-core/versatile|versatile S]]) __Damage__ 1d4+6 piercing"
  - name: "Melee"
    desc: "⬻ fist +16 ([[srd/pf2e/compendium/rules-elements/traits/player-core/agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/finesse|Finesse]], [[srd/pf2e/compendium/rules-elements/traits/player-core/nonlethal|Nonlethal]], [[srd/pf2e/compendium/rules-elements/traits/player-core/unarmed|Unarmed]]) __Damage__ 1d4+6 bludgeoning"
  - name: "Ranged"
    desc: "⬻ dagger +16 ([[srd/pf2e/compendium/rules-elements/traits/player-core/agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/thrown|thrown 10 feet]], [[srd/pf2e/compendium/rules-elements/traits/player-core/versatile|versatile S]]) __Damage__ 1d4+6 piercing"
abilities_bot:
  - name: "Double Take"
    desc: "If the master of disguise and the creature they're [[srd/pf2e/compendium/rules-elements/actions/player-core#Impersonate|Impersonating]] are in each others' presence, the genuine creature must [[srd/pf2e/compendium/rules-elements/actions/player-core#Lie|Lie]] if they're vouching for their own identity, and are treated as though they were Impersonating themself if someone [[srd/pf2e/compendium/rules-elements/actions/player-core#Seek|Seeks]] in an attempt to pierce their disguise. The genuine creature can use their [[srd/pf2e/compendium/rules-elements/skills/deception|Deception]] modifier, [[srd/pf2e/compendium/rules-elements/skills/diplomacy|Diplomacy]] modifier, or a +15 modifier, whichever is highest."
  - name: "Impeccable Disguise"
    desc: "⬽ The master of disguise creates a disguise and [[srd/pf2e/compendium/rules-elements/actions/player-core#Impersonate|Impersonates]]. They gain a +5 status bonus to [[srd/pf2e/compendium/rules-elements/skills/deception|Deception]] checks to Impersonate or to tell a [[srd/pf2e/compendium/rules-elements/actions/player-core#Lie|Lie]] that helps them maintain their disguise. When a spell or magical effect tries to read their mind, detect whether they're lying, or reveal their identity, they can attempt a Deception check against the spell or effect's DC. If they succeed, the effect reveals information appropriate to their cover identity or nothing (the GM determines which)."
  - name: "Shocking Reveal"
    desc: "⬻ ([[srd/pf2e/compendium/rules-elements/traits/player-core/manipulate|Manipulate]]) The master of disguise removes their disguise with a dramatic gesture. Any creatures that previously failed to see through the disguise is [[srd/pf2e/compendium/rules-elements/conditions#Off-Guard|off-guard]] to the master of disguise until the end of the turn."
  - name: "Sneak Attack"
    desc: "The master of disguise deals an additional 3d6 precision damage to [[srd/pf2e/compendium/rules-elements/conditions#Off-Guard|off-guard]] creatures. Know Your Enemy A master of disguise presents an opportunity for GMs to make past events relevant again. An NPC who was previously significant may well have been a master of disguise who is now revealing themself to the PCs years later, opening a web of connections the PCs never knew existed until now."
sourcebook: "_NPC Core_, page 22."
```

```encounter-table
name: Master Of Disguise
creatures:
  - 1: Master Of Disguise
```
