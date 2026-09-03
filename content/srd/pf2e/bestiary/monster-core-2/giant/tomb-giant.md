---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Tomb Giant"
tags:
  - pf2e/creature/level/12
  - pf2e/creature/trait/giant
  - pf2e/creature/trait/humanoid
  - pf2e/creature/trait/large
statblock: inline
name: "Tomb Giant"
level: 12
source: "Monster Core 2"
aon_id: "creature-4411"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=4411"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC2"
name: "Tomb Giant"
level: "Creature 12"
size: "Large"
trait_01: "Giant"
trait_02: "Humanoid"
modifier: 25
perception:
  - name: "Perception"
    desc: "Perception +25; darkvision, lifesense (imprecise) 60 feet"
languages: "Common, Jotun, Necril"
skills:
  - name: "Skills"
    desc: "Athletics +25, Medicine +25, Occultism +23, Religion +25, Stealth +21"
abilityMods: [7, 3, 6, 3, 7, 4]
abilities_top:
  - name: "Items"
    desc: "_+1 striking scythe_, black onyx gems worth 300 gp"
ac: 32
armorclass:
  - name: "AC"
    desc: "32; __Fort__: +22; __Ref__: +19; __Will__: +25"
hp: 255
health:
  - name: "HP"
    desc: "255 (void healing); __Immunities__ death effects"
speed: "30 feet"
attacks:
  - name: "Melee"
    desc: "⬻ scythe +27 (deadly d10, magical, reach 10 feet, trip) __Damage__ 2d10+13 slashing"
  - name: "Melee"
    desc: "⬻ claw +26 (Agile, reach 10 feet, unarmed) __Damage__ 3d6+13 slashing plus dooming touch"
  - name: "Ranged"
    desc: "⬻ rock +24 (Brutal, range increment 120 feet) __Damage__ 3d8+13 bludgeoning"
abilities_bot:
  - name: "Dooming Touch"
    desc: "(Divine, void) The tomb giant's claws carry the accursed power of their foul gods. A creature hit by the tomb giant's claw Strike becomes doomed 1."
  - name: "Font of Death"
    desc: "⬽ (Concentrate, unholy, void) The tomb giant turns the spiritual tide on a creature that has just died, temporarily transforming it into a volatile vessel powered by the Void. The tomb giant touches a creature that died within the past 24 hours, infusing its flesh and bone with void energy. Once during the next hour, the tomb giant can spend a single action (from any distance) to release this void from the corpse in an explosion that deals 10d8 void damage in a 15-foot burst (DC 32 basic Fortitude save); if not released before the end of the hour, the energy dissipates harmlessly. The tomb giant can't use Font of Death while a previous corpse remains infused."
spellcasting:
  - name: "Divine Innate Spells"
    desc: "DC 32 - __5th__ Bind Undead (×3), Harm (×3)"
  - name: "Rituals"
    desc: "DC 32 - __2nd__ Create Undead"
sourcebook: "_Monster Core 2_, page 164."
```

```encounter-table
name: Tomb Giant
creatures:
  - 1: Tomb Giant
```
