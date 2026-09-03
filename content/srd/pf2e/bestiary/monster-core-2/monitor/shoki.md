---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Shoki"
tags:
  - pf2e/creature/level/9
  - pf2e/creature/trait/monitor
  - pf2e/creature/trait/psychopomp
  - pf2e/creature/trait/medium
statblock: inline
name: "Shoki"
level: 9
source: "Monster Core 2"
aon_id: "creature-4524"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=4524"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC2"
name: "Shoki"
level: "Creature 9"
size: "Medium"
trait_01: "Monitor"
trait_02: "Psychopomp"
modifier: 21
perception:
  - name: "Perception"
    desc: "Perception +21; darkvision, lifesense 60 feet"
languages: "Chthonian, Diabolic, Empyrean, Requian; _truespeech_"
skills:
  - name: "Skills"
    desc: "Boneyard Lore +19, Deception +20, Diplomacy +20, Intimidation +20, Occultism +16, Religion +19, Society +16, Stealth +14"
abilityMods: [4, 1, 4, 3, 6, 5]
abilities_top:
  - name: "Items"
    desc: "countless religious symbols, Staff"
ac: 27
armorclass:
  - name: "AC"
    desc: "27; __Fort__: +19; __Ref__: +14; __Will__: +21 +1 status to all saves vs. magic"
hp: 150
health:
  - name: "HP"
    desc: "150; __Immunities__ death effects, disease; __Resistances__ poison 10, void 10"
speed: "25 feet"
attacks:
  - name: "Melee"
    desc: "⬻ staff +19 (Magical, two-hand d8) __Damage__ 2d4+6 bludgeoning plus shepherd's touch"
abilities_bot:
  - name: "Infuse Staff"
    desc: "(Divine) A shoki's staff becomes a _+1 striking staff_ and is treated as if it were adamantine while the shoki wields it. A shoki's staff has Hardness 14 and HP 56 (BT 28) while possessed by the shoki and Hardness 5 and HP 20 (BT 10) while out of the shoki's possession. A shoki whose staff is taken or destroyed can infuse a new one with an hour of work."
  - name: "Soul Lock"
    desc: "⬺ (Divine, Incapacitation)"
  - name: "Requirements"
    desc: "The shoki doesn't have a soul locked within their staff"
  - name: "Effect"
    desc: "The shoki attempts to capture the soul of a creature on the brink of death: an undead creature, a creature with the dying condition, or a creature that died within the last minute. The target must attempt a DC 32 Will save with the following results."
  - name: "Critical Success"
    desc: "The creature is unaffected and becomes temporarily immune to Soul Lock."
  - name: "Success"
    desc: "The shoki's staff tugs at the creature's soul but doesn't trap it. If the creature is living, it becomes doomed 1 (or increases its doomed condition by 1). If the creature is a corporeal undead, it becomes enfeebled 2. If the creature is an incorporeal undead, it becomes stupefied 2. The creature then becomes temporarily immune to Soul Lock for 24 hours."
  - name: "Failure"
    desc: "The shoki captures the creature's soul in its staff. If the creature is living, it dies. If the creature is a corporeal undead, its body becomes an inanimate corpse. While the soul is locked in the staff, the target can't be returned to life or undeath or rejuvenate through any means, save for powerful magic, such a _wish_ ritual. If the shoki's staff is destroyed or the shoki wills it, the soul is released. A shoki's staff can only hold one soul at a time."
  - name: "Shepherd's Touch"
    desc: "A psychopomp's Strikes affect incorporeal creatures with the effects of a _ghost touch_ property rune and deal 2d6 void damage to living creatures and 2d6 vitality damage to undead. Tools Of The Trade Shokis utilize numerous tools to aid them in their work, including religious symbols, magic, soul-trapping staves, and false empathy—though shokis spout impassioned speeches and play upon mortal emotions, they hold no compassion for the dead."
spellcasting:
  - name: "Divine Innate Spells"
    desc: "DC 28, attack +20 - __Cantrips (5th)__ Detect Magic, Frostbite, Read Aura, Stabilize, Vitality Lash - __2nd__ Calm, Invisibility (at will; self only) - __4th__ Holy Light (×3), Read Omens - __5th__ Heal (×3), Mind Probe - __6th__ Spirit Blast - __7th__ Interplanar Teleport (self and locked soul only; to the Boneyard only) - __Constant (5th)__ Truespeech"
sourcebook: "_Monster Core 2_, page 264."
```

```encounter-table
name: Shoki
creatures:
  - 1: Shoki
```
