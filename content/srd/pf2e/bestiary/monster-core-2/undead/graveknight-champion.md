---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Graveknight Champion"
tags:
  - pf2e/creature/level/15
  - pf2e/creature/trait/uncommon
  - pf2e/creature/trait/undead
  - pf2e/creature/trait/unholy
  - pf2e/creature/trait/medium
statblock: inline
name: "Graveknight Champion"
level: 15
source: "Monster Core 2"
aon_id: "creature-4420"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=4420"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC2"
name: "Graveknight Champion"
level: "Creature 15"
size: "Medium"
trait_01: "Uncommon"
trait_02: "Undead"
trait_03: "Unholy"
modifier: 27
perception:
  - name: "Perception"
    desc: "Perception +27; darkvision"
languages: "[[srd/pf2e/compendium/rules-elements/languages#Common|Common]], [[srd/pf2e/compendium/rules-elements/languages#Necril|Necril]]"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/athletics|Athletics]] +31, [[srd/pf2e/compendium/rules-elements/skills/lore|Deity Lore]] +27, [[srd/pf2e/compendium/rules-elements/skills/intimidation|Intimidation]] +29, [[srd/pf2e/compendium/rules-elements/skills/religion|Religion]] +27"
abilityMods: [8, 4, 5, 2, 4, 6]
abilities_top:
  - name: "Items"
    desc: "[[srd/pf2e/compendium/equipment/weapons/bow/composite-shortbow|Composite Shortbow]] (20 arrows), _[[srd/pf2e/compendium/equipment/armor/magic-armor-3-major-resilient|+2 resilient]] [[srd/pf2e/compendium/equipment/armor#Full Plate|full plate]]_, [[srd/pf2e/compendium/equipment/weapons/pick/greatpick|Greatpick]]"
ac: 38
armorclass:
  - name: "AC"
    desc: "38; __Fort__: +28; __Ref__: +26; __Will__: +25"
hp: 275
health:
  - name: "HP"
    desc: "275 (rejuvenation, void healing); __Immunities__ [[srd/pf2e/compendium/rules-elements/conditions#Persistent Damage|bleed]], [[srd/pf2e/compendium/rules-elements/traits/player-core/death|death]], [[srd/pf2e/compendium/rules-elements/traits/player-core/disease|disease]], [[srd/pf2e/compendium/rules-elements/traits/player-core/fire|fire]], [[srd/pf2e/compendium/rules-elements/conditions#Paralyzed|paralyzed]], [[srd/pf2e/compendium/rules-elements/traits/player-core/poison|poison]], [[srd/pf2e/compendium/rules-elements/conditions#Unconscious|unconscious]]"
abilities_mid:
  - name: "Clutching Armor"
    desc: "⬲ ([[srd/pf2e/compendium/rules-elements/traits/player-core/arcane|arcane]])"
  - name: "Trigger"
    desc: "A creature attempts to move away from the graveknight champion"
  - name: "Effect"
    desc: "The graveknight champion's armor animates and attempts to Grab the triggering creature. It makes an [[srd/pf2e/compendium/rules-elements/skills/athletics|Athletics]] check to [[srd/pf2e/compendium/rules-elements/actions/player-core#Grapple|Grapple]] at +29. The armor can continue to Grapple the creature normally. Since the armor is grappling the creature, the graveknight doesn't need a free hand to do so."
  - name: "Reactive Strike"
    desc: "⬲"
speed: "25 feet"
attacks:
  - name: "Melee"
    desc: "⬻ _greatpick_ +30 ([[srd/pf2e/compendium/rules-elements/traits/player-core/fatal|fatal d12]], [[srd/pf2e/compendium/rules-elements/traits/player-core/fire|fire]], [[srd/pf2e/compendium/rules-elements/traits/player-core/magical|magical]]) __Damage__ 3d10+16 slashing plus 1d6 fire"
  - name: "Melee"
    desc: "⬻ fist +30 ([[srd/pf2e/compendium/rules-elements/traits/player-core/agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/fire|fire]], [[srd/pf2e/compendium/rules-elements/traits/player-core/magical|magical]]) __Damage__ 3d6+16 bludgeoning plus 1d6 fire"
  - name: "Ranged"
    desc: "⬻ _composite shortbow_ +28 ([[srd/pf2e/compendium/rules-elements/traits/player-core/deadly|deadly d10]], [[srd/pf2e/compendium/rules-elements/traits/player-core/fire|fire]], [[srd/pf2e/compendium/rules-elements/traits/player-core/magical|magical]], range increment 60 feet, reload 0) __Damage__ 3d6+10 piercing plus 1d6 fire"
