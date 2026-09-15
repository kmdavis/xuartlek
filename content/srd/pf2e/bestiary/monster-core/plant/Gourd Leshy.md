---
noteType: pf2eMonster
aliases: "Gourd Leshy"
tags:
  - pf2e/creature/level/1
  - pf2e/creature/trait/leshy
  - pf2e/creature/trait/plant
  - pf2e/creature/trait/small
statblock: inline
name: "Gourd Leshy"
level: 1
source: "Monster Core"
aon_url: "https://2e.aonprd.com/NPCs.aspx?ID=3080"
socialImage: og-image.png
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC"
name: "Gourd Leshy"
level: "Creature 1"
size: "Small"
trait_01: "Leshy"
trait_02: "Plant"
modifier: 5
perception:
  - name: "Perception"
    desc: "+5; low-light vision"
languages: "[[srd/pf2e/compendium/rules-elements/Languages#Common|Common]], [[srd/pf2e/compendium/rules-elements/Languages#Fey|Fey]]; [[srd/pf2e/compendium/spells/rank-3/Speak with Plants|_speak with plants_]] (gourds only)"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/Nature|Nature]] +5, [[srd/pf2e/compendium/rules-elements/skills/Stealth|Stealth]] +7"
abilityMods: [2, 4, 2, -1, 2, 0]
abilities_top:
  - name: "Keepsake"
    desc: "([[srd/pf2e/compendium/rules-elements/traits/player-core/Primal|primal]]) The leshy can store an item of light Bulk or less in their head, concealing it as [[srd/pf2e/compendium/spells/rank-3/Veil of Privacy|_veil of privacy_]]. If stored for 24 hours, the item benefits from [[srd/pf2e/compendium/spells/rank-1/Mending|_mending_]]."
ac: 17
armorclass:
  - name: "AC"
    desc: "17; __Fort__: +5; __Ref__: +9; __Will__: +7"
hp: 20
health:
  - name: "HP"
    desc: "20"
abilities_mid:
  - name: "Verdant Burst"
    desc: "([[srd/pf2e/compendium/rules-elements/traits/player-core/Healing|healing]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Primal|primal]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Vitality|vitality]]) When a gourd leshy dies, a burst of primal energy explodes from their body, restoring 1d8 Hit Points to each [[srd/pf2e/compendium/rules-elements/traits/player-core/Plant|plant]] creature in a 30-foot emanation. This area is filled with gourds, becoming difficult terrain. If the terrain is not a viable environment for these plants, they wither after 24 hours."
speed: "25 feet"
attacks:
  - name: "Melee"
    desc: "⬻ fist +7 ([[srd/pf2e/compendium/rules-elements/traits/player-core/Agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Finesse|Finesse]]) __Damage__ 1d4+2 bludgeoning plus ensnare"
  - name: "Ranged"
    desc: "⬻ seed +9 (range increment 30 feet) __Damage__ 1d6+2 bludgeoning plus ensnare"
abilities_bot:
  - name: "Change Shape"
    desc: "⬻ ([[srd/pf2e/compendium/rules-elements/traits/player-core/Concentrate|Concentrate]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Polymorph|Polymorph]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Primal|Primal]]) The leaf leshy transforms into a Small gourd-bearing plant. This ability otherwise uses the effects of [[srd/pf2e/compendium/spells/rank-2/One with Plants|_one with plants_]]."
  - name: "Ensnare"
    desc: "When the gourd leshy damages a creature with a fist or seed Strike, vines lash out from the leshy (or seed) and wrap around the target's limbs. The target must attempt a DC 17 Reflex save. On a failure, the target takes a –10-foot status penalty to its Speed for 1 round; on a critical failure, the target is [[srd/pf2e/compendium/rules-elements/Conditions#Immobilized|immobilized]] for 1 round and the penalty to Speed lasts for 1 minute."
spellcasting:
  - name: "Primal Innate Spells"
    desc: "DC 15 - __Constant (3rd)__ [[srd/pf2e/compendium/spells/rank-3/Speak with Plants|Speak with Plants]] (gourds only)"
sourcebook: "_Monster Core_, page 217."
```

```encounter-table
name: Gourd Leshy
creatures:
  - 1: Gourd Leshy
```
