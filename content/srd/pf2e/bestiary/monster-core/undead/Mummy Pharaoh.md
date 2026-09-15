---
noteType: pf2eMonster
aliases: "Mummy Pharaoh"
tags:
  - pf2e/creature/level/9
  - pf2e/creature/trait/mummy
  - pf2e/creature/trait/rare
  - pf2e/creature/trait/undead
  - pf2e/creature/trait/unholy
  - pf2e/creature/trait/medium
statblock: inline
name: "Mummy Pharaoh"
level: 9
source: "Monster Core"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=3102"
socialImage: og-image.png
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC"
name: "Mummy Pharaoh"
level: "Creature 9"
size: "Medium"
trait_01: "Mummy"
trait_02: "Rare"
trait_03: "Undead"
trait_04: "Unholy"
modifier: 20
perception:
  - name: "Perception"
    desc: "+20; darkvision"
languages: "[[srd/pf2e/compendium/rules-elements/Languages#Necril|Necril]]; plus any two languages they knew while alive"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/Deception|Deception]] +18, [[srd/pf2e/compendium/rules-elements/skills/Intimidation|Intimidation]] +20, [[srd/pf2e/compendium/rules-elements/skills/Occultism|Occultism]] +15, [[srd/pf2e/compendium/rules-elements/skills/Religion|Religion]] +20, [[srd/pf2e/compendium/rules-elements/skills/Stealth|Stealth]] +13"
abilityMods: [5, 2, 4, 0, 5, 5]
abilities_top:
  - name: "Rejuvenation"
    desc: "([[srd/pf2e/compendium/rules-elements/traits/player-core/Divine|divine]]) When a mummy pharaoh is destroyed, necromantic energies rebuild its body in its tomb over 1d10 days. If the body is destroyed during that time, the process starts anew. A reforming mummy pharaoh is destroyed permanently if their tomb is [[srd/pf2e/compendium/spells/rituals/Consecrate|_consecrated_]]."
  - name: "Items"
    desc: "_+1 [[srd/pf2e/compendium/equipment/runes/Striking|striking]] [[srd/pf2e/compendium/equipment/weapons/spear/Longspear|longspear]]_"
ac: 27
armorclass:
  - name: "AC"
    desc: "27; __Fort__: +19; __Ref__: +15; __Will__: +20 +1 status to all saves vs. [[srd/pf2e/compendium/rules-elements/traits/player-core/Vitality|vitality]]"
hp: 175
health:
  - name: "HP"
    desc: "175 (sacred wrappings, void healing); __Immunities__ bleed, [[srd/pf2e/compendium/rules-elements/traits/player-core/Death|death]] effects, [[srd/pf2e/compendium/rules-elements/traits/player-core/Disease|disease]], [[srd/pf2e/compendium/rules-elements/Conditions#Paralyzed|paralyzed]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Poison|poison]], [[srd/pf2e/compendium/rules-elements/Conditions#Unconscious|unconscious]]; __Weaknesses__ [[srd/pf2e/compendium/rules-elements/traits/player-core/Fire|fire]] 10, [[srd/pf2e/compendium/rules-elements/traits/player-core/Water|water]] 10"
abilities_mid:
  - name: "Undead Mastery"
    desc: "([[srd/pf2e/compendium/rules-elements/traits/player-core/Aura|aura]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Divine|divine]]) 100 feet. Commanded or allied [[srd/pf2e/compendium/rules-elements/traits/player-core/Undead|undead]] in the aura that have a lower level than the mummy pharaoh gain a +1 circumstance bonus to attack rolls, damage rolls, AC, saves, and skill checks."
  - name: "Reactive Strike"
    desc: "⬲ The mummy pharaoh can use Reactive Strike when a creature within its reach uses a [[srd/pf2e/compendium/rules-elements/traits/player-core/Concentrate|concentrate]] action, in addition to its normal trigger. It can disrupt triggering concentrate actions, and it disrupts actions on any hit, not just a critical hit."
  - name: "Sacred Wrappings"
    desc: "([[srd/pf2e/compendium/rules-elements/traits/player-core/Divine|divine]]) When a creature deals physical damage to the pharaoh or triggers one of the pharaoh's weaknesses, it must succeed at a DC 28 Will save or become [[srd/pf2e/compendium/rules-elements/Conditions#Doomed|doomed 1]]. Regardless of the results of the save, the creature is then immune to that mummy's sacred wrappings for 24 hours."
speed: "20 feet"
attacks:
  - name: "Melee"
    desc: "⬻ _longspear_ +21 ([[srd/pf2e/compendium/rules-elements/traits/player-core/Magical|Magical]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Reach|reach 10 feet]]) __Damage__ 2d8+11 piercing plus 1d6 void"
  - name: "Melee"
    desc: "⬻ fist +20 ([[srd/pf2e/compendium/rules-elements/traits/player-core/Agile|Agile]]) __Damage__ 1d10+11 bludgeoning plus 1d6 void"
abilities_bot:
  - name: "Sandstorm Wrath"
    desc: "⬺ ([[srd/pf2e/compendium/rules-elements/traits/player-core/Concentrate|Concentrate]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Divine|Divine]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Earth|Earth]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Fire|Fire]]) The mummy pharaoh exhales a 60-foot cone of superheated sand that deals 5d6 fire and 5d6 slashing damage (DC 28 basic Reflex save). The mummy pharaoh can't use Sandstorm Wrath again for 1d4 rounds."
  - name: "Veil of Sand"
    desc: "⬻ ([[srd/pf2e/compendium/rules-elements/traits/player-core/Aura|Aura]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Divine|Divine]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Earth|Earth]]) Sand whirls around the mummy pharaoh in a 5-foot emanation until the beginning of their next turn. Creatures inside the sand are [[srd/pf2e/compendium/rules-elements/Conditions#Concealed|concealed]] to those outside it and any living creature ending its turn within the sand takes 4d6 slashing damage with a DC 28 basic Fortitude save. Veil of Sand ends if the mummy takes damage from their water weakness."
sourcebook: "_Monster Core_, page 235."
```

```encounter-table
name: Mummy Pharaoh
creatures:
  - 1: Mummy Pharaoh
```
