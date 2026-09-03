---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Ore Louse"
tags:
  - pf2e/creature/level/5
  - pf2e/creature/trait/amphibious
  - pf2e/creature/trait/beast
  - pf2e/creature/trait/water
  - pf2e/creature/trait/medium
statblock: inline
name: "Ore Louse"
level: 5
source: "Rage of Elements"
aon_id: "creature-2665"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=2665"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "RoE"
name: "Ore Louse"
level: "Creature 5"
size: "Medium"
trait_01: "Amphibious"
trait_02: "Beast"
trait_03: "Water"
modifier: 14
perception:
  - name: "Perception"
    desc: "Perception +14; darkvision, metal scent 30 feet, wavesense 120 feet (imprecise)"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/athletics|Athletics]] +12"
abilityMods: [1, 4, 2, -2, 3, 0]
abilities_top:
  - name: "Metal Scent"
    desc: "An ore louse can smell metal as a precise sense."
ac: 22
armorclass:
  - name: "AC"
    desc: "22; __Fort__: +13; __Ref__: +15; __Will__: +10"
hp: 60
health:
  - name: "HP"
    desc: "60"
speed: "35 feet, swim 60 feet; water stride"
attacks:
  - name: "Melee"
    desc: "⬻ mandibles +14 ([[srd/pf2e/compendium/rules-elements/traits/player-core/finesse|Finesse]]) __Damage__ 2d8+4 piercing plus rust and metal snack"
  - name: "Melee"
    desc: "⬻ leg +14 ([[srd/pf2e/compendium/rules-elements/traits/player-core/finesse|Finesse]], [[srd/pf2e/compendium/rules-elements/traits/player-core/reach|10 feet reach]]) __Damage__ 2d8+4 bludgeoning plus Knockdown"
  - name: "Melee"
    desc: "⬻ oxidizing spit +14 (range increment 20 feet) __Damage__ 2d8 acid plus rust"
abilities_bot:
  - name: "Consume Living Metal"
    desc: "⬻ ([[srd/pf2e/compendium/rules-elements/traits/player-core/manipulate|Manipulate]])"
  - name: "Requirements"
    desc: "The ore louse is adjacent to a creature that died within the last hour and had the [[srd/pf2e/compendium/rules-elements/traits/player-core/metal|metal]] trait or was another ore louse"
  - name: "Effect"
    desc: "An ore louse can replenish its health by eating the remains of its kin or a once-living metal creature. The ore louse feasts upon the corpse, regaining 3d6 Hit Points. The ore louse can regain Hit Points from a given corpse only once."
  - name: "Metal Snack"
    desc: "An ore louse gains 5 temporary Hit Points each time its mandibles Strike either damages or breaks a metal item using its rust ability, or if it hits a creature that has the [[srd/pf2e/compendium/rules-elements/traits/player-core/metal|metal]] trait or is made of metal."
  - name: "Rust"
    desc: "An ore louse's Strikes causes metal to rapidly rust and corrode. If it succeeds at a mandibles or oxidizing spit Strike, the ore louse deals 3d6 damage (or double damage on a critical hit) to a metal item the target is wearing or holding, ignoring its Hardness. If the ore louse hits an unattended metal item, the item takes this damage automatically. If a creature uses the Shield Block reaction with a metal shield against the attacks, the shield is automatically [[srd/pf2e/compendium/rules-elements/conditions#Broken|broken]], but no other item is rusted on that attack."
  - name: "Water Stride"
    desc: "The ore louse can stand and move on the surface of water or other liquids without falling through. The ore louse can go underwater if it wishes, but it must Swim to do so. Ore Louse Boots Due to their ability to walk on water, numerous attempts have been made to use ore louse legs to produce footwear. Techniques tested so far include hollowing out the chitin or harvesting and refining the fine leg spikes. None of these attempts have succeeded as of yet."
sourcebook: "_Rage of Elements_, page 185."
```

```encounter-table
name: Ore Louse
creatures:
  - 1: Ore Louse
```
