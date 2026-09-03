---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Virtuosic Lyrebird"
tags:
  - pf2e/creature/level/6
  - pf2e/creature/trait/beast
  - pf2e/creature/trait/tiny
statblock: inline
name: "Virtuosic Lyrebird"
level: 6
source: "Howl of the Wild"
aon_id: "creature-3322"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=3322"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "HotW"
name: "Virtuosic Lyrebird"
level: "Creature 6"
size: "Tiny"
trait_01: "Beast"
modifier: 14
perception:
  - name: "Perception"
    desc: "Perception +14"
skills:
  - name: "Skills"
    desc: "Acrobatics +15, Arcana +14, Performance +16, Stealth +12"
abilityMods: [4, 5, 2, 3, 2, 4]
ac: 24
armorclass:
  - name: "AC"
    desc: "24; __Fort__: +9; __Ref__: +17; __Will__: +14"
hp: 65
health:
  - name: "HP"
    desc: "65"
abilities_mid:
  - name: "Counter-Melody"
    desc: "⬲ (auditory, magic)"
  - name: "Trigger"
    desc: "An opponent within 60 feet Casts a Spell"
  - name: "Effect"
    desc: "The virtuosic lyrebird makes a counteract check against the triggering spell (+14 counteract modifier)."
speed: "15 feet, fly 60 feet"
attacks:
  - name: "Melee"
    desc: "⬻ beak +12 (Finesse) __Damage__ 2d8+4 piercing"
  - name: "Melee"
    desc: "⬻ talon +12 (Agile, Finesse) __Damage__ 2d6+4 piercing"
abilities_bot:
  - name: "Arcane Harmony"
    desc: "⬻ (Arcane, Auditory)"
  - name: "Effect"
    desc: "The virtuosic lyrebird sings a subtle trill that others can use to embellish their magic. The next virtuosic lyrebird to Cast a Spell within 60 feet of the first lyrebird that used Arcane Harmony chooses one of the following two benefits, after which the Arcane Harmony ends. The spell gains a +2 status bonus to damage per spell rank.One target of the spell takes a –2 status penalty to saves against the spell."
  - name: "Spell Mimicry"
    desc: "⭓"
  - name: "Frequency"
    desc: "once per day"
  - name: "Requirements"
    desc: "A creature Casts a Spell of 3rd rank or lower since the end of the virtuosic lyrebird' s last turn, and the virtuosic lyrebird heard the incantation for the spell"
  - name: "Effect"
    desc: "The virtuosic lyrebird learns the spell enough to mimic and cast it this turn, using as many actions as the original spell took."
  - name: "Spellsong Casting"
    desc: "The virtuosic lyrebird's exquisite vocal control lets it cast spells purely through its song. While it must be able to vocalize to Cast a Spell, it doesn't need to gesture, removing the manipulate trait from any spell that it casts. If it Casts a Spell with the linguistic trait (usually with its Spell Mimicry), it can Cast that Spell in Common, even though the bird doesn't truly understand the language."
spellcasting:
  - name: "Arcane Spontaneous Spells"
    desc: "DC 24, attack +16 - __Cantrips (3rd)__ Bullhorn, Daze, Figment, Ignition, Telekinetic Projectile - __1st__ Command, Fear, Gust of Wind - __2nd__ Breathe Fire, Shatter - __3rd__ Force Barrage, Hypnotize"
sourcebook: "_Howl of the Wild_, page 193."
```

```encounter-table
name: Virtuosic Lyrebird
creatures:
  - 1: Virtuosic Lyrebird
```
