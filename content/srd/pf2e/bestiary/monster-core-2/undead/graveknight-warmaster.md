---
obsidianUIMode: preview
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
aon_id: "creature-4419"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=4419"
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
    desc: "Perception +26; darkvision"
languages: "[[srd/pf2e/compendium/rules-elements/languages#Common|Common]], [[srd/pf2e/compendium/rules-elements/languages#Necril|Necril]]"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/athletics|Athletics]] +28, [[srd/pf2e/compendium/rules-elements/skills/deception|Deception]] +26, [[srd/pf2e/compendium/rules-elements/skills/intimidation|Intimidation]] +28, [[srd/pf2e/compendium/rules-elements/skills/religion|Religion]] +24, [[srd/pf2e/compendium/rules-elements/skills/society|Society]] +25, [[srd/pf2e/compendium/rules-elements/skills/lore|Warfare Lore]] +27"
abilityMods: [8, 4, 5, 3, 4, 6]
abilities_top:
  - name: "Items"
    desc: "_[[srd/pf2e/compendium/equipment/armor/magic-armor-3-major-resilient|+1 resilient]] [[srd/pf2e/compendium/equipment/armor#Full Plate|full plate]]_, [[srd/pf2e/compendium/equipment/weapons/crossbow/heavy-crossbow|Heavy Crossbow]] (20 bolts), [[srd/pf2e/compendium/equipment/weapons/flail/war-flail|War Flail]]"
ac: 37
armorclass:
  - name: "AC"
    desc: "37; __Fort__: +27; __Ref__: +24; __Will__: +24"
hp: 255
health:
  - name: "HP"
    desc: "255 (rejuvenation, void healing); __Immunities__ [[srd/pf2e/compendium/rules-elements/conditions#Persistent Damage|bleed]], [[srd/pf2e/books/player-core/chapter-8-playing-the-game/hit-points-healing-and-dying#Death Effects|death effects]], [[srd/pf2e/compendium/rules-elements/traits/player-core/disease|disease]], [[srd/pf2e/compendium/rules-elements/traits/player-core/electricity|electricity]], [[srd/pf2e/compendium/rules-elements/conditions#Paralyzed|paralyzed]], [[srd/pf2e/compendium/rules-elements/traits/player-core/poison|poison]], [[srd/pf2e/compendium/rules-elements/conditions#Unconscious|unconscious]]"
abilities_mid:
  - name: "Hungry Armor"
    desc: "A creature that Strikes a graveknight warmaster with a melee weapon must succeed at a DC 31 Reflex save or be disarmed of that weapon. If the creature critically fails, the weapon ends up in the graveknight's space. A creature that hits a graveknight warmaster with an unarmed attack must succeed at a DC 31 Reflex save or become [[srd/pf2e/compendium/rules-elements/conditions#Grabbed|grabbed]] by the graveknight until the end of its next turn, when it [[srd/pf2e/compendium/rules-elements/actions/player-core#Escape|Escapes]], or when the graveknight moves, whichever comes first."
  - name: "Sacrilegious Aura"
    desc: "([[srd/pf2e/compendium/rules-elements/traits/player-core/aura|aura]], [[srd/pf2e/compendium/rules-elements/traits/player-core/divine|divine]], [[srd/pf2e/compendium/rules-elements/traits/player-core/unholy|unholy]]) 30 feet. When a creature in the aura uses a [[srd/pf2e/compendium/rules-elements/traits/player-core/vitality|vitality]] spell or ability, the graveknight warmaster automatically attempts to [[srd/pf2e/books/player-core/chapter-7-spells/counteracting|counteract]] it, with a +23 counteract modifier."
  - name: "Reactive Strike"
    desc: "⬲"
