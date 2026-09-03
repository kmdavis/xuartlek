---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Noxious Needler"
tags:
  - pf2e/creature/level/9
  - pf2e/creature/trait/alchemical
  - pf2e/creature/trait/construct
  - pf2e/creature/trait/mindless
  - pf2e/creature/trait/uncommon
  - pf2e/creature/trait/large
statblock: inline
name: "Noxious Needler"
level: 9
source: "Monster Core"
aon_id: "creature-3109"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=3109"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC"
name: "Noxious Needler"
level: "Creature 9"
size: "Large"
trait_01: "Alchemical"
trait_02: "Construct"
trait_03: "Mindless"
trait_04: "Uncommon"
modifier: 15
perception:
  - name: "Perception"
    desc: "Perception +15; darkvision"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/athletics|Athletics]] +22"
abilityMods: [6, 4, 3, -5, 0, -5]
ac: 27
armorclass:
  - name: "AC"
    desc: "27; __Fort__: +20; __Ref__: +19; __Will__: +15"
hp: 150
health:
  - name: "HP"
    desc: "150; __Immunities__ bleed, [[srd/pf2e/compendium/rules-elements/traits/player-core/death|death]] effects, [[srd/pf2e/compendium/rules-elements/traits/player-core/disease|disease]], [[srd/pf2e/compendium/rules-elements/conditions#Doomed|doomed]], [[srd/pf2e/compendium/rules-elements/conditions#Drained|drained]], [[srd/pf2e/compendium/rules-elements/conditions#Fatigued|fatigued]], [[srd/pf2e/compendium/rules-elements/traits/player-core/healing|healing]], [[srd/pf2e/compendium/rules-elements/traits/player-core/mental|mental]], [[srd/pf2e/compendium/rules-elements/traits/player-core/nonlethal|nonlethal]] attacks, [[srd/pf2e/compendium/rules-elements/conditions#Paralyzed|paralyzed]], [[srd/pf2e/compendium/rules-elements/traits/player-core/poison|poison]], [[srd/pf2e/compendium/rules-elements/conditions#Sickened|sickened]], [[srd/pf2e/compendium/rules-elements/traits/player-core/spirit|spirit]], [[srd/pf2e/compendium/rules-elements/conditions#Unconscious|unconscious]], [[srd/pf2e/compendium/rules-elements/traits/player-core/vitality|vitality]], [[srd/pf2e/compendium/rules-elements/traits/player-core/void|void]]; __Resistances__ physical 10 (except adamantine or bludgeoning), spells 10 (except [[srd/pf2e/compendium/rules-elements/traits/player-core/sonic|sonic]])"
abilities_mid:
  - name: "Alchemical Chambers"
    desc: "A noxious needler's body contains six alchemical chambers filled with different substances. When a noxious needler's ability calls upon a randomly determined alchemical effect, roll 1d6 and consult the following (if you roll the result of a chamber that was shattered, there is no alchemical effect): 1 acid damage; 2 cold damage; 3 electricity damage; 4 fire damage; 5 poison damage; 6 sickness, with a DC 26 Fortitude save or [[srd/pf2e/compendium/rules-elements/conditions#Sickened|sickened 1]] (sickened 2 on a critical failure)."
  - name: "Alchemical Rupture"
    desc: "When a noxious needler takes physical damage from a critical hit or is affected by a [[srd/pf2e/compendium/spells/rank-2/shatter|_shatter_]] spell, one glass chamber within its body shatters, spewing alchemical liquid in a 5-foot emanation. Roll on the alchemical chambers list (see above) to determine which one shatters—on a roll of 1–5, creatures in the area take 10d6 damage of the appropriate type (DC 28 basic Reflex). On a roll of 6, creatures must instead save against the sickness effect."
speed: "25 feet"
attacks:
  - name: "Melee"
    desc: "⬻ syringe +22 ([[srd/pf2e/compendium/rules-elements/traits/player-core/magical|Magical]], [[srd/pf2e/compendium/rules-elements/traits/player-core/reach|reach 10 feet]]) __Damage__ 2d10+6 piercing plus alchemical injection"
  - name: "Ranged"
    desc: "⬻ bomb +20 ([[srd/pf2e/compendium/rules-elements/traits/player-core/magical|Magical]], [[srd/pf2e/compendium/rules-elements/traits/player-core/thrown|thrown 20 feet]]) __Damage__ see Generate Bomb"
abilities_bot:
  - name: "Alchemical Injection"
    desc: "When a noxious needler hits a creature with a syringe Strike, roll 1d6 on the alchemical chambers list to determine the additional effect of the attack. The syringe deals an additional 2d6 damage of the appropriate type (or exposes the target to the sickness effect, as appropriate)."
  - name: "Generate Bomb"
    desc: "⬻ ([[srd/pf2e/compendium/rules-elements/traits/player-core/manipulate|Manipulate]]) The needler fills an empty vial from one of its alchemical chambers to create a bomb and then makes a bomb Strike. Roll 1d6 on the alchemical chambers list above. On a roll of 1–5, the bomb deals 3d10 damage and 3 [[srd/pf2e/compendium/rules-elements/traits/gm-core/splash|splash]] damage, matching the damage type of the chamber; you can instead choose to create an alchemical bomb of 11th level or lower that deals the same damage type, such as an [[srd/pf2e/compendium/equipment/alchemical-items/acid-flask|acid flask]] on a roll of 1. On a roll of 6, it creates a sickness bomb, which exposes the target and all creatures in the splash radius to the sickness effect; creatures hit by only the splash receive a +2 circumstance bonus to their Fortitude saves. Alchemical Leftovers When a noxious needler is defeated or disabled, each of its alchemical chambers that remains intact can be salvaged. The alchemical fluids inside are 50 gp worth of ingredients for crafting alchemical items."
sourcebook: "_Monster Core_, page 242."
```

```encounter-table
name: Noxious Needler
creatures:
  - 1: Noxious Needler
```
