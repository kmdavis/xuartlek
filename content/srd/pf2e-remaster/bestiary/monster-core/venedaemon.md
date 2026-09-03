---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Venedaemon"
tags:
  - pf2e/creature/level/5
  - pf2e/creature/trait/daemon
  - pf2e/creature/trait/fiend
  - pf2e/creature/trait/unholy
  - pf2e/creature/trait/medium
statblock: inline
name: "Venedaemon"
level: 5
source: "Monster Core"
aon_id: "creature-2892"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=2892"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC"
name: "Venedaemon"
level: "Creature 5"
size: "Medium"
trait_01: "Daemon"
trait_02: "Fiend"
trait_03: "Unholy"
modifier: 12
perception:
  - name: "Perception"
    desc: "Perception +12; darkvision, smell magic (imprecise) 60 feet"
languages: "Aklo, Chthonian, Common, Daemonic, Diabolic, Draconic, Requian; telepathy 100 feet"
skills:
  - name: "Skills"
    desc: "Acrobatics +13, Arcana +16, Deception +12, Occultism +14, Religion +13, Scribing Lore +14"
abilityMods: [2, 4, 2, 5, 3, 3]
abilities_top:
  - name: "Smell Magic"
    desc: "A venedaemon is aware of magical items and active spells as an imprecise sense. The subtle differences in these scents reveal the tradition and traits of the magic."
ac: 21
armorclass:
  - name: "AC"
    desc: "21; __Fort__: +9; __Ref__: +11; __Will__: +14 +1 status to all saves vs. magic"
hp: 75
health:
  - name: "HP"
    desc: "75; __Immunities__ death effects; __Weaknesses__ holy 5"
speed: "25 feet"
attacks:
  - name: "Melee"
    desc: "⬻ tentacle +13 (Agile, Finesse, Magical, reach 10 feet, Unholy) __Damage__ 2d6+5 bludgeoning"
abilities_bot:
  - name: "Residual Force"
    desc: "⬻ (Arcane, Force)"
  - name: "Requirements"
    desc: "The venedaemon's most recent action was to cast a spell"
  - name: "Effect"
    desc: "Fading runes cling to the venedaemon's tentacles. The venedaemon makes a tentacle Strike that has a reach of 20 feet and deals 2d4 additional force damage."
  - name: "Soul Spell"
    desc: "If a venedaemon ingest a soul gem from a cacodaemon, they can recover an expended spell slot instead of gaining fast healing. The spell slot's rank can be no higher than half the level of the creature whose soul was consumed, rounded up."
  - name: "Twisted Whispers"
    desc: "⬻ (Arcane, Auditory, Concentrate, Linguistic, Mental) The venedaemon whispers to a creature within 15 feet, which must succeed at a DC 22 Will save or be stupefied 2 for 1 minute (or stupefied 3 on a critical failure). Regardless of the results of the save, the creature is immune to Twisted Whispers for 24 hours."
spellcasting:
  - name: "Arcane Spontaneous Spells"
    desc: "DC 22 - __Cantrips (3rd)__ Electric Arc, Shield, Sigil, Telekinetic Hand, Void Warp - __1st__ Enfeeble, Fear, Force Barrage, Illusory Disguise (4 slots) - __2nd__ Blazing Bolt, Dispel Magic, Invisibility, Noise Blast (4 slots) - __3rd__ Fireball, Levitate, Paralyze (3 slots)"
  - name: "Divine Innate Spells"
    desc: "DC 22 - __4th__ Translocate"
sourcebook: "_Monster Core_, page 73."
```

```encounter-table
name: Venedaemon
creatures:
  - 1: Venedaemon
```
