---
obsidianUIMode: preview
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
aon_id: "creature-2845"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=2845"
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
    desc: "Perception +32; hears heartbeats (imprecise) 60 feet, darkvision"
languages: "[[srd/pf2e/compendium/rules-elements/languages#Common|Common]], [[srd/pf2e/compendium/rules-elements/languages#Elven|Elven]]"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/acrobatics|Acrobatics]] +31, [[srd/pf2e/compendium/rules-elements/skills/intimidation|Intimidation]] +32, [[srd/pf2e/compendium/rules-elements/skills/occultism|Occultism]] +25"
abilityMods: [-5, 6, 2, 0, 7, 7]
abilities_top:
  - name: "Hears Heartbeats"
    desc: "The banshee can hear heartbeats within 60 feet of it as an imprecise sense."
  - name: "Sunlight Powerlessness"
    desc: "A banshee in sunlight is [[srd/pf2e/compendium/rules-elements/conditions#Clumsy|clumsy 2]] and [[srd/pf2e/compendium/rules-elements/conditions#Stunned|stunned 2]]."
ac: 39
armorclass:
  - name: "AC"
    desc: "39; __Fort__: +25; __Ref__: +29; __Will__: +32"
hp: 250
health:
  - name: "HP"
    desc: "250 (void healing); __Immunities__ bleed, [[srd/pf2e/compendium/rules-elements/traits/player-core/death|death]] effects, [[srd/pf2e/compendium/rules-elements/traits/player-core/disease|disease]], [[srd/pf2e/compendium/rules-elements/conditions#Paralyzed|paralyzed]], [[srd/pf2e/compendium/rules-elements/traits/player-core/poison|poison]], precision, [[srd/pf2e/compendium/rules-elements/conditions#Unconscious|unconscious]]; __Resistances__ all damage 12 (except [[srd/pf2e/compendium/rules-elements/traits/player-core/force|force]], [[srd/pf2e/compendium/equipment/runes/ghost-touch|_ghost touch_]], [[srd/pf2e/compendium/rules-elements/traits/player-core/spirit|spirit]], or [[srd/pf2e/compendium/rules-elements/traits/player-core/vitality|vitality]]; double resistance vs. non-[[srd/pf2e/compendium/rules-elements/traits/player-core/magical|magical]])"
abilities_mid:
  - name: "Vengeful Spite"
    desc: "⬲ ([[srd/pf2e/compendium/rules-elements/traits/player-core/occult|occult]])"
  - name: "Trigger"
    desc: "A foe critically hits the banshee, or the banshee critically fails their save against a foe's damaging effect"
  - name: "Effect"
    desc: "The banshee lashes back at their tormentor, dealing 4d10+14 mental damage with a DC 38 basic Will save and applying the effects of terrifying touch based on the results of the same Will save."
speed: "fly 60 feet"
attacks:
  - name: "Melee"
    desc: "⬻ hand +32 ([[srd/pf2e/compendium/rules-elements/traits/player-core/finesse|Finesse]], [[srd/pf2e/compendium/rules-elements/traits/player-core/magical|Magical]]) __Damage__ 4d10+14 void plus terrifying touch"
abilities_bot:
  - name: "Spectral Ripple"
    desc: "When a banshee Strides at least 10 feet, they're [[srd/pf2e/compendium/rules-elements/conditions#Concealed|concealed]] until the start of their next turn."
  - name: "Terrifying Touch"
    desc: "([[srd/pf2e/compendium/rules-elements/traits/player-core/emotion|Emotion]], [[srd/pf2e/compendium/rules-elements/traits/player-core/fear|Fear]], [[srd/pf2e/compendium/rules-elements/traits/player-core/occult|Occult]]) A creature damaged by the banshee's touch that isn't already [[srd/pf2e/compendium/rules-elements/conditions#Frightened|frightened]] must attempt a DC 38 Will save (DC 43 if the attack was a critical hit). If the creature fails its save, it's frightened 2; on a critical failure, the creature also cowers with fear and is [[srd/pf2e/compendium/rules-elements/conditions#Stunned|stunned 4]]. If the creature is protected against fear by a spell or magic item, the banshee's touch first attempts to counteract the protection effect, with the effect of a 9th-rank [[srd/pf2e/compendium/spells/rank-2/dispel-magic|_dispel magic_]] spell."
  - name: "Wail"
    desc: "⬺ ([[srd/pf2e/compendium/rules-elements/traits/player-core/auditory|Auditory]], [[srd/pf2e/compendium/rules-elements/traits/player-core/concentrate|Concentrate]], [[srd/pf2e/compendium/rules-elements/traits/player-core/death|Death]], [[srd/pf2e/compendium/rules-elements/traits/player-core/occult|Occult]]) The banshee unleashes a soul-chilling [[srd/pf2e/compendium/spells/rank-9/wails-of-the-damned|_wails of the damned_]] (DC 38). This Wail overcomes [[srd/pf2e/compendium/spells/rank-2/silence|_silence_]] and similar effects of 5th rank or lower. The banshee can instead use Wail as a three-action activity to overcome such effects of up to 8th rank. The banshee's Wail resonates for 1 round, and any creature that comes within the area during that time must attempt a save against the effect. A creature can't be affected more than once by the same Wail. The banshee can't Wail again for 1d4 rounds. Born from Tragedy The banshee represents one of the most tragic of undead, a soul so wracked with agony and fury over a betrayal in life that, in death, it lingers on as a great evil. That most of those who become banshees were not evil in life only deepens this tragic theme, and many elven adventurers see it as their duty not only to put banshees to rest, but to right the wrong that saw their creation in the first place."
sourcebook: "_Monster Core_, page 37."
```

```encounter-table
name: Banshee
creatures:
  - 1: Banshee
```
