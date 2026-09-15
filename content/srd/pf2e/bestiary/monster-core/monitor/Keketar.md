---
noteType: pf2eMonster
aliases: "Keketar"
tags:
  - pf2e/creature/level/17
  - pf2e/creature/trait/monitor
  - pf2e/creature/trait/protean
  - pf2e/creature/trait/large
statblock: inline
name: "Keketar"
level: 17
source: "Monster Core"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=3146"
socialImage: og-image.png
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC"
name: "Keketar"
level: "Creature 17"
size: "Large"
trait_01: "Monitor"
trait_02: "Protean"
modifier: 30
perception:
  - name: "Perception"
    desc: "+30; entropy sense (imprecise) 60 feet, darkvision"
languages: "[[srd/pf2e/compendium/rules-elements/Languages#Chthonian|Chthonian]], [[srd/pf2e/compendium/rules-elements/Languages#Empyrean|Empyrean]], Protean; telepathy 100 feet, [[srd/pf2e/compendium/spells/rank-5/Truespeech|_truespeech_]]"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/Acrobatics|Acrobatics]] +26, [[srd/pf2e/compendium/rules-elements/skills/Athletics|Athletics]] +33, [[srd/pf2e/compendium/rules-elements/skills/Deception|Deception]] +32, [[srd/pf2e/compendium/rules-elements/skills/Diplomacy|Diplomacy]] +34, [[srd/pf2e/compendium/rules-elements/skills/Intimidation|Intimidation]] +34, [[srd/pf2e/compendium/rules-elements/skills/Religion|Religion]] +30, [[srd/pf2e/compendium/rules-elements/skills/Stealth|Stealth]] +30"
abilityMods: [8, 5, 7, 5, 7, 7]
abilities_top:
  - name: "Entropy Sense"
    desc: "([[srd/pf2e/compendium/rules-elements/traits/player-core/Divine|divine]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Prediction|prediction]]) A protean can anticipate the most likely presence of a creature through a supernatural insight into chaotic probabilities and chance. This grants them the ability to sense creatures within the listed range. [[srd/pf2e/compendium/spells/rank-3/Veil of Privacy|_Veil of privacy_]] prevents a creature from being detected via entropy sense automatically (without a counteract check)."
ac: 40
armorclass:
  - name: "AC"
    desc: "40; __Fort__: +30; __Ref__: +28; __Will__: +34 +1 status to all saves vs. [[srd/pf2e/compendium/rules-elements/traits/player-core/Magical|magic]]"
hp: 260
health:
  - name: "HP"
    desc: "260 (fast healing 10); __Resistances__ precision 10, protean anatomy 25"
abilities_mid:
  - name: "Protean Anatomy"
    desc: "([[srd/pf2e/compendium/rules-elements/traits/player-core/Divine|divine]]) A protean's vital organs shift and change shape and position constantly. Immediately after the protean takes acid, electricity, or sonic damage, they gain the listed amount of resistance to that damage type. This lasts for 1 hour or until the next time the protean takes damage of one of the other types (in which case their resistance changes to match that type), whichever comes first. The protean is immune to [[srd/pf2e/compendium/rules-elements/traits/player-core/Polymorph|polymorph]] effects unless they're a willing target. If [[srd/pf2e/compendium/rules-elements/Conditions#Blinded|blinded]] or [[srd/pf2e/compendium/rules-elements/Conditions#Deafened|deafened]], the protean automatically recovers at the end of their next turn as new sensory organs grow to replace the compromised ones."
  - name: "Spatial Riptide"
    desc: "([[srd/pf2e/compendium/rules-elements/traits/player-core/Aura|aura]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Divine|divine]]) 30 feet. A creature using a [[srd/pf2e/compendium/rules-elements/traits/player-core/Teleportation|teleportation]] ability within the aura or arriving in it via teleportation must succeed at a DC 38 Fortitude save or wink out of existence for 1d4 rounds before completing the teleport. The creature can't act, sense anything, or be targeted. On a successful save, the creature completes the teleport normally but is [[srd/pf2e/compendium/rules-elements/Conditions#Stunned|stunned 1]]. Keketars are immune to this effect."
  - name: "Reactive Strike"
    desc: "⬲"
