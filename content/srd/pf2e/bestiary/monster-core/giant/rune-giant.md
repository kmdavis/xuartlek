---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Rune Giant"
tags:
  - pf2e/creature/level/16
  - pf2e/creature/trait/giant
  - pf2e/creature/trait/humanoid
  - pf2e/creature/trait/unholy
  - pf2e/creature/trait/gargantuan
statblock: inline
name: "Rune Giant"
level: 16
source: "Monster Core"
aon_id: "creature-3017"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=3017"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC"
name: "Rune Giant"
level: "Creature 16"
size: "Gargantuan"
trait_01: "Giant"
trait_02: "Humanoid"
trait_03: "Unholy"
modifier: 28
perception:
  - name: "Perception"
    desc: "Perception +28; low-light vision"
languages: "[[srd/pf2e/compendium/rules-elements/languages#Common|Common]], [[srd/pf2e/compendium/rules-elements/languages#Jotun|Jotun]], [[srd/pf2e/compendium/rules-elements/languages#Petran|Petran]]"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/arcana|Arcana]] +28, [[srd/pf2e/compendium/rules-elements/skills/athletics|Athletics]] +32, [[srd/pf2e/compendium/rules-elements/skills/crafting|Crafting]] +28, [[srd/pf2e/compendium/rules-elements/skills/intimidation|Intimidation]] +28, [[srd/pf2e/compendium/rules-elements/skills/society|Society]] +27"
abilityMods: [9, 2, 7, 2, 6, 4]
abilities_top:
  - name: "Items"
    desc: "_+2 [[srd/pf2e/compendium/equipment/runes/striking-major|greater striking]] [[srd/pf2e/compendium/equipment/weapons/sword/greatsword|greatsword]]_, _+1 [[srd/pf2e/compendium/equipment/runes/striking-major|striking]] [[srd/pf2e/compendium/equipment/weapons/spear/longspear|longspear]]_, _+1 [[srd/pf2e/compendium/equipment/armor#Splint Mail|splint mail]]_"
ac: 38
armorclass:
  - name: "AC"
    desc: "38; __Fort__: +33; __Ref__: +26; __Will__: +28"
hp: 330
health:
  - name: "HP"
    desc: "330; __Immunities__ [[srd/pf2e/compendium/rules-elements/traits/player-core/fire|fire]]"
abilities_mid:
  - name: "Reactive Strike"
    desc: "⬲ The rune giant gains an additional reaction at the beginning of each of their turns that they can use only for a Reactive Strike."
speed: "45 feet; fly 45 feet"
attacks:
  - name: "Melee"
    desc: "⬻ _greatsword_ +33 ([[srd/pf2e/compendium/rules-elements/traits/player-core/magical|Magical]], [[srd/pf2e/compendium/rules-elements/traits/player-core/reach|reach 20 feet]], [[srd/pf2e/compendium/rules-elements/traits/player-core/versatile|versatile P]]) __Damage__ 3d12+17 slashing"
  - name: "Melee"
    desc: "⬻ _longspear_ +32 ([[srd/pf2e/compendium/rules-elements/traits/player-core/magical|Magical]], [[srd/pf2e/compendium/rules-elements/traits/player-core/reach|reach 25 feet]]) __Damage__ 2d8+17 piercing"
  - name: "Melee"
    desc: "⬻ fist +31 ([[srd/pf2e/compendium/rules-elements/traits/player-core/agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/reach|reach 20 feet]]) __Damage__ 3d8+17 bludgeoning"
