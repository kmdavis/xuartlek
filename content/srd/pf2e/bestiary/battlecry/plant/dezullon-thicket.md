---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Dezullon Thicket"
tags:
  - pf2e/creature/level/15
  - pf2e/creature/trait/plant
  - pf2e/creature/trait/troop
  - pf2e/creature/trait/gargantuan
statblock: inline
name: "Dezullon Thicket"
level: 15
source: "Battlecry!"
aon_id: "creature-3910"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=3910"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "BC"
name: "Dezullon Thicket"
level: "Creature 15"
size: "Gargantuan"
trait_01: "Plant"
trait_02: "Troop"
modifier: 25
perception:
  - name: "Perception"
    desc: "Perception +25; low-light vision"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/acrobatics|Acrobatics]] +29, [[srd/pf2e/compendium/rules-elements/skills/athletics|Athletics]] +27, [[srd/pf2e/compendium/rules-elements/skills/stealth|Stealth]] +29"
abilityMods: [6, 8, 4, -4, 3, -1]
ac: 36
armorclass:
  - name: "AC"
    desc: "36; __Fort__: +24; __Ref__: +28; __Will__: +23"
hp: 270
health:
  - name: "HP"
    desc: "270 (4 segments) , regeneration 30 (deactivated by [[srd/pf2e/compendium/rules-elements/traits/player-core/fire|fire]]); __Resistances__ [[srd/pf2e/compendium/rules-elements/traits/player-core/acid|acid]] 20; __Weaknesses__ area damage 15, [[srd/pf2e/compendium/rules-elements/traits/gm-core/splash|splash]] damage 15"
abilities_mid:
  - name: "Regrowth"
    desc: "When the dezullon thicket's regeneration raises its Hit Points above a listed threshold after losing a segment for dropping below it, the thicket immediately regains that lost segment."
  - name: "Stench"
    desc: "([[srd/pf2e/compendium/rules-elements/traits/player-core/aura|aura]], [[srd/pf2e/compendium/rules-elements/traits/player-core/olfactory|olfactory]]) 30 feet, DC 33"
  - name: "Troop Defenses"
    desc: ""
speed: "25 feet; troop movement"
abilities_bot:
  - name: "Acid Rain"
    desc: "The dezullon thicket discharges a cascade of acidic digestive juices as a ranged attack, dealing 6d6 acid damage in a 10-foot [[srd/pf2e/books/player-core/chapter-8-playing-the-game/area#Burst|burst]] within 30 feet (DC 33 [[srd/pf2e/books/player-core/chapter-8-playing-the-game/checks#Basic Saving Throws|basic]] Reflex save) and exposing any creature struck to amnesia venom. When the thicket is reduced to 2 segments, this area decreases to a 5-foot burst."
  - name: "Amnesia Venom"
    desc: "([[srd/pf2e/compendium/rules-elements/traits/player-core/mental|Mental]], [[srd/pf2e/compendium/rules-elements/traits/player-core/poison|Poison]])"
  - name: "Saving Throw"
    desc: "DC 33 Fortitude"
  - name: "Maximum Duration"
    desc: "6 rounds"
  - name: "Stage 1"
    desc: "[[srd/pf2e/compendium/rules-elements/conditions#Clumsy|clumsy]] 1 (1 round); Stage 2 clumsy 2 (1 round); Stage 3 [[srd/pf2e/compendium/rules-elements/conditions#Confused|confused]], [[srd/pf2e/compendium/rules-elements/conditions#Off-Guard|off-guard]], and clumsy 3 (1 round); Stage 4 as Stage 3 and permanently forget the last hour (1 round)"
  - name: "Constrict"
    desc: "⬻ 1d10+6 bludgeoning, DC 36"
  - name: "Mass Improved Grab"
    desc: "⭓"
  - name: "Trigger"
    desc: "A creature fails or critically fails their Reflex save against the dezullon thicket's Thrashing Vines"
  - name: "Effect"
    desc: "The dezullon thicket attempts an [[srd/pf2e/compendium/rules-elements/skills/athletics|Athletics]] check to [[srd/pf2e/compendium/rules-elements/actions/player-core#Grapple|Grapple]] the triggering creature. A dezullon thicket can Grapple as many creatures as it has remaining segments, though it needs to spend an action to extend the duration on subsequent rounds. These attempts neither apply nor count toward the creature's multiple attack penalty."
  - name: "Root"
    desc: "⬻ ([[srd/pf2e/compendium/rules-elements/traits/player-core/concentrate|Concentrate]]) Until the next time it acts, the dezullon thicket appears to be a field of normal pitcher plants. It has an automatic result of 49 (53 in forests or swamps) on [[srd/pf2e/compendium/rules-elements/skills/deception|Deception]] checks and DCs to pass as a grove of noncreature plants."
  - name: "Thrashing Vines"
    desc: ""
  - name: "Frequency"
    desc: "once per round"
  - name: "Effect"
    desc: "The thicket makes a melee attack against each enemy within a 5-foot [[srd/pf2e/books/player-core/chapter-8-playing-the-game/area#Emanation|emanation]] (DC 33 [[srd/pf2e/books/player-core/chapter-8-playing-the-game/checks#Basic Saving Throws|basic]] Reflex save). The damage depends on the number of actions. ⬻ 1d8+3 bludgeoning plus 1d6 acid ⬺ 2d8+11 bludgeoning plus 2d6 acid and Mass Improved Grab ⬽ 3d8+12 bludgeoning plus 3d6 acid and Mass Improved Grab"
sourcebook: "_Battlecry!_, page 177."
```

```encounter-table
name: Dezullon Thicket
creatures:
  - 1: Dezullon Thicket
```
