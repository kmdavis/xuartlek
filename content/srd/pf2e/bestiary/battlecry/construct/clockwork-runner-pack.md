---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Clockwork Runner Pack"
tags:
  - pf2e/creature/level/5
  - pf2e/creature/trait/clockwork
  - pf2e/creature/trait/construct
  - pf2e/creature/trait/mindless
  - pf2e/creature/trait/troop
  - pf2e/creature/trait/uncommon
  - pf2e/creature/trait/gargantuan
statblock: inline
name: "Clockwork Runner Pack"
level: 5
source: "Battlecry!"
aon_id: "creature-3908"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=3908"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "BC"
name: "Clockwork Runner Pack"
level: "Creature 5"
size: "Gargantuan"
trait_01: "Clockwork"
trait_02: "Construct"
trait_03: "Mindless"
trait_04: "Troop"
trait_05: "Uncommon"
modifier: 12
perception:
  - name: "Perception"
    desc: "Perception +12; darkvision"
skills:
  - name: "Skills"
    desc: "Athletics +12, Stealth +13"
abilityMods: [2, 6, 0, -5, 5, -5]
ac: 21
armorclass:
  - name: "AC"
    desc: "21; __Fort__: +9; __Ref__: +15; __Will__: +9"
hp: 75
health:
  - name: "HP"
    desc: "75 (4 segments); __Immunities__ bleed, death effects, disease, doomed, drained, fatigued, healing, mental, nonlethal attacks, paralyzed, poison, sickened, unconscious, vitality, void; __Weaknesses__ area damage 5, electricity 5, splash damage 5, orichalcum 5"
abilities_mid:
  - name: "Troop Defenses"
    desc: ""
speed: "30 feet, climb 20 feet; troop movement"
abilities_bot:
  - name: "Fire Crossbows"
    desc: "⬺ The clockwork runners reload the crossbows built onto their backs, then launch a ranged attack in the form of a volley. This volley is a 10-foot burst within 120 feet that deals 2d8 piercing damage (DC 19 basic Reflex save). When the clockwork runners are reduced to 2 segments, this area decreases to a 5-foot burst."
  - name: "Scratch and Bite"
    desc: ""
  - name: "Frequency"
    desc: "once per round"
  - name: "Effect"
    desc: "The clockwork runners engage in a pack attack against each enemy in a 5-foot emanation, with a DC 19 basic Reflex save. The damage depends on the number of actions. ⬻ 1d8 piercing or slashing damage ⬺ 2d8+3 piercing or slashing damage ⬽ 2d8+7 piercing or slashing damage"
  - name: "War Pounce"
    desc: "⬻"
  - name: "Frequency"
    desc: "once per round"
  - name: "Effect"
    desc: "The clockwork runner pack Strides, ignoring difficult terrain (but not greater difficult terrain). At the end of this movement, each enemy in a 5-foot emanation takes 1d8 piercing or slashing damage (DC 19 basic Reflex save)."
sourcebook: "_Battlecry!_, page 176."
```

```encounter-table
name: Clockwork Runner Pack
creatures:
  - 1: Clockwork Runner Pack
```
