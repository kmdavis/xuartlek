---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Sea Hag"
tags:
  - pf2e/creature/level/3
  - pf2e/creature/trait/amphibious
  - pf2e/creature/trait/hag
  - pf2e/creature/trait/humanoid
  - pf2e/creature/trait/medium
statblock: inline
name: "Sea Hag"
level: 3
source: "Monster Core"
aon_id: "creature-3040"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=3040"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC"
name: "Sea Hag"
level: "Creature 3"
size: "Medium"
trait_01: "Amphibious"
trait_02: "Hag"
trait_03: "Humanoid"
modifier: 10
perception:
  - name: "Perception"
    desc: "Perception +10; darkvision"
languages: "[[srd/pf2e/compendium/rules-elements/languages#Aklo|Aklo]], [[srd/pf2e/compendium/rules-elements/languages#Common|Common]], [[srd/pf2e/compendium/rules-elements/languages#Fey|Fey]], [[srd/pf2e/compendium/rules-elements/languages#Jotun|Jotun]], [[srd/pf2e/compendium/rules-elements/languages#Thalassic|Thalassic]]"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/acrobatics|Acrobatics]] +8, [[srd/pf2e/compendium/rules-elements/skills/athletics|Athletics]] +11, [[srd/pf2e/compendium/rules-elements/skills/deception|Deception]] +10, [[srd/pf2e/compendium/rules-elements/skills/occultism|Occultism]] +8, [[srd/pf2e/compendium/rules-elements/skills/stealth|Stealth]] +8"
abilityMods: [4, 3, 4, 1, 3, 3]
abilities_top:
  - name: "Coven"
    desc: "A sea hag adds [[srd/pf2e/compendium/spells/rank-2/humanoid-form|_humanoid form_]], [[srd/pf2e/compendium/spells/rank-5/mariners-curse|_mariner's curse_]], and [[srd/pf2e/compendium/spells/rank-2/water-walk|_water walk_]] to their coven's spells. Their spell DC when leading a coven is 20."
ac: 19
armorclass:
  - name: "AC"
    desc: "19; __Fort__: +11; __Ref__: +8; __Will__: +10 +1 status to all saves vs. [[srd/pf2e/compendium/rules-elements/traits/player-core/magical|magic]]"
hp: 45
health:
  - name: "HP"
    desc: "45; __Immunities__ [[srd/pf2e/compendium/rules-elements/traits/player-core/polymorph|polymorph]]; __Weaknesses__ cold iron 3"
speed: "25 feet, swim 35 feet"
attacks:
  - name: "Melee"
    desc: "⬻ claw +12 ([[srd/pf2e/compendium/rules-elements/traits/player-core/agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/magical|Magical]]) __Damage__ 1d10+4 slashing"
abilities_bot:
  - name: "Dread Gaze"
    desc: "⬺ ([[srd/pf2e/compendium/rules-elements/traits/player-core/curse|Curse]], [[srd/pf2e/compendium/rules-elements/traits/player-core/emotion|Emotion]], [[srd/pf2e/compendium/rules-elements/traits/player-core/fear|Fear]], [[srd/pf2e/compendium/rules-elements/traits/player-core/mental|Mental]], [[srd/pf2e/compendium/rules-elements/traits/player-core/occult|Occult]]) The hag gazes upon a creature, afflicting it with a gnawing sense of impending doom, with a result depending on its Will save (DC 20). The target doesn't need to be able to see the sea hag."
  - name: "Critical Success"
    desc: "The creature is unaffected."
  - name: "Success"
    desc: "The creature is [[srd/pf2e/compendium/rules-elements/conditions#Frightened|frightened 1]]."
  - name: "Failure"
    desc: "The creature is frightened 1 and is [[srd/pf2e/compendium/rules-elements/conditions#Slowed|slowed 1]] for 1 round. If the target was [[srd/pf2e/compendium/rules-elements/conditions#Dying|dying]], it remains [[srd/pf2e/compendium/rules-elements/conditions#Unconscious|unconscious]] for 1 day. At the end of the day, it must attempt a Fortitude save against the same DC; if it fails, it dies."
  - name: "Critical Failure"
    desc: "As failure, but the creature is frightened 2 and slowed 1 for 1 minute."
  - name: "Sea Hag's Bargain"
    desc: "([[srd/pf2e/compendium/rules-elements/traits/player-core/concentrate|Concentrate]], [[srd/pf2e/compendium/rules-elements/traits/player-core/exploration|Exploration]], [[srd/pf2e/compendium/rules-elements/traits/player-core/occult|Occult]], [[srd/pf2e/compendium/rules-elements/traits/player-core/polymorph|Polymorph]]) The sea hag can make a bargain with a willing creature who must be of sound mind. The creature gives away a special or cherished quality—such as its courage, its beauty, or its voice. In exchange, the sea hag spends 1 minute polymorphing the creature into a form the target desires. This functions as Change Shape. It might be a total transformation or just changing one or more aspects of the target's body, and it can't make the creature more than one size smaller or larger. The creature changes its Speeds as appropriate for the new form. It doesn't change the attack and damage bonuses with its Strikes, but it might change the damage type the Strikes deal. This has an unlimited duration, and as long as it's transformed, the creature is [[srd/pf2e/compendium/rules-elements/conditions#Sickened|sickened 2]] and can't reduce its sickened condition below 2. The creature can slowly and carefully eat and drink despite being sickened. The only way to restore the lost quality used as payment is to defeat the sea hag or make another bargain for its return. Ending the bargain in this way also removes the transformation."
sourcebook: "_Monster Core_, page 188."
```

```encounter-table
name: Sea Hag
creatures:
  - 1: Sea Hag
```
