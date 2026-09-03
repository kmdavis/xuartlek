---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Vicharamuni"
tags:
  - pf2e/creature/level/10
  - pf2e/creature/trait/beast
  - pf2e/creature/trait/holy
  - pf2e/creature/trait/uncommon
  - pf2e/creature/trait/large
statblock: inline
name: "Vicharamuni"
level: 10
source: "Monster Core"
aon_id: "creature-3104"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=3104"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC"
name: "Vicharamuni"
level: "Creature 10"
size: "Large"
trait_01: "Beast"
trait_02: "Holy"
trait_03: "Uncommon"
modifier: 22
perception:
  - name: "Perception"
    desc: "Perception +22; darkvision"
languages: "Common, Empyrean"
skills:
  - name: "Skills"
    desc: "Acrobatics +22, Athletics +21, Deception +18, Diplomacy +21, Heaven Lore +21, Stealth +20"
abilityMods: [5, 6, 5, 3, 5, 4]
ac: 31
armorclass:
  - name: "AC"
    desc: "31; __Fort__: +20; __Ref__: +21; __Will__: +22"
hp: 175
health:
  - name: "HP"
    desc: "175"
speed: "25 feet, swim 25 feet"
attacks:
  - name: "Melee"
    desc: "⬻ fangs +22 (Finesse, Holy, reach 10 feet) __Damage__ 3d10+8 piercing plus vicharamuni venom"
  - name: "Melee"
    desc: "⬻ tail +22 (Agile, Finesse, Holy, reach 20 feet) __Damage__ 3d8+8 bludgeoning plus coils of knowledge"
  - name: "Ranged"
    desc: "⬻ spit +22 (Agile, Holy, Poison, range increment 30 feet) __Damage__ vicharamuni venom"
abilities_bot:
  - name: "Coils of Knowledge"
    desc: "(Force, Magical) The naga's grip is more spiritual than physical. A creature hit by a smaranava's tail must succeed at a DC 29 Will save or become grabbed by the tail until they Escape, the naga releases them with an Interact action, or the naga dies. A captive takes a –4 status penalty to Escape, but can choose to attempt an Occultism or Religion check to Escape instead of the usual options without taking this penalty."
  - name: "Greater Constrict"
    desc: "⬻ 3d8+5 bludgeoning, DC 29"
  - name: "Spiritual Venom"
    desc: "A vicharamuni can choose to negate any damage that its venom does to a creature. In addition, the naga can cast any of its divine spells on a creature that is affected by its venom, regardless of range or line of effect."
  - name: "Vicharamuni Venom"
    desc: "(Divine, Holy, Mental, Poison, Spirit)"
  - name: "Saving Throw"
    desc: "DC 29 Will"
  - name: "Maximum Duration"
    desc: "6 rounds"
  - name: "Stage 1"
    desc: "3d6 spirit (1 round)"
  - name: "Stage 2"
    desc: "3d6 spirit and drained 1 (1 round)"
spellcasting:
  - name: "Divine Spontaneous Spells"
    desc: "DC 29, attack +21 - __Cantrips (5th)__ Daze, Detect Magic, Frostbite, Light, Read Aura, Stabilize, Telekinetic Hand - __1st__ Heal, Protection, Spirit Link (4 slots) - __2nd__ Calm, Noise Blast, See the Unseen (4 slots) - __3rd__ Crisis of Faith, Holy Light, Mind Reading (4 slots) - __4th__ Cleanse Affliction, Lightning Bolt, Fly (4 slots) - __5th__ Breath of Life, Dispel Magic, Divine Immolation (4 slots)"
sourcebook: "_Monster Core_, page 237."
```

```encounter-table
name: Vicharamuni
creatures:
  - 1: Vicharamuni
```
