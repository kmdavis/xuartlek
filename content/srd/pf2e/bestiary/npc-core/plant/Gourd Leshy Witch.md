---
noteType: pf2eMonster
aliases: "Gourd Leshy Witch"
tags:
  - pf2e/creature/level/6
  - pf2e/creature/trait/leshy
  - pf2e/creature/trait/plant
  - pf2e/creature/trait/small
statblock: inline
name: "Gourd Leshy Witch"
level: 6
source: "NPC Core"
aon_url: "https://2e.aonprd.com/NPCs.aspx?ID=3659"
socialImage: og-image.png
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "NPC"
name: "Gourd Leshy Witch"
level: "Creature 6"
size: "Small"
trait_01: "Leshy"
trait_02: "Plant"
modifier: 12
perception:
  - name: "Perception"
    desc: "+12; low-light vision"
languages: "[[srd/pf2e/compendium/rules-elements/Languages#Common|Common]], [[srd/pf2e/compendium/rules-elements/Languages#Fey|Fey]]; [[srd/pf2e/compendium/spells/rank-3/Speak with Plants|_speak with plants_]] (gourds only)"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/Acrobatics|Acrobatics]] +12, [[srd/pf2e/compendium/rules-elements/skills/Intimidation|Intimidation]] +13, [[srd/pf2e/compendium/rules-elements/skills/Nature|Nature]] +14, [[srd/pf2e/compendium/rules-elements/skills/Occultism|Occultism]] +16, [[srd/pf2e/compendium/rules-elements/skills/Survival|Survival]] +12"
abilityMods: [2, 2, 1, 4, 2, 1]
abilities_top:
  - name: "Items"
    desc: "_+1 broom_ (functions as a [[srd/pf2e/compendium/equipment/weapons/club/Staff|staff]]), Dagger"
ac: 22
armorclass:
  - name: "AC"
    desc: "22; __Fort__: +11; __Ref__: +14; __Will__: +14"
hp: 80
health:
  - name: "HP"
    desc: "80"
abilities_mid:
  - name: "Verdant Burst"
    desc: "([[srd/pf2e/compendium/rules-elements/traits/player-core/Healing|healing]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Primal|primal]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Vitality|vitality]]) When the gourd leshy witch dies, a burst of primal energy explodes from their body, restoring 4d8 Hit Points to each plant creature in a 30-foot emanation. This area immediately sprouts gourds, becoming difficult terrain. If the terrain is not a viable environment for these plants, they wither after 24 hours."
speed: "25 feet"
attacks:
  - name: "Melee"
    desc: "⬻ _broom_ +13 ([[srd/pf2e/compendium/rules-elements/traits/player-core/Magical|Magical]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Two-Hand|two-hand 1d8]]) __Damage__ 1d4+6 bludgeoning plus 1d6 void"
  - name: "Melee"
    desc: "⬻ dagger +12 ([[srd/pf2e/compendium/rules-elements/traits/player-core/Agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Finesse|Finesse]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Versatile|versatile S]]) __Damage__ 1d4+6 piercing plus 1d6 void"
  - name: "Melee"
    desc: "⬻ fist +12 ([[srd/pf2e/compendium/rules-elements/traits/player-core/Agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Finesse|Finesse]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Nonlethal|Nonlethal]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Unarmed|Unarmed]]) __Damage__ 1d4+6 bludgeoning plus 1d6 void"
  - name: "Ranged"
    desc: "⬻ dagger +12 ([[srd/pf2e/compendium/rules-elements/traits/player-core/Agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Finesse|Finesse]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Thrown|thrown 10 feet]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Versatile|versatile S]]) __Damage__ 1d4+6 piercing plus 1d6 void"
abilities_bot:
  - name: "Witch Hex Spells"
    desc: "DC 24, 1 Focus Point - __3rd__ [[srd/pf2e/compendium/spells/cantrips/Wilding Word|Wilding Word]]"
  - name: "Change Shape"
    desc: "⬻ ([[srd/pf2e/compendium/rules-elements/traits/player-core/Concentrate|Concentrate]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Polymorph|Polymorph]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Plant|primal The gourd leshy witch transforms into a Small gourd. This ability otherwise uses the effects of _one with plants_.]])"
  - name: "Short Flight"
    desc: "([[srd/pf2e/compendium/rules-elements/traits/player-core/Concentrate|Concentrate]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Occult|Occult]])"
  - name: "Frequency"
    desc: "once per round"
  - name: "Requirements"
    desc: "The gourd leshy witch is wielding a broom"
  - name: "Effect"
    desc: "The gourd leshy hops on their broom, which briefly takes flight. The witch [[srd/pf2e/compendium/rules-elements/actions/player-core#Fly|Flies]] 20 feet (or 40 feet if they spend 2 actions), though they must end this movement on solid ground or fall at the end of their turn."
  - name: "Sweeping Spell"
    desc: "⬻ ([[srd/pf2e/compendium/rules-elements/traits/player-core/Manipulate|Manipulate]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Occult|Occult]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Spellshape|Spellshape]])"
  - name: "Requirements"
    desc: "The gourd leshy witch is wielding their broom"
  - name: "Effect"
    desc: "If the next action the gourd leshy witch uses is to cast a non-[[srd/pf2e/compendium/rules-elements/traits/player-core/Cantrip|cantrip]] spell that deals damage to a single target, the witch's broom flies out and attempts to [[srd/pf2e/compendium/rules-elements/actions/player-core#Shove|Shove]] that creature with an [[srd/pf2e/compendium/rules-elements/skills/Athletics|Athletics]] modifier of +16. On a critical success, the target is also knocked [[srd/pf2e/compendium/rules-elements/Conditions#Prone|prone]]. The broom immediately returns to the gourd leshy witch's hand."
spellcasting:
  - name: "Occult Prepared Spells"
    desc: "DC 24, attack +16 - __Cantrips (3rd)__ [[srd/pf2e/compendium/spells/cantrips/Daze|Daze]], [[srd/pf2e/compendium/spells/cantrips/Detect Magic|Detect Magic]], [[srd/pf2e/compendium/spells/cantrips/Figment|Figment]], [[srd/pf2e/compendium/spells/cantrips/Shield|Shield]], [[srd/pf2e/compendium/spells/cantrips/Void Warp|Void Warp]] - __1st__ [[srd/pf2e/compendium/spells/rank-1/Fear|Fear]] (×2), [[srd/pf2e/compendium/spells/rank-1/Ill Omen|Ill Omen]] - __2nd__ [[srd/pf2e/compendium/spells/rank-1/Force Barrage|Force Barrage]], [[srd/pf2e/compendium/spells/rank-1/Grim Tendrils|Grim Tendrils]], [[srd/pf2e/compendium/spells/rank-2/Paranoia|Paranoia]] - __3rd__ [[srd/pf2e/compendium/spells/rank-1/Force Barrage|Force Barrage]], [[srd/pf2e/compendium/spells/rank-3/Slow|Slow]], [[srd/pf2e/compendium/spells/rank-3/Vampiric Feast|Vampiric Feast]]"
  - name: "Primal Innate Spells"
    desc: "DC 24 - __Constant (3rd)__ [[srd/pf2e/compendium/spells/rank-3/Speak with Plants|Speak with Plants]] (gourds only)"
sourcebook: "_NPC Core_, page 202."
```

```encounter-table
name: Gourd Leshy Witch
creatures:
  - 1: Gourd Leshy Witch
```
