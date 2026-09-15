---
noteType: pf2eMonster
aliases: "Hungry Ghost"
tags:
  - pf2e/creature/level/6
  - pf2e/creature/trait/ghost
  - pf2e/creature/trait/incorporeal
  - pf2e/creature/trait/spirit
  - pf2e/creature/trait/undead
  - pf2e/creature/trait/unholy
  - pf2e/creature/trait/medium
statblock: inline
name: "Hungry Ghost"
level: 6
source: "Monster Core 2"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=4406"
socialImage: og-image.png
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC2"
name: "Hungry Ghost"
level: "Creature 6"
size: "Medium"
trait_01: "Ghost"
trait_02: "Incorporeal"
trait_03: "Spirit"
trait_04: "Undead"
trait_05: "Unholy"
modifier: 13
perception:
  - name: "Perception"
    desc: "+13; darkvision"
languages: "[[srd/pf2e/compendium/rules-elements/Languages#Common|Common]], [[srd/pf2e/compendium/rules-elements/Languages#Necril|Necril]]; one other language"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/Deception|Deception]] +14, [[srd/pf2e/compendium/rules-elements/skills/Diplomacy|Diplomacy]] +14, [[srd/pf2e/compendium/rules-elements/skills/Lore|Ghost Lore]] +18, [[srd/pf2e/compendium/rules-elements/skills/Religion|Religion]] +15"
abilityMods: [-5, 5, 0, 4, 5, 4]
abilities_top:
  - name: "Living Visage"
    desc: "While they have more than 30 HP, the hungry ghost appears to be a living creature. They have an automatic result of 34 on [[srd/pf2e/compendium/rules-elements/skills/Deception|Deception]] checks and DCs to conceal their undead status and can Feed on the Living covertly (below)."
  - name: "Ravenous Undoing"
    desc: "In each 24-hour period, the hungry ghost must use Feed on the Living to consume 30 HP (any HP the ghost would gain count toward this total, even if the ghost has enough HP that they don't actually regain the full amount). If the ghost hasn't consumed enough HP, they mindlessly and recklessly feed on any living creature they come across until satiated."
ac: 23
armorclass:
  - name: "AC"
    desc: "23; __Fort__: +12; __Ref__: +15; __Will__: +15"
hp: 60
health:
  - name: "HP"
    desc: "60 (rejuvenation, void healing); __Immunities__ [[srd/pf2e/compendium/rules-elements/Conditions#Persistent Damage|bleed]], [[srd/pf2e/books/player-core/chapter-8-playing-the-game/Hit Points, Healing, and Dying#Death Effects|death effects]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Disease|disease]], [[srd/pf2e/compendium/rules-elements/Conditions#Paralyzed|paralyzed]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Poison|poison]], precision, [[srd/pf2e/compendium/rules-elements/Conditions#Unconscious|unconscious]]; __Resistances__ all damage 5 (except [[srd/pf2e/compendium/rules-elements/traits/player-core/Force|force]], [[srd/pf2e/compendium/equipment/runes/Ghost Touch|_ghost touch_]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Spirit|spirit]], or [[srd/pf2e/compendium/rules-elements/traits/player-core/Vitality|vitality]]; double resistance vs. non-magical)"
abilities_mid:
  - name: "Rejuvenation"
    desc: "([[srd/pf2e/compendium/rules-elements/traits/player-core/Divine|divine]]) When a hungry ghost is destroyed, they reform after 2d4 days fully healed at the location where they were last destroyed. They're only permanently destroyed when they have been given a proper burial, have had their grave cleaned and maintained for at least a year, or have been judged to be redeemed by [[srd/pf2e/compendium/deities/gods-of-the-inner-sea/Pharasma|Pharasma]]."
speed: "fly 25 feet"
attacks:
  - name: "Melee"
    desc: "⬻ ghostly touch +17 ([[srd/pf2e/compendium/rules-elements/traits/player-core/Agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Finesse|finesse]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Magical|magical]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Unarmed|unarmed]]) __Damage__ 2d8+4 void"
abilities_bot:
  - name: "Feed on the Living"
    desc: "⬺ ([[srd/pf2e/compendium/rules-elements/traits/player-core/Divine|Divine]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Void|void]]) The hungry ghost touches a living creature in reach to steal its life force. If the ghost is in their living visage, they can disguise Feed on the Living as a benign touch and delay the effects for up to 1 minute while keeping the target unaware of the effect. A creature can be affected by only one delayed Feed on the Living at a time, and if the ghost loses their living visage during that minute, the delayed effect is lost. When Feed on the Living takes effect, the target takes 2d8+4 void damage, depending on the result of its DC 24 Fortitude save."
  - name: "Critical Success"
    desc: "The target's life energy overpowers the ghost. The hungry ghost takes 5 vitality damage, and the target is unaffected."
  - name: "Success"
    desc: "The target takes half damage, and the hungry ghost regains HP equal to the damage dealt."
  - name: "Failure"
    desc: "The target takes full damage and is [[srd/pf2e/compendium/rules-elements/Conditions#Enfeebled|enfeebled]] 1 for 1 minute, and the hungry ghost regains HP equal to the damage dealt."
  - name: "Critical Failure"
    desc: "The target takes double damage and is enfeebled 2 for 1 minute, and the hungry ghost regains HP equal to the damage dealt. Unremembered, Unmourned A ghost is driven by an all-consuming need, connected to their death but often unclear to the ghost themself. Fragments of their previous life still bind to the ghost's identity, but they become shrouded or twisted in service of the ghost's death energy. They pull the ghost toward committing horrific and vengeful acts, like invisible marionette strings clutched by a sinister force. This disconnect means the ghost is rarely helpful to those who hope to set it to rest, forcing them to seek out clues from the environment or other creatures' recollections. Even a hungry ghost, compelled to commit good deeds, is helpless to keep control against their need to feed."
sourcebook: "_Monster Core 2_, page 160."
```

```encounter-table
name: Hungry Ghost
creatures:
  - 1: Hungry Ghost
```
