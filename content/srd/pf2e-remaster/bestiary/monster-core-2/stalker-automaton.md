---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Stalker Automaton"
tags:
  - pf2e/creature/level/5
  - pf2e/creature/trait/automaton
  - pf2e/creature/trait/construct
  - pf2e/creature/trait/rare
  - pf2e/creature/trait/medium
statblock: inline
name: "Stalker Automaton"
level: 5
source: "Monster Core 2"
aon_id: "creature-4091"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=4091"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC2"
name: "Stalker Automaton"
level: "Creature 5"
size: "Medium"
trait_01: "Automaton"
trait_02: "Construct"
trait_03: "Rare"
modifier: 15
perception:
  - name: "Perception"
    desc: "Perception +15; darkvision"
languages: "Common; one other language the stalker knew in life (usually Jistkan); telepathy 60 feet"
skills:
  - name: "Skills"
    desc: "Acrobatics +12, Athletics +11, Stealth +14, Survival +13"
abilityMods: [4, 5, 3, 3, 4, 1]
abilities_top:
  - name: "Adaptive Camouflage"
    desc: "The stalker's magically treated metal frame constantly shifts and changes to match their surroundings. The stalker does not need cover or concealment to Hide."
ac: 21
armorclass:
  - name: "AC"
    desc: "21; __Fort__: +10; __Ref__: +14; __Will__: +13"
hp: 65
health:
  - name: "HP"
    desc: "65; __Immunities__ bleed, death effects, disease, doomed, drained, fatigued, healing, nonlethal attacks, paralyzed, poison, sickened, unconscious, vitality, void; __Resistances__ physical 5 (except adamantine)"
speed: "30 feet, climb 20 feet"
attacks:
  - name: "Melee"
    desc: "⬻ jaws +15 __Damage__ 2d10+6 piercing"
  - name: "Melee"
    desc: "⬻ claw +15 (Agile) __Damage__ 2d6+6 slashing"
abilities_bot:
  - name: "Astral Blink"
    desc: "⬻ (Concentrate, Manipulate, Teleportation)"
  - name: "Frequency"
    desc: "once per round"
  - name: "Effect"
    desc: "The stalker steps sideways into the astral realm, reappearing nearby. The stalker teleports to an unoccupied space within 15 feet that they can see."
  - name: "Astral Pounce"
    desc: "⬺"
  - name: "Requirements"
    desc: "The stalker hasn't used Astral Blink this round"
  - name: "Effect"
    desc: "The stalker Astral Blinks or Strides and makes a Strike at the end of that movement. If the stalker began this action hidden, it remains hidden until after this ability's Strike. The stalker then Astral Blinks or Strides again, whichever it did not already do."
  - name: "Sneak Attack"
    desc: "The stalker deals an additional 1d6 precision damage to off-guard creatures."
spellcasting:
  - name: "Arcane Innate Spells"
    desc: "DC 20 - __4th__ Translocate (at will)"
sourcebook: "_Monster Core 2_, page 48."
```

```encounter-table
name: Stalker Automaton
creatures:
  - 1: Stalker Automaton
```
