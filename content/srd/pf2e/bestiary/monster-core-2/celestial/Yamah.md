---
noteType: pf2eMonster
aliases: "Yamah"
tags:
  - pf2e/creature/level/5
  - pf2e/creature/trait/azata
  - pf2e/creature/trait/celestial
  - pf2e/creature/trait/holy
  - pf2e/creature/trait/medium
statblock: inline
name: "Yamah"
level: 5
source: "Monster Core 2"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=4093"
socialImage: og-image.png
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC2"
name: "Yamah"
level: "Creature 5"
size: "Medium"
trait_01: "Azata"
trait_02: "Celestial"
trait_03: "Holy"
modifier: 12
perception:
  - name: "Perception"
    desc: "+12; darkvision, [[srd/pf2e/compendium/spells/cantrips/Detect Magic|_detect magic_]]"
languages: "[[srd/pf2e/compendium/rules-elements/Languages#Diabolic|Diabolic]], [[srd/pf2e/compendium/rules-elements/Languages#Draconic|Draconic]], [[srd/pf2e/compendium/rules-elements/Languages#Empyrean|Empyrean]]; [[srd/pf2e/compendium/spells/rank-5/Truespeech|_truespeech_]]"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/Acrobatics|Acrobatics]] +13, [[srd/pf2e/compendium/rules-elements/skills/Arcana|Arcana]] +10, [[srd/pf2e/compendium/rules-elements/skills/Deception|Deception]] +12, [[srd/pf2e/compendium/rules-elements/skills/Diplomacy|Diplomacy]] +12, [[srd/pf2e/compendium/rules-elements/skills/Religion|Religion]] +13, [[srd/pf2e/compendium/rules-elements/skills/Stealth|Stealth]] +13"
abilityMods: [3, 4, 2, 3, 4, 5]
abilities_top:
  - name: "Items"
    desc: "Starknife, _forceful quartz bracelet_ with 3 gems"
ac: 21
armorclass:
  - name: "AC"
    desc: "21; __Fort__: +9; __Ref__: +13; __Will__: +13"
hp: 75
health:
  - name: "HP"
    desc: "75; __Weaknesses__ cold iron 5, [[srd/pf2e/compendium/rules-elements/traits/player-core/Unholy|unholy]] 5"
abilities_mid:
  - name: "Free Mind"
    desc: "⬲ ([[srd/pf2e/compendium/rules-elements/traits/player-core/Mental|mental]])"
  - name: "Trigger"
    desc: "An ally of the yamah's attempts a saving throw against an effect that has the [[srd/pf2e/compendium/rules-elements/traits/player-core/Mental|mental]] trait"
  - name: "Effect"
    desc: "The ally's gains a +4 status bonus to the saving throw. If the ally rolls a success, they get a critical success instead."
speed: "25 feet, fly 70 feet"
attacks:
  - name: "Melee"
    desc: "⬻ _starknife_ +15 ([[srd/pf2e/compendium/rules-elements/traits/player-core/Agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Deadly|deadly d6]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Finesse|Finesse]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Holy|Holy]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Magical|Magical]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Thrown|thrown 20 feet]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Versatile|versatile S]]) __Damage__ 2d4+8 piercing"
  - name: "Ranged"
    desc: "⬻ _starknife_ +15 ([[srd/pf2e/compendium/rules-elements/traits/player-core/Agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Deadly|deadly d6]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Finesse|Finesse]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Holy|Holy]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Magical|Magical]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Thrown|thrown 20 feet]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Versatile|versatile S]]) __Damage__ 2d4+8 piercing"
abilities_bot:
  - name: "Crystallized Attack"
    desc: "⭓ ([[srd/pf2e/compendium/rules-elements/traits/player-core/Divine|Divine]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Manipulate|Manipulate]])"
  - name: "Requirements"
    desc: "The yamah has a charged gem on its _forceful quartz bracelet_"
  - name: "Effect"
    desc: "The yamah channels the magic from an active gem, causing its starknife to glow with unnatural brightness. Their next starknife Strike before the end of their turn deals an extra 1d6 force damage and increases its thrown range to 60 feet. This drains one of their quartz gems."
  - name: "Sneak Attack"
    desc: "The yamah's Strikes deal an extra 1d6 precision damage to [[srd/pf2e/compendium/rules-elements/Conditions#Off-Guard|off-guard]] creatures."
  - name: "Starstrike"
    desc: "Any non-magical [[srd/pf2e/compendium/equipment/weapons/knife/Starknife|starknife]] becomes a _+1 [[srd/pf2e/compendium/equipment/runes/Striking|striking]] [[srd/pf2e/compendium/equipment/runes/Returning|returning]] weapon_ while a yamah wields it."
  - name: "Steal Magic"
    desc: "⬺ ([[srd/pf2e/compendium/rules-elements/traits/player-core/Concentrate|Concentrate]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Divine|Divine]]) The yamah makes a melee spell attack against a creature under the effects of a spell; a yamah automatically succeeds with this attack against a willing creature. On a success, the yamah's divine touch attempts to counteract the spell (counteract rank 3, counteract modifier +16). A successful counteract siphons the magical energy into one of the gems on its _forceful quartz bracelet_, recharging it. Yamah Bracelets Each yamah wears a personalized bracelet, embedded with quartz gems that reflect the cosmos. These are empowered by unseen magic, recharging when the yamah has 8 hours of rest. These bracelets have a unique divine connection to their respective yamah, and the bracelets only function for that yamah. On occasion, a yamah will gift the bracelet to a mortal, more as a symbol of trust and a sign that the individual is protected than an attempt to share power."
spellcasting:
  - name: "Divine Innate Spells"
    desc: "DC 21, attack +14 - __Cantrips (3rd)__ [[srd/pf2e/compendium/spells/cantrips/Divine Lance|Divine Lance]] - __2nd__ [[srd/pf2e/compendium/spells/rank-1/Heal|Heal]] (×2), [[srd/pf2e/compendium/spells/rank-2/Invisibility|Invisibility]], [[srd/pf2e/compendium/spells/rank-2/Sure Footing|Sure Footing]] - __3rd__ [[srd/pf2e/compendium/spells/rank-3/Holy Light|Holy Light]], [[srd/pf2e/compendium/spells/rank-2/Dispel Magic|Dispel Magic]] - __Constant (5th)__ [[srd/pf2e/compendium/spells/cantrips/Detect Magic|Detect Magic]], [[srd/pf2e/compendium/spells/rank-5/Truespeech|Truespeech]]"
sourcebook: "_Monster Core 2_, page 50."
```

```encounter-table
name: Yamah
creatures:
  - 1: Yamah
```
