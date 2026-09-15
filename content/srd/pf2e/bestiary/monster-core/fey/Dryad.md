---
noteType: pf2eMonster
aliases: "Dryad"
tags:
  - pf2e/creature/level/3
  - pf2e/creature/trait/fey
  - pf2e/creature/trait/nymph
  - pf2e/creature/trait/plant
  - pf2e/creature/trait/wood
  - pf2e/creature/trait/medium
statblock: inline
name: "Dryad"
level: 3
source: "Monster Core"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=3112"
socialImage: og-image.png
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC"
name: "Dryad"
level: "Creature 3"
size: "Medium"
trait_01: "Fey"
trait_02: "Nymph"
trait_03: "Plant"
trait_04: "Wood"
modifier: 10
perception:
  - name: "Perception"
    desc: "+10; low-light vision"
languages: "[[srd/pf2e/compendium/rules-elements/Languages#Common|Common]], [[srd/pf2e/compendium/rules-elements/Languages#Elven|Elven]], [[srd/pf2e/compendium/rules-elements/Languages#Fey|Fey]], [[srd/pf2e/compendium/rules-elements/Languages#Muan|Muan]]"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/Acrobatics|Acrobatics]] +9, [[srd/pf2e/compendium/rules-elements/skills/Athletics|Athletics]] +5, [[srd/pf2e/compendium/rules-elements/skills/Crafting|Crafting]] +7, [[srd/pf2e/compendium/rules-elements/skills/Diplomacy|Diplomacy]] +9, [[srd/pf2e/compendium/rules-elements/skills/Nature|Nature]] +13, [[srd/pf2e/compendium/rules-elements/skills/Stealth|Stealth]] +9, [[srd/pf2e/compendium/rules-elements/skills/Survival|Survival]] +12"
abilityMods: [0, 4, 1, 2, 3, 4]
abilities_top:
  - name: "Nature Empathy"
    desc: "The dryad can ask questions of, receive answers from, and use the [[srd/pf2e/compendium/rules-elements/skills/Diplomacy|Diplomacy]] skill with [[srd/pf2e/compendium/rules-elements/traits/player-core/Animal|animals]] and [[srd/pf2e/compendium/rules-elements/traits/player-core/Plant|plants]]."
ac: 17
armorclass:
  - name: "AC"
    desc: "17; __Fort__: +6; __Ref__: +11; __Will__: +10"
hp: 55
health:
  - name: "HP"
    desc: "55; __Weaknesses__ cold iron 5, [[srd/pf2e/compendium/rules-elements/traits/player-core/Fire|fire]] 5"
abilities_mid:
  - name: "Tree Dependent"
    desc: "A dryad is bonded to a single great tree. If she is more than 300 feet away from it for 24 hours or more, she gains the weak adjustments until she returns. She can perform a 24-hour ritual to bond herself to a new tree."
speed: "25 feet"
attacks:
  - name: "Melee"
    desc: "⬻ branch +12 ([[srd/pf2e/compendium/rules-elements/traits/player-core/Finesse|Finesse]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Magical|Magical]]) __Damage__ 1d12+2 bludgeoning"
abilities_bot:
  - name: "Tree Meld"
    desc: "⬺ A [[srd/pf2e/compendium/spells/rank-2/One with Plants|_one with plants_]] spell cast by a dryad has an unlimited duration. In addition, if the dryad merges with her bonded tree, she can choose to instead enter an extradimensional living space within the tree, and can bring up to two adjacent, willing creatures with her; the spell gains the [[srd/pf2e/compendium/rules-elements/traits/player-core/Extradimensional|extradimensional]] trait. The dryad can still be expelled from this space."
spellcasting:
  - name: "Primal Innate Spells"
    desc: "DC 20, attack +12 - __Cantrips (2nd)__ [[srd/pf2e/compendium/spells/cantrips/Tangle Vine|Tangle Vine]] - __2nd__ [[srd/pf2e/compendium/spells/rank-2/Entangling Flora|Entangling Flora]] (at will), [[srd/pf2e/compendium/spells/rank-2/One with Plants|One with Plants]] (at will) - __4th__ [[srd/pf2e/compendium/spells/rank-1/Charm|Charm]] (×3), [[srd/pf2e/compendium/spells/rank-4/Suggestion|Suggestion]] - __5th__ [[srd/pf2e/compendium/spells/rank-5/Nature's Pathway|Nature's Pathway]] (×2)"
sourcebook: "_Monster Core_, page 244."
```

```encounter-table
name: Dryad
creatures:
  - 1: Dryad
```
