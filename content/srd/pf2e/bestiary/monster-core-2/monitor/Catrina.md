---
noteType: pf2eMonster
aliases: "Catrina"
tags:
  - pf2e/creature/level/5
  - pf2e/creature/trait/monitor
  - pf2e/creature/trait/psychopomp
  - pf2e/creature/trait/medium
statblock: inline
name: "Catrina"
level: 5
source: "Monster Core 2"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=4522"
socialImage: og-image.png
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC2"
name: "Catrina"
level: "Creature 5"
size: "Medium"
trait_01: "Monitor"
trait_02: "Psychopomp"
modifier: 13
perception:
  - name: "Perception"
    desc: "+13; darkvision, lifesense 60 feet"
languages: "[[srd/pf2e/compendium/rules-elements/Languages#Chthonian|Chthonian]], [[srd/pf2e/compendium/rules-elements/Languages#Diabolic|Diabolic]], [[srd/pf2e/compendium/rules-elements/Languages#Empyrean|Empyrean]], Requian; telepathy 120 feet, [[srd/pf2e/compendium/spells/rank-5/Truespeech|_truespeech_]]"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/Acrobatics|Acrobatics]] +14, [[srd/pf2e/compendium/rules-elements/skills/Lore|Boneyard Lore]] +11, [[srd/pf2e/compendium/rules-elements/skills/Diplomacy|Diplomacy]] +14, [[srd/pf2e/compendium/rules-elements/skills/Intimidation|Intimidation]] +14, [[srd/pf2e/compendium/rules-elements/skills/Medicine|Medicine]] +12, [[srd/pf2e/compendium/rules-elements/skills/Occultism|Occultism]] +11, [[srd/pf2e/compendium/rules-elements/skills/Religion|Religion]] +12"
abilityMods: [0, 5, 4, 2, 4, 5]
ac: 22
armorclass:
  - name: "AC"
    desc: "22; __Fort__: +11; __Ref__: +12; __Will__: +13 +1 status to all saves vs. [[srd/pf2e/compendium/rules-elements/traits/player-core/Magical|magic]]"
hp: 75
health:
  - name: "HP"
    desc: "75; __Immunities__ [[srd/pf2e/compendium/rules-elements/traits/player-core/Death|death]] effects, [[srd/pf2e/compendium/rules-elements/traits/player-core/Disease|disease]]; __Resistances__ [[srd/pf2e/compendium/rules-elements/traits/player-core/Poison|poison]] 5, [[srd/pf2e/compendium/rules-elements/traits/player-core/Void|void]] 5"
abilities_mid:
  - name: "Calming Presence"
    desc: "([[srd/pf2e/compendium/rules-elements/traits/player-core/Aura|aura]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Divine|divine]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Emotion|emotion]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Incapacitation|incapacitation]]) 30 feet. A creature that begins its turn within the area must attempt a DC 18 Will save."
  - name: "Critical Success"
    desc: "The creature is unaffected and is temporarily immune to calming presence for 24 hours."
  - name: "Success"
    desc: "The creature's attack rolls take a –1 status penalty for 1 round."
  - name: "Failure"
    desc: "Any [[srd/pf2e/compendium/rules-elements/traits/player-core/Emotion|emotion]] effects that would affect the creature are suppressed, and the creature can't use hostile actions. If the creature is subjected to hostility from any other creature, it ceases to be affected by calming presence and is temporarily immune to calming presence for 24 hours."
  - name: "Critical Failure"
    desc: "As failure, but hostility doesn't end the effect."
speed: "25 feet"
attacks:
  - name: "Melee"
    desc: "⬻ fist +14 ([[srd/pf2e/compendium/rules-elements/traits/player-core/Agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Finesse|Finesse]]) __Damage__ 2d8+2 bludgeoning plus shepherd's touch"
abilities_bot:
  - name: "Compel Condemned"
    desc: "⬻ ([[srd/pf2e/compendium/rules-elements/traits/player-core/Divine|Divine]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Incapacitation|Incapacitation]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Mental|Mental]]) The catrina telepathically compels a creature within 30 feet to approach and allow the catrina to kiss them, in preparation for using Kiss of Death. The target must attempt a DC 22 Will save."
  - name: "Success"
    desc: "The creature is unaffected and is temporarily immune to Compel Condemned for 24 hours."
  - name: "Failure"
    desc: "The creature must spend each of its actions to move closer to the catrina as quickly as possible while avoiding obvious dangers. If the compelled creature is adjacent to the catrina, it stays still and doesn't act. If the creature takes any damage, the effect ends and the creature is temporarily immune to Compel Condemned for 24 hours. This effect lasts for 1 round, but if the catrina uses this ability again on subsequent rounds, it extend the duration by 1 round for all affected creatures."
  - name: "Critical Failure"
    desc: "As failure, but damage does not end the effect."
  - name: "Kiss of Death"
    desc: "⬺ ([[srd/pf2e/compendium/rules-elements/traits/player-core/Death|Death]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Divine|Divine]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Manipulate|Manipulate]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Void|Void]]) The catrina gives a long, passionate kiss to an [[srd/pf2e/compendium/rules-elements/Conditions#Unconscious|unconscious]] or willing creature, dealing 3d6 void damage. Any creature damaged by the same catrina's Kiss of Death for 3 consecutive rounds becomes [[srd/pf2e/compendium/rules-elements/Conditions#Unconscious|unconscious]] and is [[srd/pf2e/compendium/rules-elements/Conditions#Dying|dying 1]]."
  - name: "Shepherd's Touch"
    desc: "A psychopomp's Strikes affect [[srd/pf2e/compendium/rules-elements/traits/gm-core/Incorporeal|incorporeal]] creatures with the effects of a [[srd/pf2e/compendium/equipment/runes/Ghost Touch|_ghost touch_]] property rune and deal 1d6 void damage to living creatures and 1d6 vitality damage to [[srd/pf2e/compendium/rules-elements/traits/player-core/Undead|undead]]. Dealing With Grief Death often comes with great emotional distress. While catrinas handle these feelings for souls in the afterlife, the emotions of the deceased's loved ones can become a complication. In most cases, a different type of psychopomp—calacas—will handle the matter in the mortal [[srd/pf2e/compendium/gm/Planes#The Universe|Universe]]. Similar to catrinas in appearance, these skeletal psychopomps make use of song to ease the feelings of mortals. In extreme cases, such as the threat of a loved one pursuing vile necromancy to restore the dead, a catrina can establish a brief communication between the dead and their loved ones."
spellcasting:
  - name: "Divine Innate Spells"
    desc: "DC 22 - __Cantrips (3rd)__ [[srd/pf2e/compendium/spells/cantrips/Light|Light]] - __2nd__ [[srd/pf2e/compendium/spells/rank-2/Invisibility|Invisibility]] (at will; self only) - __3rd__ [[srd/pf2e/compendium/spells/rank-1/Illusory Disguise|Illusory Disguise]] - __4th__ [[srd/pf2e/compendium/spells/rank-4/Talking Corpse|Talking Corpse]] (at will), [[srd/pf2e/compendium/spells/rank-4/Translocate|Translocate]] - __Constant (5th)__ [[srd/pf2e/compendium/spells/rank-5/Truespeech|Truespeech]]"
sourcebook: "_Monster Core 2_, page 263."
```

```encounter-table
name: Catrina
creatures:
  - 1: Catrina
```
