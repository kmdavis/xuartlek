---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Storm Snake"
tags:
  - pf2e/creature/level/5
  - pf2e/creature/trait/beast
  - pf2e/creature/trait/dragon
  - pf2e/creature/trait/electricity
  - pf2e/creature/trait/large
statblock: inline
name: "Storm Snake"
level: 5
source: "Howl of the Wild"
aon_id: "creature-3314"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=3314"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "HotW"
name: "Storm Snake"
level: "Creature 5"
size: "Large"
trait_01: "Beast"
trait_02: "Dragon"
trait_03: "Electricity"
modifier: 12
perception:
  - name: "Perception"
    desc: "Perception +12; low-light vision"
skills:
  - name: "Skills"
    desc: "Acrobatics +11, Stealth +10"
abilityMods: [3, 5, 2, -1, 3, 0]
ac: 21
armorclass:
  - name: "AC"
    desc: "21; __Fort__: +12; __Ref__: +15; __Will__: +9"
hp: 70
health:
  - name: "HP"
    desc: "70; __Resistances__ electricity 8"
abilities_mid:
  - name: "Static Shock"
    desc: "⬲"
  - name: "Trigger"
    desc: "A creature touches the storm snake or damages it with an unarmed melee attack or non-reach melee weapon"
  - name: "Effect"
    desc: "The triggering enemy is shocked for 2d8 electricity damage (DC 19 basic Fortitude save). On a failed save, the target is stunned 1."
speed: "30 feet, fly 30 feet"
attacks:
  - name: "Melee"
    desc: "⬻ tail +12 __Damage__ 2d4+5 slashing plus 1d4 electricity"
abilities_bot:
  - name: "Lightning Strike"
    desc: "⬻ The storm snake redirects the lightning it has absorbed from storms, dealing 2d10 electricity damage to a single target within 20 feet (DC 19 basic Reflex save). On a failure, the target is dazzled until the end of its next turn."
  - name: "Static Field"
    desc: "⬺ The storm snake gathers all static electricity in the area before releasing it in a 30-foot emanation that deals 3d12 electricity damage to all non-plant creatures (DC 19 Reflex save) and grants plant creatures 5 temporary Hit Points that last for 1 minute. Plant life in the area begins to grow significantly faster than the average for plants of their genus; in forests, fields, or otherwise floral locations, this immediately transforms the area into nonmagical difficult terrain. The storm snake can't use Static field again for 1d4 rounds."
sourcebook: "_Howl of the Wild_, page 185."
```

```encounter-table
name: Storm Snake
creatures:
  - 1: Storm Snake
```
