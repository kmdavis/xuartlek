---
noteType: pf2eMonster
aliases: "Draconal"
tags:
  - pf2e/creature/level/20
  - pf2e/creature/trait/agathion
  - pf2e/creature/trait/celestial
  - pf2e/creature/trait/holy
  - pf2e/creature/trait/large
statblock: inline
name: "Draconal"
level: 20
source: "Monster Core 2"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=4021"
socialImage: og-image.png
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC2"
name: "Draconal"
level: "Creature 20"
size: "Large"
trait_01: "Agathion"
trait_02: "Celestial"
trait_03: "Holy"
modifier: 36
perception:
  - name: "Perception"
    desc: "+36; darkvision"
languages: "[[srd/pf2e/compendium/rules-elements/Languages#Diabolic|Diabolic]], [[srd/pf2e/compendium/rules-elements/Languages#Draconic|Draconic]], [[srd/pf2e/compendium/rules-elements/Languages#Empyrean|Empyrean]]; [[srd/pf2e/compendium/spells/rank-2/Speak with Animals|_speak with animals_]], [[srd/pf2e/compendium/spells/rank-5/Truespeech|_truespeech_]]"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/Arcana|Arcana]] +38, [[srd/pf2e/compendium/rules-elements/skills/Crafting|Crafting]] +30, [[srd/pf2e/compendium/rules-elements/skills/Deception|Deception]] +35, [[srd/pf2e/compendium/rules-elements/skills/Diplomacy|Diplomacy]] +37, [[srd/pf2e/compendium/rules-elements/skills/Intimidation|Intimidation]] +35, [[srd/pf2e/compendium/rules-elements/skills/Medicine|Medicine]] +34, [[srd/pf2e/compendium/rules-elements/skills/Nature|Nature]] +34, [[srd/pf2e/compendium/rules-elements/skills/Lore|Nirvana Lore]] +36, [[srd/pf2e/compendium/rules-elements/skills/Religion|Religion]] +36, [[srd/pf2e/compendium/rules-elements/skills/Society|Society]] +32, [[srd/pf2e/compendium/rules-elements/skills/Survival|Survival]] +32"
abilityMods: [10, 5, 8, 8, 10, 9]
ac: 45
armorclass:
  - name: "AC"
    desc: "45; __Fort__: +34; __Ref__: +31; __Will__: +38"
hp: 370
health:
  - name: "HP"
    desc: "370 , regeneration 20 (deactivated by [[srd/pf2e/compendium/rules-elements/traits/player-core/Unholy|unholy]]); __Resistances__ [[srd/pf2e/compendium/rules-elements/traits/player-core/Spirit|spirit]] 15; __Weaknesses__ [[srd/pf2e/compendium/rules-elements/traits/player-core/Unholy|unholy]] 20"
abilities_mid:
  - name: "Dragon's Salvation"
    desc: "⬲"
  - name: "Trigger"
    desc: "A creature within the draconal's reach would take damage"
  - name: "Effect"
    desc: "Before applying the damage, the draconal casts [[srd/pf2e/compendium/spells/focus/Lay on Hands|_lay on hands_]] on the triggering creature."
speed: "30 feet, fly 90 feet"
attacks:
  - name: "Melee"
    desc: "⬻ jaws +38 ([[srd/pf2e/compendium/rules-elements/traits/player-core/Holy|Holy]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Magical|Magical]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Reach|reach 15 feet]]) __Damage__ 3d12+18 piercing plus 4d6 spirit"
  - name: "Melee"
    desc: "⬻ claw +38 ([[srd/pf2e/compendium/rules-elements/traits/player-core/Agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Holy|Holy]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Magical|Magical]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Reach|reach 10 feet]]) __Damage__ 3d8+18 slashing plus 4d6 spirit"
abilities_bot:
  - name: "Champion Focus Spell"
    desc: "DC 46, 3 Focus Points - __10th__ [[srd/pf2e/compendium/spells/focus/Lay on Hands|Lay on Hands]]"
  - name: "Breath of Wisdom"
    desc: "⬺ ([[srd/pf2e/compendium/rules-elements/traits/player-core/Divine|Divine]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Holy|Holy]]) The draconal breathes a blast of energy that deals 21d6 spirit damage to creatures they choose to damage in a 60-foot [[srd/pf2e/books/player-core/chapter-8-playing-the-game/Area#Cone|cone]] (DC 44 basic Reflex save). They can make this effect [[srd/pf2e/compendium/rules-elements/traits/player-core/Nonlethal|nonlethal]] for selected creatures in the area or choose not to damage certain creatures at all. They can't use Breath of Wisdom again for 1d4 rounds."
  - name: "Dragon's Wisdom"
    desc: "Draconals embody the core value of wisdom, and all wisdom is obtained through understanding. If a draconal successfully [[srd/pf2e/compendium/rules-elements/actions/player-core#Recall Knowledge|Recalls Knowledge]] about a creature, they learn their highest weakness in addition to any other obtained knowledge, and any spirit damage they do to that creature becomes damage of their highest known weakness instead. Draconals And Dragons Draconals hold a great respect for dragons, particularly great dragons, but as they rarely visit the mortal [[srd/pf2e/compendium/gm/Planes#The Universe|Universe]], interactions between the two groups tends to be minimal. Despite a general respect for dragonkind, draconals often revile malicious dragons. In times of strife, draconals use their might and wisdom against the forces of wickedness. They stand alongside [[srd/pf2e/compendium/gm/creature-families/Dragon, Empyreal|empyreal]] and other celestial dragons to face off against unholy forces."
spellcasting:
  - name: "Divine Innate Spells"
    desc: "DC 46, attack +38 - __9th__ [[srd/pf2e/compendium/spells/rank-5/Breath of Life|Breath of Life]], [[srd/pf2e/compendium/spells/rank-2/Dispel Magic|Dispel Magic]], [[srd/pf2e/compendium/spells/rank-7/Divine Decree|Divine Decree]], [[srd/pf2e/compendium/spells/rank-8/Earthquake|Earthquake]], [[srd/pf2e/compendium/spells/rank-1/Heal|Heal]] (×3), [[srd/pf2e/compendium/spells/rank-9/Implosion|Implosion]], [[srd/pf2e/compendium/spells/rank-9/Wrathful Storm|Wrathful Storm]] - __10th__ [[srd/pf2e/compendium/spells/rank-10/Manifestation|Manifestation]] - __Constant (7th)__ [[srd/pf2e/compendium/spells/rank-2/Speak with Animals|Speak with Animals]], [[srd/pf2e/compendium/spells/rank-6/Truesight|Truesight]], [[srd/pf2e/compendium/spells/rank-5/Truespeech|Truespeech]]"
sourcebook: "_Monster Core 2_, page 18."
```

```encounter-table
name: Draconal
creatures:
  - 1: Draconal
```
