---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Moon Hag"
tags:
  - pf2e/creature/level/10
  - pf2e/creature/trait/hag
  - pf2e/creature/trait/humanoid
  - pf2e/creature/trait/uncommon
  - pf2e/creature/trait/medium
statblock: inline
name: "Moon Hag"
level: 10
source: "Monster Core 2"
aon_id: "creature-4436"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=4436"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC2"
name: "Moon Hag"
level: "Creature 10"
size: "Medium"
trait_01: "Hag"
trait_02: "Humanoid"
trait_03: "Uncommon"
modifier: 22
perception:
  - name: "Perception"
    desc: "Perception +22; darkvision"
languages: "[[srd/pf2e/compendium/rules-elements/languages#Aklo|Aklo]], [[srd/pf2e/compendium/rules-elements/languages#Common|Common]], [[srd/pf2e/compendium/rules-elements/languages#Jotun|Jotun]]"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/deception|Deception]] +19, [[srd/pf2e/compendium/rules-elements/skills/intimidation|Intimidation]] +17, [[srd/pf2e/compendium/rules-elements/skills/occultism|Occultism]] +21, [[srd/pf2e/compendium/rules-elements/skills/religion|Religion]] +22"
abilityMods: [7, 5, 3, 5, 6, 3]
ac: 28
armorclass:
  - name: "AC"
    desc: "28; __Fort__: +17; __Ref__: +19; __Will__: +22"
hp: 190
health:
  - name: "HP"
    desc: "190; __Immunities__ [[srd/pf2e/compendium/rules-elements/conditions#Confused|confused]]"
abilities_mid:
  - name: "Ferocity"
    desc: "⬲"
  - name: "Moonlight's Kiss"
    desc: "A moon hag in an area illuminated by moonlight gains a +2 status bonus to AC and initiative rolls. In the light of a full moon, they're [[srd/pf2e/compendium/rules-elements/conditions#Quickened|quickened]], and can use the extra action only to [[srd/pf2e/compendium/rules-elements/actions/player-core#Stride|Stride]] or [[srd/pf2e/compendium/rules-elements/actions/player-core#Strike|Strike]]. If the moon hag has a [[srd/pf2e/books/player-core/chapter-8-playing-the-game/movement#Fly Speed|fly Speed]], they can use the extra action to [[srd/pf2e/compendium/rules-elements/actions/player-core#Fly|Fly]] as well."
speed: "25 feet"
attacks:
  - name: "Melee"
    desc: "⬻ claw +23 ([[srd/pf2e/compendium/rules-elements/traits/player-core/agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/magical|magical]]) __Damage__ 2d12+10 slashing"
abilities_bot:
  - name: "Change Shape"
    desc: "⬻ ([[srd/pf2e/compendium/rules-elements/traits/player-core/concentrate|Concentrate]], [[srd/pf2e/compendium/rules-elements/traits/player-core/occult|occult]], [[srd/pf2e/compendium/rules-elements/traits/player-core/polymorph|polymorph]]) The moon hag can take on the appearance of any Medium humanoid woman. This doesn't change their Speed or their attack and damage bonuses with their Strikes, but it might change the damage type their Strikes deal (typically to bludgeoning)."
  - name: "Dreadful Prediction"
    desc: "⬻ ([[srd/pf2e/compendium/rules-elements/traits/player-core/curse|Curse]], [[srd/pf2e/compendium/rules-elements/traits/player-core/occult|occult]], [[srd/pf2e/compendium/rules-elements/traits/player-core/mental|mental]])"
  - name: "Frequency"
    desc: "once per round"
  - name: "Effect"
    desc: "The moon hag howls a series of dreadful, apocalyptic predictions at a single creature within 30 feet, shattering its perceptions of reality. The target must attempt a DC 29 Will save and takes a –2 circumstance penalty to the save if it can see the moon. On a failure, the creature becomes [[srd/pf2e/compendium/rules-elements/conditions#Stupefied|stupefied]] 2 (stupefied 3 on a critical failure) until the curse is removed. Regardless of the outcome, the creature is then temporarily immune for 24 hours."
  - name: "Rend"
    desc: "⬻ claw"
  - name: "Ride the Moonbeams"
    desc: "⬻ ([[srd/pf2e/compendium/rules-elements/traits/player-core/concentrate|Concentrate]], [[srd/pf2e/compendium/rules-elements/traits/player-core/manipulate|manipulate]], [[srd/pf2e/compendium/rules-elements/traits/player-core/occult|occult]], [[srd/pf2e/compendium/rules-elements/traits/player-core/teleportation|teleportation]])"
  - name: "Frequency"
    desc: "once per round"
  - name: "Effect"
    desc: "The moon hag teleports themself and any items they're wearing and holding to another space within 30 feet, or 60 feet if they're in moonlight. They then gain a 25-foot [[srd/pf2e/books/player-core/chapter-8-playing-the-game/movement#Fly Speed|fly Speed]] until the end of their next turn. If the moon hag is in the air when the effect ends, they float to the ground, taking no falling damage."
spellcasting:
  - name: "Occult Innate Spells"
    desc: "DC 29 - __5th__ [[srd/pf2e/compendium/spells/rank-4/confusion|Confusion]], [[srd/pf2e/compendium/spells/rank-1/fear|Fear]] (at will), [[srd/pf2e/compendium/spells/rank-4/read-omens|Read Omens]], [[srd/pf2e/compendium/spells/rank-4/talking-corpse|Talking Corpse]] (×3), [[srd/pf2e/compendium/spells/rank-5/truespeech|Truespeech]]"
sourcebook: "_Monster Core 2_, page 189."
```

```encounter-table
name: Moon Hag
creatures:
  - 1: Moon Hag
```
