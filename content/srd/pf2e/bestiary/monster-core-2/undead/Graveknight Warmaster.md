---
noteType: pf2eMonster
aliases: "Graveknight Warmaster"
tags:
  - pf2e/creature/level/14
  - pf2e/creature/trait/uncommon
  - pf2e/creature/trait/undead
  - pf2e/creature/trait/unholy
  - pf2e/creature/trait/medium
statblock: inline
name: "Graveknight Warmaster"
level: 14
source: "Monster Core 2"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=4419"
socialImage: og-image.png
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC2"
name: "Graveknight Warmaster"
level: "Creature 14"
size: "Medium"
trait_01: "Uncommon"
trait_02: "Undead"
trait_03: "Unholy"
modifier: 26
perception:
  - name: "Perception"
    desc: "+26; darkvision"
languages: "[[srd/pf2e/compendium/rules-elements/Languages#Common|Common]], [[srd/pf2e/compendium/rules-elements/Languages#Necril|Necril]]"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/Athletics|Athletics]] +28, [[srd/pf2e/compendium/rules-elements/skills/Deception|Deception]] +26, [[srd/pf2e/compendium/rules-elements/skills/Intimidation|Intimidation]] +28, [[srd/pf2e/compendium/rules-elements/skills/Religion|Religion]] +24, [[srd/pf2e/compendium/rules-elements/skills/Society|Society]] +25, [[srd/pf2e/compendium/rules-elements/skills/Lore|Warfare Lore]] +27"
abilityMods: [8, 4, 5, 3, 4, 6]
abilities_top:
  - name: "Items"
    desc: "_[[srd/pf2e/compendium/equipment/armor/Magic Armor|+1 resilient]] [[srd/pf2e/compendium/equipment/Armor#Full Plate|full plate]]_, [[srd/pf2e/compendium/equipment/weapons/crossbow/Heavy Crossbow|Heavy Crossbow]] (20 bolts), [[srd/pf2e/compendium/equipment/weapons/flail/War Flail|War Flail]]"
ac: 37
armorclass:
  - name: "AC"
    desc: "37; __Fort__: +27; __Ref__: +24; __Will__: +24"
hp: 255
health:
  - name: "HP"
    desc: "255 (rejuvenation, void healing); __Immunities__ [[srd/pf2e/compendium/rules-elements/Conditions#Persistent Damage|bleed]], [[srd/pf2e/books/player-core/chapter-8-playing-the-game/Hit Points, Healing, and Dying#Death Effects|death effects]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Disease|disease]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Electricity|electricity]], [[srd/pf2e/compendium/rules-elements/Conditions#Paralyzed|paralyzed]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Poison|poison]], [[srd/pf2e/compendium/rules-elements/Conditions#Unconscious|unconscious]]"
abilities_mid:
  - name: "Hungry Armor"
    desc: "A creature that Strikes a graveknight warmaster with a melee weapon must succeed at a DC 31 Reflex save or be disarmed of that weapon. If the creature critically fails, the weapon ends up in the graveknight's space. A creature that hits a graveknight warmaster with an unarmed attack must succeed at a DC 31 Reflex save or become [[srd/pf2e/compendium/rules-elements/Conditions#Grabbed|grabbed]] by the graveknight until the end of its next turn, when it [[srd/pf2e/compendium/rules-elements/actions/player-core#Escape|Escapes]], or when the graveknight moves, whichever comes first."
  - name: "Sacrilegious Aura"
    desc: "([[srd/pf2e/compendium/rules-elements/traits/player-core/Aura|aura]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Divine|divine]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Unholy|unholy]]) 30 feet. When a creature in the aura uses a [[srd/pf2e/compendium/rules-elements/traits/player-core/Vitality|vitality]] spell or ability, the graveknight warmaster automatically attempts to [[srd/pf2e/books/player-core/chapter-7-spells/Counteracting|counteract]] it, with a +23 counteract modifier."
  - name: "Reactive Strike"
    desc: "⬲"
