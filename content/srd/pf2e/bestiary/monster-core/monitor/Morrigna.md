---
noteType: pf2eMonster
aliases: "Morrigna"
tags:
  - pf2e/creature/level/15
  - pf2e/creature/trait/monitor
  - pf2e/creature/trait/psychopomp
  - pf2e/creature/trait/medium
statblock: inline
name: "Morrigna"
level: 15
source: "Monster Core"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=3149"
socialImage: og-image.png
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC"
name: "Morrigna"
level: "Creature 15"
size: "Medium"
trait_01: "Monitor"
trait_02: "Psychopomp"
modifier: 28
perception:
  - name: "Perception"
    desc: "+28; darkvision, lifesense 60 feet"
languages: "[[srd/pf2e/compendium/rules-elements/Languages#Chthonian|Chthonian]], [[srd/pf2e/compendium/rules-elements/Languages#Diabolic|Diabolic]], [[srd/pf2e/compendium/rules-elements/Languages#Empyrean|Empyrean]], [[srd/pf2e/compendium/rules-elements/Languages#Necril|Necril]], Requian; [[srd/pf2e/compendium/spells/rank-2/Speak with Animals|_speak with animals_]], [[srd/pf2e/compendium/spells/rank-5/Truespeech|_truespeech_]]"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/Athletics|Athletics]] +27, Boneyard Lore +28, [[srd/pf2e/compendium/rules-elements/skills/Diplomacy|Diplomacy]] +27, [[srd/pf2e/compendium/rules-elements/skills/Intimidation|Intimidation]] +29, [[srd/pf2e/compendium/rules-elements/skills/Religion|Religion]] +29, [[srd/pf2e/compendium/rules-elements/skills/Society|Society]] +24, [[srd/pf2e/compendium/rules-elements/skills/Stealth|Stealth]] +27"
abilityMods: [8, 4, 4, 3, 6, 4]
abilities_top:
  - name: "Items"
    desc: "_+2 [[srd/pf2e/compendium/equipment/runes/Striking|striking]] [[srd/pf2e/compendium/equipment/weapons/club/Bo Staff|bo staff]]_"
ac: 38
armorclass:
  - name: "AC"
    desc: "38; __Fort__: +25; __Ref__: +27; __Will__: +29 +1 status to all saves vs. [[srd/pf2e/compendium/rules-elements/traits/player-core/Magical|magic]]"
hp: 240
health:
  - name: "HP"
    desc: "240 , regeneration 20 (deactivated by [[srd/pf2e/compendium/rules-elements/traits/player-core/Acid|acid]] or [[srd/pf2e/compendium/rules-elements/traits/player-core/Fire|fire]]); __Immunities__ [[srd/pf2e/compendium/rules-elements/traits/player-core/Death|death]] effects, [[srd/pf2e/compendium/rules-elements/traits/player-core/Disease|disease]]; __Resistances__ [[srd/pf2e/compendium/rules-elements/traits/player-core/Poison|poison]] 15, [[srd/pf2e/compendium/rules-elements/traits/player-core/Void|void]] 15"
abilities_mid:
  - name: "Wrappings Lash"
    desc: "⬲"
  - name: "Trigger"
    desc: "A creature within reach of the morrigna's web wrappings uses an action to Strike or attempt a skill check"
  - name: "Effect"
    desc: "The morrigna makes a web wrappings Strike against the triggering creature. If the strike is a critical hit, the triggering action is disrupted."
speed: "30 feet, climb 30 feet"
attacks:
  - name: "Melee"
    desc: "⬻ _bo staff_ +31 ([[srd/pf2e/compendium/rules-elements/traits/player-core/Magical|Magical]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Parry|Parry]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Reach|reach 10 feet]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Trip|Trip]]) __Damage__ 2d8+14 bludgeoning plus 4d6 shepherd's touch"
  - name: "Melee"
    desc: "⬻ web wrappings +29 ([[srd/pf2e/compendium/rules-elements/traits/player-core/Magical|Magical]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Reach|reach 10 feet]]) __Damage__ 3d12+14 bludgeoning plus Grab and 4d6 shepherd's touch"