abilities_bot:
  - name: "Command Giants"
    desc: "When a rune giant casts a [[srd/pf2e/compendium/rules-elements/traits/player-core/mental|mental]] spell against another [[srd/pf2e/compendium/rules-elements/traits/player-core/giant|giant]], the DC is 39, rather than 35."
  - name: "Demand"
    desc: "⭓ ([[srd/pf2e/compendium/rules-elements/traits/player-core/arcane|Arcane]], [[srd/pf2e/compendium/rules-elements/traits/player-core/mental|Mental]]) When a rune giant casts their innate [[srd/pf2e/compendium/spells/rank-5/sending|_sending_]] spell, they can also cast [[srd/pf2e/compendium/spells/rank-4/suggestion|_suggestion_]] on the target."
  - name: "Flashing Runes"
    desc: "⭓ ([[srd/pf2e/compendium/rules-elements/traits/player-core/arcane|Arcane]], [[srd/pf2e/compendium/rules-elements/traits/player-core/light|Light]])"
  - name: "Trigger"
    desc: "The rune giant uses an arcane ability or casts an arcane spell"
  - name: "Effect"
    desc: "The runes on the giant's body flash with magical energy. Each creature within a 10-foot emanation must attempt a DC 35 Fortitude save."
  - name: "Critical Success"
    desc: "The creature is unaffected."
  - name: "Success"
    desc: "The creature is [[srd/pf2e/compendium/rules-elements/conditions#Dazzled|dazzled]] for 1 round."
  - name: "Failure"
    desc: "The creature is [[srd/pf2e/compendium/rules-elements/conditions#Blinded|blinded]] for 1 round."
  - name: "Invoke Rune"
    desc: "⬻ ([[srd/pf2e/compendium/rules-elements/traits/player-core/arcane|Arcane]], [[srd/pf2e/compendium/rules-elements/traits/player-core/concentrate|Concentrate]], [[srd/pf2e/compendium/rules-elements/traits/player-core/electricity|Electricity]]) The rune giant invokes one of the runes on their body, causing the rune to spray forth a 30-foot cone of sparks that deals 6d12 electricity damage to all creatures in the cone (DC 37 basic Reflex save). The giant can't use Invoke Rune again for 1d4 rounds. A glowing copy of the invoked rune appears on a single weapon the giant holds, granting the weapon one effect listed below of the giant's choice. The effect on the weapon lasts for 1 minute. If the giant places a new rune on a weapon, any previously placed rune immediately vanishes, ending its effect."
  - name: "Rune of Destruction"
    desc: "The weapon gains the [[srd/pf2e/compendium/rules-elements/traits/player-core/deadly|deadly]] trait with three weapon damage dice of the same die size as for the base weapon, and a creature hit with the weapon is [[srd/pf2e/compendium/rules-elements/conditions#Drained|drained 1]] unless it succeeds at a DC 35 Fortitude save."
  - name: "Rune of Flames"
    desc: "The weapon deals an additional 3d6 fire damage on all attacks."
  - name: "Rune of Smiting"
    desc: "When the weapon hits, the giant can Push the target back 10 feet, or 20 feet on a critical hit."
  - name: "Rune of Space"
    desc: "During the rune giant's turn, the weapon's [[srd/pf2e/compendium/rules-elements/traits/player-core/reach|reach]] is increased to 60 feet."
  - name: "Wide Swing"
    desc: "⬻ The rune giant makes a single greatsword Strike and compares the attack roll result to the ACs of up to two foes within their reach. This counts as two attacks for the giant's multiple attack penalty. The First Rune Giants On Golarion, the first rune giants were created by the powerful rulers of the ancient nation of Thassilon. The runelords gifted rune giants their ability to control other giants, using them to command armies of oversized builders and soldiers to create and defend oversized structures."
spellcasting:
  - name: "Arcane Innate Spells"
    desc: "DC 35 - __4th__ [[srd/pf2e/compendium/spells/rank-1/charm|Charm]] (at will), [[srd/pf2e/compendium/spells/rank-4/suggestion|Suggestion]] (at will) - __5th__ [[srd/pf2e/compendium/spells/rank-5/sending|Sending]] - __6th__ [[srd/pf2e/compendium/spells/rank-6/dominate|Dominate]] (×3), [[srd/pf2e/compendium/spells/rank-6/truesight|Truesight]] - __8th__ [[srd/pf2e/compendium/spells/rank-1/charm|Charm]], [[srd/pf2e/compendium/spells/rank-4/suggestion|Suggestion]] - __Constant (7th)__ [[srd/pf2e/compendium/spells/rank-4/fly|Fly]]"
sourcebook: "_Monster Core_, page 169."
```

```encounter-table
name: Rune Giant
creatures:
  - 1: Rune Giant
```