speed: "25 feet"
attacks:
  - name: "Melee"
    desc: "⬻ _war flail_ +29 ([[srd/pf2e/compendium/rules-elements/traits/player-core/Disarm|Disarm]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Electricity|electricity]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Magical|magical]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Sweep|sweep]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Trip|trip]]) __Damage__ 3d10+14 bludgeoning plus 1d6 electricity"
  - name: "Melee"
    desc: "⬻ fist +29 ([[srd/pf2e/compendium/rules-elements/traits/player-core/Agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Electricity|electricity]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Magical|magical]]) __Damage__ 3d6+14 bludgeoning plus 1d6 electricity"
  - name: "Ranged"
    desc: "⬻ heavy crossbow +25 ([[srd/pf2e/compendium/rules-elements/traits/player-core/Electricity|Electricity]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Magical|magical]], range increment 120 feet, reload 2) __Damage__ 3d10+6 piercing plus 1d6 electricity"
abilities_bot:
  - name: "Devastating Blast"
    desc: "⬺ ([[srd/pf2e/compendium/rules-elements/traits/player-core/Arcane|Arcane]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Electricity|electricity]]) The graveknight warmaster unleashes a 30-foot [[srd/pf2e/books/player-core/chapter-8-playing-the-game/Area#Cone|cone]] of energy. Creatures in the area take 8d12 electricity with a DC 34 [[srd/pf2e/books/player-core/chapter-8-playing-the-game/Checks#Basic Saving Throws|basic]] Reflex save. The graveknight warmaster can use this ability once every 1d4 rounds."
  - name: "Exemplar of Violence"
    desc: "⬺ ([[srd/pf2e/compendium/rules-elements/traits/player-core/Visual|Visual]])"
  - name: "Frequency"
    desc: "once per round"
  - name: "Effect"
    desc: "The graveknight attempts a Strike as their armor flashes with sinister power that spurs allies to violence. After the Strike, allies who can see the graveknight can use a reaction to [[srd/pf2e/compendium/rules-elements/actions/player-core#Step|Step]] or [[srd/pf2e/compendium/rules-elements/actions/player-core#Stride|Stride]], but they must end this movement in a space adjacent to an enemy. One ally of the graveknight's choice can instead use a reaction to Strike."
  - name: "Graveknight's Curse"
    desc: "([[srd/pf2e/compendium/rules-elements/traits/player-core/Arcane|Arcane]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Curse|curse]]) This curse affects anyone who wears a graveknight's armor for at least 1 hour"
  - name: "Saving Throw"
    desc: "DC 39 Will save; Onset 1 hour"
  - name: "Stage 1"
    desc: "[[srd/pf2e/compendium/rules-elements/Conditions#Doomed|doomed]] 1 and can't remove armor (1 day)"
  - name: "Stage 2"
    desc: "doomed 2, –10- foot status penalty to Speeds, and can't remove armor (1 day)"
  - name: "Stage 3"
    desc: "dies and transforms into the armor's graveknight."
  - name: "Phantom Mount"
    desc: "⬽ ([[srd/pf2e/compendium/rules-elements/traits/player-core/Arcane|Arcane]]) The graveknight warmaster summons a supernatural mount, as [[srd/pf2e/compendium/spells/rank-2/Marvelous Mount|_marvelous mount_]] heightened to a 7th rank. Unlike _marvelous mount_, the steed's AC and saving throw bonuses are all 4 lower than the graveknight's, and the steed has AC 34, Fort +23, Ref +20, Will +20, and 85 Hit Points. If the steed is destroyed, the graveknight warmaster must wait 1 hour before using this ability again.; the steed has"
  - name: "Ruinous Weapons"
    desc: "Any weapon or unarmed attack the graveknight uses gains the effects of a _[[srd/pf2e/compendium/equipment/weapons/Magic Weapon|+1 greater striking]] weapon_ and a _[[srd/pf2e/compendium/equipment/runes/Shock|greater shock]]_ weapon rune."
  - name: "Weapon Master"
    desc: "The graveknight captain has access to the [[srd/pf2e/books/player-core/chapter-6-equipment/Weapons#Critical Specialization|critical specialization]] effects of any weapons they wield."
sourcebook: "_Monster Core 2_, page 172."
```

```encounter-table
name: Graveknight Warmaster
creatures:
  - 1: Graveknight Warmaster
```