abilities_bot:
  - name: "Change Shape"
    desc: "⬻ ([[srd/pf2e/compendium/rules-elements/traits/player-core/Concentrate|Concentrate]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Divine|Divine]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Polymorph|Polymorph]]) A morrigna can take the appearance of any Small or Medium animal or humanoid. This doesn't change their Speed or their attack and damage modifiers with their Strikes, but it might change the damage type their Strikes deal. Unless they choose to manifest their web wrappings in their new form, they cannot make web wrappings Strikes."
  - name: "Shepherd's Touch"
    desc: "A morrigna's Strikes have the benefit of a [[srd/pf2e/compendium/equipment/runes/Ghost Touch|_ghost touch_]] property rune and deal an additional 4d6 void damage to living creatures or 4d6 vitality damage to undead."
  - name: "Spider Minions"
    desc: "⬽ ([[srd/pf2e/compendium/rules-elements/traits/player-core/Divine|Divine]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Summon|Summon]]) The morrigna summons a giant tarantula (page 321) or spider swarm. These spiders have the [[srd/pf2e/compendium/rules-elements/traits/player-core/Summoned|summoned]] trait and remain for 10 minutes or until reduced to 0 Hit Points, whichever comes first. The morrigna does not need to Sustain the Spell to direct these summoned creatures, and the morrigna can have any number of summoned spiders in existence at once. The morrigna can see through the eyes of any of their summoned spiders at any time."
spellcasting:
  - name: "Divine Spontaneous Spells"
    desc: "DC 35, attack +30 - __Cantrips (8th)__ [[srd/pf2e/compendium/spells/cantrips/Detect Magic|Detect Magic]], [[srd/pf2e/compendium/spells/cantrips/Read Aura|Read Aura]], [[srd/pf2e/compendium/spells/cantrips/Stabilize|Stabilize]], [[srd/pf2e/compendium/spells/cantrips/Vitality Lash|Vitality Lash]], [[srd/pf2e/compendium/spells/cantrips/Void Warp|Void Warp]] - __1st__ [[srd/pf2e/compendium/spells/rank-1/Bane|Bane]], [[srd/pf2e/compendium/spells/rank-1/Bless|Bless]], [[srd/pf2e/compendium/spells/rank-1/Enfeeble|Enfeeble]] (4 slots) - __2nd__ [[srd/pf2e/compendium/spells/rank-2/Calm|Calm]], [[srd/pf2e/compendium/spells/rank-2/See the Unseen|See the Unseen]], [[srd/pf2e/compendium/spells/rank-2/Silence|Silence]] (4 slots) - __3rd__ [[srd/pf2e/compendium/spells/rank-3/Blindness|Blindness]], [[srd/pf2e/compendium/spells/rank-3/Crisis of Faith|Crisis of Faith]], [[srd/pf2e/compendium/spells/rank-3/Dream Message|Dream Message]] (4 slots) - __4th__ [[srd/pf2e/compendium/spells/rank-4/Dispelling Globe|Dispelling Globe]], [[srd/pf2e/compendium/spells/rank-4/Read Omens|Read Omens]], [[srd/pf2e/compendium/spells/rank-4/Unfettered Movement|Unfettered Movement]] (4 slots) - __5th__ [[srd/pf2e/compendium/spells/rank-2/Dispel Magic|Dispel Magic]], [[srd/pf2e/compendium/spells/rank-5/Scouting Eye|Scouting Eye]], [[srd/pf2e/compendium/spells/rank-5/Sending|Sending]] (4 slots) - __6th__ [[srd/pf2e/compendium/spells/rank-6/Field of Life|Field of Life]], [[srd/pf2e/compendium/spells/rank-1/Heal|Heal]], [[srd/pf2e/compendium/spells/rank-6/Spirit Blast|Spirit Blast]] (4 slots)"
  - name: "Divine Innate Spells"
    desc: "DC 37 - __4th__ [[srd/pf2e/compendium/spells/rank-4/Talking Corpse|Talking Corpse]] - __Constant (5th)__ [[srd/pf2e/compendium/spells/rank-5/Truespeech|Truespeech]], [[srd/pf2e/compendium/spells/rank-2/Speak with Animals|Speak with Animals]]"
  - name: "Rituals"
    desc: "DC 37 - __5th__ Call Spirit"
sourcebook: "_Monster Core_, page 276."
```

```encounter-table
name: Morrigna
creatures:
  - 1: Morrigna
```
