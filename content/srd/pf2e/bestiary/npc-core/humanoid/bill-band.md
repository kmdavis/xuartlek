---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Bill-Band"
tags:
  - pf2e/creature/level/5
  - pf2e/creature/trait/halfling
  - pf2e/creature/trait/humanoid
  - pf2e/creature/trait/troop
  - pf2e/creature/trait/gargantuan
statblock: inline
name: "Bill-Band"
level: 5
source: "NPC Core"
aon_id: "creature-3645"
aon_url: "https://2e.aonprd.com/NPCs.aspx?ID=3645"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "NPC"
name: "Bill-Band"
level: "Creature 5"
size: "Gargantuan"
trait_01: "Halfling"
trait_02: "Humanoid"
trait_03: "Troop"
modifier: 10
perception:
  - name: "Perception"
    desc: "Perception +10; keen eyes"
languages: "Common, Halfling"
skills:
  - name: "Skills"
    desc: "Acrobatics +12, Athletics +13, Intimidation +13, Sports Lore +11"
abilityMods: [4, 3, 4, 0, -1, 2]
abilities_top:
  - name: "Keen Eyes"
    desc: "The halfling gains a +2 circumstance bonus when using the Seek action to find hidden or undetected creatures within 30 feet of them. Whenever the halfling targets a creature that is concealed or hidden from them, reduce the DC of the flat check to 3 for a concealed target or 9 for a hidden one."
ac: 20
armorclass:
  - name: "AC"
    desc: "20; __Fort__: +13; __Ref__: +12; __Will__: +8 +3 status vs. Intimidation checks"
hp: 90
health:
  - name: "HP"
    desc: "90 (4 segments); __Weaknesses__ area damage 5, splash damage 5"
abilities_mid:
  - name: "Troop Defenses"
    desc: ""
speed: "25 feet; overwhelming scrum, troop movement"
abilities_bot:
  - name: "Down to Our Level"
    desc: "⬺"
  - name: "Frequency"
    desc: "once per round"
  - name: "Effect"
    desc: "The bill-band deliberately gets under the feet of their opponents, proving they are greater than the sum of their parts. The bill-band attempts to Trip all creatures in or adjacent to their space. They roll one Athletics check and compare the result to the Reflex DC of each target."
  - name: "Firecracker Salvo"
    desc: "⬺"
  - name: "Frequency"
    desc: "once per round"
  - name: "Effect"
    desc: "The bill-band launches a barrage of lit firecrackers that, upon impact, burst into light and sound. Each creature in a 10-foot burst within 60 feet takes 1d12 sonic damage with a DC 19 basic Reflex save. A creature that fails its save is also dazzled for 1 round. When the bill-band is reduced to 2 or fewer segments, this area decreases to a 5-foot burst."
  - name: "Overwhelming Scrum"
    desc: "The bill-band swarms in and around other creatures. They can move into other creatures' spaces, and other creatures can move into their spaces. The bill-band's spaces are difficult terrain to other creatures. __Stick It to 'Em!__"
  - name: "Frequency"
    desc: "once per round"
  - name: "Effect"
    desc: "The bill-band swings barely coordinated fists and feet at each enemy in their space and in a 5-foot emanation, with a DC 19 basic Reflex save. The damage depends on the number of actions. ⬻ 1d6 bludgeoning damage ⬺ 2d6+4 bludgeoning damage ⬽ 3d6+6 bludgeoning damage."
sourcebook: "_NPC Core_, page 190."
```

```encounter-table
name: Bill-Band
creatures:
  - 1: Bill-Band
```
