---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Caligni Caller"
tags:
  - pf2e/creature/level/6
  - pf2e/creature/trait/caligni
  - pf2e/creature/trait/humanoid
  - pf2e/creature/trait/medium
statblock: inline
name: "Caligni Caller"
level: 6
source: "Monster Core 2"
aon_id: "creature-4289"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=4289"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC2"
name: "Caligni Caller"
level: "Creature 6"
size: "Medium"
trait_01: "Caligni"
trait_02: "Humanoid"
modifier: 11
perception:
  - name: "Perception"
    desc: "Perception +11; greater darkvision, light blindness"
languages: "Caligni, Sakvroth"
skills:
  - name: "Skills"
    desc: "Arcana +9, Intimidation +14, Occultism +13, Stealth +15"
abilityMods: [2, 5, 1, 1, 1, 4]
abilities_top:
  - name: "Items"
    desc: "Dagger"
ac: 24
armorclass:
  - name: "AC"
    desc: "24; __Fort__: +9; __Ref__: +15; __Will__: +11"
hp: 80
health:
  - name: "HP"
    desc: "80"
abilities_mid:
  - name: "Death Umbra"
    desc: "(darkness) When the caller dies, an explosion of shadow devours their body. Each creature in a 10-foot emanation must attempt a DC 22 Fortitude save."
  - name: "Critical Success"
    desc: "The creature is unaffected."
  - name: "Success"
    desc: "The creature is enfeebled 1 for 1 minute."
  - name: "Failure"
    desc: "The creature is enfeebled 2 and slowed 1 for 1 minute."
speed: "25 feet"
attacks:
  - name: "Melee"
    desc: "⬻ dagger +15 (Agile, finesse, versatile S) __Damage__ 1d4+4 piercing plus 1d6 void"
abilities_bot:
  - name: "Sneak Attack"
    desc: "The caller's Strikes deal an additional 2d6 precision damage to off-guard creatures."
spellcasting:
  - name: "Occult Innate Spells"
    desc: "DC 24, attack +16 - __Cantrips (3rd)__ Detect Magic, Void Warp - __2nd__ Darkness (at will) - __3rd__ Chilling Darkness (×2), Grim Tendrils (×3) - __4th__ Darkness - __5th__ Umbral Journey"
  - name: "Rituals"
    desc: "DC 24 - __3rd__ Owb Pact"
sourcebook: "_Monster Core 2_, page 65."
```

```encounter-table
name: Caligni Caller
creatures:
  - 1: Caligni Caller
```
