---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Dragon Turtle"
tags:
  - pf2e/creature/level/9
  - pf2e/creature/trait/amphibious
  - pf2e/creature/trait/dragon
  - pf2e/creature/trait/huge
statblock: inline
name: "Dragon Turtle"
level: 9
source: "Monster Core"
aon_id: "creature-2956"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=2956"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC"
name: "Dragon Turtle"
level: "Creature 9"
size: "Huge"
trait_01: "Amphibious"
trait_02: "Dragon"
modifier: 18
perception:
  - name: "Perception"
    desc: "Perception +18; darkvision"
languages: "Common, Draconic, Thalassic"
skills:
  - name: "Skills"
    desc: "Athletics +21, Diplomacy +18, Intimidation +18, Stealth +13, Survival +17"
abilityMods: [6, 0, 4, 2, 4, 2]
ac: 29
armorclass:
  - name: "AC"
    desc: "29; __Fort__: +19; __Ref__: +15; __Will__: +17"
hp: 140
health:
  - name: "HP"
    desc: "140; __Immunities__ paralyzed, sleep"
abilities_mid:
  - name: "Shell Block"
    desc: "⬲"
  - name: "Trigger"
    desc: "A creature adjacent to the dragon turtle targets the turtle with a melee attack"
  - name: "Effect"
    desc: "The dragon turtle rolls their shell toward the triggering creature, gaining a +2 circumstance bonus to their AC against the triggering attack."
speed: "20 feet, swim 30 feet"
attacks:
  - name: "Melee"
    desc: "⬻ jaws +21 (reach 10 feet) __Damage__ 2d12+9 piercing"
  - name: "Melee"
    desc: "⬻ claw +21 (Agile) __Damage__ 2d8+9 slashing"
abilities_bot:
  - name: "Capsize"
    desc: "⬻ (Attack) The dragon turtle tries to capsize an adjacent aquatic vessel of their size or smaller. The dragon turtle must succeed at a DC 30 Athletics check (reduce the DC by 5 for each size smaller than the dragon turtle) or the pilot's Sailing Lore DC, whichever is higher."
  - name: "Conjure Storm"
    desc: "⬻ (Air, Aura, Primal, Water) The dragon turtle summons a mighty storm to rage around themself. The area in a 30-foot emanation around the turtle becomes difficult terrain for all other flying and swimming creatures. The dragon turtle can end the storm by taking this action again."
  - name: "Draconic Frenzy"
    desc: "⬺ The dragon turtle makes two claw Strikes and one jaws Strike in any order."
  - name: "Tsunami"
    desc: "⬺ (Primal, Water) The dragon turtle unleashes their destructive prowess by creating a massive growing wave that deals 7d6 bludgeoning damage in a 60-foot cone (DC 27 basic Reflex save). The wave's damage increases by 10 for creatures who are more than 30 feet away. A creature that fails its save is knocked prone. The dragon turtle can't use Tsunami again for 1d4 rounds. Dragon Turtle Rides Being offered a ride from a dragon turtle is a great honor. While they can provide emergency transportation with such a ride, a dragon turtle may offer one simply to enjoy the company of a dear friend or listen to the wisdom of a great sage."
sourcebook: "_Monster Core_, page 126."
```

```encounter-table
name: Dragon Turtle
creatures:
  - 1: Dragon Turtle
```