speed: "25 feet"
attacks:
  - name: "Melee"
    desc: "⬻ _war flail_ +29 ([[srd/pf2e/compendium/rules-elements/traits/player-core/disarm|Disarm]], [[srd/pf2e/compendium/rules-elements/traits/player-core/electricity|electricity]], [[srd/pf2e/compendium/rules-elements/traits/player-core/magical|magical]], [[srd/pf2e/compendium/rules-elements/traits/player-core/sweep|sweep]], [[srd/pf2e/compendium/rules-elements/traits/player-core/trip|trip]]) __Damage__ 3d10+14 bludgeoning plus 1d6 electricity"
  - name: "Melee"
    desc: "⬻ fist +29 ([[srd/pf2e/compendium/rules-elements/traits/player-core/agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/electricity|electricity]], [[srd/pf2e/compendium/rules-elements/traits/player-core/magical|magical]]) __Damage__ 3d6+14 bludgeoning plus 1d6 electricity"
  - name: "Ranged"
    desc: "⬻ heavy crossbow +25 ([[srd/pf2e/compendium/rules-elements/traits/player-core/electricity|Electricity]], [[srd/pf2e/compendium/rules-elements/traits/player-core/magical|magical]], range increment 120 feet, reload 2) __Damage__ 3d10+6 piercing plus 1d6 electricity"
abilities_bot:
  - name: "Devastating Blast"
    desc: "⬺ ([[srd/pf2e/compendium/rules-elements/traits/player-core/arcane|Arcane]], [[srd/pf2e/compendium/rules-elements/traits/player-core/electricity|electricity]]) The graveknight warmaster unleashes a 30-foot [[srd/pf2e/books/player-core/chapter-8-playing-the-game/area#Cone|cone]] of energy. Creatures in the area take 8d12 electricity with a DC 34 [[srd/pf2e/books/player-core/chapter-8-playing-the-game/checks#Basic Saving Throws|basic]] Reflex save. The graveknight warmaster can use this ability once every 1d4 rounds."
  - name: "Exemplar of Violence"
    desc: "⬺ ([[srd/pf2e/compendium/rules-elements/traits/player-core/visual|Visual]])"
  - name: "Frequency"
    desc: "once per round"
  - name: "Effect"
    desc: "The graveknight attempts a Strike as their armor flashes with sinister power that spurs allies to violence. After the Strike, allies who can see the graveknight can use a reaction to [[srd/pf2e/compendium/rules-elements/actions/player-core#Step|Step]] or [[srd/pf2e/compendium/rules-elements/actions/player-core#Stride|Stride]], but they must end this movement in a space adjacent to an enemy. One ally of the graveknight's choice can instead use a reaction to Strike."
  - name: "Graveknight's Curse"
    desc: "([[srd/pf2e/compendium/rules-elements/traits/player-core/arcane|Arcane]], [[srd/pf2e/compendium/rules-elements/traits/player-core/curse|curse]]) This curse affects anyone who wears a graveknight's armor for at least 1 hour"
  - name: "Saving Throw"
    desc: "DC 39 Will save; Onset 1 hour"
  - name: "Stage 1"
    desc: "[[srd/pf2e/compendium/rules-elements/conditions#Doomed|doomed]] 1 and can't remove armor (1 day)"
  - name: "Stage 2"
    desc: "doomed 2, –10- foot status penalty to Speeds, and can't remove armor (1 day)"
  - name: "Stage 3"
    desc: "dies and transforms into the armor's graveknight."
  - name: "Phantom Mount"
    desc: "⬽ ([[srd/pf2e/compendium/rules-elements/traits/player-core/arcane|Arcane]]) The graveknight warmaster summons a supernatural mount, as [[srd/pf2e/compendium/spells/rank-2/marvelous-mount|_marvelous mount_]] heightened to a 7th rank. Unlike _marvelous mount_, the steed's AC and saving throw bonuses are all 4 lower than the graveknight's, and the steed has AC 34, Fort +23, Ref +20, Will +20, and 85 Hit Points. If the steed is destroyed, the graveknight warmaster must wait 1 hour before using this ability again.; the steed has"
  - name: "Ruinous Weapons"
    desc: "Any weapon or unarmed attack the graveknight uses gains the effects of a _[[srd/pf2e/compendium/equipment/weapons/magic-weapon-3-major-striking|+1 greater striking]] weapon_ and a _[[srd/pf2e/compendium/equipment/runes/shock-greater|greater shock]]_ weapon rune."
  - name: "Weapon Master"
    desc: "The graveknight captain has access to the [[srd/pf2e/books/player-core/chapter-6-equipment/weapons#Critical Specialization|critical specialization]] effects of any weapons they wield."
sourcebook: "_Monster Core 2_, page 172."
```

```encounter-table
name: Graveknight Warmaster
creatures:
  - 1: Graveknight Warmaster
```
