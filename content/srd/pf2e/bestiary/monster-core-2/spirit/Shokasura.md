---
noteType: pf2eMonster
aliases: "Shokasura"
tags:
  - pf2e/creature/level/1
  - pf2e/creature/trait/asura
  - pf2e/creature/trait/spirit
  - pf2e/creature/trait/unholy
  - pf2e/creature/trait/small
statblock: inline
name: "Shokasura"
level: 1
source: "Monster Core 2"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=4085"
socialImage: og-image.png
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC2"
name: "Shokasura"
level: "Creature 1"
size: "Small"
trait_01: "Asura"
trait_02: "Spirit"
trait_03: "Unholy"
modifier: 8
perception:
  - name: "Perception"
    desc: "+8; darkvision"
languages: "[[srd/pf2e/compendium/rules-elements/Languages#Common|Common]], [[srd/pf2e/compendium/rules-elements/Languages#Diabolic|Diabolic]]; telepathy (touch)"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/Acrobatics|Acrobatics]] +7, [[srd/pf2e/compendium/rules-elements/skills/Deception|Deception]] +9, [[srd/pf2e/compendium/rules-elements/skills/Performance|Performance]] +7, [[srd/pf2e/compendium/rules-elements/skills/Religion|Religion]] +7, [[srd/pf2e/compendium/rules-elements/skills/Stealth|Stealth]] +7"
abilityMods: [0, 4, 1, 0, 3, 4]
ac: 16
armorclass:
  - name: "AC"
    desc: "16; __Fort__: +4; __Ref__: +9; __Will__: +7"
hp: 22
health:
  - name: "HP"
    desc: "22; __Immunities__ [[srd/pf2e/compendium/rules-elements/traits/player-core/Curse|curses]]; __Weaknesses__ [[srd/pf2e/compendium/rules-elements/traits/player-core/Holy|holy]] 2"
speed: "25 feet, climb 15 feet"
attacks:
  - name: "Melee"
    desc: "⬻ claw +9 ([[srd/pf2e/compendium/rules-elements/traits/player-core/Agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Finesse|Finesse]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Unholy|Unholy]]) __Damage__ 1d8 slashing and 1 spirit"
  - name: "Melee"
    desc: "⬻ thorn +9 ([[srd/pf2e/compendium/rules-elements/traits/player-core/Agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Unholy|Unholy]]) __Damage__ 1d8 piercing plus grieving venom and 1 spirit"
abilities_bot:
  - name: "Change Shape"
    desc: "⬻ ([[srd/pf2e/compendium/rules-elements/traits/player-core/Concentrate|Concentrate]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Divine|Divine]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Polymorph|Polymorph]]) The shokasura takes on the appearance of a Small [[srd/pf2e/compendium/rules-elements/traits/player-core/Humanoid|humanoid]]. This doesn't change the shokasura's Speed or their attack and damage modifiers with their Strikes, but it might change the damage type their Strikes deal (typically to bludgeoning). The asura typically loses their thorn Strike unless the humanoid form has a similar unarmed attack. This alternate form has a specific, persistent appearance, which the shokasura can change by performing a 1-hour ritual."
  - name: "Grieving Venom"
    desc: "([[srd/pf2e/compendium/rules-elements/traits/player-core/Poison|Poison]])"
  - name: "Saving Throw"
    desc: "DC 17 Will"
  - name: "Maximum Duration"
    desc: "4 rounds"
  - name: "Stage 1"
    desc: "1d4 poison damage and [[srd/pf2e/compendium/rules-elements/Conditions#Enfeebled|enfeebled 1]] (1 round)"
  - name: "Stage 2"
    desc: "1d4 poison damage, and enfeebled 2 (1 round)"
  - name: "Stage 3"
    desc: "1d4 poison damage, [[srd/pf2e/compendium/rules-elements/Conditions#Slowed|slowed 1]], and the creature cannot use reactions (1 round)"
spellcasting:
  - name: "Divine Innate Spells"
    desc: "DC 17 - __Cantrips (1st)__ [[srd/pf2e/compendium/spells/cantrips/Read Aura|Read Aura]] - __2nd__ [[srd/pf2e/compendium/spells/rank-1/Charm|Charm]], [[srd/pf2e/compendium/spells/rank-2/Stupefy|Stupefy]] - __Constant (3rd)__ [[srd/pf2e/compendium/spells/rank-3/Veil of Privacy|Veil of Privacy]] (self only)"
sourcebook: "_Monster Core 2_, page 42."
```

```encounter-table
name: Shokasura
creatures:
  - 1: Shokasura
```
