---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Lampad"
tags:
  - pf2e/creature/level/5
  - pf2e/creature/trait/earth
  - pf2e/creature/trait/fey
  - pf2e/creature/trait/nymph
  - pf2e/creature/trait/medium
statblock: inline
name: "Lampad"
level: 5
source: "Monster Core 2"
aon_id: "creature-4490"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=4490"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC2"
name: "Lampad"
level: "Creature 5"
size: "Medium"
trait_01: "Earth"
trait_02: "Fey"
trait_03: "Nymph"
modifier: 12
perception:
  - name: "Perception"
    desc: "Perception +12; darkvision"
languages: "Aklo, Common, Fey, Sakvroth"
skills:
  - name: "Skills"
    desc: "Acrobatics +12, Athletics +9, Diplomacy +14, Nature +10, Occultism +11, Performance +14, Society +9, Stealth +12"
abilityMods: [0, 5, 4, 2, 3, 5]
ac: 21
armorclass:
  - name: "AC"
    desc: "21; __Fort__: +11; __Ref__: +14; __Will__: +12"
hp: 85
health:
  - name: "HP"
    desc: "85; __Weaknesses__ cold iron 5"
abilities_mid:
  - name: "Cavern Dependent"
    desc: "A lampad is mystically bonded to a single cavern or other self-contained underground area and must remain within 300 feet of it. If they move beyond that range, they become sickened 1 and are unable to recover. They must attempt a DC 19 Fortitude save every hour or increase their sickened value by 1 (to a maximum of sickened 4). After 24 hours, they become drained 1, with this value increasing by 1 every additional 24 hours. A lampad can perform a 24- hour ritual to bond to a new cavern."
speed: "25 feet, climb 25 feet (on stone only)"
attacks:
  - name: "Melee"
    desc: "⬻ earthen fist +14 (Agile, finesse) __Damage__ 2d10+2 bludgeoning"
  - name: "Ranged"
    desc: "⬻ light wisp +14 (Magical, range increment 30 feet) __Damage__ 1d8+2 mental plus 1d6 fire and 1d6 vitality"
abilities_bot:
  - name: "Weep"
    desc: "⬻ (Auditory, emotion, mental, primal)"
  - name: "Frequency"
    desc: "once per round"
  - name: "Effect"
    desc: "The lampad begins a heart-wrenching fit of weeping, inspiring sympathetic sobbing in nearby creatures. Every non-lampad creature within 30 feet who hears the lampad's weeping must succeed at a DC 20 Will save or be unable to use reactions for 1 round and slowed 1 on its next turn as it sobs uncontrollably. Strong Emotions While lampads are ever vigilant in their assigned tasks, they're known to become lonely and forlorn, as the majority of underground denizens make poor company. True companionship and conversation are among the few things that can keep a moody lampad from sporadically weeping, though like most creatures they find such tears cathartic, feeling better after a good cry."
spellcasting:
  - name: "Primal Innate Spells"
    desc: "DC 22 - __Cantrips (4th)__ Light - __2nd__ Heal, Revealing Light - __3rd__ One with Stone (at will), Pummeling Rubble - __4th__ Shape Stone"
sourcebook: "_Monster Core 2_, page 236."
```

```encounter-table
name: Lampad
creatures:
  - 1: Lampad
```
