---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Jah-Tohl"
tags:
  - pf2e/creature/level/8
  - pf2e/creature/trait/aberration
  - pf2e/creature/trait/uncommon
  - pf2e/creature/trait/large
statblock: inline
name: "Jah-Tohl"
level: 8
source: "Monster Core"
aon_id: "creature-2930"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=2930"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC"
name: "Jah-Tohl"
level: "Creature 8"
size: "Large"
trait_01: "Aberration"
trait_02: "Uncommon"
modifier: 18
perception:
  - name: "Perception"
    desc: "Perception +18; darkvision, thoughtsense 60 feet"
languages: "Aklo, Chthonian, Draconic, Protean, Sakvroth; telepathy 100 feet"
skills:
  - name: "Skills"
    desc: "Acrobatics +17, Arcana +18, Athletics +16, Lore +18, Occultism +21, Stealth +17"
abilityMods: [6, 3, 5, 4, 4, 3]
abilities_top:
  - name: "Thoughtsense"
    desc: "The jah-tohl senses a creature's mental essence as a precise sense with the listed range; it cannot sense mindless creatures with thoughtsense."
ac: 26
armorclass:
  - name: "AC"
    desc: "26; __Fort__: +15; __Ref__: +13; __Will__: +18 +1 status on all saves vs. magic"
hp: 140
health:
  - name: "HP"
    desc: "140; __Immunities__ confused; __Weaknesses__ brain loss"
abilities_mid:
  - name: "Brain Blisters"
    desc: "A jah-tohl has seven brain blisters on its back that it uses to house stolen brains. A jah-tohl without all seven blisters full is stupefied with a value equal to the number of empty blisters."
  - name: "Brain Loss"
    desc: "If a jah-tohl takes 30 damage from a critical hit or 25 mental damage, it must succeed at a DC 26 save (Fortitude for critical damage or Will for mental damage) or one of its brain blisters is destroyed."
speed: "25 feet, fly 30 feet"
attacks:
  - name: "Melee"
    desc: "⬻ jaws +20 __Damage__ 2d12+6 piercing plus mind snatcher venom"
  - name: "Melee"
    desc: "⬻ claw +20 (Agile) __Damage__ 2d8+6 slashing"
abilities_bot:
  - name: "Mind Snatcher Venom"
    desc: "(Poison)"
  - name: "Saving Throw"
    desc: "DC 26 Fortitude"
  - name: "Maximum Duration"
    desc: "6 rounds"
  - name: "Stage 1"
    desc: "1d6 poison and enfeebled 1 (1 round)"
  - name: "Stage 2"
    desc: "1d6 poison, enfeebled 1, and slowed 1 (1 round)"
  - name: "Stage 3"
    desc: "2d6 poison, enfeebled 2, and slowed 1 (1 round)"
  - name: "Collect Brain"
    desc: "⬻ (Manipulate) The jahtohl extracts the brain of a creature within its reach that has been dead for no more than 1 minute. It can then use an Interact action to secure the brain in one of its empty brain blisters and heal 20 Hit Points."
spellcasting:
  - name: "Occult Spontaneous Spells"
    desc: "DC 26, attack +18 - __Cantrips (4th)__ Detect Magic, Figment, Light, Telekinetic Hand - __1st__ Enfeeble, Mindlink, Sure Strike (4 slots) - __2nd__ Humanoid Form, Invisibility, Paranoia (4 slots) - __3rd__ Dispel Magic, Haste, Paralyze (3 slots) - __4th__ Confusion, Vision of Death (2 slots)"
sourcebook: "_Monster Core_, page 106."
```

```encounter-table
name: Jah-Tohl
creatures:
  - 1: Jah-Tohl
```
