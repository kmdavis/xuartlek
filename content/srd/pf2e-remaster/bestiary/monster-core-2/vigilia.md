---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Vigilia"
tags:
  - pf2e/creature/level/11
  - pf2e/creature/trait/aeon
  - pf2e/creature/trait/monitor
  - pf2e/creature/trait/medium
statblock: inline
name: "Vigilia"
level: 11
source: "Monster Core 2"
aon_id: "creature-4013"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=4013"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC2"
name: "Vigilia"
level: "Creature 11"
size: "Medium"
trait_01: "Aeon"
trait_02: "Monitor"
modifier: 24
perception:
  - name: "Perception"
    desc: "Perception +24; darkvision, _see the unseen_"
languages: "Common, Diabolic, Empyrean, Utopian"
skills:
  - name: "Skills"
    desc: "Athletics +20, Legal Lore +17"
abilityMods: [7, 3, 5, 2, 5, -1]
ac: 30
armorclass:
  - name: "AC"
    desc: "30; __Fort__: +23; __Ref__: +18; __Will__: +20"
hp: 190
health:
  - name: "HP"
    desc: "190; __Immunities__ disease, emotion, fear; __Resistances__ electricity 10"
speed: "30 feet"
attacks:
  - name: "Melee"
    desc: "⬻ fist +24 (Magical, Nonlethal) __Damage__ 2d10+10 bludgeoning plus 1d10 electricity"
abilities_bot:
  - name: "Electrical Purge"
    desc: "⬺ (Divine, Electricity, Nonlethal) The vigilia releases lightning from their body in a 30-foot emanation dealing 4d10 electricity damage (DC 30 basic Reflex save) to all creatures that aren't aeons or constructs. The vigilia is then slowed 1 for 1 round."
  - name: "Lightning Chain"
    desc: "⬻ (Divine, Electricity, Nonlethal) The vigilia wraps momentary chains of electrical energy around a creature within 60 feet, dealing 2d10 electricity damage (DC 30 basic Reflex save). A creature that fails its save is also pulled 10 feet toward the vigilia (20 feet on a critical failure)."
  - name: "Take Prisoner"
    desc: "⬻ The vigilia Interacts to pick up a Medium or smaller unconscious creature within its reach, then Strides."
spellcasting:
  - name: "Divine Innate Spells"
    desc: "DC 30 - __Constant (2nd)__ See the Unseen"
sourcebook: "_Monster Core 2_, page 11."
```

```encounter-table
name: Vigilia
creatures:
  - 1: Vigilia
```
