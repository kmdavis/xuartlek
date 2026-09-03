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
    desc: "Acrobatics +29, Athletics +27, Stealth +29"
abilityMods: [6, 8, 4, -4, 3, -1]
ac: 36
armorclass:
  - name: "AC"
    desc: "36; __Fort__: +24; __Ref__: +28; __Will__: +23"
hp: 270
health:
  - name: "HP"
    desc: "270 (4 segments) , regeneration 30 (deactivated by fire); __Resistances__ acid 20; __Weaknesses__ area damage 15, splash damage 15"
abilities_mid:
  - name: "Regrowth"
    desc: "When the dezullon thicket's regeneration raises its Hit Points above a listed threshold after losing a segment for dropping below it, the thicket immediately regains that lost segment."
  - name: "Stench"
    desc: "(aura, olfactory) 30 feet, DC 33"
  - name: "Troop Defenses"
    desc: ""
speed: "25 feet; troop movement"
abilities_bot:
  - name: "Acid Rain"
    desc: "The dezullon thicket discharges a cascade of acidic digestive juices as a ranged attack, dealing 6d6 acid damage in a 10-foot burst within 30 feet (DC 33 basic Reflex save) and exposing any creature struck to amnesia venom. When the thicket is reduced to 2 segments, this area decreases to a 5-foot burst."
  - name: "Amnesia Venom"
    desc: "(Mental, Poison)"
  - name: "Saving Throw"
    desc: "DC 33 Fortitude"
  - name: "Maximum Duration"
    desc: "6 rounds"
  - name: "Stage 1"
    desc: "clumsy 1 (1 round); Stage 2 clumsy 2 (1 round); Stage 3 confused, off-guard, and clumsy 3 (1 round); Stage 4 as Stage 3 and permanently forget the last hour (1 round)"
  - name: "Constrict"
    desc: "⬻ 1d10+6 bludgeoning, DC 36"
  - name: "Mass Improved Grab"
    desc: "⭓"
  - name: "Trigger"
    desc: "A creature fails or critically fails their Reflex save against the dezullon thicket's Thrashing Vines"
  - name: "Effect"
    desc: "The dezullon thicket attempts an Athletics check to Grapple the triggering creature. A dezullon thicket can Grapple as many creatures as it has remaining segments, though it needs to spend an action to extend the duration on subsequent rounds. These attempts neither apply nor count toward the creature's multiple attack penalty."
  - name: "Root"
    desc: "⬻ (Concentrate) Until the next time it acts, the dezullon thicket appears to be a field of normal pitcher plants. It has an automatic result of 49 (53 in forests or swamps) on Deception checks and DCs to pass as a grove of noncreature plants."
  - name: "Thrashing Vines"
    desc: ""
  - name: "Frequency"
    desc: "once per round"
  - name: "Effect"
    desc: "The thicket makes a melee attack against each enemy within a 5-foot emanation (DC 33 basic Reflex save). The damage depends on the number of actions. ⬻ 1d8+3 bludgeoning plus 1d6 acid ⬺ 2d8+11 bludgeoning plus 2d6 acid and Mass Improved Grab ⬽ 3d8+12 bludgeoning plus 3d6 acid and Mass Improved Grab"
sourcebook: "_Battlecry!_, page 177."
```

```encounter-table
name: Dezullon Thicket
creatures:
  - 1: Dezullon Thicket
```
