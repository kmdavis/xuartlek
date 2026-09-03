---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Sand Sentry"
tags:
  - pf2e/creature/level/6
  - pf2e/creature/trait/earth
  - pf2e/creature/trait/elemental
  - pf2e/creature/trait/medium
statblock: inline
name: "Sand Sentry"
level: 6
source: "Monster Core 2"
aon_id: "creature-4384"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=4384"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC2"
name: "Sand Sentry"
level: "Creature 6"
size: "Medium"
trait_01: "Earth"
trait_02: "Elemental"
modifier: 14
perception:
  - name: "Perception"
    desc: "Perception +14; darkvision, tremorsense (imprecise) 60 feet"
languages: "Petran"
skills:
  - name: "Skills"
    desc: "Acrobatics +14, Stealth +14"
abilityMods: [5, 2, 4, 0, 2, 1]
ac: 24
armorclass:
  - name: "AC"
    desc: "24; __Fort__: +16; __Ref__: +12; __Will__: +14"
hp: 90
health:
  - name: "HP"
    desc: "90; __Immunities__ bleed, paralyzed, poison, sleep"
abilities_mid:
  - name: "Glass Armor"
    desc: "When the sand sentry takes electricity or fire damage, its outer layer of sand fuses into sheets of hardened glass for 1 minute. This increases the sand sentry's AC to 26 and grants it resistance 5 to acid, cold, electricity, fire, force, piercing, and slashing damage. A sand sentry can't use earth glide while glass armor is active."
speed: "25 feet, burrow 50 feet; earth glide"
attacks:
  - name: "Melee"
    desc: "⬻ fist +17 __Damage__ 2d8+8 bludgeoning plus blinding sand"
abilities_bot:
  - name: "Earth Glide"
    desc: "A sand sentry can Burrow through earthen matter, including rock. When it does so, it moves at its full burrow Speed, leaving no tunnels or signs of its passing."
  - name: "Blinding Sand"
    desc: "When the sand sentry critically hits with a fist Strike, the target is blinded for 1 round. Sand Simulacra Sand sentries have no true culture or society of their own, but they're endlessly fascinated with the society and culture of humanoids they encounter. They can shape their appearance to mimic any similarly sized humanoids, and although they always remain obviously composed of sand, they do their best to copy the day-to-day activities they observe other humanoids performing. Of course, structures and objects sand sentries build from sand never last, but this never seems to stifle their obsession."
sourcebook: "_Monster Core 2_, page 146."
```

```encounter-table
name: Sand Sentry
creatures:
  - 1: Sand Sentry
```
