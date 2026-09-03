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
languages: "Aklo, Common, Fey, Jotun, Thalassic"
skills:
  - name: "Skills"
    desc: "Acrobatics +8, Athletics +11, Deception +10, Occultism +8, Stealth +8"
abilityMods: [4, 3, 4, 1, 3, 3]
abilities_top:
  - name: "Coven"
    desc: "A sea hag adds _humanoid form_, _mariner's curse_, and _water walk_ to their coven's spells. Their spell DC when leading a coven is 20."
ac: 19
armorclass:
  - name: "AC"
    desc: "19; __Fort__: +11; __Ref__: +8; __Will__: +10 +1 status to all saves vs. magic"
hp: 45
health:
  - name: "HP"
    desc: "45; __Immunities__ polymorph; __Weaknesses__ cold iron 3"
speed: "25 feet, swim 35 feet"
attacks:
  - name: "Melee"
    desc: "⬻ claw +12 (Agile, Magical) __Damage__ 1d10+4 slashing"
abilities_bot:
  - name: "Dread Gaze"
    desc: "⬺ (Curse, Emotion, Fear, Mental, Occult) The hag gazes upon a creature, afflicting it with a gnawing sense of impending doom, with a result depending on its Will save (DC 20). The target doesn't need to be able to see the sea hag."
  - name: "Critical Success"
    desc: "The creature is unaffected."
  - name: "Success"
    desc: "The creature is frightened 1."
  - name: "Failure"
    desc: "The creature is frightened 1 and is slowed 1 for 1 round. If the target was dying, it remains unconscious for 1 day. At the end of the day, it must attempt a Fortitude save against the same DC; if it fails, it dies."
  - name: "Critical Failure"
    desc: "As failure, but the creature is frightened 2 and slowed 1 for 1 minute."
  - name: "Sea Hag's Bargain"
    desc: "(Concentrate, Exploration, Occult, Polymorph) The sea hag can make a bargain with a willing creature who must be of sound mind. The creature gives away a special or cherished quality—such as its courage, its beauty, or its voice. In exchange, the sea hag spends 1 minute polymorphing the creature into a form the target desires. This functions as Change Shape. It might be a total transformation or just changing one or more aspects of the target's body, and it can't make the creature more than one size smaller or larger. The creature changes its Speeds as appropriate for the new form. It doesn't change the attack and damage bonuses with its Strikes, but it might change the damage type the Strikes deal. This has an unlimited duration, and as long as it's transformed, the creature is sickened 2 and can't reduce its sickened condition below 2. The creature can slowly and carefully eat and drink despite being sickened. The only way to restore the lost quality used as payment is to defeat the sea hag or make another bargain for its return. Ending the bargain in this way also removes the transformation."
sourcebook: "_Monster Core_, page 188."
```

```encounter-table
name: Sea Hag
creatures:
  - 1: Sea Hag
```
