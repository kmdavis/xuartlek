---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Hell Hound Pack"
tags:
  - pf2e/creature/level/8
  - pf2e/creature/trait/beast
  - pf2e/creature/trait/fiend
  - pf2e/creature/trait/fire
  - pf2e/creature/trait/troop
  - pf2e/creature/trait/unholy
  - pf2e/creature/trait/gargantuan
statblock: inline
name: "Hell Hound Pack"
level: 8
source: "Battlecry!"
aon_id: "creature-3922"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=3922"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "BC"
name: "Hell Hound Pack"
level: "Creature 8"
size: "Gargantuan"
trait_01: "Beast"
trait_02: "Fiend"
trait_03: "Fire"
trait_04: "Troop"
trait_05: "Unholy"
modifier: 16
perception:
  - name: "Perception"
    desc: "Perception +16; darkvision, scent (imprecise) 60 feet"
languages: "Diabolic; can't speak any language"
skills:
  - name: "Skills"
    desc: "Acrobatics +15, Athletics +16, Survival +16"
abilityMods: [6, 4, 3, -2, 3, -2]
ac: 26
armorclass:
  - name: "AC"
    desc: "26; __Fort__: +16; __Ref__: +17; __Will__: +14"
hp: 135
health:
  - name: "HP"
    desc: "135 (4 segments); __Immunities__ fire; __Weaknesses__ area damage 8, cold 10, splash damage 8"
abilities_mid:
  - name: "Hellish Revenge"
    desc: "⬲"
  - name: "Trigger"
    desc: "The hell hound pack is critically hit by a Strike or spell attack"
  - name: "Effect"
    desc: "The hell hound pack's Hellfire Breath recharges. They can immediately use it as part of this reaction."
  - name: "Troop Defenses"
    desc: ""
speed: "40 feet; troop movement"
abilities_bot:
  - name: "Hellfire Breath"
    desc: "⬻ (Divine, Fire, Unholy) The hell hounds in the pack combine their efforts to bathe the battlefield in hellish flame, dealing 2d10 fire damage to all creatures in two 15- foot cones (DC 25 basic Reflex save) that can't overlap. The hell hound pack can't use Hellfire Breath again for 1d4 rounds. If the pack would take fire damage or be targeted by a fire effect, its Hellfire Breath recharges."
  - name: "Infernal Mauling"
    desc: "(Magical, Unholy)"
  - name: "Frequency"
    desc: "once per round"
  - name: "Effect"
    desc: "The pack tears into each enemy in a 5-foot emanation with their flaming jaws (DC 23 basic Reflex save). The damage dealt depends on the number of actions. ⬻ 1d4 piercing damage plus 1d6 fire damage ⬺ 1d8+7 piercing damage plus 2d6 fire damage ⬽ 2d8+7 piercing damage plus 2d6 fire damage"
sourcebook: "_Battlecry!_, page 183."
```

```encounter-table
name: Hell Hound Pack
creatures:
  - 1: Hell Hound Pack
```
