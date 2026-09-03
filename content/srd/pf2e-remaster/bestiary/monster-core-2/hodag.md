---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Hodag"
tags:
  - pf2e/creature/level/6
  - pf2e/creature/trait/beast
  - pf2e/creature/trait/uncommon
  - pf2e/creature/trait/large
statblock: inline
name: "Hodag"
level: 6
source: "Monster Core 2"
aon_id: "creature-4440"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=4440"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC2"
name: "Hodag"
level: "Creature 6"
size: "Large"
trait_01: "Beast"
trait_02: "Uncommon"
modifier: 14
perception:
  - name: "Perception"
    desc: "Perception +14; darkvision, scent (imprecise) 30 feet"
languages: "Common; (can't speak any language)"
skills:
  - name: "Skills"
    desc: "Athletics +13, Stealth +14, Survival +12"
abilityMods: [5, 4, 5, -2, 4, 0]
abilities_top:
  - name: "Trackless"
    desc: "A hodag sweeps the ground behind it with its tail as it moves, obscuring its tracks. The DCs of checks to Track a hodag are increased by 10."
ac: 24
armorclass:
  - name: "AC"
    desc: "24; __Fort__: +17; __Ref__: +14; __Will__: +12"
hp: 90
health:
  - name: "HP"
    desc: "90"
abilities_mid:
  - name: "Ferocity"
    desc: "⬲"
speed: "25 feet, burrow 15 feet"
attacks:
  - name: "Melee"
    desc: "⬻ jaws +17 __Damage__ 2d8+8 piercing"
  - name: "Melee"
    desc: "⬻ claw +17 (Agile) __Damage__ 2d6+8 slashing"
  - name: "Melee"
    desc: "⬻ spiked tail +17 (reach 10 feet, versatile P) __Damage__ 2d6+8 bludgeoning plus Knockdown"
abilities_bot:
  - name: "Rip and Tear"
    desc: "⬺ The hodag makes two claw Strikes and one jaws Strike in any order."
  - name: "Toss"
    desc: "⬺ The hodag Strides, then makes a Strike against a target in reach. If it moves at least 20 feet and succeeds at its Strike, the hodag deals damage normally and then attempts an Athletics check against the creature's Fortitude DC to toss the enemy into the air. On a success, the tossed creature is thrown 10 feet in a straight line in the direction of the hodag's choice and then lands prone. If the creature is knocked into a solid object, it takes 1d6 bludgeoning damage before landing prone. The hodag can instead toss a creature straight up in the air. The creature lands in the same square where it started, takes 1d6 bludgeoning damage, and falls prone. Hodag Tales Those who've encountered hodags tend to create larger-than-life reports of the sighting. In the dense Verduran Forest, lumberjacks working for the Lumber Consortium regale each other with competing stories about Big Marna, a legendary hodag who the loggers claim has killed two dozen people. Inhabitants of Echo Wood in the River Kingdoms spin lore about Black Shiv, a hodag spotted haunting the outskirts of small settlements, and hunters and miners in the southwestern reaches of Ravounel speak of a frightening undead hodag called Ghouliegut."
sourcebook: "_Monster Core 2_, page 192."
```

```encounter-table
name: Hodag
creatures:
  - 1: Hodag
```
