---
noteType: pf2eMonster
aliases: "Banshee"
tags:
  - pf2e/creature/level/17
  - pf2e/creature/trait/ghost
  - pf2e/creature/trait/spirit
  - pf2e/creature/trait/uncommon
  - pf2e/creature/trait/undead
  - pf2e/creature/trait/unholy
  - pf2e/creature/trait/medium
statblock: inline
name: "Banshee"
level: 17
source: "Monster Core"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=2845"
socialImage: og-image.png
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC"
name: "Banshee"
level: "Creature 17"
size: "Medium"
trait_01: "Ghost"
trait_02: "Spirit"
trait_03: "Uncommon"
trait_04: "Undead"
trait_05: "Unholy"
modifier: 32
perception:
  - name: "Perception"
    desc: "+32; hears heartbeats (imprecise) 60 feet, darkvision"
languages: "[[srd/pf2e/compendium/rules-elements/Languages#Common|Common]], [[srd/pf2e/compendium/rules-elements/Languages#Elven|Elven]]"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/Acrobatics|Acrobatics]] +31, [[srd/pf2e/compendium/rules-elements/skills/Intimidation|Intimidation]] +32, [[srd/pf2e/compendium/rules-elements/skills/Occultism|Occultism]] +25"
abilityMods: [-5, 6, 2, 0, 7, 7]
abilities_top:
  - name: "Hears Heartbeats"
    desc: "The banshee can hear heartbeats within 60 feet of it as an imprecise sense."
  - name: "Sunlight Powerlessness"
    desc: "A banshee in sunlight is [[srd/pf2e/compendium/rules-elements/Conditions#Clumsy|clumsy 2]] and [[srd/pf2e/compendium/rules-elements/Conditions#Stunned|stunned 2]]."
ac: 39
armorclass:
  - name: "AC"
    desc: "39; __Fort__: +25; __Ref__: +29; __Will__: +32"
hp: 250
health:
  - name: "HP"
    desc: "250 (void healing); __Immunities__ bleed, [[srd/pf2e/compendium/rules-elements/traits/player-core/Death|death]] effects, [[srd/pf2e/compendium/rules-elements/traits/player-core/Disease|disease]], [[srd/pf2e/compendium/rules-elements/Conditions#Paralyzed|paralyzed]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Poison|poison]], precision, [[srd/pf2e/compendium/rules-elements/Conditions#Unconscious|unconscious]]; __Resistances__ all damage 12 (except [[srd/pf2e/compendium/rules-elements/traits/player-core/Force|force]], [[srd/pf2e/compendium/equipment/runes/Ghost Touch|_ghost touch_]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Spirit|spirit]], or [[srd/pf2e/compendium/rules-elements/traits/player-core/Vitality|vitality]]; double resistance vs. non-[[srd/pf2e/compendium/rules-elements/traits/player-core/Magical|magical]])"
abilities_mid:
  - name: "Vengeful Spite"
    desc: "⬲ ([[srd/pf2e/compendium/rules-elements/traits/player-core/Occult|occult]])"
  - name: "Trigger"
    desc: "A foe critically hits the banshee, or the banshee critically fails their save against a foe's damaging effect"
  - name: "Effect"
    desc: "The banshee lashes back at their tormentor, dealing 4d10+14 mental damage with a DC 38 basic Will save and applying the effects of terrifying touch based on the results of the same Will save."
speed: "fly 60 feet"
attacks:
  - name: "Melee"
    desc: "⬻ hand +32 ([[srd/pf2e/compendium/rules-elements/traits/player-core/Finesse|Finesse]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Magical|Magical]]) __Damage__ 4d10+14 void plus terrifying touch"
abilities_bot:
  - name: "Spectral Ripple"
    desc: "When a banshee Strides at least 10 feet, they're [[srd/pf2e/compendium/rules-elements/Conditions#Concealed|concealed]] until the start of their next turn."
  - name: "Terrifying Touch"
    desc: "([[srd/pf2e/compendium/rules-elements/traits/player-core/Emotion|Emotion]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Fear|Fear]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Occult|Occult]]) A creature damaged by the banshee's touch that isn't already [[srd/pf2e/compendium/rules-elements/Conditions#Frightened|frightened]] must attempt a DC 38 Will save (DC 43 if the attack was a critical hit). If the creature fails its save, it's frightened 2; on a critical failure, the creature also cowers with fear and is [[srd/pf2e/compendium/rules-elements/Conditions#Stunned|stunned 4]]. If the creature is protected against fear by a spell or magic item, the banshee's touch first attempts to counteract the protection effect, with the effect of a 9th-rank [[srd/pf2e/compendium/spells/rank-2/Dispel Magic|_dispel magic_]] spell."
  - name: "Wail"
    desc: "⬺ ([[srd/pf2e/compendium/rules-elements/traits/player-core/Auditory|Auditory]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Concentrate|Concentrate]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Death|Death]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Occult|Occult]]) The banshee unleashes a soul-chilling [[srd/pf2e/compendium/spells/rank-9/Wails of the Damned|_wails of the damned_]] (DC 38). This Wail overcomes [[srd/pf2e/compendium/spells/rank-2/Silence|_silence_]] and similar effects of 5th rank or lower. The banshee can instead use Wail as a three-action activity to overcome such effects of up to 8th rank. The banshee's Wail resonates for 1 round, and any creature that comes within the area during that time must attempt a save against the effect. A creature can't be affected more than once by the same Wail. The banshee can't Wail again for 1d4 rounds. Born from Tragedy The banshee represents one of the most tragic of undead, a soul so wracked with agony and fury over a betrayal in life that, in death, it lingers on as a great evil. That most of those who become banshees were not evil in life only deepens this tragic theme, and many elven adventurers see it as their duty not only to put banshees to rest, but to right the wrong that saw their creation in the first place."
sourcebook: "_Monster Core_, page 37."
```

```encounter-table
name: Banshee
creatures:
  - 1: Banshee
```
