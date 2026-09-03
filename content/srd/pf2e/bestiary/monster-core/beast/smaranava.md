---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Smaranava"
tags:
  - pf2e/creature/level/7
  - pf2e/creature/trait/beast
  - pf2e/creature/trait/uncommon
  - pf2e/creature/trait/large
statblock: inline
name: "Smaranava"
level: 7
source: "Monster Core"
aon_id: "creature-3103"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=3103"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC"
name: "Smaranava"
level: "Creature 7"
size: "Large"
trait_01: "Beast"
trait_02: "Uncommon"
modifier: 15
perception:
  - name: "Perception"
    desc: "Perception +15; darkvision"
languages: "Common, Empyrean"
skills:
  - name: "Skills"
    desc: "Acrobatics +17, Arcana +16, Athletics +13, Deception +16, Intimidation +16, Stealth +19"
abilityMods: [2, 6, 4, 3, 2, 3]
ac: 27
armorclass:
  - name: "AC"
    desc: "27; __Fort__: +15; __Ref__: +17; __Will__: +15"
hp: 115
health:
  - name: "HP"
    desc: "115"
speed: "30 feet, swim 30 feet"
attacks:
  - name: "Melee"
    desc: "⬻ fangs +20 (Finesse, Magical) __Damage__ 2d10+5 piercing plus smaranava venom"
  - name: "Melee"
    desc: "⬻ tail +20 (Agile, Finesse, Magical, reach 15 feet) __Damage__ 2d8+5 bludgeoning plus coils of knowledge"
abilities_bot:
  - name: "Coils of Knowledge"
    desc: "(Force, Magical) The naga's grip is more spiritual than physical. A creature hit by a smaranava's tail must succeed at a DC 25 Will save or become grabbed by the tail until they Escape, the naga releases them with an Interact action, or the naga dies. A captive takes a –4 status penalty to Escape, but can choose to attempt an Occultism or Religion check to Escape instead of the usual options without taking this penalty."
  - name: "Constrict"
    desc: "⬻ 2d8+5 bludgeoning, DC 25"
  - name: "Smaranava Venom"
    desc: "(Incapacitation, Mental, Poison) When a holy creature succeeds at a saving throw against this poison, it is immediately cured"
  - name: "Saving Throw"
    desc: "DC 25 Will"
  - name: "Maximum Duration"
    desc: "5 minutes"
  - name: "Stage 1"
    desc: "slowed 1 (1 round)"
  - name: "Stage 2"
    desc: "slowed 2 (1 round)"
  - name: "Stage 3"
    desc: "unconscious with no Perception check to wake up (1 minute)"
spellcasting:
  - name: "Occult Innate Spells"
    desc: "DC 25 - __Cantrips (4th)__ Detect Magic, Read Aura, Telekinetic Hand - __3rd__ Dispel Magic, Lightning Bolt, Mind Reading"
sourcebook: "_Monster Core_, page 236."
```

```encounter-table
name: Smaranava
creatures:
  - 1: Smaranava
```