speed: "40 feet, fly 50 feet, swim 40 feet; unfettered movement"
attacks:
  - name: "Melee"
    desc: "⬻ jaws +33 ([[srd/pf2e/compendium/rules-elements/traits/player-core/Magical|Magical]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Reach|reach 10 feet]]) __Damage__ 3d12+16 piercing plus warpwave strike"
  - name: "Melee"
    desc: "⬻ claw +33 ([[srd/pf2e/compendium/rules-elements/traits/player-core/Agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Magical|Magical]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Reach|reach 10 feet]]) __Damage__ 2d12+16 slashing plus warpwave strike"
  - name: "Melee"
    desc: "⬻ tail +33 ([[srd/pf2e/compendium/rules-elements/traits/player-core/Reach|reach 15 feet]]) __Damage__ 2d12+16 bludgeoning plus Grab"
abilities_bot:
  - name: "Change Shape"
    desc: "⬻ ([[srd/pf2e/compendium/rules-elements/traits/player-core/Concentrate|Concentrate]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Divine|Divine]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Polymorph|Polymorph]]) The keketar can take the appearance of any Huge or smaller creature. This doesn't change their Speed or their attack and damage bonuses with their Strikes but might change the damage type their Strikes deal."
  - name: "Constrict"
    desc: "⬻ 1d10+15 bludgeoning, DC 42"
  - name: "Reshape Reality"
    desc: "([[srd/pf2e/compendium/rules-elements/traits/player-core/Concentrate|Concentrate]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Divine|Divine]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Polymorph|Polymorph]]) When the keketar casts [[srd/pf2e/compendium/spells/rank-4/Mirage|_mirage_]], they infuse the illusion with quasi-real substance. Creatures that do not disbelieve the illusion treat structures and terrain created through the spell as though they were real, ascending illusory stairs, becoming trapped by illusory quicksand, and so on."
  - name: "Warpwave Strike"
    desc: "([[srd/pf2e/compendium/rules-elements/traits/player-core/Divine|Divine]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Polymorph|Polymorph]]) A creature struck by a keketar's jaws or claw Strike must succeed at a DC 36 Fortitude save or be subject to a warpwave."
spellcasting:
  - name: "Divine Innate Spells"
    desc: "DC 42, attack +32 - __4th__ [[srd/pf2e/compendium/spells/rank-4/Confusion|Confusion]] (at will), [[srd/pf2e/compendium/spells/rank-4/Translocate|Translocate]] (at will), [[srd/pf2e/compendium/spells/rank-4/Unfettered Movement|Unfettered Movement]] - __5th__ [[srd/pf2e/compendium/spells/rank-4/Creation|Creation]] (at will), [[srd/pf2e/compendium/spells/rank-4/Mirage|Mirage]] (×2; see reshape reality), [[srd/pf2e/compendium/spells/rank-4/Translocate|Translocate]] - __6th__ [[srd/pf2e/compendium/spells/rank-6/Teleport|Teleport]] (at will; self only) - __7th__ [[srd/pf2e/compendium/spells/rank-6/Disintegrate|Disintegrate]], [[srd/pf2e/compendium/spells/rank-2/Dispel Magic|Dispel Magic]] (at will), [[srd/pf2e/compendium/spells/rank-2/Shatter|Shatter]] (at will), [[srd/pf2e/compendium/spells/rank-7/Warp Mind|Warp Mind]] (×3) - __8th__ [[srd/pf2e/compendium/spells/rank-4/Confusion|Confusion]], [[srd/pf2e/compendium/spells/rank-6/Cursed Metamorphosis|Cursed Metamorphosis]] - __9th__ [[srd/pf2e/compendium/spells/rank-4/Divine Wrath|Divine Wrath]], [[srd/pf2e/compendium/spells/rank-9/Unfathomable Song|Unfathomable Song]] - __Constant (5th)__ [[srd/pf2e/compendium/spells/rank-5/Truespeech|Truespeech]]"
sourcebook: "_Monster Core_, page 272."
```

```encounter-table
name: Keketar
creatures:
  - 1: Keketar
```
