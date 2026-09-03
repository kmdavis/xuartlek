---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Drainberry Bush"
tags:
  - pf2e/creature/level/7
  - pf2e/creature/trait/plant
  - pf2e/creature/trait/uncommon
  - pf2e/creature/trait/large
statblock: inline
name: "Drainberry Bush"
level: 7
source: "Monster Core 2"
aon_id: "creature-4373"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=4373"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC2"
name: "Drainberry Bush"
level: "Creature 7"
size: "Large"
trait_01: "Plant"
trait_02: "Uncommon"
modifier: 16
perception:
  - name: "Perception"
    desc: "Perception +16; lifesense 120 feet"
languages: "[[srd/pf2e/compendium/rules-elements/languages#Aklo|Aklo]], [[srd/pf2e/compendium/rules-elements/languages#Common|Common]], [[srd/pf2e/compendium/rules-elements/languages#Fey|Fey]]; (can't speak any language), telepathy 100 feet"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/acrobatics|Acrobatics]] +11, [[srd/pf2e/compendium/rules-elements/skills/athletics|Athletics]] +17, [[srd/pf2e/compendium/rules-elements/skills/diplomacy|Diplomacy]] +13, [[srd/pf2e/compendium/rules-elements/skills/nature|Nature]] +17, [[srd/pf2e/compendium/rules-elements/skills/stealth|Stealth]] +11"
abilityMods: [6, 2, 6, -2, 4, 2]
abilities_top:
  - name: "Nature Empathy"
    desc: "The drainberry bush can use [[srd/pf2e/compendium/rules-elements/skills/diplomacy|Diplomacy]] to [[srd/pf2e/compendium/rules-elements/actions/player-core#Make an Impression|Make an Impression]] on and make very simple [[srd/pf2e/compendium/rules-elements/actions/player-core#Request|Requests]] of animals and plant creatures."
ac: 23
armorclass:
  - name: "AC"
    desc: "23; __Fort__: +17; __Ref__: +13; __Will__: +13"
hp: 135
health:
  - name: "HP"
    desc: "135; __Resistances__ [[srd/pf2e/compendium/rules-elements/traits/player-core/void|void]] 10; __Weaknesses__ [[srd/pf2e/compendium/rules-elements/traits/player-core/fire|fire]] 5"
speed: "25 feet, climb 20 feet"
attacks:
  - name: "Melee"
    desc: "⬻ vine +17 ([[srd/pf2e/compendium/rules-elements/traits/player-core/reach|reach 20 feet]]) __Damage__ 2d8+10 bludgeoning plus Improved Grab"
abilities_bot:
  - name: "Blood Berries"
    desc: "The drainberry bush must drain blood from living creatures for sustenance. This causes clusters of bright red berries to grow among its branches. Each cluster of berries lasts for 1 day, and it typically has 1d6+3 clusters when encountered. When consumed, a cluster restores 2d8+10 Hit Points. This effect has the [[srd/pf2e/compendium/rules-elements/traits/player-core/healing|healing]] and [[srd/pf2e/compendium/rules-elements/traits/player-core/primal|primal]] traits. A creature can pluck a cluster of berries with a successful unarmed [[srd/pf2e/compendium/rules-elements/actions/player-core#Strike|Strike]] or [[srd/pf2e/compendium/rules-elements/skills/thievery|Thievery]] check against the bush's AC."
  - name: "Consume Berries"
    desc: "⬻ ([[srd/pf2e/compendium/rules-elements/traits/player-core/healing|Healing]], [[srd/pf2e/compendium/rules-elements/traits/player-core/primal|primal]], [[srd/pf2e/compendium/rules-elements/traits/player-core/vitality|vitality]]) The bush draws nourishment from one cluster of blood berries, regaining 2d8+10 Hit Points. That berry cluster wrinkles and dies."
  - name: "Drain Blood"
    desc: "⬻"
  - name: "Requirements"
    desc: "The drainberry bush has at least one living creature [[srd/pf2e/compendium/rules-elements/conditions#Grabbed|grabbed]] with one of its vines"
  - name: "Effect"
    desc: "The bush squeezes all creatures it has grabbed, its hollow thorns piercing flesh and siphoning blood. Each creature must succeed at a DC 25 Fortitude save or take 2d8+10 piercing damage and become [[srd/pf2e/compendium/rules-elements/conditions#Drained|drained]] 1 (double damage and drained 2 on a critical failure). For every creature damaged this way, a cluster of blood berries (see above) immediately grows along the bush's branches."
  - name: "Storm of Vines"
    desc: "⬺ The drainberry bush makes up to four vine Strikes, each against a different target. These attacks count toward the bush's multiple attack penalty, but the multiple attack penalty doesn't increase until after the bush makes all these attacks. Drainberry Collections As drainberry bushes sell their berries to others, they collect coins and small curios—such as a cameo depicting a fey noble, a lock of golden hair knotted in a complex pattern, or a ring inscribed “To my dearest Memdaria.” Not all of these baubles have monetary value, but those that don't certainly had emotional value to the original owner. Occasionally, a drainberry bush accepts intangible trade goods, such as odes celebrating the bush's grandeur."
sourcebook: "_Monster Core 2_, page 139."
```

```encounter-table
name: Drainberry Bush
creatures:
  - 1: Drainberry Bush
```
