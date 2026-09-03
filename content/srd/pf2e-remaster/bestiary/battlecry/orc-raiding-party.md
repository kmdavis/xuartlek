---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Orc Raiding Party"
tags:
  - pf2e/creature/level/5
  - pf2e/creature/trait/humanoid
  - pf2e/creature/trait/orc
  - pf2e/creature/trait/troop
  - pf2e/creature/trait/gargantuan
statblock: inline
name: "Orc Raiding Party"
level: 5
source: "Battlecry!"
aon_id: "creature-3931"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=3931"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "BC"
name: "Orc Raiding Party"
level: "Creature 5"
size: "Gargantuan"
trait_01: "Humanoid"
trait_02: "Orc"
trait_03: "Troop"
modifier: 15
perception:
  - name: "Perception"
    desc: "Perception +15"
languages: "Common, Orcish"
skills:
  - name: "Skills"
    desc: "Athletics +13, Intimidation +12"
abilityMods: [5, 4, 4, 0, 1, 1]
ac: 21
armorclass:
  - name: "AC"
    desc: "21; __Fort__: +10; __Ref__: +15; __Will__: +12"
hp: 75
health:
  - name: "HP"
    desc: "75 (4 segments); __Weaknesses__ area damage 5, splash damage 5"
abilities_mid:
  - name: "Ferocious Fall"
    desc: "⬲"
  - name: "Trigger"
    desc: "The orc raiding party is about to lose a segment due to passing a Hit Point threshold"
  - name: "Effect"
    desc: "The dying orc raiders lash out as they fall. Each enemy in a 5-foot emanation takes 1d6+2 piercing damage (DC 19 basic Reflex save); this occurs before the raiding party loses a segment."
  - name: "Troop Defenses"
    desc: ""
speed: "25 feet; troop movement"
abilities_bot:
  - name: "Break Through"
    desc: "⬽"
  - name: "Frequency"
    desc: "once per 10 minutes"
  - name: "Effect"
    desc: "The orc raiders exploit a gap in enemy lines. The orc raiding party Strides twice; it can pass through spaces of Medium or smaller creatures but can't end its movement in them. All enemies whose spaces the orc raiding party passed through or were adjacent to at any point during their movement take 1d6+2 piercing damage (DC 19 basic Reflex save). A creature who critically fails this save is also pushed 5 feet away from the orc raiding party. Break Through damages each creature only once."
  - name: "Iron Rain"
    desc: "⬺ The orc raiders launch a multitude of javelins at foes in a deadly volley. This volley is a 10-foot burst within 30 feet that deals 3d6 piercing damage with a DC 19 basic Reflex save. When the orc raiding party is reduced to 2 or fewer segments, this area decreases to a 5-foot burst."
  - name: "Rip Them Up"
    desc: ""
  - name: "Frequency"
    desc: "once per round"
  - name: "Effect"
    desc: "The orc raiders batter all enemies in a 5-foot emanation with coordinated knuckle dagger strikes (DC 19 basic Reflex save). The damage depends on the number of actions. ⬻ 1d6+2 piercing damage ⬺ 2d6+5 piercing damage ⬽ 3d6+7 piercing damage"
sourcebook: "_Battlecry!_, page 187."
```

```encounter-table
name: Orc Raiding Party
creatures:
  - 1: Orc Raiding Party
```
