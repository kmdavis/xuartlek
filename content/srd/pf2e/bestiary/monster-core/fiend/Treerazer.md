---
noteType: pf2eMonster
aliases: "Treerazer"
tags:
  - pf2e/creature/level/25
  - pf2e/creature/trait/amphibious
  - pf2e/creature/trait/demon
  - pf2e/creature/trait/fiend
  - pf2e/creature/trait/unholy
  - pf2e/creature/trait/unique
  - pf2e/creature/trait/huge
statblock: inline
name: "Treerazer"
level: 25
source: "Monster Core"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=3218"
socialImage: og-image.png
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC"
name: "Treerazer"
level: "Creature 25"
size: "Huge"
trait_01: "Amphibious"
trait_02: "Demon"
trait_03: "Fiend"
trait_04: "Unholy"
trait_05: "Unique"
modifier: 46
perception:
  - name: "Perception"
    desc: "+46; darkvision, [[srd/pf2e/compendium/spells/rank-6/Truesight|_truesight_]]"
languages: "[[srd/pf2e/compendium/rules-elements/Languages#Chthonian|Chthonian]], [[srd/pf2e/compendium/rules-elements/Languages#Common|Common]], [[srd/pf2e/compendium/rules-elements/Languages#Elven|Elven]], [[srd/pf2e/compendium/rules-elements/Languages#Fey|Fey]]; telepathy 300 feet"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/Acrobatics|Acrobatics]] +40, [[srd/pf2e/compendium/rules-elements/skills/Arcana|Arcana]] +38, [[srd/pf2e/compendium/rules-elements/skills/Athletics|Athletics]] +45, [[srd/pf2e/compendium/rules-elements/skills/Intimidation|Intimidation]] +46, [[srd/pf2e/compendium/rules-elements/skills/Nature|Nature]] +49, [[srd/pf2e/compendium/rules-elements/skills/Occultism|Occultism]] +38, [[srd/pf2e/compendium/rules-elements/skills/Religion|Religion]] +45, [[srd/pf2e/compendium/rules-elements/skills/Stealth|Stealth]] +40"
abilityMods: [12, 9, 11, 7, 8, 8]
abilities_top:
  - name: "Items"
    desc: "_Blackaxe_"
ac: 54
armorclass:
  - name: "AC"
    desc: "54; __Fort__: +42; __Ref__: +40; __Will__: +43"
hp: 550
health:
  - name: "HP"
    desc: "550 , regeneration 50 (deactivated by [[srd/pf2e/compendium/rules-elements/traits/player-core/Holy|holy]]); __Immunities__ [[srd/pf2e/compendium/rules-elements/traits/player-core/Death|death]] effects, [[srd/pf2e/compendium/rules-elements/traits/player-core/Disease|disease]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Mental|mental]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Poison|poison]]; __Resistances__ [[srd/pf2e/compendium/rules-elements/traits/player-core/Acid|acid]] 20, [[srd/pf2e/compendium/rules-elements/traits/player-core/Cold|cold]] 15, [[srd/pf2e/compendium/rules-elements/traits/player-core/Fire|fire]] 15, physical 20 (except cold iron); __Weaknesses__ holy 20"
abilities_mid:
  - name: "Aura of Corruption"
    desc: "([[srd/pf2e/compendium/rules-elements/traits/player-core/Aura|aura]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Plant|plant]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Primal|primal]]) 120 feet. Plants near Treerazer twist, deform, and transform into thorny or fungoid parodies of their natural shapes. A living creature in this area must succeed at a DC 47 Fortitude save each round or become partially transformed into plantlike matter. Those who fail this saving throw are treated as if they were [[srd/pf2e/compendium/rules-elements/traits/player-core/Plant|plants]] for the purposes of any effect that particularly harms or inconveniences plant creatures more than other creatures, but do not gain any benefits of being plant creatures. This effect lasts as long as the creature remains within the area of corruption and for 1 minute thereafter."
  - name: "Reactive Strike"
    desc: "⬲"
speed: "60 feet, fly 60 feet, swim 40 feet; unfettered movement"
attacks:
  - name: "Melee"
    desc: "⬻ _Blackaxe_ +47 ([[srd/pf2e/compendium/rules-elements/traits/player-core/Acid|Acid]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Magical|Magical]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Reach|reach 15 feet]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Sweep|Sweep]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Unholy|Unholy]]) __Damage__ 5d12+18 slashing plus 1d6 acid (plus an additional 2d6 slashing to plants)"
  - name: "Melee"
    desc: "⬻ jaws +45 ([[srd/pf2e/compendium/rules-elements/traits/player-core/Agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Magical|Magical]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Reach|reach 15 feet]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Unholy|Unholy]]) __Damage__ 5d10+20 slashing"
