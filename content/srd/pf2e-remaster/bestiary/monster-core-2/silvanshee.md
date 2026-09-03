---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Silvanshee"
tags:
  - pf2e/creature/level/1
  - pf2e/creature/trait/agathion
  - pf2e/creature/trait/celestial
  - pf2e/creature/trait/holy
  - pf2e/creature/trait/tiny
statblock: inline
name: "Silvanshee"
level: 1
source: "Monster Core 2"
aon_id: "creature-4018"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=4018"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC2"
name: "Silvanshee"
level: "Creature 1"
size: "Tiny"
trait_01: "Agathion"
trait_02: "Celestial"
trait_03: "Holy"
modifier: 8
perception:
  - name: "Perception"
    desc: "Perception +8; darkvision"
languages: "Common, Diabolic, Draconic, Empyrean; _speak with animals_"
skills:
  - name: "Skills"
    desc: "Acrobatics +7, Arcana +3, Medicine +6, Nirvana Lore +3, Stealth +7"
abilityMods: [-2, 4, 2, 0, 3, 2]
abilities_top:
  - name: "Cat's Curiosity"
    desc: "A silvanshee's core value is curiosity. This enables them to seek out new experiences and information beyond their current understanding. A silvanshee can use trained skill actions for all skills, even if they're untrained."
ac: 16
armorclass:
  - name: "AC"
    desc: "16; __Fort__: +5; __Ref__: +9; __Will__: +6"
hp: 20
health:
  - name: "HP"
    desc: "20; __Weaknesses__ unholy 3"
speed: "25 feet, fly 40 feet"
attacks:
  - name: "Melee"
    desc: "⬻ jaws +9 (Finesse, Holy, Magical) __Damage__ 1d6–2 piercing plus 1d4 spirit"
  - name: "Melee"
    desc: "⬻ claw +9 (Agile, Finesse, Holy, Magical) __Damage__ 1d4–2 slashing plus 1d4 spirit"
abilities_bot:
  - name: "Champion Focus Spell"
    desc: "DC 17, 1 Focus Point - __1st__ Lay on Hands"
  - name: "Cat's Poise"
    desc: "When a silvanshee uses their _vapor form_ spell, the mist form remains roughly the size and shape of a cat, and the silvanshee retains their fly Speed in this form. Silvanshee Allies Silvanshees will work with heroes who remain patient with their curiosity and skittishness. They're inquisitive, alternating between affection and aloofness. They do what they can to aid and defend their companions, but their strong sense of self-preservation means they'll likely flee if they sense they can't win a fight."
spellcasting:
  - name: "Divine Innate Spells"
    desc: "DC 17 - __Cantrips (1st)__ Know the Way, Light, Prestidigitation, Stabilize - __4th__ Read Omens, Vapor Form (×3) - __Constant (2nd)__ Speak with Animals"
sourcebook: "_Monster Core 2_, page 16."
```

```encounter-table
name: Silvanshee
creatures:
  - 1: Silvanshee
```
