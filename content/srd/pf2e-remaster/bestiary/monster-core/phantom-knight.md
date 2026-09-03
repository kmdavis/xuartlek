---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Phantom Knight"
tags:
  - pf2e/creature/level/4
  - pf2e/creature/trait/ethereal
  - pf2e/creature/trait/incorporeal
  - pf2e/creature/trait/phantom
  - pf2e/creature/trait/spirit
  - pf2e/creature/trait/uncommon
  - pf2e/creature/trait/medium
statblock: inline
name: "Phantom Knight"
level: 4
source: "Monster Core"
aon_id: "creature-3135"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=3135"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC"
name: "Phantom Knight"
level: "Creature 4"
size: "Medium"
trait_01: "Ethereal"
trait_02: "Incorporeal"
trait_03: "Phantom"
trait_04: "Spirit"
trait_05: "Uncommon"
modifier: 13
perception:
  - name: "Perception"
    desc: "Perception +13; darkvision"
languages: "Common"
skills:
  - name: "Skills"
    desc: "Intimidation +12"
abilityMods: [-5, 4, 0, 0, 5, 4]
abilities_top:
  - name: "Walk the Ethereal Line"
    desc: "⬺ The phantom walks the thin line between the Ethereal Plane and the Universe in order to exist on both planes simultaneously. They can shift back to solely the Ethereal Plane by using this ability again."
ac: 21
armorclass:
  - name: "AC"
    desc: "21; __Fort__: +8; __Ref__: +12; __Will__: +13 –1 status penalty to all saves vs. death effects"
hp: 45
health:
  - name: "HP"
    desc: "45; __Immunities__ bleed, disease, paralyzed, poison, precision; __Resistances__ all damage 3 (except force, _ghost touch_, or spirit; double resistance vs. non-magical)"
abilities_mid:
  - name: "Susceptible to Death"
    desc: "Though phantoms aren't alive, neither are they undead, and they are uniquely vulnerable to the effects of death. A phantom whose Hit Points are reduced to 0 as a result of a death effect (such as from a spell like _execute_) is immediately whisked away to the River of Souls, where their soul resumes the usual path to the afterlife."
speed: "fly 25 feet"
attacks:
  - name: "Melee"
    desc: "⬻ phantom sword +14 (Finesse, Magical, versatile P) __Damage__ 1d8+7 slashing"
  - name: "Ranged"
    desc: "⬻ phantom bow +14 (deadly d10, Magical, range increment 120 feet, volley 30 feet) __Damage__ 1d8+5 piercing"
abilities_bot:
  - name: "Phantom Touch"
    desc: "(Spirit) Each time they make a Strike, a phantom can choose to deal spirit damage instead of the normal physical damage type."
sourcebook: "_Monster Core_, page 262."
```

```encounter-table
name: Phantom Knight
creatures:
  - 1: Phantom Knight
```
