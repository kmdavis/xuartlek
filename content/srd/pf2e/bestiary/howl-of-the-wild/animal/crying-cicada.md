---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Crying Cicada"
tags:
  - pf2e/creature/level/3
  - pf2e/creature/trait/animal
  - pf2e/creature/trait/small
statblock: inline
name: "Crying Cicada"
level: 3
source: "Howl of the Wild"
aon_id: "creature-3258"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=3258"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "HotW"
name: "Crying Cicada"
level: "Creature 3"
size: "Small"
trait_01: "Animal"
modifier: 11
perception:
  - name: "Perception"
    desc: "Perception +11; darkvision"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/deception|Deception]] +12, [[srd/pf2e/compendium/rules-elements/skills/stealth|Stealth]] +10, [[srd/pf2e/compendium/rules-elements/skills/survival|Survival]] +8"
abilityMods: [2, 4, 5, -5, 1, 3]
abilities_top:
  - name: "Wings Flat"
    desc: "When the crying cicada is still and perched on a tree, it blends seamlessly into the environment. It has an automatic result of 30 on [[srd/pf2e/compendium/rules-elements/skills/deception|Deception]] checks and DCs to pass as part of the tree."
ac: 19
armorclass:
  - name: "AC"
    desc: "19; __Fort__: +10; __Ref__: +12; __Will__: +7"
hp: 48
health:
  - name: "HP"
    desc: "48; __Immunities__ [[srd/pf2e/compendium/rules-elements/traits/player-core/poison|poison]]"
speed: "15 feet, fly 30 feet"
attacks:
  - name: "Melee"
    desc: "⬻ proboscis +9 __Damage__ 1d8+5 piercing plus 1d4 poison"
  - name: "Melee"
    desc: "⬻ slam +9 __Damage__ 1d6+4 bludgeoning plus crying cicada poison"
abilities_bot:
  - name: "Crying Cicada Poison"
    desc: "([[srd/pf2e/compendium/rules-elements/traits/gm-core/inhaled|Inhaled]], [[srd/pf2e/compendium/rules-elements/traits/player-core/poison|Poison]])"
  - name: "Saving Throw"
    desc: "DC 19 Fortitude"
  - name: "Maximum Duration"
    desc: "6 rounds"
  - name: "Stage 1"
    desc: "1d6 poison damage plus [[srd/pf2e/compendium/rules-elements/conditions#Slowed|slowed 1]] (1 round)"
  - name: "Stage 2"
    desc: "1d6 poison damage plus [[srd/pf2e/compendium/rules-elements/conditions#Slowed|slowed 2]] (1 round)"
  - name: "Stage 3"
    desc: "2d6 poison damage plus slowed 2 and [[srd/pf2e/compendium/rules-elements/conditions#Stupefied|stupefied 1]] (1 round)."
  - name: "Sob"
    desc: "⬻ ([[srd/pf2e/compendium/rules-elements/traits/player-core/auditory|Auditory]], [[srd/pf2e/compendium/rules-elements/traits/player-core/emotion|Emotion]], [[srd/pf2e/compendium/rules-elements/traits/player-core/mental|Mental]]) The crying cicada mimics the noise of a wounded animal or crying child. Non-cicada creatures within a 150-foot emanation must attempt a DC 19 Will save or be distressed by the pleas for help. The effect lasts for 1 round, but if the cicada uses this ability again on subsequent rounds, it extends the duration by 1 round for all affected creatures. Once a creature succeeds at any save against Sob, that creature is temporarily immune to Sob for 24 hours."
  - name: "Success"
    desc: "The creature is unaffected."
  - name: "Failure"
    desc: "The creature believes an animal or child needs help somewhere nearby. The creature is [[srd/pf2e/compendium/rules-elements/conditions#Fascinated|fascinated]], and it must spend each of its actions to [[srd/pf2e/compendium/rules-elements/actions/player-core#Seek|Seek]] or move closer to the cicada as expediently as possible, while avoiding obvious dangers. If the creature is adjacent to the cicada, it stays still and doesn't act."
  - name: "Steal Voice"
    desc: "⬺ ([[srd/pf2e/compendium/rules-elements/traits/player-core/auditory|Auditory]])"
  - name: "Requirements"
    desc: "An enemy creature has spoken since the crying cicada's last turn"
  - name: "Effect"
    desc: "The crying cicada learns and mimics the sound of its opponent's voice. It can't make new sentences, but it can choose to repeat select parts of the phrases it has heard. All non-cicada creatures within 30 feet, other than the owner of the stolen voice, must succeed at a DC 19 Will save to disbelieve the mimicry."
  - name: "Wing Flurry"
    desc: "⬻ The crying cicada beats its wings together, exposing all creatures within a 10-foot burst to crying cicada poison."
sourcebook: "_Howl of the Wild_, page 134."
```

```encounter-table
name: Crying Cicada
creatures:
  - 1: Crying Cicada
```
