---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Millindemalion"
tags:
  - pf2e/creature/level/13
  - pf2e/creature/trait/fey
  - pf2e/creature/trait/small
statblock: inline
name: "Millindemalion"
level: 13
source: "Monster Core 2"
aon_id: "creature-4474"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=4474"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC2"
name: "Millindemalion"
level: "Creature 13"
size: "Small"
trait_01: "Fey"
modifier: 23
perception:
  - name: "Perception"
    desc: "Perception +23; low-light vision"
languages: "[[srd/pf2e/compendium/rules-elements/languages#Aklo|Aklo]], [[srd/pf2e/compendium/rules-elements/languages#Common|Common]], [[srd/pf2e/compendium/rules-elements/languages#Fey|Fey]]"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/crafting|Crafting]] +28, [[srd/pf2e/compendium/rules-elements/skills/lore|Millinery Lore]] +30, [[srd/pf2e/compendium/rules-elements/skills/occultism|Occultism]] +24, [[srd/pf2e/compendium/rules-elements/skills/society|Society]] +24, [[srd/pf2e/compendium/rules-elements/skills/stealth|Stealth]] +27"
abilityMods: [4, 8, 1, 7, 4, 2]
abilities_top:
  - name: "Items"
    desc: "_[[srd/pf2e/compendium/equipment/weapons/magic-weapon-3-major-striking|+1 striking]] [[srd/pf2e/compendium/equipment/weapons/knife/shears-weapon-446|shears]]_"
ac: 33
armorclass:
  - name: "AC"
    desc: "33; __Fort__: +20; __Ref__: +27; __Will__: +23 unsettling mind"
hp: 275
health:
  - name: "HP"
    desc: "275; __Weaknesses__ [[srd/pf2e/compendium/equipment/materials/cold-iron-object-high-grade|cold iron]] 10"
abilities_mid:
  - name: "Unsettling Mind"
    desc: "([[srd/pf2e/compendium/rules-elements/traits/player-core/mental|mental]]) Attempting to touch the frenetic mind of a millindemalion is a dangerous task. When the millindemalion succeeds at a saving throw against a [[srd/pf2e/compendium/rules-elements/traits/player-core/mental|mental]] effect, the creature originating that effect takes 4d6 mental damage."
  - name: "Reactive Strike"
    desc: "⬲ The millindemalion can use Hat Toss against the triggering creature instead of making a Strike, making a melee attack roll with a +27 modifier to do so."
speed: "30 feet"
attacks:
  - name: "Melee"
    desc: "⬻ _shears_ +27 ([[srd/pf2e/compendium/rules-elements/traits/player-core/deadly|deadly d8]], [[srd/pf2e/compendium/rules-elements/traits/player-core/finesse|finesse]], [[srd/pf2e/compendium/rules-elements/traits/player-core/versatile|versatile P]]) __Damage__ 2d4+14 slashing plus 1d6 mental"
abilities_bot:
  - name: "Hat Toss"
    desc: "⬻ ([[srd/pf2e/compendium/rules-elements/traits/player-core/manipulate|Manipulate]], [[srd/pf2e/compendium/rules-elements/traits/player-core/mental|mental]], [[srd/pf2e/compendium/rules-elements/traits/player-core/primal|primal]]) The millindemalion quickly crafts a mindaltering hat in combat and tosses it onto a target with a flick of their wrist. The millindemalion chooses one of the effects below and makes a ranged attack roll with a +27 modifier and a range increment of 20 feet. On a hit, the target must succeed at a DC 33 Will saving throw or experience the listed effect with a duration of 1d4+1 rounds. If the millindemalion critically succeeds at the ranged Strike, the target takes a –4 circumstance penalty to the save. A target can only wear one millindemalion hat at a time; a new hat replaces any previous hat. The hat can't be removed before the condition ends , but when the condition ends (or on a successful save), the hat falls to pieces."
  - name: "Befuddling Bowler"
    desc: "The hat clouds the target's mind; the target becomes [[srd/pf2e/compendium/rules-elements/conditions#Stupefied|stupefied]] 2."
  - name: "Bewitching Beret"
    desc: "The target is infatuated with its new hat's creator, becoming [[srd/pf2e/compendium/rules-elements/conditions#Fascinated|fascinated]] by the millindemalion."
  - name: "Dazzling Deerstalker"
    desc: "The target can barely see with the hat falling down over its eyes and gains the [[srd/pf2e/compendium/rules-elements/conditions#Dazzled|dazzled]] condition."
  - name: "Fettering Fedora"
    desc: "The target feels a heavy weight pressing down on it from the hat and takes a –10 foot circumstance penalty to its Speeds."
  - name: "Tiring Tricorn"
    desc: "The target grows sleepy and becomes [[srd/pf2e/compendium/rules-elements/conditions#Slowed|slowed]] 1."
  - name: "Sneak Attack"
    desc: "A millindemalion's Strikes deal an extra 4d6 precision damage to [[srd/pf2e/compendium/rules-elements/conditions#Off-Guard|off-guard]] creatures. Similar Fey Millindemalion practice a cruel form of hat-making, but there have been sightings of similar trickster fey who can craft shoes that never stop dancing or jackets that inflict wild mood swings onto their victims."
sourcebook: "_Monster Core 2_, page 222."
```

```encounter-table
name: Millindemalion
creatures:
  - 1: Millindemalion
```
