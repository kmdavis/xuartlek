---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Coil Spy"
tags:
  - pf2e/creature/level/4
  - pf2e/creature/trait/humanoid
  - pf2e/creature/trait/serpentfolk
  - pf2e/creature/trait/medium
statblock: inline
name: "Coil Spy"
level: 4
source: "Monster Core"
aon_id: "creature-3183"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=3183"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC"
name: "Coil Spy"
level: "Creature 4"
size: "Medium"
trait_01: "Humanoid"
trait_02: "Serpentfolk"
modifier: 10
perception:
  - name: "Perception"
    desc: "Perception +10; darkvision, scent (imprecise) 30 feet"
languages: "Aklo, Common, Dwarven, Gnomish, Sakvroth; telepathy 100 feet"
skills:
  - name: "Skills"
    desc: "Acrobatics +10, Deception +13, Diplomacy +11, Intimidation +11, Occultism +10, Society +10, Stealth +12, Thievery +12"
abilityMods: [2, 4, 1, 4, 2, 5]
abilities_top:
  - name: "Items"
    desc: "Hand Crossbow (20 bolts), Spider Venom (2), Shortsword, Thieves' Toolkit"
ac: 22
armorclass:
  - name: "AC"
    desc: "22; __Fort__: +9; __Ref__: +12; __Will__: +10 (+4 status vs. mental) +1 status to all saves vs. magic"
hp: 48
health:
  - name: "HP"
    desc: "48; __Resistances__ poison 5"
abilities_mid:
  - name: "Thin of Blood"
    desc: "Zyss serpentfolk recover slowly from injuries. When they take physical damage from a critical hit, they gain 1d4 persistent bleed damage. They take a –2 circumstance penalty to flat checks to recover from persistent damage and saving throws against afflictions."
speed: "25 feet"
attacks:
  - name: "Melee"
    desc: "⬻ shortsword +14 (Agile, Finesse, versatile S) __Damage__ 1d6+5 piercing plus serpentfolk venom"
  - name: "Melee"
    desc: "⬻ fangs +14 (Finesse) __Damage__ 1d6+5 piercing plus serpentfolk venom"
  - name: "Ranged"
    desc: "⬻ hand crossbow +10 (range increment 60 feet, reload 1) __Damage__ 1d6+3 piercing plus serpentfolk venom or spider venom"
abilities_bot:
  - name: "Deceptive Reposition"
    desc: "⬻ The Coil spy Strides up to half their Speed and attempts a Feint, in either order."
  - name: "Maintain Disguise"
    desc: "A Coil spy can maintain an ongoing _illusory disguise_ as long as they are conscious without having to re-cast the spell; they need only Cast the Spell again to reassume their _illusory disguise_ if they wish to change their appearance or if the active spell is dispelled. Coil spies typically seek privacy when they need to sleep, as an ongoing _illusory disguise_ ends an hour after they fall unconscious."
  - name: "Serpentfolk Venom"
    desc: "(Poison)"
  - name: "Saving Throw"
    desc: "DC 19 Fortitude"
  - name: "Maximum Duration"
    desc: "6 rounds"
  - name: "Stage 1"
    desc: "1d4 poison damage and enfeebled 1 (1 round)"
  - name: "Stage 2"
    desc: "2d4 poison damage and enfeebled 1 (1 round)"
  - name: "Sneak Attack"
    desc: "The Coil spy's Strikes deal an extra 2d6 precision damage to off-guard creatures."
spellcasting:
  - name: "Occult Innate Spells"
    desc: "DC 21 - __1st__ Ventriloquism (at will) - __2nd__ Blur (self only; at will) - __3rd__ Illusory Disguise (at will) - __4th__ Suggestion"
sourcebook: "_Monster Core_, page 304."
```

```encounter-table
name: Coil Spy
creatures:
  - 1: Coil Spy
```
