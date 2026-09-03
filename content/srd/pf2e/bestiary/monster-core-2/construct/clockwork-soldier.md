---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Clockwork Soldier"
tags:
  - pf2e/creature/level/6
  - pf2e/creature/trait/clockwork
  - pf2e/creature/trait/construct
  - pf2e/creature/trait/mindless
  - pf2e/creature/trait/uncommon
  - pf2e/creature/trait/medium
statblock: inline
name: "Clockwork Soldier"
level: 6
source: "Monster Core 2"
aon_id: "creature-4295"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=4295"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC2"
name: "Clockwork Soldier"
level: "Creature 6"
size: "Medium"
trait_01: "Clockwork"
trait_02: "Construct"
trait_03: "Mindless"
trait_04: "Uncommon"
modifier: 16
perception:
  - name: "Perception"
    desc: "Perception +16; darkvision"
skills:
  - name: "Skills"
    desc: "Athletics +15"
abilityMods: [6, 2, 4, -5, 4, -5]
abilities_top:
  - name: "Wind-Up"
    desc: "24 hours, DC 22, standby"
  - name: "Items"
    desc: "_+1 halberd_"
ac: 24
armorclass:
  - name: "AC"
    desc: "24; __Fort__: +16; __Ref__: +14; __Will__: +12 +2 vs. Disarm"
hp: 80
health:
  - name: "HP"
    desc: "80; __Immunities__ bleed, death effects, disease, doomed, drained, fatigued, healing, mental, nonlethal attacks, paralyzed, poison, sickened, spirit, unconscious, vitality, void; __Resistances__ physical 5 (except adamantine or orichalcum); __Weaknesses__ electricity 5, orichalcum 5"
abilities_mid:
  - name: "Reactive Strike"
    desc: "⬲"
speed: "25 feet"
attacks:
  - name: "Melee"
    desc: "⬻ halberd +17 (Magical, reach 10 feet, versatile S) __Damage__ 1d10+10 piercing"
  - name: "Melee"
    desc: "⬻ fist +16 (Agile) __Damage__ 1d8+10 bludgeoning plus Grab"
abilities_bot:
  - name: "Activate Defenses"
    desc: "⬻ One of the soldier's external plates extends on a mechanical actuator to defend the soldier or an adjacent creature of the soldier's choice. The creature gains a +2 circumstance bonus to AC until the start of the soldier's next turn or until it is no longer adjacent to the soldier, whichever comes first. The soldier can have no more than one plate extended at a time."
sourcebook: "_Monster Core 2_, page 71."
```

```encounter-table
name: Clockwork Soldier
creatures:
  - 1: Clockwork Soldier
```
