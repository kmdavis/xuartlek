---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Boggard Scouting Party"
tags:
  - pf2e/creature/level/6
  - pf2e/creature/trait/amphibious
  - pf2e/creature/trait/boggard
  - pf2e/creature/trait/humanoid
  - pf2e/creature/trait/troop
  - pf2e/creature/trait/gargantuan
statblock: inline
name: "Boggard Scouting Party"
level: 6
source: "Battlecry!"
aon_id: "creature-3905"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=3905"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "BC"
name: "Boggard Scouting Party"
level: "Creature 6"
size: "Gargantuan"
trait_01: "Amphibious"
trait_02: "Boggard"
trait_03: "Humanoid"
trait_04: "Troop"
modifier: 19
perception:
  - name: "Perception"
    desc: "Perception +19; darkvision"
languages: "Boggard, Common"
skills:
  - name: "Skills"
    desc: "Acrobatics +13, Athletics +15, Stealth +13"
abilityMods: [5, 4, 2, 0, 2, 0]
ac: 23
armorclass:
  - name: "AC"
    desc: "23; __Fort__: +17; __Ref__: +14; __Will__: +11"
hp: 90
health:
  - name: "HP"
    desc: "90 (4 segments); __Weaknesses__ area damage 5, splash damage 5"
abilities_mid:
  - name: "Troop Defenses"
    desc: ""
speed: "20 feet, swim 25 feet; troop movement"
abilities_bot:
  - name: "Chorus of Croaks"
    desc: "⬻ (Auditory, Emotion, Fear, Mental) The boggard scouting party unleashes a chorus of terrifying croaks. Any non-boggard within 30 feet becomes frightened 1 unless they succeed at a DC 21 Will save; those who critically succeed are temporarily immune for 1 minute."
  - name: "Coordinated Tongue Pull"
    desc: "⬻"
  - name: "Frequency"
    desc: "once per round"
  - name: "Effect"
    desc: "Several boggards use their tongues to grapple an enemy within 10 feet to pull them closer. The target must attempt a DC 21 Reflex save. On a failure, they are grabbed and pulled 5 feet closer to the scouting party. A creature grabbed in this way isn't immobilized, but it can't move more than 10 feet from the scouting party. A creature can sever one of the tongues with a Strike against AC 21 that deals at least 5 slashing damage. This doesn't damage the scouting party."
  - name: "Morningstar Massacre"
    desc: ""
  - name: "Frequency"
    desc: "once per round"
  - name: "Effect"
    desc: "The boggards execute coordinated melee attacks against each enemy in a 5-foot emanation, with a DC 21 basic Reflex save. The damage dealt depends on the number of actions. ⬻ 1d6 bludgeoning or piercing damage ⬺ 2d6+7 bludgeoning or piercing damage ⬽ 2d6+11 bludgeoning or piercing damage"
  - name: "Sling Barrage"
    desc: "⬺ The dreadknot draws and loads slings to launch a coordinated barrage. This barrage is a 10-foot burst within 50 feet that deals 3d6 bludgeoning damage (DC 21 basic Reflex save). When the scouting party is reduced to 2 segments, this area decreases to a 5-foot burst."
  - name: "Swamp Passage"
    desc: "A boggard scouting party ignores difficult terrain caused by swamp terrain features."
sourcebook: "_Battlecry!_, page 175."
```

```encounter-table
name: Boggard Scouting Party
creatures:
  - 1: Boggard Scouting Party
```
