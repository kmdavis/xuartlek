---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Giant Ant Army"
tags:
  - pf2e/creature/level/7
  - pf2e/creature/trait/animal
  - pf2e/creature/trait/troop
  - pf2e/creature/trait/gargantuan
statblock: inline
name: "Giant Ant Army"
level: 7
source: "Battlecry!"
aon_id: "creature-3918"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=3918"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "BC"
name: "Giant Ant Army"
level: "Creature 7"
size: "Gargantuan"
trait_01: "Animal"
trait_02: "Troop"
modifier: 15
perception:
  - name: "Perception"
    desc: "Perception +15; darkvision, scent (imprecise) 30 feet"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/athletics|Athletics]] +17, [[srd/pf2e/compendium/rules-elements/skills/survival|Survival]] +15"
abilityMods: [6, 2, 6, -4, 2, -4]
ac: 24
armorclass:
  - name: "AC"
    desc: "24; __Fort__: +17; __Ref__: +14; __Will__: +12"
hp: 120
health:
  - name: "HP"
    desc: "120 (4 segments); __Weaknesses__ area damage 7, [[srd/pf2e/compendium/rules-elements/traits/gm-core/splash|splash]] damage 7"
abilities_mid:
  - name: "Troop Defenses"
    desc: ""
speed: "40 feet, climb 20 feet; troop movement"
abilities_bot:
  - name: "Giant Ant Venom"
    desc: "([[srd/pf2e/compendium/rules-elements/traits/player-core/poison|Poison]])"
  - name: "Saving Throw"
    desc: "DC 24 Fortitude"
  - name: "Maximum Duration"
    desc: "6 rounds"
  - name: "Stage 1"
    desc: "2d8 poison damage and [[srd/pf2e/compendium/rules-elements/conditions#Enfeebled|enfeebled]] 1 (1 round)"
  - name: "Stage 2"
    desc: "3d6 poison damage and enfeebled 2 (1 round)"
  - name: "Stage 3"
    desc: "2d10 poison damage and enfeebled 3 (1 round)"
  - name: "Grasping Mandibles"
    desc: "⬻"
  - name: "Requirements"
    desc: "The giant ant army's last action was a Mandible Frenzy that at least one creature failed their save against or the giant ant army has at least one creature [[srd/pf2e/compendium/rules-elements/conditions#Grabbed|grabbed]] or [[srd/pf2e/compendium/rules-elements/conditions#Restrained|restrained]]"
  - name: "Effect"
    desc: "If used after Grasping Mandibles, the giant ant army can attempt an [[srd/pf2e/compendium/rules-elements/skills/athletics|Athletics]] check to [[srd/pf2e/compendium/rules-elements/actions/player-core#Grapple|Grapple]], comparing the result to the Fortitude DC of each creature who failed its saving throw, up to as many creatures as the giant ant army has remaining segments. The giant any army can instead use Grasping Mandibles to choose one creature it's grabbing or restraining to automatically extend that condition to the end of the army's next turn."
  - name: "Haul Away"
    desc: "⬻"
  - name: "Requirements"
    desc: "The giant ant army has at least one creature [[srd/pf2e/compendium/rules-elements/conditions#Restrained|restrained]]"
  - name: "Effect"
    desc: "The army Strides up to its Speed, carrying any restrained creatures with it. If the creature is Gargantuan, the giant ant army is [[srd/pf2e/compendium/rules-elements/conditions#Encumbered|encumbered]]."
  - name: "Mandible Frenzy"
    desc: ""
  - name: "Frequency"
    desc: "once per round"
  - name: "Effect"
    desc: "The army makes a savage bite attack against each enemy in a 5-foot [[srd/pf2e/books/player-core/chapter-8-playing-the-game/area#Emanation|emanation]] (DC 22 [[srd/pf2e/books/player-core/chapter-8-playing-the-game/checks#Basic Saving Throws|basic]] Reflex save). The damage dealt depends on the number of actions. ⬻ 1d8 slashing damage plus Grasping Mandibles ⬺ 2d8+6 slashing damage plus Grasping Mandibles ⬽ 2d8+11 slashing damage"
  - name: "Overwhelm"
    desc: "⬺ The giant ant army swarms over a Large or larger creature that it has grabbed, pinning the creature in place and causing it to become [[srd/pf2e/compendium/rules-elements/conditions#Restrained|restrained]] until the start of the giant ant army's next turn or until it Escapes. A creature that begins its turn restrained by the army is repeatedly stung by the clinging ants, automatically taking 2d6 piercing damage and suffering the effects of giant ant venom."
sourcebook: "_Battlecry!_, page 181."
```

```encounter-table
name: Giant Ant Army
creatures:
  - 1: Giant Ant Army
```
