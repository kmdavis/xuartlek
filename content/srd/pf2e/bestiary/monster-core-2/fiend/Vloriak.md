---
noteType: pf2eMonster
aliases: "Vloriak"
tags:
  - pf2e/creature/level/5
  - pf2e/creature/trait/demon
  - pf2e/creature/trait/fiend
  - pf2e/creature/trait/unholy
  - pf2e/creature/trait/medium
statblock: inline
name: "Vloriak"
level: 5
source: "Monster Core 2"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=4319"
socialImage: og-image.png
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC2"
name: "Vloriak"
level: "Creature 5"
size: "Medium"
trait_01: "Demon"
trait_02: "Fiend"
trait_03: "Unholy"
modifier: 13
perception:
  - name: "Perception"
    desc: "+13; darkvision"
languages: "[[srd/pf2e/compendium/rules-elements/Languages#Chthonian|Chthonian]], [[srd/pf2e/compendium/rules-elements/Languages#Empyrean|Empyrean]], [[srd/pf2e/compendium/rules-elements/Languages#Talican|Talican]]; telepathy 100 feet"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/Athletics|Athletics]] +13, [[srd/pf2e/compendium/rules-elements/skills/Intimidation|Intimidation]] +12"
abilityMods: [4, 2, 4, -1, 4, 3]
ac: 21
armorclass:
  - name: "AC"
    desc: "21; __Fort__: +15; __Ref__: +11; __Will__: +13 +1 status to all saves vs. magic"
hp: 90
health:
  - name: "HP"
    desc: "90; __Resistances__ [[srd/pf2e/compendium/rules-elements/traits/player-core/Acid|acid]] 5; __Weaknesses__ [[srd/pf2e/compendium/equipment/materials/Cold Iron|cold iron]] 5, [[srd/pf2e/compendium/rules-elements/traits/player-core/Holy|holy]] 5"
abilities_mid:
  - name: "Restoration Vulnerability"
    desc: "A vloriak feels agonizing pain when a creature or object recovers from a debilitating effect in their proximity. The first time in a round in which a creature that is within sight of the demon reduces the value of their [[srd/pf2e/compendium/rules-elements/Conditions#Clumsy|clumsy]], [[srd/pf2e/compendium/rules-elements/Conditions#Enfeebled|enfeebled]], [[srd/pf2e/compendium/rules-elements/Conditions#Sickened|sickened]], or [[srd/pf2e/compendium/rules-elements/Conditions#Stupefied|stupefied]] condition, the demon takes 3d6 mental damage and cannot Lick Rust on their next turn."
speed: "25 feet"
attacks:
  - name: "Melee"
    desc: "⬻ claw +15 ([[srd/pf2e/compendium/rules-elements/traits/player-core/Unholy|Unholy]]) __Damage__ 2d6+6 slashing plus 1d6 spirit"
  - name: "Melee"
    desc: "⬻ tongue +15 ([[srd/pf2e/compendium/rules-elements/traits/player-core/Agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Reach|reach 10 feet]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Unholy|unholy]]) __Damage__ 2d6+2 acid plus 1d6 spirit and rust"
abilities_bot:
  - name: "Lick Rust"
    desc: "⬻ ([[srd/pf2e/compendium/rules-elements/traits/player-core/Attack|Attack]])"
  - name: "Requirements"
    desc: "The vloriak rusted a metal item with their tongue this turn"
  - name: "Effect"
    desc: "The vloriak attempts a tongue [[srd/pf2e/compendium/rules-elements/actions/player-core#Strike|Strike]] on the same target they just attacked. If it hits, it deals no damage as the demon licks away the rust and regains 2d6 Hit Points (or 4d6 Hit Points if the Strike was a critical hit). The vloriak can't Lick Rust on their next turn."
  - name: "Rust"
    desc: "A vloriak's saliva causes metal to rust rapidly. If they succeed at a tongue [[srd/pf2e/compendium/rules-elements/actions/player-core#Strike|Strike]] or [[srd/pf2e/compendium/rules-elements/actions/player-core#Disarm|Disarm]] attempt, the vloriak deals 2d6 acid damage (doubled on a critical hit) to a metal item the target is wearing or holding, ignoring its [[srd/pf2e/books/player-core/chapter-6-equipment/Shields#Hardness|Hardness]]. If the vloriak hits an unattended metal item, the item takes this damage automatically. If a creature uses the Shield Block reaction with a metal shield against a tongue attack, the shield is automatically [[srd/pf2e/compendium/rules-elements/Conditions#Broken|broken]], but no other item is rusted on that attack."
  - name: "Spew Rusted Shards"
    desc: "⬺ ([[srd/pf2e/compendium/rules-elements/traits/player-core/Divine|Divine]]) The vloriak spews a 15-foot [[srd/pf2e/books/player-core/chapter-8-playing-the-game/Area#Cone|cone]] of acid and rusted metal. Creatures in the area take 3d6 acid and 3d6 piercing damage (DC 22 [[srd/pf2e/books/player-core/chapter-8-playing-the-game/Checks#Basic Saving Throws|basic]] Reflex save). A creature that takes any piercing damage is exposed to [[srd/pf2e/compendium/gm/Diseases#Tetanus|tetanus]]. The vloriak can't Spew Rusted Shards for 1d4 rounds. Vlorian Influence Vloriaks hail from the [[srd/pf2e/compendium/gm/Planes#Outer Rifts|Outer Rifts]] realm of Vlorus, and as such, carry within themselves the potential for decay and rusting ruin. Other creatures that dwell in Vlorus—particularly fiends who rise to power there—can gain similar powers over rust as well. [[srd/pf2e/compendium/gm/creature-families/Qlippoth|Qlippoth]] are especially suited to this realm."
spellcasting:
  - name: "Divine Innate Spells"
    desc: "DC 22, attack +14 - __Cantrips (3rd)__ [[srd/pf2e/compendium/spells/cantrips/Caustic Blast|Caustic Blast]] - __2nd__ [[srd/pf2e/compendium/spells/rank-2/Acid Grip|Acid Grip]] (×3), [[srd/pf2e/compendium/spells/rank-2/Shatter|Shatter]] - __3rd__ [[srd/pf2e/compendium/spells/rank-3/Paralyze|Paralyze]]"
sourcebook: "_Monster Core 2_, page 91."
```

```encounter-table
name: Vloriak
creatures:
  - 1: Vloriak
```
