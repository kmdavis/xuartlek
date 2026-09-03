---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Graveknight"
tags:
  - pf2e/creature/level/10
  - pf2e/creature/trait/graveknight
  - pf2e/creature/trait/undead
  - pf2e/creature/trait/unholy
  - pf2e/creature/trait/medium
statblock: inline
name: "Graveknight"
level: 10
source: "Monster Core"
aon_id: "creature-3030"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=3030"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC"
name: "Graveknight"
level: "Creature 10"
size: "Medium"
trait_01: "Graveknight"
trait_02: "Undead"
trait_03: "Unholy"
modifier: 19
perception:
  - name: "Perception"
    desc: "Perception +19; darkvision"
languages: "Common, Necril"
skills:
  - name: "Skills"
    desc: "Athletics +23, Intimidation +22, Religion +19, Warfare Lore +20"
abilityMods: [7, 4, 4, 2, 3, 5]
abilities_top:
  - name: "Items"
    desc: "Composite Longbow (20 arrows), _+1 resilient full plate_, Greatsword"
ac: 31
armorclass:
  - name: "AC"
    desc: "31; __Fort__: +21; __Ref__: +19; __Will__: +18"
hp: 175
health:
  - name: "HP"
    desc: "175 (rejuvenation, void healing (page 360)); __Immunities__ bleed, cold, death effects, disease, paralyzed, poison, unconscious"
abilities_mid:
  - name: "Sacrilegious Aura"
    desc: "30 feet. Counteract modifier +17"
  - name: "Reactive Strike"
    desc: "⬲"
speed: "25 feet"
attacks:
  - name: "Melee"
    desc: "⬻ _frost greatsword_ +24 (Cold, Magical, versatile P) __Damage__ 2d12+10 slashing plus 1d6 cold"
  - name: "Melee"
    desc: "⬻ frost fist +24 (Agile, Cold, Magical) __Damage__ 2d6+10 bludgeoning plus 1d6 cold"
  - name: "Ranged"
    desc: "⬻ _frost composite longbow_ +21 (Cold, deadly d10, Magical, range increment 100 feet, Propulsive, reload 0, volley 30 feet) __Damage__ 2d8+6 piercing plus 1d6 cold"
abilities_bot:
  - name: "Devastating Blast"
    desc: "⬺ (Arcane, Cold) 11d6 cold, DC 29"
  - name: "Graveknight's Curse"
    desc: "DC 33"
  - name: "Phantom Mount"
    desc: "⬽ (Arcane) HP 58; AC 27; Fort +17, Ref +15, Will +14"
  - name: "Weapon Master"
    desc: ""
sourcebook: "_Monster Core_, page 179."
```

```encounter-table
name: Graveknight
creatures:
  - 1: Graveknight
```