abilities_bot:
  - name: "Defoliation"
    desc: "⬺ ([[srd/pf2e/compendium/rules-elements/traits/player-core/Plant|Plant]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Primal|Primal]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Unholy|Unholy]]) Treerazer exudes a pulse of sickly green light in a 30-foot-radius emanation. All plants in the area (including creatures under the effect of his aura of corruption) blacken and wither. Non-creature plants immediately wither and die. [[srd/pf2e/compendium/rules-elements/traits/player-core/Plant|Plant]] and [[srd/pf2e/compendium/rules-elements/traits/player-core/Fungus|fungus]] creatures take 20d8 void damage with a DC 49 basic Fortitude save. A creature that fails its save is [[srd/pf2e/compendium/rules-elements/Conditions#Doomed|doomed 1]] for 1 minute and [[srd/pf2e/compendium/rules-elements/Conditions#Sickened|sickened 3]]. Treerazer can choose to exclude any number of plants or fungi in the area from this effect, and generally does so to preserve twisted and corrupted plants or fungi, or plant and fungus creatures that are allied to his cause. Treerazer can't use Defoliation for 1d4 rounds."
  - name: "Dispelling Strike"
    desc: "⭓ ([[srd/pf2e/compendium/rules-elements/traits/player-core/Primal|Primal]])"
  - name: "Frequency"
    desc: "once per round"
  - name: "Trigger"
    desc: "Treerazer hits a creature, object, or spell effect with a weapon Strike or subjects one to Defoliation"
  - name: "Effect"
    desc: "Treerazer casts his innate [[srd/pf2e/compendium/spells/rank-2/Dispel Magic|_dispel magic_]], targeting the creature he hit with his Strike or one spell affecting that creature."
  - name: "Staggering Strike"
    desc: "When Treerazer scores a critical hit with a melee attack, the target is [[srd/pf2e/compendium/rules-elements/Conditions#Stunned|stunned 2]]. Spawn Of Cyth-V'sug Treerazer was once the favored minion and lieutenant (some even say child) of the demon lord Cyth-V'sug, Lord of Fungus and Parasites. After a failed attempt to wrest that role in the [[srd/pf2e/compendium/gm/Planes#Outer Rifts|Outer Rifts]] away from Cyth-V'sug, Treerazer fled to the mortal [[srd/pf2e/compendium/gm/Planes#The Universe|Universe]]. Cyth-V'sug was unable (or perhaps only unwilling) to pursue but took steps to ensure that Treerazer would remain there by exiling him, severing Treerazer's bond to the Outer Rifts—if the Lord of the Blasted Tarn is slain, his animus will not return to the Outer Rifts and reform. Death, to Treerazer, is a permanent thing. Treerazer's Cultists Treerazer is worshipped by cultists throughout the Inner Sea region. The majority of these can be found within or near the expanse of the Tanglebriar, consisting of fungus-corrupted fey, debased elves, or other sinister demon worshippers. Beyond Tanglebriar, his cultists are rarer and tend to be loners or leaders of very small groups. Treerazer's religious symbol is a bleeding dead tree that's been split in half."
  - name: "Areas of Concern"
    desc: "corruption of nature, pollution, and slaughter of elves"
  - name: "Edicts"
    desc: "corrupt plant life with evil or fungal influences, slay elves, feast on rotten flesh or fungus"
  - name: "Anathema"
    desc: "grant mercy to elves, plant trees, encourage natural plant growth"
  - name: "Divine Attribute"
    desc: "Strength or Wisdom Devotee Benefits"
  - name: "Cleric Spells"
    desc: "1st: [[srd/pf2e/compendium/spells/rank-1/Grim Tendrils|_grim tendrils_]], 3rd: [[srd/pf2e/compendium/spells/rank-3/Wall of Thorns|_wall of thorns_]], 6th: [[srd/pf2e/compendium/spells/rank-6/Tangling Creepers|_tangling creepers_]]"
  - name: "Divine Font"
    desc: "[[srd/pf2e/compendium/spells/rank-1/Harm|_harm_]] or [[srd/pf2e/compendium/spells/rank-1/Heal|_heal_]]"
  - name: "Divine Sanctification"
    desc: "must choose unholy"
  - name: "Divine Skill"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/Nature|Nature]]"
  - name: "Domains"
    desc: "[[srd/pf2e/compendium/character/Domains#Destruction|destruction]], [[srd/pf2e/compendium/character/Domains#Nature|nature]], [[srd/pf2e/compendium/character/Domains#Nightmares|nightmares]], [[srd/pf2e/compendium/character/Domains#Tyranny|tyranny]]"
  - name: "Favored Weapon"
    desc: "[[srd/pf2e/compendium/equipment/weapons/axe/Greataxe|greataxe]]"
spellcasting:
  - name: "Primal Innate Spells"
    desc: "DC 49, attack +43 - __Cantrips (9th)__ [[srd/pf2e/compendium/spells/cantrips/Telekinetic Projectile|Telekinetic Projectile]] - __2nd__ [[srd/pf2e/compendium/spells/rank-2/Telekinetic Maneuver|Telekinetic Maneuver]] (at will) - __3rd__ [[srd/pf2e/compendium/spells/rank-3/Earthbind|Earthbind]] (at will) - __4th__ [[srd/pf2e/compendium/spells/rank-4/Unfettered Movement|Unfettered Movement]] - __6th__ [[srd/pf2e/compendium/spells/rank-6/Tangling Creepers|Tangling Creepers]] (at will) - __9th__ [[srd/pf2e/compendium/spells/rank-2/Dispel Magic|Dispel Magic]] (at will) - __10th__ [[srd/pf2e/compendium/spells/rank-8/Desiccate|Desiccate]], [[srd/pf2e/compendium/spells/rank-10/Freeze Time|Freeze Time]], [[srd/pf2e/compendium/spells/rank-3/Wall of Thorns|Wall of Thorns]] - __Constant (8th)__ [[srd/pf2e/compendium/spells/rank-6/Truesight|Truesight]]"
  - name: "Rituals"
    desc: "DC 49 - __1st__ [[srd/pf2e/compendium/spells/rituals/Demonic Pact|Demonic Pact]] - __5th__ [[srd/pf2e/compendium/spells/rituals/Planar Servitor|Planar Servitor]]"
sourcebook: "_Monster Core_, page 328."
```

```encounter-table
name: Treerazer
creatures:
  - 1: Treerazer
```
