---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Doprillu"
tags:
  - pf2e/creature/level/14
  - pf2e/creature/trait/aberration
  - pf2e/creature/trait/medium
statblock: inline
name: "Doprillu"
level: 14
source: "Monster Core 2"
aon_id: "creature-4344"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=4344"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC2"
name: "Doprillu"
level: "Creature 14"
size: "Medium"
trait_01: "Aberration"
modifier: 22
perception:
  - name: "Perception"
    desc: "Perception +22; darkvision, [[srd/pf2e/compendium/spells/rank-2/see-the-unseen|_see the unseen_]]"
languages: "[[srd/pf2e/compendium/rules-elements/languages#Aklo|Aklo]], [[srd/pf2e/compendium/rules-elements/languages#Common|Common]], [[srd/pf2e/compendium/rules-elements/languages#Sakvroth|Sakvroth]]"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/acrobatics|Acrobatics]] +26, [[srd/pf2e/compendium/rules-elements/skills/athletics|Athletics]] +28, [[srd/pf2e/compendium/rules-elements/skills/intimidation|Intimidation]] +22, [[srd/pf2e/compendium/rules-elements/skills/stealth|Stealth]] +24"
abilityMods: [8, 6, 7, 1, 4, 2]
ac: 35
armorclass:
  - name: "AC"
    desc: "35; __Fort__: +27; __Ref__: +28; __Will__: +24 +2 status to all saves vs. [[srd/pf2e/compendium/rules-elements/traits/player-core/fear|fear]]"
hp: 260
health:
  - name: "HP"
    desc: "260 , regeneration 20 (deactivated by cold); __Immunities__ [[srd/pf2e/compendium/rules-elements/conditions#Enfeebled|enfeebled]] (while wearing their mask), [[srd/pf2e/compendium/rules-elements/conditions#Slowed|slowed]] (while wearing their mask); __Resistances__ [[srd/pf2e/compendium/rules-elements/traits/player-core/fire|fire]] 15"
abilities_mid:
  - name: "Mask of Power"
    desc: "A doprillu's unique, self-created wooden mask is the source of much of their power. A doprillu deprived of their mask loses their regeneration and immunity to [[srd/pf2e/compendium/rules-elements/conditions#Enfeebled|enfeebled]] and [[srd/pf2e/compendium/rules-elements/conditions#Slowed|slowed]], and they immediately become enfeebled 1. The enfeebled value increases by 1 at the start of each of the doprillu's turns, to a maximum of enfeebled 4. If the mask is put back on, the doprillu immediately regains their abilities and loses the enfeebled condition. A creature can pull off a doprillu's mask with a successful DC 34 [[srd/pf2e/compendium/rules-elements/skills/athletics|Athletics]] check."
  - name: "Volcanic Veins"
    desc: "([[srd/pf2e/compendium/rules-elements/traits/player-core/fire|fire]]) Fiery magma runs through the doprillu's veins burning those in their clutches. A creature that starts its turn grabbed by the doprillu takes 7d6 fire damage."
  - name: "Deflect Arrow"
    desc: "⬲"
  - name: "Trigger"
    desc: "The doprillu is the target of a physical ranged attack"
  - name: "Requirements"
    desc: "The doprillu is aware of the attack, isn't [[srd/pf2e/compendium/rules-elements/conditions#Off-Guard|off-guard]] against it, and has a hand free"
  - name: "Effect"
    desc: "The doprillu gains a +4 circumstance bonus to its AC against the triggering attack."
speed: "40 feet, climb 40 feet"
attacks:
  - name: "Melee"
    desc: "⬻ fist +30 ([[srd/pf2e/compendium/rules-elements/traits/player-core/agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/magical|magical]]) __Damage__ 3d8+16 bludgeoning plus 2d6 fire and Improved Grab"
abilities_bot:
  - name: "Body Strike"
    desc: "⬻"
  - name: "Requirements"
    desc: "The doprillu has a creature [[srd/pf2e/compendium/rules-elements/conditions#Grabbed|grabbed]]"
  - name: "Effect"
    desc: "The doprillu swings the grabbed creature as a weapon. This Strike has a +30 attack modifier and deals 3d8+16 bludgeoning damage. The Strike is magical and has a reach of 10 feet. On a hit, the grabbed creature takes half the damage dealt to the target."
  - name: "Whirlwind Throw"
    desc: "⬺"
  - name: "Requirements"
    desc: "The doprillu has a creature [[srd/pf2e/compendium/rules-elements/conditions#Grabbed|grabbed]]"
  - name: "Effect"
    desc: "The doprillu whirls the grabbed creature about, making a separate Body Strike against each creature in reach. After making a Strike against all creatures in reach, the doprillu can hurl the grabbed creature up to 50 feet as a ranged Strike. This Strike has the same attack modifier and damage as Body Strike, but it has the [[srd/pf2e/compendium/rules-elements/traits/player-core/thrown|thrown 20 feet]] weapon trait. Apply the doprillu's multiple attack penalty to the Strikes normally. Doprillu Masks A doprillu’s stylized mask isn’t a part of the creature themself, though doprillus inherently understand the mask’s purpose and power. When born, doprillus start out weak and small. Once one matures and gains sufficient intelligence and manual dexterity, they carve a personal mask. The first time they don the mask, a doprillu rushes out to seek a fight. This mask is never replaced, and it might be marred from hundreds of battles. Beneath the mask is a hauntingly blank face with tiny eyes and a pitch-black mouth, lacking any other features."
spellcasting:
  - name: "Occult Innate Spells"
    desc: "DC 28 - __Constant (6th)__ [[srd/pf2e/compendium/spells/rank-2/see-the-unseen|See the Unseen]]"
sourcebook: "_Monster Core 2_, page 117."
```

```encounter-table
name: Doprillu
creatures:
  - 1: Doprillu
```
