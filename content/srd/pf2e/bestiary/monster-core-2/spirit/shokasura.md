---
obsidianUIMode: preview
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
aon_id: "creature-4085"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=4085"
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
    desc: "Perception +8; darkvision"
languages: "Common, Diabolic; telepathy (touch)"
skills:
  - name: "Skills"
    desc: "Acrobatics +7, Deception +9, Performance +7, Religion +7, Stealth +7"
abilityMods: [0, 4, 1, 0, 3, 4]
ac: 16
armorclass:
  - name: "AC"
    desc: "16; __Fort__: +4; __Ref__: +9; __Will__: +7"
hp: 22
health:
  - name: "HP"
    desc: "22; __Immunities__ curses; __Weaknesses__ holy 2"
speed: "25 feet, climb 15 feet"
attacks:
  - name: "Melee"
    desc: "⬻ claw +9 (Agile, Finesse, Unholy) __Damage__ 1d8 slashing and 1 spirit"
  - name: "Melee"
    desc: "⬻ thorn +9 (Agile, Unholy) __Damage__ 1d8 piercing plus grieving venom and 1 spirit"
abilities_bot:
  - name: "Change Shape"
    desc: "⬻ (Concentrate, Divine, Polymorph) The shokasura takes on the appearance of a Small humanoid. This doesn't change the shokasura's Speed or their attack and damage modifiers with their Strikes, but it might change the damage type their Strikes deal (typically to bludgeoning). The asura typically loses their thorn Strike unless the humanoid form has a similar unarmed attack. This alternate form has a specific, persistent appearance, which the shokasura can change by performing a 1-hour ritual."
  - name: "Grieving Venom"
    desc: "(Poison)"
  - name: "Saving Throw"
    desc: "DC 17 Will"
  - name: "Maximum Duration"
    desc: "4 rounds"
  - name: "Stage 1"
    desc: "1d4 poison damage and enfeebled 1 (1 round)"
  - name: "Stage 2"
    desc: "1d4 poison damage, and enfeebled 2 (1 round)"
  - name: "Stage 3"
    desc: "1d4 poison damage, slowed 1, and the creature cannot use reactions (1 round)"
spellcasting:
  - name: "Divine Innate Spells"
    desc: "DC 17 - __Cantrips (1st)__ Read Aura - __2nd__ Charm, Stupefy - __Constant (3rd)__ Veil of Privacy (self only)"
sourcebook: "_Monster Core 2_, page 42."
```

```encounter-table
name: Shokasura
creatures:
  - 1: Shokasura
```
