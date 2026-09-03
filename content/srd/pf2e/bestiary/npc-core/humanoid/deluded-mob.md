---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Deluded Mob"
tags:
  - pf2e/creature/level/4
  - pf2e/creature/trait/human
  - pf2e/creature/trait/humanoid
  - pf2e/creature/trait/troop
  - pf2e/creature/trait/gargantuan
statblock: inline
name: "Deluded Mob"
level: 4
source: "NPC Core"
aon_id: "creature-3611"
aon_url: "https://2e.aonprd.com/NPCs.aspx?ID=3611"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "NPC"
name: "Deluded Mob"
level: "Creature 4"
size: "Gargantuan"
trait_01: "Human"
trait_02: "Humanoid"
trait_03: "Troop"
modifier: 7
perception:
  - name: "Perception"
    desc: "Perception +7"
languages: "Common"
skills:
  - name: "Skills"
    desc: "Athletics +12, Conspiracy Lore +6, Intimidation +9"
abilityMods: [6, 1, 4, 0, -1, 1]
abilities_top:
  - name: "Irrational"
    desc: "The deluded mob is severely disconnected from reality. Diplomacy checks to Make an Impression or otherwise sway their worldview automatically fail."
ac: 19
armorclass:
  - name: "AC"
    desc: "19; __Fort__: +12; __Ref__: +9; __Will__: +7 victim complex"
hp: 75
health:
  - name: "HP"
    desc: "75 (4 segments); __Weaknesses__ area damage 5, splash damage 5"
abilities_mid:
  - name: "Troop Defenses"
    desc: ""
  - name: "Victim Complex"
    desc: "As they lose members, the deluded mob takes the opposition against them as proof that they're right, bolstering their resolve. The deluded mob gains a +2 circumstance bonus to Will saves at 50 or fewer Hit Points, or a +4 circumstance bonus at 25 HP or fewer."
speed: "25 feet; troop movement"
abilities_bot:
  - name: "Flail Desperately"
    desc: ""
  - name: "Frequency"
    desc: "once per round"
  - name: "Effect"
    desc: "The deluded mob uses their fists, wooden planks, and anything else they can pick up to attack each enemy in a 5-foot emanation with fervor, if not coordination (DC 18 basic Reflex save). The damage depends on the number of actions. ⬻ 1d8 piercing or bludgeoning damage ⬺ 1d8+6 piercing or bludgeoning damage ⬽ 2d8+6 piercing or bludgeoning damage"
  - name: "Surrounded"
    desc: "When they feel cornered, the mob lashes out more recklessly. While the deluded mob is flanked, Flail Desperately and Throw Detritus are DC 17 and deal an additional 2 damage per action spent on the activity."
  - name: "Throw Detritus"
    desc: "⬺ The deluded mob hurls detritus in a 10-foot burst within 30 feet that deals 2d8 bludgeoning damage with a DC 18 basic Reflex save. When the mob is reduced to 2 or fewer segments, this area decreases to a 5-foot burst."
sourcebook: "_NPC Core_, page 155."
```

```encounter-table
name: Deluded Mob
creatures:
  - 1: Deluded Mob
```
