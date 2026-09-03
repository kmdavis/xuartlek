---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Grioth Cultist"
tags:
  - pf2e/creature/level/3
  - pf2e/creature/trait/grioth
  - pf2e/creature/trait/humanoid
  - pf2e/creature/trait/rare
  - pf2e/creature/trait/medium
statblock: inline
name: "Grioth Cultist"
level: 3
source: "Monster Core 2"
aon_id: "creature-4426"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=4426"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC2"
name: "Grioth Cultist"
level: "Creature 3"
size: "Medium"
trait_01: "Grioth"
trait_02: "Humanoid"
trait_03: "Rare"
modifier: 10
perception:
  - name: "Perception"
    desc: "Perception +10; greater darkvision, echolocation (precise) 20 feet"
languages: "Aklo, Grioth; telepathy 30 feet"
skills:
  - name: "Skills"
    desc: "Acrobatics +8, Occultism +9, Religion +10, Stealth +10"
abilityMods: [0, 3, 2, 2, 3, 0]
abilities_top:
  - name: "Echolocation"
    desc: "A grioth can use their hearing as a precise sense at the listed range."
  - name: "Items"
    desc: "voidglass kukri"
ac: 18
armorclass:
  - name: "AC"
    desc: "18; __Fort__: +7; __Ref__: +10; __Will__: +10"
hp: 40
health:
  - name: "HP"
    desc: "40; __Immunities__ cold; __Weaknesses__ fire 5"
abilities_mid:
  - name: "Light Blindness"
    desc: ""
  - name: "No Breath"
    desc: "A grioth doesn't breathe except to speak and is immune to effects that require breathing (such as an inhaled poison)."
speed: "25 feet, fly 30 feet"
attacks:
  - name: "Melee"
    desc: "⬻ kukri +10 (Agile, finesse, trip) __Damage__ 1d6+2 slashing"
  - name: "Melee"
    desc: "⬻ jaws +10 (Agile, finesse) __Damage__ 1d8+2 piercing plus grioth venom"
abilities_bot:
  - name: "Grioth Venom"
    desc: "(Emotion, fear, mental, poison)"
  - name: "Saving Throw"
    desc: "DC 20 Fortitude"
  - name: "Maximum Duration"
    desc: "6 rounds"
  - name: "Stage 1"
    desc: "frightened 1 (1 round)"
  - name: "Stage 2"
    desc: "frightened 2 (1 round)"
  - name: "Stage 3"
    desc: "frightened 3 (1 round)"
  - name: "Invoke Haunter of the Dark"
    desc: "⬺ (Divine, mental, visual)"
  - name: "Frequency"
    desc: "once per day"
  - name: "Effect"
    desc: "The grioth cultist waves a hand in a complex pattern to invoke dark powers, dealing 3d8 mental damage. Each nongrioth creature within 20 feet must attempt a DC 20 Will save."
  - name: "Critical Success"
    desc: "The creature is unaffected."
  - name: "Success"
    desc: "The creature takes half damage"
  - name: "Failure"
    desc: "The creature takes full damage and becomes stupefied 1 for 1 round"
  - name: "Critical Failure"
    desc: "The creature takes double damage and becomes stupefied 1 for 1 minute."
  - name: "Shock Mind"
    desc: "⬺ (Mental, occult) The grioth scout makes a Strike with a voidglass weapon. If the Strike hits, it deals an additional 2d6 mental damage, and the target must succeed at a DC 20 Will save (this has the incapacitation trait) or become confused for 1 round."
spellcasting:
  - name: "Divine Prepared Spells"
    desc: "DC 20, attack +12 - __Cantrips (3rd)__ Divine Lance, Forbidding Ward, Message, Prestidigitation, Stabilize - __1st__ Fear, Harm, Heal, Ventriloquism - __2nd__ Dispel Magic, Heal, Noise Blast"
  - name: "Occult Innate Spells"
    desc: "DC 19, attack +11 - __Cantrips (2nd)__ Daze, Detect Magic, Telekinetic Hand, Telekinetic Projectile - __2nd__ Phantom Pain"
sourcebook: "_Monster Core 2_, page 179."
```

```encounter-table
name: Grioth Cultist
creatures:
  - 1: Grioth Cultist
```
