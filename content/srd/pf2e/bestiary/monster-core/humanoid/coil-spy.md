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
languages: "[[srd/pf2e/compendium/rules-elements/languages#Aklo|Aklo]], [[srd/pf2e/compendium/rules-elements/languages#Common|Common]], [[srd/pf2e/compendium/rules-elements/languages#Dwarven|Dwarven]], [[srd/pf2e/compendium/rules-elements/languages#Gnomish|Gnomish]], [[srd/pf2e/compendium/rules-elements/languages#Sakvroth|Sakvroth]]; telepathy 100 feet"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/acrobatics|Acrobatics]] +10, [[srd/pf2e/compendium/rules-elements/skills/deception|Deception]] +13, [[srd/pf2e/compendium/rules-elements/skills/diplomacy|Diplomacy]] +11, [[srd/pf2e/compendium/rules-elements/skills/intimidation|Intimidation]] +11, [[srd/pf2e/compendium/rules-elements/skills/occultism|Occultism]] +10, [[srd/pf2e/compendium/rules-elements/skills/society|Society]] +10, [[srd/pf2e/compendium/rules-elements/skills/stealth|Stealth]] +12, [[srd/pf2e/compendium/rules-elements/skills/thievery|Thievery]] +12"
abilityMods: [2, 4, 1, 4, 2, 5]
abilities_top:
  - name: "Items"
    desc: "Hand Crossbow (20 bolts), [[srd/pf2e/compendium/equipment/alchemical-items/spider-venom|Spider Venom]] (2), Shortsword, [[srd/pf2e/compendium/equipment/adventuring-gear/thieves-toolkit-infiltrator-picks|Thieves' Toolkit]]"
ac: 22
armorclass:
  - name: "AC"
    desc: "22; __Fort__: +9; __Ref__: +12; __Will__: +10 (+4 status vs. [[srd/pf2e/compendium/rules-elements/traits/player-core/mental|mental]]) +1 status to all saves vs. [[srd/pf2e/compendium/rules-elements/traits/player-core/magical|magic]]"
hp: 48
health:
  - name: "HP"
    desc: "48; __Resistances__ [[srd/pf2e/compendium/rules-elements/traits/player-core/poison|poison]] 5"
abilities_mid:
  - name: "Thin of Blood"
    desc: "Zyss serpentfolk recover slowly from injuries. When they take physical damage from a critical hit, they gain 1d4 persistent bleed damage. They take a –2 circumstance penalty to flat checks to recover from persistent damage and saving throws against afflictions."
speed: "25 feet"
attacks:
  - name: "Melee"
    desc: "⬻ shortsword +14 ([[srd/pf2e/compendium/rules-elements/traits/player-core/agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/finesse|Finesse]], [[srd/pf2e/compendium/rules-elements/traits/player-core/versatile|versatile S]]) __Damage__ 1d6+5 piercing plus serpentfolk venom"
  - name: "Melee"
    desc: "⬻ fangs +14 ([[srd/pf2e/compendium/rules-elements/traits/player-core/finesse|Finesse]]) __Damage__ 1d6+5 piercing plus serpentfolk venom"
  - name: "Ranged"
    desc: "⬻ hand crossbow +10 (range increment 60 feet, reload 1) __Damage__ 1d6+3 piercing plus serpentfolk venom or spider venom"
abilities_bot:
  - name: "Deceptive Reposition"
    desc: "⬻ The Coil spy Strides up to half their Speed and attempts a [[srd/pf2e/compendium/rules-elements/actions/player-core#Feint|Feint]], in either order."
  - name: "Maintain Disguise"
    desc: "A Coil spy can maintain an ongoing [[srd/pf2e/compendium/spells/rank-1/illusory-disguise|_illusory disguise_]] as long as they are conscious without having to re-cast the spell; they need only Cast the Spell again to reassume their _illusory disguise_ if they wish to change their appearance or if the active spell is dispelled. Coil spies typically seek privacy when they need to sleep, as an ongoing _illusory disguise_ ends an hour after they fall unconscious."
  - name: "Serpentfolk Venom"
    desc: "([[srd/pf2e/compendium/rules-elements/traits/player-core/poison|Poison]])"
  - name: "Saving Throw"
    desc: "DC 19 Fortitude"
  - name: "Maximum Duration"
    desc: "6 rounds"
  - name: "Stage 1"
    desc: "1d4 poison damage and [[srd/pf2e/compendium/rules-elements/conditions#Enfeebled|enfeebled 1]] (1 round)"
  - name: "Stage 2"
    desc: "2d4 poison damage and enfeebled 1 (1 round)"
  - name: "Sneak Attack"
    desc: "The Coil spy's Strikes deal an extra 2d6 precision damage to [[srd/pf2e/compendium/rules-elements/conditions#Off-Guard|off-guard]] creatures."
spellcasting:
  - name: "Occult Innate Spells"
    desc: "DC 21 - __1st__ [[srd/pf2e/compendium/spells/rank-1/ventriloquism|Ventriloquism]] (at will) - __2nd__ [[srd/pf2e/compendium/spells/rank-2/blur|Blur]] (self only; at will) - __3rd__ [[srd/pf2e/compendium/spells/rank-1/illusory-disguise|Illusory Disguise]] (at will) - __4th__ [[srd/pf2e/compendium/spells/rank-4/suggestion|Suggestion]]"
sourcebook: "_Monster Core_, page 304."
```

```encounter-table
name: Coil Spy
creatures:
  - 1: Coil Spy
```