abilities_bot:
  - name: "Innate Divine Spells"
    desc: "DC 33, attack +25 - __Cantrips (7th)__ [[srd/pf2e/compendium/spells/cantrips/divine-lance|Divine Lance]], [[srd/pf2e/compendium/spells/cantrips/light|Light]], [[srd/pf2e/compendium/spells/cantrips/shield|Shield]], [[srd/pf2e/compendium/spells/cantrips/void-warp|Void Warp]] - __4th__ [[srd/pf2e/compendium/spells/rank-3/fireball|Fireball]] - __5th__ [[srd/pf2e/compendium/spells/rank-3/chilling-darkness|Chilling Darkness]], [[srd/pf2e/compendium/spells/rank-5/divine-immolation|Divine Immolation]] - __6th__ [[srd/pf2e/compendium/spells/rank-3/fireball|Fireball]], [[srd/pf2e/compendium/spells/rank-2/spiritual-armament|Spiritual Armament]] - __7th__ [[srd/pf2e/compendium/spells/rank-7/eclipse-burst|Eclipse Burst]], [[srd/pf2e/compendium/spells/rank-7/execute|Execute]]"
  - name: "Channel Magic"
    desc: "⬺ The graveknight champion redirects magical energies through its armor, allowing it to deliver magic through an attack. The graveknight champion Casts a Spell that takes 1 or 2 actions to cast and requires a spell attack modifier. The effects of the spell don't occur immediately but are imbued into an attack instead. The graveknight champion then makes a melee Strike with a weapon or unarmed attack. The spell is coupled with the attack, using the attack roll result to determine the effects of both the Strike and the spell. This counts as two attacks for the graveknight's multiple attack penalty but doesn't apply the penalty until after they've completed Channeling Magic. The graveknight champion can't use Channel Magic again for 1d4 rounds."
  - name: "Devastating Blast"
    desc: "⬺ ([[srd/pf2e/compendium/rules-elements/traits/player-core/arcane|Arcane]], [[srd/pf2e/compendium/rules-elements/traits/player-core/fire|fire]]) The graveknight champion unleashes a 30-foot [[srd/pf2e/books/player-core/chapter-8-playing-the-game/area#Cone|cone]] of energy. Creatures in the area take 9d12 fire with a DC 36 [[srd/pf2e/books/player-core/chapter-8-playing-the-game/checks#Basic Saving Throws|basic]] Reflex save. The graveknight champion can use this ability once every 1d4 rounds."
  - name: "Graveknight's Curse"
    desc: "([[srd/pf2e/compendium/rules-elements/traits/player-core/arcane|Arcane]], [[srd/pf2e/compendium/rules-elements/traits/player-core/curse|curse]]) This curse affects anyone who wears a graveknight champion's armor for at least 1 hour"
  - name: "Saving Throw"
    desc: "DC 40 Will save"
  - name: "Onset"
    desc: "1 hour"
  - name: "Stage 1"
    desc: "[[srd/pf2e/compendium/rules-elements/conditions#Doomed|doomed]] 1 and can't remove armor (1 day)"
  - name: "Stage 2"
    desc: "doomed 2, –10- foot status penalty to Speeds, and can't remove armor (1 day)"
  - name: "Stage 3"
    desc: "dies and transforms into the armor's graveknight."
  - name: "Ruinous Weapons"
    desc: "Any weapon or unarmed attack the graveknight uses gains the effects of a _[[srd/pf2e/compendium/equipment/weapons/magic-weapon-3-major-striking|+1 greater striking]] weapon_ and a _[[srd/pf2e/compendium/equipment/runes/flaming-greater|greater flaming]]_ weapon rune."
  - name: "Weapon Master"
    desc: "The graveknight has access to the [[srd/pf2e/books/player-core/chapter-6-equipment/weapons#Critical Specialization|critical specialization]] effects of any weapons they wield."
sourcebook: "_Monster Core 2_, page 173."
```

```encounter-table
name: Graveknight Champion
creatures:
  - 1: Graveknight Champion
```
